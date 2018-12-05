# Your optional code here
# You can import some modules or create additional functions
#num = 1229910
def sum_of_nums(num):
    num_str = str(num)
    if len(num_str)==1:
        return int(num_str)
    if len(num_str)>1:
        sum = 0
        for n in num_str:
            sum = sum + int(n)
        return sum_of_nums(sum)
        
#print(type(sum_of_nums(num)))


def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.
    num_str = str(number)
    div_by_5 = False
    div_by_3 = False
    result = num_str
    
    if num_str[-1]=='0' or num_str[-1]=='5':
        div_by_5 = True
        result = "Buzz"
    
    if sum_of_nums(number) in [3,6,9]:
        div_by_3 = True
        result = "Fizz"
        
    if div_by_5 and div_by_3:
        result = "Fizz Buzz"
    

    # replace this for solution
    return result

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
