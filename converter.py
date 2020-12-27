class BinaryConverter():
    

    def binary_to_decimal(self):

        sum = 0
        value = input("Enter a binary value: ")

        for i, num in enumerate(reversed(value)):
                if num == '1':
                    sum = sum + 2 ** i

        print("Your answer is:", sum)
        print("\n")


    def binary_to_octal(self):

        sum = 0
        r = []

        value = input("Enter a binary value: ")

        for i, num in enumerate(reversed(value)):
            if num == '1':
                sum = sum + 2 ** i

        while sum // 8 != 0:
            q = sum // 8
            r.append(str(sum % 8))
            sum = q
        
        r.append(str(sum % 8))
        r.reverse()
        result = ''.join(r)
        octal = int(result)
        print("Your answer is:", octal)
        print("\n")


    def binary_to_hexadeciaml(self):
        
        sum = 0
        r = []

        value = input("Enter a binary value: ")

        for i, num in enumerate(reversed(value)):
            if num == '1':
                sum = sum + 2 ** i

        while sum // 16 != 0:
            q = sum // 16
            r.append(str(sum % 16))
            sum = q
        
        r.append(str(sum % 16))
        r.reverse()

        for i, num in enumerate(r):
            if num == '10':
                r[i] = 'A'
            elif num == '11':
                r[i] = 'B'
            elif num == '12':
                r[i] = 'C'
            elif num == '13':
                r[i] = 'D'
            elif num == '14':
                r[i] = 'E'
            elif num == '15':
                r[i] = 'F'


            hexa = ''.join(r)
            print("Your answer is:", hexa)
            print("\n")



    def binary_to_grey(self):

        value = input("Enter a binary value: ")
        value = list(value)
        value1 = list(value)

        for i in range(len(value)-1):
            value[i+1] = int(value1[i]) ^ int(value1[i+1])

        value = [str(x) for x in value]

        print(''.join(value))
        print("\n")



    def binary_to_bcd(self):

        sum = 0
        value = input("Enter a binary value: ")

        for i, num in enumerate(reversed(value)):
                if num == '1':
                    sum = sum + 2 ** i

        if (sum == 0) : 
                print("0000")
        
        rev = 0

        while (sum > 0) : 
            rev = rev * 10 + (sum % 10)
            sum = sum // 10

        while (rev > 0) : 

            binary = str(rev % 10)
            
            print("{0:04b}".format(int(binary, 16)), end = " ") 

            rev = rev // 10

                


    def binary_to_excess(self):

        sum = 0
        value = input("Enter a binary value: ")

        for i, num in enumerate(reversed(value)):
                if num == '1':
                    sum = sum + 2 ** i

        sum = list(str(sum))
        print(sum)

        for i in range(len(sum)):
            sum[i] = int(sum[i]) + 3

        print(sum)

        sum = [str(x) for x in sum]

        print(sum)

        for i in range(len(sum)):
        
            if sum[i] == '0':
                sum[i] = '0000'

            elif sum[i] == '1':
                sum[i] = '0001'

            elif sum[i] == '2':
                sum[i] = '0010'

            elif sum[i] == '3':
                sum[i] = '0011'

            elif sum[i] == '4':
                sum[i] = '0100'

            elif sum[i] == '5':
                sum[i] = '0101'

            elif sum[i] == '6':
                sum[i] = '0110'

            elif sum[i] == '7':
                sum[i] = '0111'

            elif sum[i] == '8':
                sum[i] = '1000'

            elif sum[i] == '9':
                sum[i] = '1001'

            elif sum[i] == '10':
                sum[i] = '1010'

            elif sum[i] == '11':
                sum[i] = '1011'

            elif sum[i] == '12':
                sum[i] = '1100'

            elif sum[i] == '13':
                sum[i] = '1101'

            elif sum[i] == '14':
                sum[i] = '1110'

            elif sum[i] == '15':
                sum[i] = '1111'

        print("".join(sum))

    
    
    def decimal_to_binary(self):

        value = int(input("Enter a decimal value: "))


        print(f"Your answer is: {value :b}")

    
    
    def octal_to_binary(self):

        value = input("Enter a octal value: ")

        octal = int(value, 8)


        print(f"Your answer is: {octal :b}")


    
    def hexadecimal_to_binary(self):

        value = input("Enter a hexadecimal value: ")

        hexa = int(value, 16)


        print(f"Your answer is: {hexa :b}")

    
    
    def grey_to_binary(self):

        value = input("Enter a binary value: ")
        value = list(value)

        for i in range(len(value)-1):
            value[i+1] = int(value[i]) ^ int(value[i+1])

        value = [str(x) for x in value]

        print(''.join(value))
        print("\n")


    
    
    def bcd_to_binary(self):

        value = input("Enter a BCD vale: ")
        check = 0 
        check0 = 0 
        num = 0 
        sum = 0 
        mul = 1 
        rev = 0 
        

        for i in range(len(value) - 1, -1, -1): 
            

            sum += (ord(value[i]) - ord('0')) * mul 
            mul *= 2 
            check += 1 
            

            if (check == 4 or i == 0): 
                if (sum == 0 and check0 == 0): 
                    num = 1 
                    check0 = 1 
                    
                else: 
                    

                    num = num * 10 + sum 
                    
                check = 0 
                sum = 0 
                mul = 1 
                

        while (num > 0): 
            rev = rev * 10 + (num % 10) 
            num //= 10 
            
        if (check0 == 1): 
            print("Your decimal value is:", rev - 1)
            print('\n')
            
        print("Your decimal value is:", rev)
        print('\n')


        print(f"Your answer is: {rev :b}")

    
    
    def excess_to_binary(self):
        
        value = input("Enter a excess-3 code: ")
        data = []


        if len(value) % 4 != 0:
            value = '0' * (4 - (len(value)%4)) + value

        for i in range(len(value), -1, -4):
            data.append(value[i:i+4])

        for i in range(len(data) - 1):
            if len(data[i]) == 0:
                data.remove(data[i])

        print(data)
        data.reverse()
        print(data)



        print(data)

        for i in range(len(data)):
        
            if data[i] == '0000':
                data[i] = '0'

            elif data[i] == '0001':
                data[i] = '1'

            elif data[i] == '0010':
                data[i] = '2'

            elif data[i] == '0011':
                data[i] = '3'

            elif data[i] == '0100':
                data[i] = '4'

            elif data[i] == '0101':
                data[i] = '5'

            elif data[i] == '0110':
                data[i] = '6'

            elif data[i] == '0111':
                data[i] = '7'

            elif data[i] == '1000':
                data[i] = '8'

            elif data[i] == '1001':
                data[i] = '9'

            elif data[i] == '1010':
                data[i] = '10'

            elif data[i] == '1011':
                data[i] = '11'

            elif data[i] == '1100':
                data[i] = '12'

            elif data[i] == '1101':
                data[i] = '13'

            elif data[i] == '1110':
                data[i] = '14'

            elif data[i] == '1111':
                data[i] = '15'

        print("".join(data))

        for i in range(len(data)):
            data[i] = int(data[i]) - 3
            if data[i] < 0:
                return "Invalid number"

        data = [str(x) for x in data]

        decimal = int("".join(data))
        print("Decimal value is:", decimal)

        r = []

        while decimal // 2 != 0:
            q = decimal // 2
            r.append(str(decimal % 2))
            decimal = q

        r.append(str(decimal % 2))
        r.reverse()
        result = ''.join(r)
        binary = int(result)
        print("Your answer is:", binary)