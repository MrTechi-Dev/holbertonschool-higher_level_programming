#include <Python.h>
#include <stdio.h>
#include <wchar.h>
/**
 * print_python_string -  Basic information about Python bytes
 * @p: Pointer
 *
 * Return: NULL or address
 */
void print_python_string(PyObject *p)
{
	PyTypeObject *x =  p->ob_type;

	printf("[.] string object info\n");
	if (strcmp(x->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AS_UNICODE(p));
}
