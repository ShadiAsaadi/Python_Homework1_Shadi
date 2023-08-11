############### The first question ###############
import math
Number = int(input("Please enter a number: "))
prime_numbers_list = [2]
def get_number(Number):
 if Number == 2:
  sum_prime_numbers == 0 
 for j in range(3, Number):
    for i in range(2, j):
      if math.remainder(j, i) == 0:
       break
    else:
     prime_numbers_list.append(j)
 sum_prime_numbers = sum(prime_numbers_list) 
 print("sum of prime numbers: ", sum_prime_numbers)      
get_number(Number)