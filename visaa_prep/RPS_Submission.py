V,C=input().split()
if(V=='R' and C=='P')or (V=='P' and C=='S') or (V=='S' and C=='R'):
    print("Charan")
elif(C=='R' and V=='P') or (C=='P' and V=='S')or (C=='S' and V=='R'):
    print("Vignesh")
else:
    print("NULL")
