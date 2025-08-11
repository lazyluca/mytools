PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT  = "718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391"

def pi_real(n):
    if n not in range(0, 100):
        print("Erro")
        return None
    pi_n = "3." + PI_INT[:n-1]
    return pi_n

def e_real(n):
    if n not in range(0, 100):
        print("Erro")
        return None
    e_n = "2." + E_INT[:n-1]
    return e_n

