'''
FatihDursun_Uzer.py
18120205041
Fatih Dursun Üzer

Ekrana araba,ağaç, yol ve kırmızı bir top çizdiren Python Programı.
Araba sol ve sağ ok tuşları ile hareket eder ve ağaca çarpmayacak şekilde ilerlemesi sağlanır.
Kırmızı top ise ağaca çarpmayacak şekilde sağ-sol hareket eder.
'''
from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import *

theta=4 #Kırmızı top'un -1 ile 1 arasında gidip gelebilmesi icin gerekli olan cos açısı.
araba_x=0 # Arabanın x konumu


def InitGL():
    glClearColor(1.0,1.0,1.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

''' Ekrana Çizim Yapan Fonksiyon '''
def DrawGLScene():
    global theta,araba_x
    glClear(GL_COLOR_BUFFER_BIT)
    # Ağacın gövdesini çizdiriyor
    glPushMatrix()
    glViewport(300, 0, 300, 480) #Ağacın yer aldığı viewport
    glColor3f(0.447059, 0.264706, 0.164706)#kahverengi
    glPointSize(5.0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0.5, 0)
    glVertex2f(0.5, -1)
    glVertex2f(0, -1)
    glEnd()
    #Ağacın dal kısmını çizdirir
    glBegin(GL_TRIANGLES)
    glColor(0.184314, 0.309804, 0.184314) #kapalı yeşil
    glVertex2f(-0.5, 0)
    glVertex2f(1, 0)
    glVertex2f(0.25, 1)
    glEnd()
    glPopMatrix()

    '''
    Kırmızı Top'u belirli bir alanda çizdirip x ekseninde gidip gelmesini sağlayan yer
    Top cos değerleri arasında gidip gelir. (1 ile -1 arasında)
    '''
    glPushMatrix()
    glViewport(0,300,400,250) #Kırmızı topun yer aldığı viewport
    glTranslate(cos(theta),0,0)
    glColor3f(1,0.4,0)
    glutSolidSphere(0.1,100,100)
    glPopMatrix()


    glPushMatrix()
    glViewport(0, 0, 640, 480) #Arabanın ve Yol'un yer aldığı viewport
    gluOrtho2D(-15, 15, -15, 15)
    '''
    Polygon ile yol çizimi.
    '''
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3f(0, 1, 1)
    glVertex2f(-15, -5)
    glVertex2f(15, -5)
    glVertex2f(15, -15)
    glVertex2f(-15, -15)
    glVertex2f(-15, -5)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0.768, 0.878, 0.698) #Yolun rengi
    glVertex2f(-15, -5.25)
    glVertex2f(15, -5.25)
    glVertex2f(15, -14.75)
    glVertex2f(-15, -14.75)
    glVertex2f(-15, -5.25)
    glEnd()
    glPopMatrix()

    '''
    Arabanın üstü,gövdesi ve tekerlerinin çiziminin yer aldığı bölüm.
    Arabanın üst kısmı kare, gövdesi dikdörtgen, tekerlekleri ise daire şeklindedir.
    '''
    glPushMatrix()
    glTranslate(araba_x,0,0)
    glColor3f(0, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(-5,5)
    glVertex2f(-5,0)
    glVertex2f(-10,0)
    glVertex2f(-10,5)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0.309804,0.184314,0.309804)
    glVertex2f(-12,0)
    glVertex2f(-3,0)
    glVertex2f(-3,-3)
    glVertex2f(-12,-3)
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glPushMatrix()
    glTranslatef(-11,-4,0)
    glutSolidSphere(1,20,20)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-4, -4, 0)
    glutSolidSphere(1, 20, 20)
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()
    glFlush()
    theta+=0.001
    glutPostRedisplay()


'''
Sol Ok tuşuna basıldığında araba geri geri gider.
Sağ Ok tuşuna basılı tutulduğunda ise araba ağaca çarpacak kadar yakın olana dek ileri gider
'''
def keyboardPressed(*args):
    global theta_araba,araba_x
    if args[0]==GLUT_KEY_LEFT:
        if araba_x > -1:
            araba_x-=0.1
    elif args[0]==GLUT_KEY_RIGHT:
        if araba_x<8:
            araba_x+=0.1
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Vize")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    InitGL()
    glutSpecialFunc(keyboardPressed)
    glutMainLoop()
main()

