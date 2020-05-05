def input_int_positive():
    """
    Sanitizes input in instances that only a positive integer is supported
    """
    while True:
        try:
            helper = int(input())
        except ValueError:
            print("Please input a number!")
        else:
            if helper < 0:
                print("Please input a positive number!")
                helper = int(input())
            break
    return helper


def input_int_negative():
    """
    Sanitizes input in instances that only a negative integer is supported
    """
    while True:
        try:
            helper = int(input())
        except ValueError:
            print("Please input a negative number!")
        else:
            if helper > 0:
                print("Please input a negative number!")
                helper = int(input())
            break
    return helper


def input_int():
    """
    Sanitizes input in instances that only an integer is supported
    """
    while True:
        try:
            helper = int(input())
        except ValueError:
            print("Please input a number!")
        else:
            break
    return helper


