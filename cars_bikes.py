
t=int(input("enter the test case no.:"))

for tir in range (1,t+1):
    n=int(input("enter no of tyre which is divisible by 4: "))
    if n%4==0 and n in range(2,1001):
        print("NO")
    b=n%4
    if b>1:
        print("YES")
    else:
        print("NO")
     