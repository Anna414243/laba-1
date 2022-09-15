def count_zero(number):
    number = str(number)
    return len(number) - len(number.rstrip('0'))
print(count_zero(1000100))
