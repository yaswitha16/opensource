n,m=map(int, input().split())
arr=list(map(int, input().split()))
sum1=0
sum2=0
for num in arr:
    if num%m==0:
        sum1+=num
    else:
        sum2+=num
print(sum1-sum2)
