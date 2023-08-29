def safe_print_list_integers(my_list=[], x=0):
    index = s = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index += 1
                s += 1
            else:
                print()
                return s
        except (ValueError, TypeError):
            index += 1
