print('-'*50)
print(' '*20 + 'PRICE LIST')
print('-'*50)

products = ('Pencil', 1, 'Rubber', 0.75, 'Notebook', 5.50, 'Pencil case', 3.5, 'Book', 10, 'Pens', 4, 'Bag', 50)

for prod in range(len(products)):
    if prod % 2 == 0:
        print(f'{products[prod]:.<30}', end='') # specification goes to the left
    else:
        print(f'$ {products[prod]:>5.2f}') # specification goes to the right
print('-'*50)