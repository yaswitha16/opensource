x,n=map(int,input().split())
max_capacity=x*100
if max_capacity>=n:
    additional_planes=0
else:
    additional_planes=(n-max_capacity+99)//100
print(additional_planes)
