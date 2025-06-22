def dtb(d,block):
    if not(type(d) == type(5) and type(block) == type(5)):
        return []
    delta = []
    d_prime = d
    i = 0
    iota = 0
    while d_prime > 0:
        if i % block == 0:
            delta.append([])
        digit = d_prime % 2
        if i // block > iota:
            iota = i // block
        delta[iota].append(digit)
        if d_prime // 2 == 0 and len(delta[iota]) < block:
            while len(delta[iota]) < block:
                delta[iota].append(0)
        i += 1
        d_prime //= 2
    #for i,block in enumerate(delta):
    #    delta[i] = block[::-1]
    #delta = delta[::-1]
    return delta

################################################

def check_blocks(bravo_1,bravo_2):
    bool = True
    if len(bravo_1) > 0 and len(bravo_2) > 0:
        for b in bravo_1:
            if len(b) == 0:
                bool = False
            if type(b) != type([]):
                bool = False
            for b_1 in b:
                if type(b_1) != type(2) or b_1 > 1:
                    bool = False
        for b in bravo_2:
            if len(b) == 0:
                bool = False
            if type(b) != type([]):
                bool = False
            for b_2 in b:
                if type(b_2) != type(2) or b_2 > 1:
                    bool = False
    else:
        bool = False
    return bool
    
################################################

def block_sum(bravo_1,bravo_2):
    if check_blocks(bravo_1,bravo_2) == True:
        pass
    else:
        return []
    alpha = []
    i_1 = 0
    i_2 = 0
    n_1 = len(bravo_1) * len(bravo_1[0])
    n_2 = len(bravo_2) * len(bravo_2[0])
    block_1 = len(bravo_1[0])
    block_2 = len(bravo_2[0])
    N = 0
    if n_1 > n_2:
        N = n_1
        i = n_2
        iota = i // block_2
        while i < n_1:
            if i % block_2 == 0:
                bravo_2.append([])
            if i // block_2 > iota:
                iota = i // block_2
            bravo_2[iota].append(0)
            i += 1
    elif n_1 < n_2:
        N = n_2
        i = n_1
        iota = i // block_1
        while i < n_2:
            if i % block_1 == 0:
                bravo_1.append([])
            if i // block_1 > iota:
                iota = i // block_1
            bravo_1[iota].append(0)
            i += 1
    else:
        N = n_1

    i = 0
    iota = 0
    carry = 0
    bool = False
    while i < N:
        if i % block_1 == 0:
            alpha.append([])
        if i // block_1 > iota:
            iota = i // block_1
        if bool == False:
            digit = (bravo_1[i//block_1][i%block_1]^bravo_2[i//block_2][i%block_2])
            
            conjunction = bravo_1[i//block_1][i%block_1] & bravo_2[i//block_2][i%block_2]
            
            if i > 0:
                alpha[iota].append(carry^digit)
                #carry = carry & digit
                if carry > 0:
                    carry = (carry & conjunction) | (carry & digit)
                else:
                    carry = conjunction
            else:
                alpha[iota].append(digit)
                carry = conjunction
        else:
            alpha[iota].append(carry)
            while len(alpha[iota]) < block_1:
                alpha[iota].append(0)
            carry = 0
        if i == N - 1 and carry > 0:
            N += 1
            bool = True
        i += 1
    return alpha
        
    
################################################
    
def block_product(bravo_1,bravo_2):
    if check_blocks(bravo_1,bravo_2) == True:
        pass
    else:
        return []
    
