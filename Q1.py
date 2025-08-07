# Write a function to which we pass a parameter and print the factors of a given number_attracting_components

def print_factors(num):     
    factors = []
    for i in range(1, num+1):
        if (num % i == 0):
            factors.append(i)
    return factors
num = int(input("Enter a number to find its factors"))
output=factors(num)
print(f"The factors of {num} are: {output}")



