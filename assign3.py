from math import gcd
def find_sum():
    sum=0
    for i in range(1000):
        if(i%3==0 or i%5==0):
            sum+=i
    return sum
res=find_sum()
#print(res)

'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

def find_fibo_sum():
    f1=1
    f2=2
    n=0
    sum=2
    while n<4000000:
        n=f1+f2
        f1=f2
        f2=n
        if(n%2==0):
            sum+=n
    return sum
#print(find_fibo_sum())

'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''
def large_palin():
    m=0
    b = False
    
    for i in range(999,100,-1):
       for j in range(i,100,-1):
           x=i*j
           #s=str(x)
           if x>m:
              s=str(x)
           if s==s[::-1]:
               m=int(s)
              
               
      
         
    print(m)
#large_palin()
          
'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

def lcm(a,b):
    lc=a*b//gcd(a,b)
    return lc
n=1    
for i in range(1,21):
   n=lcm(n,i)
print(n)
       
   
            

    

