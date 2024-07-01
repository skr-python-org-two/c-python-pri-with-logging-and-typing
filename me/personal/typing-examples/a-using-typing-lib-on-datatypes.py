import typing


def typing_on_variables():
    print("### from main function in typing-on-datatypes.py file")
    num_one: int = 25
    float_one: float = 12.5
    str_one: str = "first string"
    print("type of num_one is ::: {0} {1}    ".format(type(num_one) , num_one))
    print("type of float_one is ::: {0} {1}   ".format(type(float_one) , float_one))
    print("type of str_one is ::: {0} {1}   ".format(type(str_one) , str_one))
    num_one= 99.77
    float_one= "abc"
    str_one= 15

    print("type of num_one is ::: {0} {1}  ".format(type(num_one) , num_one))
    print("type of float_one is ::: {0} {1} ".format(type(float_one) , float_one))
    print("type of str_one is ::: {0} {1} ".format(type(str_one) , str_one ))

def main():
    typing_on_variables()


if __name__ == "__main__":
    main()


