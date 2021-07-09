def bin_search(s, e):

    m = (s + e) // 2
    if s > e:
        n_cut_tree = N - e
        remain_wood = M
        for i in range(s, N+1):
            remain_wood -= tree[i] - tree[s]
        if not remain_wood % n_cut_tree:
            return tree[s] - remain_wood // n_cut_tree
        else:
            return tree[s] - (remain_wood // n_cut_tree + 1)

    wood = 0
    for i in range(m+1, N+1):
        wood += tree[i] - tree[m]

    if wood == M:
        return tree[m]
    elif wood < M:
        return bin_search(s, m-1)
    else:
        return bin_search(m+1, e)

N, M = map(int, input().split())
tree = list(map(int, [0] + input().split()))
tree.sort()

print(bin_search(0, N))