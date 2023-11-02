# should be partition instead of binary search
def search(arr, target):
    if not arr:
        return "\n".join(map(str, [0, 0]))
    arr.sort()
    l = -1
    r = len(arr)
    while l < r - 1:
        m = l + (r - l) // 2
        if arr[m] < target:
            l = m
        else:
            r = m
    l_count = l + 1
    r_count = len(arr) - l_count
    return "\n".join(map(str, [l_count, r_count]))
        
n = int(input())
arr = list(map(int, input().strip().split()))
target = int(input())
print(search(arr, target))
