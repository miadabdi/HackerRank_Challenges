def print_formatted(number):
    # your code goes here
    width = len(str(bin(number))[2:]) + 1
    for num in range(1, number + 1):
        oct_num = str(oct(num))[2:].rjust(width, ' ')
        hexa_decimal = str(hex(num))[2:].upper().rjust(width, ' ')
        bin_num = str(bin(num))[2:].rjust(width, ' ')
        num = str(num).rjust(width - 1, ' ')
        print(num + oct_num + hexa_decimal + bin_num)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
