from ast import Expression

from numpy import iterable

class Solution:

    def fizzBuzz(self, n: int) -> list[str]: 
        ans = []

        for num in range(1,n+1):
            num_ans_str = ""

            if num % 3 == 0:
                num_ans_str += "Fizz"
            if num % 5 == 0:
                num_ans_str += "Buzz"
            if not num_ans_str:
                num_ans_str = str(num)

            ans.append(num_ans_str)  

        return ans
    #------------------------------------------------------
        n = int(input("nhap so: ") 
        for fizzbuzz in range(n):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        #if fizzbuzz % 15 == 0: 
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)
