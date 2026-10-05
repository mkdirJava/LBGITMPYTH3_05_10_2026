from cffi import FFI

ffi = FFI()

ffi.cdef("""
    double withdraw(double balance, double amount);
""")

C = ffi.verify("""
    double withdraw(double balance, double amount) {
        if (amount > balance) {
            return -1.0;
        }
        return balance - amount;
    }
""")


