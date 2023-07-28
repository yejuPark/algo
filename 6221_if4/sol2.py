import sys
sys.stdin = open('input.txt')

m1 = input()
m2 = input()

if m1 == '가위' and m2 == '가위':
    print('Result : Draw')
elif m1 == '바위' and m2 == '바위':
    print('Result : Draw')
elif m1 == '보' and m2 == '보':
    print('Result : Draw')

elif m1 == '가위' and m2 == '보':
    print('Result : Man1 Win!')
elif m1 == '바위' and m2 == '가위':
    print('Result : Man1 Win!')
elif m1 == '보' and m2 == '바위':
    print('Result : Man1 Win!')

elif m1 == '가위' and m2 == '바위':
    print('Result : Man2 Win!')
elif m1 == '바위' and m2 == '보':
    print('Result : Man2 Win!')
elif m1 == '보' and m2 == '가위':
    print('Result : Man2 Win!')
    