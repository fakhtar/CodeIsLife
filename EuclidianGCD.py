def eclidian_GCD(a,b):
    if b ==0:
        return a
    else:
        return eclidian_GCD(b,a % b)

def naieve_GCD(a,b):
    GCD = 0
    for i in range(1,a+b):
        if (a % i) == 0 and (b % i) == 0:
            GCD = i
    return GCD

print(naieve_GCD(357,234))