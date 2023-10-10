arr = []

n = int(input())
for i in range(n) :
    arr.append(int(input()))

for s in range(n-1) :

    for idx in range(1, n-s) :

        if arr[idx-1] > arr[idx] :

            temp = arr[idx-1]
            arr[idx-1] = arr[idx]
            arr[idx] = temp

for i in range(n) :
    print(arr[i])