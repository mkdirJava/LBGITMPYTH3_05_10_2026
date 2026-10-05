import struct

fOut = open("bindata.dat", "wb")
data = struct.pack("if20s",100, 3.1412, b"To be or not to be...")
print(type(data))
fOut.write(data)
fOut.close()

fIn = open("bindata.dat", "rb")
data = fIn.read(32);
fIn.close()

clean = struct.unpack("if20s", data)
print(clean)
print(clean[0]) # int
print(clean[1]) # float
txt = clean[2].decode().rstrip('\x00') # str
print(txt)
