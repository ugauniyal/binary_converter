from converter import BinaryConverter
import shutil


def start(binary):

    print("What type of conversion system you want to use? (1-2)")
    print("\n")
    print("1. Binary To Other \n2. Others To Binary")
    print("\n")

    ask = int(input("Your choice? "))
    print("\n")
    

    if ask == 1:

        print("Which conversion system you want to use?")
        print("\n")
        print("1. Binary To Decimal \n2. Binary To Octal \n3. Binary To Hexadecimal \n4. Binary To Grey Code \n5. Binary To BCD \n6. Binary To Excess-3 Code (1-6)")
        print("\n")

        ask1 = int(input("Your choice? "))
        print("\n")

        if ask1 == 1:
            binary.binary_to_decimal()

        elif ask1 == 2:
            binary.binary_to_octal()

        elif ask1 == 3:
            binary.binary_to_hexadeciaml()

        elif ask1 == 4:
            binary.binary_to_grey()

        elif ask1 == 5:
            binary.binary_to_bcd()

        elif ask1 == 6:
            binary.binary_to_excess()

        else:
            print("\n")
            print("Please choose between the given option")
            print("\n")
            start(binary)
            print("\n")


    elif ask == 2:
        print("Which conversion system you want to use?")
        print("\n")
        print("1. Decimal To Binary \n2. Octal To Binary \n3. Hexadecimal To Binary \n4. Grey Code To Binary \n5. BCD To Binary \n6. Excess-3 Code To Binary (1-6)")
        print("\n")

        ask2 = int(input("Your choice? "))

        if ask2 == 1:
            binary.decimal_to_binary()

        elif ask2 == 2:
            binary.octal_to_binary()

        elif ask2 == 3:
            binary.hexadecimal_to_binary()

        elif ask2 == 4:
            binary.grey_to_binary()

        elif ask2 == 5:
            binary.bcd_to_binary()

        elif ask2 == 6:
            binary.excess_to_binary()

        else:
            print("\n")
            print("Please choose between the given option")
            print("\n")
            start(binary)
            print("\n")

    else:
        print("\n")
        print("Please choose between the given option")
        print("\n")
        start(binary)
        print("\n")




binary = BinaryConverter()
choice = 'Y'
while choice == 'Y' or choice == 'y':
    columns = shutil.get_terminal_size().columns
    print("Binary Converter".center(columns))
    start(binary)
    choice = input('Do you want to use the converter again? (Y/N)')
    print('\n')