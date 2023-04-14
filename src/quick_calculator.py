# Define functions to create a calculator
# Define +,-,/,*
# Make this code a class
# Use this class to start using calculator which is function_oper()
class Calculator:
    def __init__(self):
        self.i = float(input("Quick Calculator\nEnter a number: "))

    def sum_oper(self,x):
        return self.i + x
    def subs_oper(self, x):
        return self.i - x
    def div_oper(self,x):
        return self.i / x
    def multi_oper(self,x):
        return self.i * x
    # Review code above and is fine, 
    # Issue starts below
    def function_oper(self):
        while True:
            print(f"\nCurrent value = {self.i}")
            print("Select operation - \n1. (+) Add\n2. (-)Subst\n3. (/) division\n4. (*) Multi\n5. print last value and Exit")
            operation = input("Operation: ")

            if operation == '1':
                x=float(input("Enter number: "))
                self.i = self.sum_oper(x)
                print(self.i)
            elif operation == '2':
                x=float(input("Enter number: "))
                self.i = self.subs_oper(x)
                print(self.i)
            elif operation == '3':
                x=float(input("Enter number: "))
                self.i = self.div_oper(x)
                print(self.i)
            elif operation == '4':
                x=float(input("Enter number: "))
                self.i = self.multi_oper(x)
                print(self.i)
            elif operation == '5':
                print("last value or result: ")
                print(self.i)
                break
            else:
                print(self.i)
                print("Operation not found, 'please try again' ")    
    
c=Calculator()
c.function_oper()