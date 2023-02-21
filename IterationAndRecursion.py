def factrecursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factrecursive(num - 1)

def factiterative(num):
    fact = 1
    for number in range(2, num+1):
        fact = number * fact
    return fact
 
def main():
    print ("Factorial results using an interative function")
    print("0! =", factiterative(0))
    print("5! =", factiterative(5))
    print("10! =", factiterative(10))
    print("25! =", factiterative(25))
    print("50! =", factiterative(50))
    print("100! =", factiterative(100))
    print ("Factorial results using a recursive function")
    print("0! =", factrecursive(0))
    print("5! =", factrecursive(5))
    print("10! =", factrecursive(10))
    print("25! =", factrecursive(25))
    print("50! =", factrecursive(50))
    print("100! =", factrecursive(100))

if __name__ == "__main__":
    main()
