import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [False] * n

# 그래프를 인접 리스트 방식으로 표현하였습니다.
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


print(arr)
