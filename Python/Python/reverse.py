n=int(input("Enter the number"))
q=0
while(n>0):
    p=n%10
    q=q*10+p
    n=n // 10
print(q)
