#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>

/*
 * compound_interest(principal, rate, times_per_year, years) -> float
 *
 * Formula:
 *   A = P * (1 + r / n)^(n * t)
 *
 * Where:
 *   P = principal
 *   r = annual interest rate as a decimal, e.g. 0.05 for 5%
 *   n = number of times interest is compounded per year
 *   t = number of years
 */
static PyObject *py_compound_interest(PyObject *self, PyObject *args)
{
    double principal;
    double rate;
    int times_per_year;
    double years;

    if (!PyArg_ParseTuple(args, "ddid", &principal, &rate, &times_per_year, &years)) {
        return NULL;
    }

    if (times_per_year <= 0) {
        PyErr_SetString(PyExc_ValueError, "times_per_year must be greater than 0");
        return NULL;
    }

    if (principal < 0.0) {
        PyErr_SetString(PyExc_ValueError, "principal must be non-negative");
        return NULL;
    }

    if (years < 0.0) {
        PyErr_SetString(PyExc_ValueError, "years must be non-negative");
        return NULL;
    }

    double amount = principal * pow(1.0 + (rate / (double)times_per_year),
                                    (double)times_per_year * years);

    return PyFloat_FromDouble(amount);
}

static PyMethodDef FinanceMethods[] = {
    {
        "compound_interest",
        py_compound_interest,
        METH_VARARGS,
        PyDoc_STR(
            "compound_interest(principal, rate, times_per_year, years)\n"
            "--\n\n"
            "Calculate compound interest.\n\n"
            "Arguments:\n"
            "  principal: initial amount\n"
            "  rate: annual interest rate as decimal (e.g. 0.05)\n"
            "  times_per_year: compounding frequency per year\n"
            "  years: number of years\n\n"
            "Returns:\n"
            "  Final amount after compounding."
        )
    },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef finance_module = {
    PyModuleDef_HEAD_INIT,
    "finance",
    "Finance helper module implemented in C.",
    -1,
    FinanceMethods
};

PyMODINIT_FUNC PyInit_finance(void)
{
    return PyModule_Create(&finance_module);
}