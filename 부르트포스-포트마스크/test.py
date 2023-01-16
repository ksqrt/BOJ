# 11723 번 집합

import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
n = int(input())

empty_set = set()

while (n != 0):
    command = input().split()
    if len(command) > 1:
        num = int(command[1])
    command = command[0]

    if command == "add":
        # num 이 집합 안에 없으면 append
        # if num not in empty_set:
        # set 은 중복 허용을 하지않아 if 문으로 찾을 필요 없음
        empty_set.add(num)
    elif command == "remove":
        # num 이 집합 안에 있으면 remove
        # if num in empty_set:
        empty_set.discard(num)
    elif command == "check":
        # num 이 집합안에 있으면 1 출력 아님 0
        if num in empty_set:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        # num 이 집합안에 있으면 제거
        if num in empty_set:
            empty_set.discard(num)
        # 없으면 추가
        else:
            empty_set.add(num)

    elif command == "all":
        empty_set = set([i for i in range(1, 21)])
    elif command == "empty":
        empty_set = set([])

    n -= 1
