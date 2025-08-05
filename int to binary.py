#converts int to binary(method 1)
def decToBinary(self, n):
        # code here 
        res = ""
        while(n!=0):
            rem = n%2 
            if(rem == 1):
                res+="1"
            else:
                res+="0"
            n = n//2 
        return res[::-1]  

'''#conversion(method 2)
n=13
print(bin(n)[2::])'''



#binary to int
'''def binary_to_int(binary_str):
    decimal = 0
    power = 0
    for digit in reversed(binary_str):
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal
binary = input("Enter a binary number: ")
print("Decimal value is:", binary_to_int(binary))'''
 
