def add_numbers2 (number1 , number2):
    a = 0
    b = 0
    for number in range(1, number2 + 1):
        print(number)
        a = a + number
    print(a)
    for number in range(1, number1 + 1):
        print(number)
        b = b + number
    print(b)
    return a-b
