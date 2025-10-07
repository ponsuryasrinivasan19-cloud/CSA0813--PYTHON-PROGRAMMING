num=list(map(int,input("").split(',')))
prime_count=0
composite_count=0
for n in num:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                composite_count+=1
                break
    else:
             prime_count+=1

print("composite count is:",composite_count)
print("prime count is:",prime_count)

#ascending order
a=list(map(int,input("").split(',')))
a.sort(reverse=True)
print(a)
