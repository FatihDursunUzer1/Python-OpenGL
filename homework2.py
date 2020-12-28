
''' Fatih Dursun Uzer
18120205041
Istanbul Medenıyet Universitesi
Bilgisayar Muhendisligi
OpenGL araba çizme ve klavye tuslarına baglı olarak arabanın rengini degistirme'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
import random as rn

#Arabanin renginin RGB kodlarını saklayan liste
carColorsRGB=[rn.random(),rn.random(),rn.random()]

'''
Pencerenin baslangictaki durumunu belirler.
'''
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0,1.0)

'''Cerceve cizimlerini saglayan fonksiyon
 x ve y koordinatlarini alip (-x,-y),(-x,y),(x,y),(x,-y),(-x,-y) noktalarini birlestirip 
 kare halini alan bir polygon olusturur
 red,green,blue ise RGB kodlaridir. 0 ile 1 arasi deger almasi gerekmektedir.
'''
def drawSquare(x,y,red,green,blue):
    glColor3f(red,green,blue)
    glBegin(GL_POLYGON)
    glVertex2f(-x,-y)
    glVertex2f(-x,y)
    glVertex2f(x,y)
    glVertex2f(x,-y)
    glVertex2f(-x,-y)
    glEnd()

'''Arabada bulunan dikdörtgenlerin cizimini saglayan fonksiyon
x1,y1,x2,y2 degerlerini alarak dikdortgen seklinde polygon olusturur.
red,green,blue ise RGB kodlaridir. 0 ile 1 arasi deger almasi gerekmektedir.
'''
def drawRectangleWithPolygon(x1,y1,x2,y2,red,green,blue):
    glColor3f(red,green,blue)
    glBegin(GL_POLYGON)
    glVertex2f(x1,y1)
    glVertex2f(x1,y2)
    glVertex2f(x2,y2)
    glVertex2f(x2,y1)
    glVertex2f(x1,y1)
    glEnd()

#Arabanın tekerlerinin cizilmesini saglayan fonksiyon
def plotTerrain(x,y):
    sides = 32
    radius = 0.15
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    for i in range(40):
        cosine = radius * cos(i * 2 * pi / sides) + x
        sine = radius * sin(i * 2 * pi / sides) + y
        glVertex2f(cosine, sine)
    glEnd()
#Gorseli cizdiren fonksiyon
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    drawSquare(0.95,0.95,1,1,1)
    drawSquare(0.925,0.925,0,0,0)
    drawSquare(0.91,0.91,1,1,1)
    drawRectangleWithPolygon(-0.325,0.275,0.325,0.625,0,0,0)
    drawRectangleWithPolygon(-0.3,0.3,0.3,0.6,carColorsRGB[0],carColorsRGB[1],carColorsRGB[2])
    drawRectangleWithPolygon(-0.650,-0.075,0.0,0.275,0,0,0)
    drawRectangleWithPolygon(-0.625,-0.050,-0.025,0.250,carColorsRGB[0],carColorsRGB[1],carColorsRGB[2])
    drawRectangleWithPolygon(0.0,-0.075,0.625,0.275,0,0,0)
    drawRectangleWithPolygon(0.025,-0.050,0.600,0.250,carColorsRGB[0],carColorsRGB[1],carColorsRGB[2])
    plotTerrain(0.3,-0.20)
    plotTerrain(-0.3,-0.20)
    glFlush()

'''Belirli klavye tuslarında arabanın renginin degismesini saglayan fonksiyon
r---> Arabayi kirmizi renk yapar
g---> Arabayi yesil renk yapar
b---> Arabayi mavi renk yapar
ESC--->Programdan cikisi saglar.
'''
def keyPressed(*args):
    print(args[0])
    if args[0] ==b'\x1b':
        sys.exit()
    if args[0]==b"r":
        carColorsRGB[0]=1
        carColorsRGB[1]=0
        carColorsRGB[2]=0
    if args[0]==b"g":
        carColorsRGB[0] = 0
        carColorsRGB[1] = 1
        carColorsRGB[2] = 0
    if args[0]==b"b":
        carColorsRGB[0] = 0
        carColorsRGB[1] = 0
        carColorsRGB[2] = 1
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(250, 250)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Car")
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyPressed)
    init()
    glutMainLoop()

main()
