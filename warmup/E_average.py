n = int(input())
arr = list(map(int, input().strip().split()))
prefix = [0] * n
prefix[0] = arr[0]
# fill the prefix sum so we do not need to calcualte it everytime and 
# the array is already sorted
for i in range(1, n):
    prefix[i] += prefix[i - 1] + arr[i]

output = []
for i in range(n):
    # two special case on the sides and one for the rest
    if i == 0:
        output.append(
            prefix[-1] - prefix[0] - arr[0] * (n - 1)
        )
    elif i == n - 1:
        output.append(
            arr[-1] * (n - 1) - prefix[-2]
        )
    else:
        output.append(
            prefix[-1] - prefix[i] - arr[i] * (n - i - 1) + arr[i] * i - prefix[i - 1]
        )

print(*output)
