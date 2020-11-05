import math

# Class Parser to read and perform math expressions
class Parser:
    def __init__(self, string): # Constructor
        self.string = string
        self.index = 0

    def getValue(self): # Returns final answer
        value = self.parseInput()
        self.skipSpace()
        
        if self.hasNext(): # Exception if any more characters left in expression
            raise Exception(
                "Found an unexpected character: '" + self.peek() + "' at index " + str(self.index)
            )
        return value

    def peek(self): # Returns value of next character in the equation, without incrementing index
        return self.string[self.index:self.index + 1]

    def hasNext(self): # Returns true if any more characters left in equation, else false if none left
        return self.index < len(self.string)

    def skipSpace(self):   # Skip space in each iteration
        while self.hasNext():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return

    def parseInput(self): # Initiating the Char/Input Check
        return self.parseAddition()
    
    def parseAddition(self):  # Function for Addition and Substraction 
        values = [self.parseMultiplication()] # each element in values array to be added
        
        while True: # While loop to iterate through expression char by char
            self.skipSpace() # skip empty space
            char = self.peek() # next char in expression
            
            if char == '+':
                self.index += 1
                values.append(self.parseMultiplication()) # Add value to values array
            elif char == '-':
                self.index += 1
                values.append(-1 * self.parseMultiplication()) # make the resultant number negative
            else:
                break
        
        return sum(values) # sum of all numbers in values array

    def parseMultiplication(self):  # Function for Multiplication and Division
        values = [self.parseParenthesis()] # each element in values is solution of parenthesis 
            
        while True:
            self.skipSpace() # skip empty space
            char = self.peek() # get next character
                
            if char == '*':
                self.index += 1
                values.append(self.parseParenthesis())
            elif char == '/':
                div_index = self.index
                self.index += 1
                denominator = self.parseParenthesis()
                     
                if denominator == 0:
                    raise Exception(
                        "Exception for dividing with 0 (occured at index " + str(div_index) + ")"
                    )
                values.append(1.0 / denominator)
            else:
                break
        value = 1.0
        
        for factor in values:
            value *= factor
        return value

    def parseParenthesis(self):   # Reading Paranthesis and parsing it' value
        self.skipSpace()
        char = self.peek()
        
        if char == '(':
            self.index += 1
            value = self.parseInput()
            self.skipSpace()
            
            if self.peek() != ')':
                raise Exception(
                    "Closing parenthesis not found " + str(self.index)
                )
            self.index += 1
            return value
        else:
            return self.parseMinusSign()

    def parseMinusSign(self):    # Function for minus sign/ negative value
        self.skipSpace()
        char = self.peek()
        
        if char == '-':
            self.index += 1
            return -1 * self.parseParenthesis()
        else:
            return self.parseValue()

    def parseValue(self):    #Function to define/parse Numbers 
        self.skipSpace()
        char = self.peek()
        
        if char in '0123456789.':
            return self.parseNumber()
 
    def parseNumber(self):    # Function to parse numbers with exceptions
        self.skipSpace() 
        strValue = ''
        decimal_found = False # flag to check for decimal values
        char = ''

        while self.hasNext():
            char = self.peek()            
            
            if char == '.':
                if decimal_found:
                    raise Exception(
                        "Found an additional decimal point " + str(self.index)
                    )
                decimal_found = True
                strValue += '.'
            elif char in '0123456789':
                strValue += char
            else:
                break
            self.index += 1

        if len(strValue) == 0:
            if char == '':
                raise Exception("Unexpected end found")
            else:
                raise Exception(
                    "Anticipating a digit at character " + str(self.index) + " but found a " + char)
        return float(strValue)