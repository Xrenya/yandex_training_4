def merge(left, right):
    l = r = 0
    output = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1

    output.extend(left[l:])
    output.extend(right[r:])
    return output

_ = input()
left = list(map(int, input().strip().split()))
_ = input()
right = list(map(int, input().strip().split()))

print(*merge(left, right))
