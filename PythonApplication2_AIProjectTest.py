from Graphic import *
from Search import *
from File import*
import time

class Switcher1(object):
    def indirect(self,i):
        method_name='muc_'+str(i)
        method=getattr(self,method_name,lambda :'Invalid')
        return method()
    def muc_1(self):
        #Tao ma tran rong
        map = Map()
        #Lay cac gia tri input tu file input.txt
        print("Nhap file input:\n(input1_1.txt, input1_2.txt, input1_3.txt)")
        string=input("Ten file: ")
        A=Input(string, map)
        #Tao ma tran va canvas theo input
        g=Graphic(map.ngang,map.doc)
        #To mau cac da giac
        for i in range(map.ngang):
            for j in range(map.doc):
                if A[i][j]==1:
                    g.Rectangle(i,j,"lightpink")
        listDaGiac=map.getDaGiac()
        for i in range(0, len(listDaGiac), 2):
            g.Rectangle(listDaGiac[i],listDaGiac[i+1],"lightcoral")

        #chay bang BFS
        bfs=BFSItem(A,(map.xStart,map.yStart),(map.xEnd,map.yEnd))
        path=bfs.BFS()
        print("Chi phi: ",len(path)-1,"\n")

        g.Rectangle(map.xStart,map.yStart,"lightskyblue")
        g.Rectangle(map.xEnd,map.yEnd,"lightskyblue")
        g.Pack()
        for j in range(1,len(path)-1):
                r=path[j][0]
                c=path[j][1]
                wait=1
                while wait:
                    g.Rectangle(r,c,"lightsteelblue")
                    g.windown.update_idletasks()
                    g.windown.update()
                    time.sleep(0.1)
                    g.Pack()
                    wait=0
        
        g.Pack()
        g.Display()
        return 1            #Gia tri de chay tiep
    def muc_2(self):
         s=1
         while s>0:                                                                  
             print("Chon thuat toan:\n\t1. A*\n\t2. Breadth First Search\n\t3. Iterative Deepening Search\n\t4. Uniform-cost Search")
             s=int(input("Chon thuat toan: "))
             sel=Switcher2()
             s=sel.indirect(s)
         return 1           #Thoat khoi switcher 2 (chon thuat toan) tiep tuc chay switcher 1 

    def muc_3(self):
        #Tao ma tran rong
        map = Map()
        #Lay cac gia tri input tu file input.txt
        print("Nhap file input:\n(input1_1.txt, input1_2.txt, input1_3.txt)")
        string=input("Ten file: ")
        A=Input(string, map)
        #Tao ma tran va canvas theo input
        g=Graphic(map.ngang,map.doc)
        #To mau cac da giac
        for i in range(map.ngang):
            for j in range(map.doc):
                if A[i][j]==1:
                    g.Rectangle(i,j,"lightpink")
        listDaGiac=map.getDaGiac()
        for i in range(0, len(listDaGiac), 2):
            g.Rectangle(listDaGiac[i],listDaGiac[i+1],"lightcoral")
        chiPhi = xuatDuongDi(A,map)
        print("Chi phi: ",chiPhi)
        #Gia tri to mau: Start, end: 3      Diem don: 4     Duong di: 2     Rong: 0     Tuong: 1 
        A[map.xStart][map.yStart]=3
        A[map.xEnd][map.yEnd]=3
        g.Rectangle(map.xStart,map.yStart,"lightskyblue")
        g.Rectangle(map.xEnd,map.yEnd,"lightskyblue")
        for i in map.danhSachDon:
            x,y=i
            A[x][y]=4
            g.Rectangle(x,y,"lightgreen")
        g.Pack()
        for i in range(map.ngang):
            for j in range(map.doc):
                if A[i][j]==2:
                    wait=1
                    while wait:               
                        g.Rectangle(i,j,"lightsteelblue")
                        g.windown.update_idletasks()
                        g.windown.update()
                        time.sleep(0.1)
                        g.Pack()
                        wait=0

        g.Pack()
        g.Display()
        return 1


    def muc_0(self):
         return 0           #gia tri de break
