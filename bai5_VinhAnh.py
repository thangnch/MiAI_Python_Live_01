import numpy

s = [6, 2, 5, 4, 8, 1, 7]

# Bien so
n_color = 0 # Bien dem so mau hien tai, khi du 7 thi la cau vong
n_rainbow = 0

rainbow_color = []
isYes = False
while True:
    isYes  =False
    # Lay danh sach cac mau da duoc xep giam dan
    indices = numpy.flip(numpy.argsort(s))

    for i in indices:
        if (s[i]>0) and (not (i in rainbow_color)):
            isYes = True
            rainbow_color.append(i)
            s[i] = s[i] - 1

            n_color = n_color + 1
            if n_color ==7:
                n_rainbow = n_rainbow + 1
                n_color = 0
                rainbow_color = []
                break # Thoat khoi for
    if not isYes :
        break

print(n_rainbow)

