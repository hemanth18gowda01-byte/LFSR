#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# GEFFE GENERATOR IMPLEMENTATION
# Author: Hemanth Gowda A
# This code implements the Geffe Generator, a type of pseudorandom number generator that combines three linear feedback shift registers (LFSRs) to produce a more secure output.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

key = int(input("Enter the key (in binary of 12 bits ): "),2)

k1,k2,k3=key>>8,(key>>4)&15,key&15

#-----------------------------------------------
# LFSR - 1 (primitive polynomial: x^4 + x + 1)
#-----------------------------------------------

list1=[]
def LFSR1(k1):
    
    reg1 = k1
    for i in range(15):
        bit4=(reg1>>3)&1
        bit1=(reg1>>0)&1
        list1.append(reg1&1)
        new_bit1=bit4^bit1

        reg1=(reg1>>1)|(new_bit1<<3)
        
    return (list1)
print(LFSR1(k1))
i1=0
for b in list1:
    i1=(i1<<1)|b
x1=(i1)
print(x1)

#--------------------------------------------------
# LFSR - 2 (primitive polynomial : x^4 + x^3 + 1)
#--------------------------------------------------

list2=[]
def LFSR2(k2):
    
    reg2 = k2
    for i in range(15):
        bit4=(reg2>>3)&1
        bit3=(reg2>>2)&1
        list2.append(reg2&1)
        new_bit2=bit4^bit3

        reg2=(reg2>>1)|(new_bit2<<3)
        
    return (list2)
print(LFSR2(k2))
i2=0
for b in list2:
    i2=(i2<<1)|b
x2=(i2)
print(x2)

#------------------------------------------------------------
# LFSR - 3 (primitive polynomial : x^4 + x^3 + x^2 + x + 1)
#------------------------------------------------------------

list3=[]
def LFSR3(k3):
    
    reg3 = k3
    for i in range(15):
        bit4=(reg3>>3)&1
        bit3=(reg3>>2)&1
        bit2=(reg3>>1)&1
        bit1=(reg3>>0)&1
        list3.append(reg3&1)
        new_bit3=bit4^bit3^bit2^bit1

        reg3=(reg3>>1)|(new_bit3<<3)
        
    return (list3)
print(LFSR3(k3))
i3=0
for b in list3:
    i3=(i3<<1)|b
x3=(i3)
print(x3)

#-------------------------------------------------
# TO MAKE IT NON - LINEAR USE POLYNOMIAL METHOD
# GEFFE GENERATOR (non-linear function 'f')
#-------------------------------------------------

KEY = (x1&x2)^(x2&x3)^(x3)
print(x1&x2,x2&x3)
print(KEY)




