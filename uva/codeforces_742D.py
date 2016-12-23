from dp.utils import *


class Solution:
    def __init__(self):
        number_of_hoes, pairs, W = read_int_array()

        self.weights = read_int_array()
        self.beauties = read_int_array()
        self.rank = [0 for x in range(number_of_hoes)]
        self.parent = [0 for x in range(number_of_hoes)]
        for i in range(number_of_hoes):
            self.make(i)
        for i in range(pairs):
            a, b = read_int_array()
            self.merge(a - 1, b - 1)
        self.groups = [[] for _ in range(number_of_hoes)]
        for i in range(number_of_hoes):
            self.groups[self.find_parent(i)].append(i)
        self.group_beauty = []
        self.group_weight = []
        self.group_indices = []
        self.dp = [[-1 for x in range(max(number_of_hoes, W + 1))] for x in range(max(number_of_hoes, W + 1))]
        for i in range(number_of_hoes):
            lis = self.groups[i]
            if not lis:
                continue
            self.group_weight.append(sum(self.weights[x] for x in lis))
            self.group_beauty.append(sum(self.beauties[x] for x in lis))
            self.group_indices.append(i)

        self.max_index = len(self.group_indices)
        print self.solve(0, W)

    def solve(self, index, weight_left):
        if index >= self.max_index or weight_left <= 0:
            return 0

        if self.dp[index][weight_left] != -1:
            return self.dp[index][weight_left]

        ans = -99999999

        for person in self.groups[self.group_indices[index]]:
            if weight_left - self.weights[person] >= 0:
                ans = max(ans, self.beauties[person] + self.solve(index + 1, weight_left - self.weights[person]))

        ans = max(ans, self.solve(index + 1, weight_left))

        if weight_left >= self.group_weight[index]:
            ans = max(ans, self.group_beauty[index] + self.solve(index + 1, weight_left - self.group_weight[index]))

        self.dp[index][weight_left] = ans
        return ans

    def make(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)
        if parent_x != parent_y:
            rank_x = self.rank[x]
            rank_y = self.rank[y]
            if rank_x > rank_y:
                self.parent[parent_y] = parent_x
                self.rank[x] += 1
            else:
                self.parent[parent_x] = parent_y
                self.rank[y] += 1


if __name__ == '__main__':
    Solution()
