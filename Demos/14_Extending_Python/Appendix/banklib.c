// banklib.c
#include <stdio.h>

__declspec(dllexport)
double calculate_interest(double balance, double rate, int years) {
    return balance * rate * years;
}

__declspec(dllexport)
void print_account_summary(double balance) {
    printf("Account balance: %.2f\n", balance);
}