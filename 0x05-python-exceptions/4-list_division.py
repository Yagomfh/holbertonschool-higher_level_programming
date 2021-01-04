#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(0, list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
            msg = ""
        except ZeroDivisionError:
            msg = "division by 0\n"
            result.append(0)
        except TypeError:
            msg = "wrong type\n"
            result.append(0)
        except IndexError:
            msg = "out of range\n"
            result.append(0)
        finally:
            print("{}".format(msg), end='')
    return result
