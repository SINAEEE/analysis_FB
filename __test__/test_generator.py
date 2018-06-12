



def squares (n=10):
    results = []
    for i in range(n +1):
        yield i**2


for x in squares(10):  # TypeError: 'int' object is not iterable
    print(x)


"""
def squares (n=10):
    results = []
    for i in range(n+1):
        results.append(i**2)

    return results

#results = squares(10)
#for x in results: 
for x in squares(10):
    print(x)
"""


"""
def squares (n=10):
    for i in range(n+1):
        print(i)

squares()
"""