# ((())) : valid expression
# ()))) : invalid expression

expression = input()

opened = '('
closed = ')'

if opened in expression:
    qo = expression.count(opened)
if closed in expression:
    qc = expression.count(closed)

if qo != qc:
    print('Invalid expression!')
else:
    print('Valid expression!')

# OTHER WAY

expr = (input())
stack = []

for symb in expr:
    if symb == '(':
        stack.append('(')
    elif symb == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')

if len(stack) == 0:
    print('Valid expression!')
else:
    print('Invalid expression!')