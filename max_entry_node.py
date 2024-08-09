def maxim(n, edge):
    weight = [0] * n

   
    for i in range(n):
        if edge[i] != -1:
            weight[edge[i]] += i

   
    max_weight = -1
    max_index = -1
    for i in range(n):
        if weight[i] > max_weight:
            max_weight = weight[i]
            max_index = i

    return max_index


arr1 = [4, 4, 1, 4, 1, 3, 8 ,8 ,8, 0, 8, 14 ,9, 15, 11, -1, 10 ,15, 22, 22, 22, 22, 22, 21]
n = len(arr1)
print(maxim(n, arr1))
