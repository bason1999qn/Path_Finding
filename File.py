from Map import *
def Input(fileName, map):
    # ma tran co kich thuoc: X x Y
    x = 0
    y = 0
    # Diem bat dau A, diem ket thuc B
    xa = xb = 0
    ya = yb = 0
    # p: So da giac
    p = 0
    file = open(fileName, "r")
    # t_line: dem so dong trong file
    t_line = 0

    # Luu cac diem don
    listTemp = []
    for line in file:
        s = 0
        t_line += 1  # So dong cua file txt
        # Neu doc dong dau tien cua file chua x,y
        if t_line == 1:
            t = 0
            for numxy in line.strip().split(','):
                s = int(numxy)
                t += 1
                if t == 1:
                    x = s
                if t == 2:
                    y = s
        # Neu doc dong 2 cua file chua toa do diem bat dau, diem ket thuc
        if t_line == 2:
            t = 0
            for numxy in line.strip().split(','):
                s = int(numxy)
                t += 1
                if t == 1:
                    xa = s
                if t == 2:
                    ya = s
                if t == 3:
                    xb = s
                if t == 4:
                    yb = s

                # Khoi tao thong so cho Map
                map.setMap(x, y, p, xa, ya, xb, yb)

                if (t > 4):
                    if (t % 2 == 1):
                        xtemp = s
                    else:
                        ytemp = s
                        listTemp.append((xtemp, ytemp))
                    map.setDon(listTemp)

                # Tao ma tran x*y
                matrix = createMatrixEmpty(map)

        # Neu doc dong 3 cua file chua so hinh da giac
        if t_line == 3:
            p = int(line)
        # Doc cac dong tiep theo chua toa do dinh cua moi da giac va luu vao list
        elif t_line > 3:
            t = 0
            list = []
            # Them cac danh sach toa do vao list
            for num in line.strip().split(','):  # Doc dong cho toi dau "," va luu gia tri vao bien s
                s = int(num)
                t += 1
                i = s
                list.append(i)  # Them danh sach cac toa do dinh i vao sau list
                map.listdagiac.append(i)
            matrix = createPology(matrix, list)

    file.close()
    return matrix