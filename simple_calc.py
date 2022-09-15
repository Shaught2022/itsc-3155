# Class for simple calculator
class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operation = ''
        self.result = 0
        self.on = True

    def calculate(self):
        if self.operation == '+':
            self.result = self.num1 + self.num2
        elif self.operation == '-':
            self.result = self.num1 - self.num2
        elif self.operation == '*':
            self.result = self.num1 * self.num2
        elif self.operation == '/':
            self.result = self.num1 / self.num2
        else:
            print('Invalid operation')

    def set_num1(self, num1):
        self.num1 = num1

    def set_num2(self, num2):
        self.num2 = num2

    def get_nums(self):
        if self.operation in '+-*/':
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))
            # Use the setter methods to assign values to num1 and num2
            self._setnum1 = num1
            self._setnum2 = num2
        else:
            print('Invalid operation')

    def get_user_input_operation(self):
        operation = input(
            'Simple Operators (+, -, *, /)\nEnter operation: ')
        return operation

    def set_operation(self):
        # Call the get_user_input_operation method
        # Assign the result to the operation variable
        self.get_user_input_operation()

        if self.operation == '+':
            self.result = self.num1 + self.num2
        if self.operation == '-':
            self.result = self.num1 - self.num2
        if self.operation == '*':
            self.result = self.num1 * self.num2
        if self.operation =='/':
            self.result = self.num1 / self.num2

    def get_result(self):
        return self.result

    def continue_prompt(self):
        continue_check = input('Do you want to continue? (y/n): ')
        if continue_check == 'y':
            self.num1 = 0
            self.num2 = 0
        elif continue_check == 'n':
            self.on = False
        else:
            print('Invalid input')
            self.continue_prompt()

    def run(self):
        while self.on:
            self.set_operation()
            self.get_nums()
            self.calculate()
            print(self.result)
            self.continue_prompt()
        print('Goodbye')

if __name__ == '__main__':
    calc = Calculator()
    calc.run()