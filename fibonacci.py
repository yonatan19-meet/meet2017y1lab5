##absolutely not fibonacci
a=0
def fib(nth):
    c=0
    b=1
    for number in range(0, nth+1):
        c=number+c
        b=b+c
    return b
