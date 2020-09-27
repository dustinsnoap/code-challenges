# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:
# n = 15,
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

def fizzBuzz(n):
    out = []
    for num in range(1, n+1):
        if not num%15: out.append('FizzBuzz')
        elif not num%3: out.append('Fizz')
        elif not num%5: out.append('Buzz')
        else: out.append(str(num))
    return out
        
tmp = fizzBuzz(15)
for n in tmp: print(n)


