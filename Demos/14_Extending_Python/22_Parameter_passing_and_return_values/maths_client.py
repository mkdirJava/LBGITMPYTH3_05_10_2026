import mymathsmodule
print(mymathsmodule.__doc__)
print(mymathsmodule.square(4))
print(mymathsmodule.power(4,3))
t1 = (1,2,3,4)
t2 = (5,6,7,8)
mytup = mymathsmodule.join(t1,t2)
print(mytup)