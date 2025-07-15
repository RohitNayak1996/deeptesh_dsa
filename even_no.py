'''
wap to check a given set of number from 0 to 100 including 0 and 100 is even or odd and
print the numbers in an organised manner. check whether the number is positive or negative
'''


def is_even(num):
    '''
    to check whether the number is even or odd
    Args:
        num:

    Returns:

    '''
    if num % 2 == 0:
        return True
    else:
        return False


def print_list_of_even_odd_and_positive_negative(start, end):
    result = 0
    max_so_far = float('-inf')
    for n in range(start, end):
        result = result + n
        if(max_so_far<n):
            print()
        else:
            print()
        if is_even(n) and is_positive(n):
            print(f"the number {n} is even and positive")
        elif is_even(n) and not is_positive(n):
            print(f"the number {n} is even and negative")
        elif not is_even(n) and is_positive(n):
            print(f"the number {n} is odd and positive")
        elif not is_even(n) and not is_positive(n):
            print(f"the number {n} is odd and negative")
    print(f"the sum of number from {start} to {end} is {result}" )

def is_positive(num):
    '''
    check whether the number is positive or not
    Args:
        num:

    Returns:

    '''
    if (num>=0):
        return True
    else:
        return False


if __name__ == '__main__':
    start = int(input("Enter 1st number: "))
    end = int(input("Enter 2nd number: "))
    print_list_of_even_odd_and_positive_negative(start, end)
