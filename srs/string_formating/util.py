def print_formatted(number):
    width = len(bin(number)) - 2  # length of binary representation without '0b'

    for i in range(1, number + 1):
        dec_str = str(i).rjust(width)
        oct_str = oct(i)[2:].rjust(width)          # remove '0o'
        hex_str = hex(i)[2:].upper().rjust(width)  # remove '0x' and uppercase
        bin_str = bin(i)[2:].rjust(width)          # remove '0b'

        print(dec_str, oct_str, hex_str, bin_str)
