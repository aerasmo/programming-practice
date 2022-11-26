class Calculator(object):
  def evaluate(self, string):
    operations = [{'*', '/'}, {'+', '-'}]
    exp = string.split()

    if len(exp) == 1:
        return float(exp[0])
    for y in range(len(operations)):  # operation in order
        for x in range(len(exp)):
            if exp[x] in operations[y]:
                new_exp = exp[:x-1] + [self.operation(exp[x], exp[x-1], exp[x+1])] + exp[x+2:]
                print(new_exp)
                return self.evaluate(' '.join(map(str, new_exp)))
                
  def operation(self, op, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '+':
        return num1 + num2
    else:
        return num1 - num2