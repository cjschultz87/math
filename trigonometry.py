#https://mathworld.wolfram.com/PiFormulas.html

def piF(a):
    piVal = float(2*pow(3,0.5))
    index = 1
    #while index < a:
    #    piVal += float(pow(-1,index+1))/float((2*index - 1))
    #    index += 1
    #piVal *= 4
    
    while index <= a:
        piVal += float(2*pow(-1,index)*pow(3,float(1)/float(2)-index))/float(2*index+1)
        index += 1
    
    return piVal
    
def sqrt(a):
    strA = ""
    
    if type(a) == int:
        if not(len(str(a)) % 2 == 0):
            strA += "0"
    elif type(a) == float:
        index = 0
        
        while index < len(str(a)):
            if str(a)[index] == ".":
                if not((index-1) % 2 == 1):
                    strA += "0"
                break
            index += 1
                
    aN = len(strA)
                    
    

    index = len(strA)
    
  
    while index < aN + len(str(a)):
        if str(a)[index-aN] == ".":
            pass
        else:
            strA += str(a)[index-aN]
        index += 1
    
    if type(a) == float:
        index = 0
        
        while index < len(str(a)):
            if str(a)[index] == ".":
                aN = index
            index += 1
    
    index = 0
    
    while index < 50 - (len(str(a)) - aN):
        strA += "0"
        index += 1
        
    rVal = ""
    
    index = 1
    
    val_0 = ""
    val_1 = "0"
    val_2 = 0
    
    while index < len(strA) * 2:
    
    
        if index > 1:
            val_0 = str(int(val_0) - val_2)
    
        val_0 += strA[index-1:index+1]
        
        index_1 = 0
        
        while int(val_1 + str(index_1)) * index_1 <= int(val_0):
            index_1 += 1
        
        #while (int(val_1) * 10 + index_1) * index_1 < int(val_0):
         #   index_1 += 1
        
        index_1 -= 1
        
        rVal += str(index_1)[len(str(index_1)) - 1]
        
        val_2 = int(val_1 + str(index_1)) * index_1
        
        val_1 = str(2*int(rVal))
        
        index += 2
    
    index = 0
    
    rValPrime = ""
    
    while index < len(strA):
        if index == aN:
            rValPrime += "."
        rValPrime += rVal[index]
        index += 1
    
    return float(rValPrime)
    
pi = 3.1415926535897932384626433
    
unitCircumference = 2 * pi

unitQuad = pi / float(2)


#https://mathworld.wolfram.com/InverseTangent.html

def atan(a):
    rVal = 0
    
    if a <= 1:
        index = 0
    
        while index < 50:
            rVal += float(pow(-1,index) * pow(a,2*index + 1))/float(2*index + 1)
            index += 1
    else:
        rVal = 9
        rVal = 7 + ((16*pow(a,2))/rVal)
        rVal = 5 + ((9*pow(a,2))/rVal)
        rVal = 3 + ((4*pow(a,2))/rVal)
        rVal = 1 + ((pow(a,2))/rVal)
        rVal = a / rVal
    
    return rVal
    

def cos(a):
	cos = 1
	index = 0
	factorial = 1
	while index < 80:
		index_1 = 1
		factorial = 1
		while index_1 <= (index + 1) * 2:
			factorial *= index_1
			index_1 += 1

		cos += float(pow(-1,index+1) *pow(a,(index+1)*2))/float(factorial)
		index += 1
		
	return cos

#https://mathworld.wolfram.com/InverseCosine.html

def acos(a):
    #rVal = 0
    
    #index = 1
    
    #while index < 15:
     #   index_1 = 1
      #  if index < 2:
        #    factorial = 1
       # else:
         #   facotrial = 2
        
        #while index_1 < index:
         #   factorial *= index_1
          #  index_1 += 1
        
    #    rVal += (0.5*(index - 1) * pow(a,2*index - 1))/(factorial * 2*index - 1)
     #   index += 1
    
    #rVal = 0.5 * pi - rVal
    
    rVal = atan(sqrt(1 - pow(a,2))/float(a))
    
    return rVal
    
def sin(a):
	sin = a
	index = 0
	factorial = 1
	while index < 80:
		index_1 = 1
		factorial = 1
		while index_1 <= (index + 1) * 2 + 1:
			factorial *= index_1
			index_1 += 1
            
		sin += float(pow(-1,index+1) *pow(a,(index+1)*2 + 1))/float(factorial)
		index += 1
		
	return sin
    
def tan(a):
    return sin(a) / cos(a)
    
def csc(a):
    return float(1)/sin(a)
    
def cot(a):
    return float(1) / tan(a)
    
def sec(a):
    return float(1) / cos(a)