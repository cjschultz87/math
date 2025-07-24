import sys

input_val = sys.argv[1]

input_base = 0
output_base = 0

try:
    input_base = int(sys.argv[2])
except:
    print "must be able to cast input base using a base 10 integer"
    
    quit()
    
try:
    output_base = int(sys.argv[3])
except:
    print "must be able to cast output base using a base 10 integer"
    quit()
    
####################################

def digitArray(val):

    iota = []
    i = 0

    while i < len(val):
        maximal = i + input_val[i:len(val)].find(' ')
        if maximal < i:
            maximal = len(val)
        
        iota.append(val[i:maximal])
        i = maximal + 1
    
    for i_i,ival in enumerate(iota):
        try:
            iota[i_i] = int(ival)
            
        except:
            print "must be able to cast number digit from a base 10 integer"
        
            quit()
            
    return iota

#####################################

def atod(alpha,b):
    rVal = 0
    
    i = 0
    
    while i < len(alpha):
        rVal += alpha[i] * pow(b,len(alpha) - (1 + i))
        
        i += 1
    
    return rVal

#####################################

def divideArray(iota,b,mod):
    
    iota_r = []
    
    iota_1 = []
    
    for i in iota:
        iota_1.append(i)
    
    i_i = 0
    
    len_b = 0
    
    exec("len_b = len(\"%d\")" % (b))
    
    remainder = 0
    
    while i_i < len(iota_1):
        maximal = i_i + len_b
        if i_i + len_b > len(iota_1):
            maximal = len(iota_1)
        
        iota_prime = atod(iota_1[i_i:maximal],b)
        
        iota_r.append(iota_prime//b)
        
        if i_i < len(iota_1) - len_b:
            exec("iota_1[i_i+1] = %d%d" % (iota_prime % b,iota_1[i_i+1]))
        
        i_i += len_b
        
    if mod == 0:
        remainder = iota_1[len(iota)-1] % b
        
        return remainder

    elif mod == 1:
        while len(iota_r) > 1 and iota_r[0] == 0:
            iota_r.pop(0)
            
        return iota_r

#####################################

input = digitArray(input_val)

for i in input:
    if not(i < input_base) == True:
        print "digits of input value must be less than the input base"
        
        quit()

output = []

input_decimal = atod(input,input_base)

sierra = ""
    
exec("sierra = \"%d\"" % (input_decimal))
    
for s in sierra:
    output.append(int(s))

if output_base != 10:
    output_prime = []
    
    while output[0] > 0:
        output_prime.append(divideArray(output,output_base,0))
        
        output = divideArray(output,output_base,1)
        
    output = output_prime[::-1]
    
print output
