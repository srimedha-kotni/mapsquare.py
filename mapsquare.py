def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print("square of numbers:",squared)