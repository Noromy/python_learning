from multiprocessing import Pool


def cube(number):
    return number + number + number

if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    #map , apply, close
    result = pool.map(cube, numbers)
    result2 = pool.apply(cube, args=(3,)) # Only take one set of argmument
  

    pool.close()
    pool.join()

    print(result)
    print(result2)