def generator(n):
    for i in range(n):
        yield i
x = generator(100)

print(next(x))
print(next(x))
