def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
num = 7;
print("factorial of",num,"is",factorial(num))
