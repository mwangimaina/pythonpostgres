import math ,statistics
#above we import the math module
# check the 'module' functions using dir

print(dir(statistics))

print(math.gcd(8,2))
print(math.sqrt(25))
print(math.factorial(3))

x = [56,67,65,44,33,22,44,33,22,89,88]

m = statistics.mean(x)
print("Mean ", m)
print("Median ", statistics.median(x))
print("Variance ", statistics.variance(x))









