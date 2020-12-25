def solve(arr, n):
    sums = [arr[i] for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                sums[i] = max(sums[i], sums[j]+arr[i])

    return max(sums)

# for each test case
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))
