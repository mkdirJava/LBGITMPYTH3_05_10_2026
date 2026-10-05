import multiprocessing as mp

#works - converting each int to a str
if __name__ == "__main__":
     with mp.Pool(4) as mp_pool:
         print(mp_pool.map(str, range(1,21)))

#won't work – we can't Pickle a lambda!
# if __name__ == "__main__":
#      with mp.Pool(4) as mp_pool:
#           print(mp_pool.map(lambda x: pow(x,3), range(1,21)))


import pathos.multiprocessing as pmp

if __name__ == "__main__":
    with pmp.Pool(4) as pmp_pool:
         print(pmp_pool.map(lambda x: pow(x,3), range(1,21)))
