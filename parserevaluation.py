import math
from mathsparser import Parser

# Driver code
def calculate(expression):   # Evaluate function to parse and process result
    try:
        p = Parser(expression)
        value = p.getValue()
    except Exception as exp: 
        notify = exp.message
        raise Exception(notify)

    # Return input + answer 
    return expression + " = "+ str(value)


if __name__ == "__main__":
    print ("***************************\n")
    print ("Pratikbhai Patel Final Project \n")
    print ("CISC 603-51 - Theory of Computation \n")
    print ("Fall 2020  \n")
    print ("***************************\n")

    print (calculate("4+2"))
    print (calculate("(1 + 2) * 13"))
    print (calculate("(3-5)/4.0 + 0.0000"))
    print (calculate("6.0 / 5 * 16"))
    print (calculate("(5+7)*(1-5)"))
    # Now lets test our exception for an extra decimal point
    # print (calculate("-(7 + 2..4) * 31"))    # Only For Python2 Interpreters