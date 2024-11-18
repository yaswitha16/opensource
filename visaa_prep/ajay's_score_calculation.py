t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    points_per_case=x//10
    total_score=points_per_case*n
    print(total_score)
