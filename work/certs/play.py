from cryptography.hazmat.primitives.serialization import pkcs7
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import pkcs7
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.x509 import load_pem_x509_certificate

from cryptography import x509
from cryptography.hazmat.primitives.serialization import pkcs7
from OpenSSL import crypto  

def sign_file_attached(file_path: str, private_key_path: str, cert_path: str, output_path: str):
    # 1. Load your private key and public certificate
    with open(private_key_path, "rb") as k_file:
        private_key = load_pem_private_key(k_file.read(), password=None)

    with open(cert_path, "rb") as c_file:
        certificate = load_pem_x509_certificate(c_file.read())

    # 2. Read the file you want to sign
    with open(file_path, "rb") as data_file:    
        file_bytes = data_file.read()

    # 3. Sign it with the data ENCAPSULATED (Attached)
    # Leaving options empty means the original file data is baked inside the signature output.
    options = [] 
    
    signed_bytes = (
        pkcs7.PKCS7SignatureBuilder()
        .set_data(file_bytes)
        .add_signer(certificate, private_key, hashes.SHA256())
        .sign(pkcs7.PKCS7SerializationFormat.DER, options)
    )

    # 4. Save the single unified signed file to disk
    with open(output_path, "wb") as out_file:
        out_file.write(signed_bytes)
        
    print(f"Successfully signed. Single file created: {output_path}")

def verify_and_extract_p7m(signed_file_path: str, trusted_cert_path: str, output_data_path: str) -> bool:
    """
    1. Verifies the .p7m attached signature using a trusted local public certificate.
    2. Extracts the underlying raw data payload out of the envelope and saves it.
    """
    # Step 1: Read the single signed .p7m binary file bytes
    with open(signed_file_path, "rb") as f:
        p7m_bytes = f.read()

    # Step 2: Load your known, trusted public certificate from disk
    with open(trusted_cert_path, "rb") as c_file:
        trusted_cert_data = c_file.read()
        # Load via standard cryptography module for validation checks
        trusted_cert = x509.load_pem_x509_certificate(trusted_cert_data)

    try:
        # Step 3: Extract the signer's certificate embedded inside the payload
        embedded_certs = pkcs7.load_der_pkcs7_certificates(p7m_bytes)
        if not embedded_certs:
            raise ValueError("No signing certificates found inside the PKCS#7 file payload.")
        
        signer_cert = embedded_certs[0]

        # Step 4: TRUST VALIDATION (Crucial Security Check)
        # Compare the unique fingerprint of the embedded certificate against your trusted local certificate
        if signer_cert.fingerprint(signer_cert.signature_hash_algorithm) != trusted_cert.fingerprint(trusted_cert.signature_hash_algorithm):
            raise PermissionError("Security Violation: The file was signed by an untrusted or altered certificate!")

        # Step 5: CRYPTOGRAPHIC EXTRACTION (Using OpenSSL engine wrapper)
        # Parse the raw bytes into an OpenSSL PKCS7 object mapping
        p7_obj = crypto.load_pkcs7_data(crypto.FILETYPE_ASN1, p7m_bytes)
        
        # Create an in-memory memory buffer stream to receive the extracted data
        bio_out = crypto._new_mem_buf()
        
        # Execute OpenSSL native verification & extraction layer
        # PKCS7_NOVERIFY tells the engine to rely on our custom strict identity check above
        verification_status = crypto._lib.PKCS7_verify(p7_obj._pkcs7, crypto._ffi.NULL, crypto._ffi.NULL, crypto._ffi.NULL, bio_out, crypto._lib.PKCS7_NOVERIFY)
        
        if verification_status != 1:
            raise crypto.Error("OpenSSL structural payload verification failed.")

        # Step 6: Convert the raw out stream buffer to Python bytes
        extracted_data_bytes = crypto._bio_to_string(bio_out)

        # Step 7: Write the clean, untouched data file out to disk
        with open(output_data_path, "wb") as out_file:
            out_file.write(extracted_data_bytes)

        print(f"Success: Signature verified and data extracted to '{output_data_path}'")
        return True

    except Exception as e:
        print(f"Cryptographic Rejection: {e}")
        return False