def test_arr(arr):
    num = set(arr)
    return len(arr) != len(num)
a = test_arr([1,2,3,4,5])
b = test_arr([1,1,2,2,3,3,4,4,5])
print("your wrong array is:-  {}  || and Right array is :-{}".format(a,b))