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

#conversion(method 2)
n=13
print(bin(n)[2::])

