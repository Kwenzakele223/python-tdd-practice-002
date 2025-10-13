"""
The Fibonacci sequence is a series of numbers where each number 
is the sum of the two preceding ones, starting from 0 and 1.
The sequence looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The function below receives an integer n, which represents the n-th term 
of the sequence, and must return a list from the first value up to the n-th term.

Example:
    n = 3
    return [0, 1, 1]
"""
def fibonacci(num: int) -> list[int]: # what does this line do:
    first_fibonacci = 0
    second_fibonacci = 1
    list_fibo = [first_fibonacci, second_fibonacci]
  

    if num <= 0: #checks if the nth the is not less then 0 
        raise ValueError
    elif num == 1: #if the nth term is 1 you must output first_fibonacci
       return first_fibonacci
    else:
        while  len(list_fibo) < num:
            n= list_fibo[- 1] + list_fibo[-2]
            list_fibo.append(n)
        return list_fibo


"""
The function below receives a list of numbers (nums) 
and returns a list of even numbers from nums in ascending order.

Example:
    nums = [1, 3, 2, 27, 50, 17, 8, 4, 98, 22]
    return [2, 4, 8, 22, 50, 98]
"""
def even(nums: list[int]) -> list[int]: 
    count = 0
    even_list = []
    for i in nums:
        if i % 2 == 0:
            even_list.append(i)
            count = count + 1
    print(len(even_list))
    return even_list

    


"""
The function below receives a list of numbers (nums) 
and returns a list of odd numbers from nums in descending order.

Example:
    nums = [1, 3, 2, 27, 50, 17, 8, 4, 98, 22]
    return [27, 17, 3, 1]
"""
def odd(nums: list[int]) -> list[int]:
    count = 0
    odd_list = []
    for i in nums:
        if i % 2 == 1:
            odd_list.append(i)
            count = count + 1
            
    print(len(odd_list)) 
    return odd_list[::-1]


"""
This function receives a list of numbers (nums)
and returns a string that says:

 * 'Odd'  if the sum of odd numbers is greater than the sum of even numbers.
 * 'Even' if the sum of even numbers is greater than the sum of odd numbers.
 * 'Tie'  if both sums are equal.

Example:
    nums = [1, 2, 3]
    sum(odd) = 4, sum(even) = 2 → returns 'Odd'
"""
def even_vs_odd(nums: list[int]) -> str:
    for i in nums:
        if i % 2 == 0:
            sum_even = sum(i)
            return sum_even
    return ""


"""
This function checks if 'n' is a prime number.

It should:
 * Return True if n is prime, False otherwise.
 * Raise a ValueError if n is negative or not an integer.

Example:
    is_prime(7) → True
    is_prime(10) → False
    is_prime(-3) → raises ValueError
"""
def is_prime(n):
    return False


"""
This function takes in a fullname, short year, 
and campus code ('jhb' or 'cpt') to generate a WeThinkCode_ email address.

Example:
    Input: ('Auston Mtabane', '2024', 'jhb')
    Output: 'aumtajhb024@student.wethinkcode.co.za'

Hint:
    - Use lowercase letters.
    - Look at the pattern of the example carefully.
"""
def generate_email(fullname: str, year: str, campus: str) -> str:
    *name, surname = fullname.split()
    name_1 = name[0]
    name_1.lower()

    return f'{name_1[0:2]}{surname.lower()[0:3]}{campus}{year[1:4]}@student.wethinkcode.co.za'





# print(even([1,2,3,4,6]))
# print(odd([1,2,3,7]))
print(fibonacci(5))
# print(even_vs_odd([1,2,3,8,5]))
print(generate_email('Oriel Kopano Dibakoane','2027','cpt'))