"""
Question 6 :
write a function to determine the HCF and LCM of n given numbers.
Input : HCF (32,16) , LCM (12,14)
Output : 16 , 84

"""

def hcf(x,y):
    list_hcf=[x,y]
    high = min(list_hcf)
    print(high)
    for i in range(1,high+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

print(hcf(32,16))

def lcm(x, y):
    list_lcm = [x,y]
    high = max(list_lcm)
    while(True):
    #  for i in range(1,high+1):
       if((high % x == 0) and (high % y == 0)):
           lcm = high
           print(lcm)
           break
       high = high + 1
    return lcm

print(lcm(12,14))

# Function to find HCF the Using Euclidian algorithm

def compute_hcf(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_hcf(x,y)
   return lcm

print(compute_hcf(32,16),compute_lcm(12,14))