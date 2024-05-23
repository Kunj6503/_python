a = [1,2,3,4,5]

def sum_array(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum

total = sum_array(a)
print(total)