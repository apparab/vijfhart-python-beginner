for x in range(0, 128):
    to_print = [str(x).ljust(4), str(hex(x)).ljust(4), str(oct(x)).ljust(5)]
    if x > 32 and x < 127:
        to_print.append(chr(x))
    print(' '.join(to_print))
