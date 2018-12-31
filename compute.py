

def count_digit(n):
    count=0
    while n>0:
        r=n%10
        n=n//10
        count+=1
    return count

c=count_digit(1234)
print("count is: ",c)
