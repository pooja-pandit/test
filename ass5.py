'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

def isPrime(number):
          
          if number > 1:

              for i in range(2,int(number**0.5)+1):
                     if (number % i) == 0:
                            return False
                            break
              else:
                 return True

s=0
for i in range(2000000):
            if isPrime(i):
               s=s+i
print(s)           
