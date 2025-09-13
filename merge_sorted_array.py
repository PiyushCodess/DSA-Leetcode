def merge(num1, m, num2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if num1[i] > num2[j]:
            num1[k] = num1[i]
            i -= 1
        else:
            num1[k] = num2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        num1[k] = num2[j]
        j -= 1
        k -= 1


num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3
merge(num1, m, num2, n)
print(num1)