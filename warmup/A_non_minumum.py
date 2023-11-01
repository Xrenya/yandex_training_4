# The idea is to use the segment tree which maintain the 
# minimum and maximum since it does not matter which value to 
# return
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))


class Tree:
    def __init__(self, array):
        self.n = len(array)
        self.build(array)

    def build(self, array):
        self.min_tree = [float("inf") for _ in range(2 * self.n - 1)]
        self.max_tree = [-float("inf") for _ in range(2 * self.n - 1)]
        for i in range(self.n):
            # fill the last elements in the array without changes
            self.min_tree[self.n - 1 + i] = array[i]
            self.max_tree[self.n - 1 + i] = array[i]

        for i in range(self.n - 2, -1, -1):
            # fill upper elements in upper tree with min and max in subarray
            self.min_tree[i] = min(self.min_tree[2 * i + 1], self.min_tree[2 * i + 2])
            self.max_tree[i] = max(self.max_tree[2 * i + 1], self.max_tree[2 * i + 2])

    def query(self, i, j):
        cur = float("inf")
        result = -float("inf")
        # set the pointer into new range query since the array now is a tree 
        i += self.n - 1
        j += self.n - 1

        while i <= j: # iterate over the tree to select min and max in requested range
            if i % 2 == 0:
                cur = min(cur, self.min_tree[i])
                result = max(result, self.max_tree[i])
            if j % 2 == 1:
                cur = min(cur, self.min_tree[j])
                result = max(result, self.max_tree[j])

            i = i // 2
            j = j // 2 - 1
        return result if (result != cur and result != float("inf") and cur != float("inf")) else "NOT FOUND"

tree = Tree(arr)
for _ in range(m):
    l, r = map(int, input().strip().split())
    print(tree.query(l, r))
