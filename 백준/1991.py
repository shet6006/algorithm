def preorder(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if i != -1 and not visited[i] :
            visited[i] = True
            preorder(graph, i, visited)

    

graph = [[],[2,3],[4,-1],[5,6],[-1,-1],[-1,-1],[-1,7],[-1,-1]]
# a => b => d => X => X => X => c => e => f => X => g
n = 7
visited = [False] * (n + 1)
preorder(graph,1,visited)

import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(26)]  # A~Z

for _ in range(n):
    root, left, right = input().split()
    
    root = ord(root) - ord('A')
    
    if left == '.':
        left = -1
    else:
        left = ord(left) - ord('A')
        
    if right == '.':
        right = -1
    else:
        right = ord(right) - ord('A')
        
    tree[root] = [left, right]


def preorder(v):
    if v == -1:
        return
    print(chr(v + ord('A')), end='')
    preorder(tree[v][0])
    preorder(tree[v][1])


def inorder(v):
    if v == -1:
        return
    inorder(tree[v][0])
    print(chr(v + ord('A')), end='')
    inorder(tree[v][1])


def postorder(v):
    if v == -1:
        return
    postorder(tree[v][0])
    postorder(tree[v][1])
    print(chr(v + ord('A')), end='')


preorder(0)
print()
inorder(0)
print()
postorder(0)
