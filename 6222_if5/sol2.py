import sys
sys.stdin = open('input.txt')

char = input()

result = []

if char.isupper():
    result = char.lower()
else:
    result = char.upper()

print(ord(char), char , ord(result), result)
