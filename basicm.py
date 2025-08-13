# This function is used for the find the position of the any number of the fibonacci series
def fibo(n):
    if n <= 0:
        print('Incorrect input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# Take user input for the range
n = int(input('Enter the number to find the Fibonacci sequence: '))

# Print the result
result = fibo(n)
print(f"The {n}th term in the Fibonacci sequence is: {result}")

def fibo_series(n):
    a=[]
    if n<=0:
        print('Invalied input')
    elif n==1:
       a=[0]
    elif n==2:
        a=[0,1]
    else:
        a=[0,1]
        for i in range(2,n):
           a.append(a[i-1]+a[i-2])
    return a
n=int(input(' enter the number :'))

result=fibo_series(n)
print(result)

def prime_list(x, y):
    '''This function is used for creating the a prime number list  in specific range which is provided by the user'''
    prime_list = []

    for i in range(x, y + 1):  # Include y in the range
        if i < 2:
            continue
        else:
            for j in range(2, int(i/2) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)

    return prime_list

x = int(input('Enter the starting range: '))
y = int(input('Enter the ending range: '))
lst = prime_list(x, y)
print(lst)


def check_prime(n):
    ''' This function is used to check the given number is prime or not 
    '''
    if n>1:
        for i in range(2, int(n/2)+1):
            if n%i==0:
                print(f' This {n} number is not a prime number ')
                break
        else:
            print(f' This {n} number is  a prime number ')
    else:
        print('This number is not valide please enter the valide number')
n=int(input ('Enter the number to check the number is prime or not :'))
lw=check_prime( n)

def circle_area(r):
    '''This function finds the area of a circle'''
    pi = 3.142
    A = pi * (r * r)
    return A

# Get user input for the radius
r = float(input('Enter the radius of the circle: '))

# Call the function
area = circle_area(r)

# Print the result
print(f'The area of a circle with radius {r} is: {area}')

def arm_num(n):
    temp = n
    # Find the length of the input number to check if it's an Armstrong number
    pow = len(str(n))
    sum1 = 0

    while temp != 0:
        r = temp % 10
        sum1 = sum1 + r**pow
        temp = temp // 10

    if n == sum1:
        print(f'This number {n} is an Armstrong number.')
    else:
        print(f'This number {n} is not an Armstrong number.')

# Get user input for the number
n = int(input('Enter the number: '))

# Call the function
arm_num(n)
