from ctypes import *

msvcrt = cdll.msvcrt
text = b"Hollow World!\n"
msvcrt.printf(b"%s", text)

mydll = cdll.LoadLibrary("C:\NQQ\Win32Dlls\DllModule7")
mydll.DllFunc7()
