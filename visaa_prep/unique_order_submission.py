n=int(input())
arr=list(map(int, input().split()))
seen=set()
for num in arr:
    if num not in seen:
        print(num, end=' ')
        seen.add(num)
