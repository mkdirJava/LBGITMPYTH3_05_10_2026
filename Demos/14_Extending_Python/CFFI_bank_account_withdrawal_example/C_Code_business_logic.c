#include <stdio.h>
// Note, code is specified here to show it as pure C
// The cffi code does not use or reference this in any way.
double withdraw(double balance, double amount) {
    if (amount > balance) {
        return -1.0;  // signal error
    }
    return balance - amount;
}