class Switcher2(object):
    def indirect(self,i):
        method_name='thuatToan_'+str(i)
        method=getattr(self,method_name,lambda :'Invalid')
        return method()
    def thuatToan_1(self):
        #Tao ma tran rong
        map = Map()
        #Lay cac gia tri input tu file input.txt
        print("Nhap file input:\n(input1_1.txt, input1_2.txt, input1_3.txt)")
        string=input("Ten file: ")
        A=Input(string, map)
        #Tao ma tran va canvas theo input
        g=Graphic(map.ngang,map.doc)
        #To mau cac da giac
        for i in range(map.ngang):
            for j in range(map.doc):
                if A[i][j]==1:
                    g.Rectangle(i,j,"lightpink")
        listDaGiac=map.getDaGiac()
        for i in range(0, len(listDaGiac), 2):
            g.Rectangle(listDaGiac[i],listDaGiac[i+1],"lightcoral")
        paths=astar(A,(map.xStart,map.yStart),(map.xEnd,map.yEnd))
        paths.reverse()
        print("Chi phi: ",len(paths))
        del paths[len(paths)-1]
        g.Rectangle(map.xStart,map.yStart,"lightskyblue")
        g.Rectangle(map.xEnd,map.yEnd,"lightskyblue")
        g.Pack()


        for i in paths:
                y,x=i
                wait=1
                while wait:
                    g.Rectangle(y,x,"lightsteelblue")
                    g.windown.update_idletasks()
                    g.windown.update()
                    time.sleep(0.1)
                    g.Pack()
                    wait=0
            
        g.Pack()
        return 1        
    def thuatToan_2(self):
         a=Switcher1()
         return a.indirect(1)
    def thuatToan_3(self):
        #Tao ma tran rong
        map = Map()
        #Lay cac gia tri input tu file input.txt
        print("Nhap file input:\n(input1_1.txt, input1_2.txt, input1_3.txt)")
        string=input("Ten file: ")
        A=Input(string, map)
        print(A)
        #Tao ma tran va canvas theo input
        g=Graphic(map.ngang,map.doc)
        #To mau cac da giac
        for i in range(map.ngang):
            for j in range(map.doc):
                if A[i][j]==1:
                    g.Rectangle(i,j,"lightpink")
        listDaGiac=map.getDaGiac()
        for i in range(0, len(listDaGiac), 2):
            g.Rectangle(listDaGiac[i],listDaGiac[i+1],"lightcoral")

        ids(A,map.xStart,map.yStart,map.xEnd,map.yEnd)
        print(A)


        g.Pack()
        g.Display()
        return 1
    def thuatToan_4(self):
        #Tao ma tran rong
        map = Map()
        #Lay cac gia tri input tu file input.txt
        print("Nhap file input:\n(input1_1.txt, input1_2.txt, input1_3.txt)")
        string=input("Ten file: ")
        A=Input(string, map)
        print(A)
        #Tao ma tran va canvas theo input
        g=Graphic(map.ngang,map.doc)
        #To mau cac da giac
        for i in range(map.ngang):
            for j in range(map.doc):
                if A[i][j]==1:
                    g.Rectangle(i,j,"lightpink")
        listDaGiac=map.getDaGiac()
        for i in range(0, len(listDaGiac), 2):
            g.Rectangle(listDaGiac[i],listDaGiac[i+1],"lightcoral")


        ucs(A,map.xStart,map.yStart,map.xEnd,map.yEnd)



        g.Pack()
        g.Display()
        return 1
    def thuatToan_0(self):
        return 0        #gia tri de break
selection=1
while selection > 0:
    print("Chon muc chay:\n\t- Muc 1.\n\t- Muc 2.\n\t- Muc 3.")
    selection=int(input("Chon muc theo so tuong ung: "))
    select=Switcher1()
    selection=select.indirect(selection)






            
'''
list = astar(A, (2, 2), (19, 16))
def update(matrix, list):
    for i in range(len(list)):
        x, y = list[i]
        matrix[x][y] = 2
    return matrix
A = update(A, list)

for i in list:
    x,y =i
    g.Rectangle(x,y,"grey")
'''