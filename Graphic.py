#su dung tkinter canvas de the hien do hoa

from tkinter import *
#import * la import tat ca nhung chuc nang cua thu vien tkinter

class Graphic:
    def __init__(self, weight, height):
        self.u=20
        self.hei = height*self.u+2*self.u
        self.wei = weight*self.u+2*self.u
        self.windown = Tk()
        self.windown.title("AI Project 1")
        self.cv = Canvas(self.windown,width=self.wei,height=self.hei,bg="white")
        self.cv.create_line(2,2,2,self.hei,self.wei,self.hei,self.wei,2,2,2)
        u=self.u
        cl=int(self.wei/u)
        r=int(self.hei/u)
        for i in range(cl):
            self.cv.create_line(i*u,0,i*u,self.hei)
            tempx=(i*u+(i+1)*u)/2+u
            tempy=u/2
            self.cv.create_text(tempx,tempy+1,text=str(i))
        for i in range(r):
            self.cv.create_line(0,i*u,self.wei,i*u)
            tempx=u/2
            tempy=(i*u+(i+1)*u)/2+u
            self.cv.create_text(tempx+1,tempy,text=str(i))
    def Display(self):
        self.windown.mainloop()
    def Rectangle(self,xstart,ystart,color):
        u=self.u
        self.cv.create_rectangle(xstart*u+u,ystart*u+u,xstart*u+2*u,ystart*u+2*u,fill=color)
    def Pack(self):
        self.cv.pack()

    