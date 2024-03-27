def modular_inverse(a, b):
    b_0 = b
    a_0 = a
    r_0 = 0 
    r = 1
    q = b_0 // a_0
    s = b_0 - q * a_0  

    while s > 0:
        temp = r_0 - q * r  
        if temp >= 0:
            temp = temp % b
        else:
            temp = b - ((-temp) % b)
        r_0 = r
        r = temp
        b_0 = a_0
        a_0 = s
        q = b_0 // a_0
        s = b_0 - q * a_0  

    if a_0 != 1:
        return None
    else:
        return r % b

def main():
    print("Find the multiplicative inverse of a number.")
    try:
        a = int(input("Enter the first number: "))  
        b = int(input("Enter the second number: ")) 

        if a<= 0 or b<=0:
            print("Invalid input. a and b must be positive integers.")

        if(a>b):
            a, b = b, a
        
        inverse = modular_inverse(a, b)
        if inverse is not None:
            print(f"The multiplicative inverse of {a} in mod {b} is: {inverse}")
        else:
            print(f"The number {a} has no inverse in modulo {b}")
    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()


