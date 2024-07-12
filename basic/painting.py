width = float(input())
height = float(input())

area = width*height

# each liter of paint paints an area of ​​2 square meters.
ink_necess = area / 2

print(f'{ink_necess:.2f} liters of paint will be necessary to paint an area of {area} square meters.')