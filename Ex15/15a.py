def fibo(max_val):
    yield 0
    a = 0
    b = 1
    while b < max_val:
        yield b
        a, b = b, a + b


for val in fibo(250):
    print(val)
