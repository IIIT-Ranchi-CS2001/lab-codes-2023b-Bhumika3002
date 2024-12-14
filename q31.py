'''Write a python script to
Form a list of K random numbers within a limit N where K and N are set by the user. Minimum value of K should be 10.
Define a function (or two functions) to return the composite numbers and prime numbers of this list as two separate lists.
Determine the square of all prime numbers and square root of all composite numbers
Plot both prime numbers Vs their squares and composites Vs their square roots on the same figure object as scatterplots. ( two different subplots on the same figure object)
'''
import random
import math
import matplotlib.pyplot as plt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_and_separate(K, N):
    random_numbers = [random.randint(1, N) for _ in range(K)]
    
    primes = [num for num in random_numbers if is_prime(num)]
    composites = [num for num in random_numbers if not is_prime(num) and num > 1]
    
    return primes, composites

def calculate_squares_and_roots(primes, composites):
    prime_squares = [p**2 for p in primes]
    composite_roots = [math.sqrt(c) for c in composites]
    
    return prime_squares, composite_roots

def plot_data(primes, prime_squares, composites, composite_roots):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.scatter(primes, prime_squares, color='blue')
    ax1.set_title('Prime Numbers vs Their Squares')
    ax1.set_xlabel('Prime Numbers')
    ax1.set_ylabel('Squares of Prime Numbers')
    
    ax2.scatter(composites, composite_roots, color='red')
    ax2.set_title('Composite Numbers vs Their Square Roots')
    ax2.set_xlabel('Composite Numbers')
    ax2.set_ylabel('Square Roots of Composite Numbers')
    
    plt.tight_layout()
    plt.show()

def main(K, N):
    if K < 10:
        print("K should be at least 10.")
        return
    
    primes, composites = generate_and_separate(K, N)
    
    prime_squares, composite_roots = calculate_squares_and_roots(primes, composites)
    
    plot_data(primes, prime_squares, composites, composite_roots)

K = int(input("Enter the number of random numbers (K, minimum 10): "))
N = int(input("Enter the upper limit for the random numbers (N): "))

main(K, N)
