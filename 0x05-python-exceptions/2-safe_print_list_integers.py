def safe_print_list_integers(my_list=[], x=0):
    value = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            value += 1
        except (ValueError, TypeError):
            continue
    print()
    return value
