import sys, traceback

try:
    open("some file name")
except IOError as err:
    tipe, val, tb = sys.exc_info()
    print("Exception lineno:", tb.tb_lineno)
    #traceback.print_exc()
#print("On we go!")