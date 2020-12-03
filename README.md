# Math parser project  ( IDE : VSCODE , Python version 2.7)

1) I have created 2 python files , a) mathparser.py and b) parserevaluation.py for my Parser project.

2) parserevaluation.py file has a driver code which will evaluate function from mathparser.py file and process its result.

3) mathparser.py is main program which takes an expression as string and then it converts it to char array. It will check each char in string and check if it is a number or an operator.

4) This program supports four basic math operations, functions, parentheses, and variables.

5) In each iteration we check for white space and skip it every time. Moreover, we have an exception for input data errors.


# Compiling from the source code

### Pre-requisite for build/run

- Any OS with Python2/ Pyhthon3 interpreter
- Any Python IDE ( I used VSCode) 

#### Running the Program 
Import project in VsCode or Pycharm and run the "parserevaluation.py"

You'll see the outputs for sample mathematical inputs. 


##### Exception Handling Testing

If you are running python2 then you can uncomment (remove # from #print) last line in  file "parserevaluation.py shown below or add your sample input to test Exception Handling

#print (calculate("-(7 + 2..4) * 31")) 
