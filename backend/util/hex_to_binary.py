HEX_TO_BINARY_CONVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def hex_to_binary(hex):
    binary_string = ''

    for c in hex:
        binary_string += HEX_TO_BINARY_CONVERSION_TABLE[c]

    return binary_string

def main():
    number = 451
    hex_number = hex(number)

    print(f'Hex number: {hex_number}')

if __name__ == '__main__':
    main()
