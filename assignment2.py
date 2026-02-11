# factorial using recurssion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")


# word count find the number of words in a sentence
def word_count(sentence):
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
count = word_count(sentence)
print(f"The number of words in the sentence is: {count}")

#fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
