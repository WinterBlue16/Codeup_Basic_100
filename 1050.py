# 풀이 1
a, b = map(int, input().split())
print(int(a==b))

# 풀이 2
a, b = map(int, input().split())

def samornot(a, b):
    if a == b:
        return 1
    else:
        return 0
    
print(samornot(a, b))