
def missing(x):
    return sorted(set(range(x[0], x[-1])) - set(x))

x = [1,2,3,4,6,7,10] 
print(missing(x))
