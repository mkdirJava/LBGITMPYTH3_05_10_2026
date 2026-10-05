a = 1
b = 0
try:
    x = a/b
except:
    import dis, sys
    tb = sys.exc_info()[2]
    dis.distb(tb)
