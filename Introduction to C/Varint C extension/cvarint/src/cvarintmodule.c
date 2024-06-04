#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *cvarint_encode(PyObject *self, PyObject *args) {
    uint64_t n=0, i=0;
    uint8_t out[10], p=0;
    if( !PyArg_ParseTuple(args, "K", &n))
        return Py_None;

    while(n){
        p= n & 0x7f;
        n>>= 7;
        p|= n ? 0x80 : 0x00;
        out[i++]= p;
    }

    return PyBytes_FromStringAndSize(out, i);
}

static PyObject *cvarint_decode(PyObject *self, PyObject *args) {
    const char *n;
    int8_t i=0;
    uint64_t out=0;
    if( !PyArg_ParseTuple(args, "s#", &n))
        return Py_None;
    i= strlen(n)-1;
    while( i >=0 ){
        out<<= 7;
        out|= n[i--] & 0x7f;
    }

    return PyLong_FromUnsignedLongLong( out);
}

static PyMethodDef CVarintMethods[] = {
    {"encode", cvarint_encode, METH_VARARGS, "Encode an integer as varint."},
    {"decode", cvarint_decode, METH_VARARGS,
     "Decode varint bytes to an integer."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef cvarintmodule = {
    PyModuleDef_HEAD_INIT, "cvarint",
    "A C implementation of protobuf varint encoding", -1, CVarintMethods};

PyMODINIT_FUNC PyInit_cvarint(void) { return PyModule_Create(&cvarintmodule); }
