w=input ('가로:')
h=input ('세로:')


try:
    w=float(w)
    h=float(h)

except expression as identifier:
    pass

area=(w*h)
perimeter=(2*(w+h))
print('사각형의넓이:', area)
print('사각형의둘레:', perimeter)