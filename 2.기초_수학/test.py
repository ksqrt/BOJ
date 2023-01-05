
import sys
input = sys.stdin.readlines()


def fun1(n):
    # n은 1이며 0으로 나누어지지 않을시마다 문자열로 만들어 1을 추가함
    # ex 1 -> 11 -> 111 이런식으로 구성
    divider = 1
    while (True):
        if divider % n == 0:
            return len(str(divider))
            break
        else:
            divider = int(str(divider)+"1")


while True:
    try:
        n = int(input())
        print(fun1(n))
    except:
        break
