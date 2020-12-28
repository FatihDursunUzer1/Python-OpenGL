'''
FatihDursun_Uzer.py
18120205041
FATİH DURSUN ÜZER
BİLGİSAYAR MUHENDİSLİGİ
 UZAY SİMULASYONU.

 (0.0) bölgesinde kendi ekseni etrafında dönen Güneş yer almaktadır.
 Dünya, Güneş ve kendi ekseni etrafında dönmektedir.
 Ay, Dünya ve kendi ekseni etrafında dönmektedir.
'''

from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math


# Dünya'nın orjine göre x eksenindeki yeri.
translate_axis_x_world=3.0
#Dünya'nın orjine göre y eksenindeki yeri
translate_axis_y_world=0.0
#cos ve sin değerlerinin içerisindeki açı değeri.
theta=0.0
#Ay'ın Dünya'ya göre x eksenindeki yeri
translate_axis_x_moon=1
#Ay'ın Dünya'ya göre y eksenindeki yeri
translate_axis_y_moon=0.0
#Güneş'in dönüş açısı
rangle_sun = 0.0
#Dünya'nın dönüş açısı
rangle_world=0.0
#Ay'ın dönüş açısı
rangle_moon=0.0

#Uzay'ı tanımlayan fonksiyon
def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)

#Koordinat bölgesini çizen fonksiyon
def drawAxis():
    glColor3f(0, 1, 1)
    for i in range(-5, 5):
        glBegin(GL_POINTS)
        glVertex2f(i, 0)
        glVertex2f(0, i)
        glEnd()
# The main drawing function.

# Uzay simulasyonunun ekrana yansımasını ve objelerin kendi ve birbirleri etrafında dönmelerini sağlayan fonksiyon
def SpaceSimulation():
    global rangle_sun
    global translate_axis_x_world
    global translate_axis_y_world
    global translate_axis_x_moon
    global translate_axis_y_moon
    global theta
    global rangle_world
    global rangle_moon
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    drawAxis()
    #Günes'in boyutunun,renginin ve rotate bölgesinin belirlendiği yer
    glPushMatrix()
    glColor(1, 0.4, 0)
    glRotatef(rangle_sun, 0, 0, 1)
    glutSolidSphere (1, 20, 20)
    glPopMatrix()

    #Dünya ve Ay'ın boyutunun,renginin ve rotate bölgelerinin belirlendiği kısım
    glPushMatrix()
    # For World
    glTranslatef(translate_axis_x_world, translate_axis_y_world, 0)
    glRotatef(rangle_world,0,0,1)
    glColor(0, 0.4, 1)
    glutSolidSphere (0.5, 20, 20)
    # Ay için
    glTranslatef(translate_axis_x_moon,translate_axis_y_moon,0)
    glRotatef(rangle_moon, 0, 0, -1)
    glColor(0.6,0.5, 0.4)
    glutSolidSphere(0.2, 20, 20)
    glPopMatrix()
    glutSwapBuffers()
    ''' Güneş,Ay ve Dünya'nın dönüş açılarının, X ve Y lokasyonlarının değişmesini sağlayan bölüm'''
    rangle_sun += 0.05 #Güneşin kendi etrafında dönüş açısını 0.5 arttırır
    rangle_world += 0.10 # Dünya'nın kendi etrafında dönüş açısını 0.10 arttırır
    rangle_moon += 0.20 # Ay'ın kendi etrafında dönüş açısını 0.10 arttırır
    translate_axis_x_world = 2.25 * math.cos(theta) #Dünya'nın Güneş etrafında dönmesi için x axis'ini değiştirir
    translate_axis_y_world = 2.25 * math.sin(theta)#Dünya'nın Güneş etrafında dönmesi için y axis'ini değiştirir
    translate_axis_x_moon = 0.75 * math.cos(theta) #Ay'ın Dünya etrafında dönmesi için x axis'ini değiştirir
    translate_axis_y_moon = 0.75 * math.sin(theta)#Ay'ın Dünya etrafında dönmesi için y axis'ini değiştirir
    theta+= 0.0001 # cos ve sin'in içinde bulunan theta değeri 0.0001 arttırılır



#Programın çalışmasını sağlayan main fonksiyonu
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Space Simulation")
    glutDisplayFunc(SpaceSimulation)
    glutIdleFunc(SpaceSimulation)
    InitGL()
    glutMainLoop()


main()



