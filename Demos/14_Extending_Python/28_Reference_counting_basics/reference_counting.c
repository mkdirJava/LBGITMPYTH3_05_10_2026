// Some examples
yObject *obj = PyLong_FromLong(10);  // ref count = 1

Py_DECREF(obj);  // ref count = 0 → object freed

PyObject *obj = PyLong_FromLong(10);
// no Py_DECREF → memory leak


PyObject *obj = PyLong_FromLong(10)
Py_DECREF(obj);
Py_DECREF(obj);  // crash
