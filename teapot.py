'''
FATİH DURSUN ÜZER
18120205041
BİLGİSAYAR MÜHENDİSLİĞİ 3.SINIF BİLGİSAYAR GRAFİKLERİ 6.ÖDEV
Ekrana iki farklı viewport tanımlayınız.
1. viewportta
3 Boyutlu bir küp bulunmaktadır. Bu küp W,A,S,D tuşları ile ileriye,geriye,sağa ve sola hareket edebilmektedir.
2. viewportta
 mavi bir çaydanlık bulunmaktadır. Fare sol tıka basılı şekilde hareket ettiğinde çaydanlık da farenin hareketine göre x veya
 y ekseni etrafında dönme hareketi yapar.
'''

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x_angle = 0.0  # Küp'ün x ekseni etrafında dönme açısı.
x_axis_translate = 0.0  # Küp'ün X konumu
y_axis_translate = 0.0  # Küp'ün Y konumu
mouse_x_axis = int()  # Mouse'a tıklandığı andaki mouse'ın X konumu
mouse_y_axis = int()  # Mouse'a tıklandığı andaki mouse'ın Y konumu
mouse_left_down = bool()  # Mouse'un sol butonuna basılıp basılmadığını gösteren boolean değer
teapot_angle_x = 0.0  # Çaydanlığın X ekseni etrafında dönüş açısı
teapot_angle_y = 0.0 # Çaydanlığın Y ekseni etrafında dönüş açısı
zoom = 1.0  # Ölçeklendirme

'''

'''
Vertexs = [[-1, 1, 1], [1, 1, 1], [1, 1, -1], [-1, 1, -1], [-1, -1, 1], [1, -1, 1], [1, -1, -1], [-1, -1, -1]]
'''
Ekranı temizleyen, perspektif ayarlayan başlangıç fonksiyonu.
'''


def Init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    '''
     gluPerspective fonksiyonunu kullanmadığım zaman sadece küpün bir yüzünü görebiliyordum. Dönme hareketi koyduğum vakit ise sadece renk değiştiriyor
     gibi duruyordu.
     https://stackoverflow.com/questions/34181567/opengl-cube-wont-render'da ki soruya verilen cevaba göre gluPerspective kullanılırsa kameranın tek yüze bakma
     sorunun çözüleceği yazıyordu.
     Birinci parametre y yönündeki görüş açısının değeri, ikinci parametre  X yönündeki görüş alanını belirleyen bir oran.
     Bu oran genellikle pencerenin eni ve boyu arasındaki oran oluyor.
     Üçüncü parametre,İzleyiciden yakın kırpma düzlemine olan mesafe (her zaman pozitif).
     Dördüncü parametre ise İzleyiciden uzak kırpma düzlemine olan mesafe (her zaman pozitif). 
     Kaynak:https://docs.microsoft.com/en-us/windows/win32/opengl/gluperspective.
     gluPerspective kullanmadan önce glMatrixMode(GL_PROJECTION) ve glLoadIdentity() kullanmak gerekiyor.
    '''
    gluPerspective(60.0, 640 / 480, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


'''
4 tane vertexi birleştirip polygon haline getirerek küp'ün bir yüzeyini çizdiren fonksiyon.
'''


def DrawCubeSurface(v1, v2, v3, v4, colors):
    glColor3f(colors[0], colors[1], colors[2])
    glBegin(GL_POLYGON)
    glVertex3f(v1[0], v1[1], v1[2])
    glVertex3f(v2[0], v2[1], v2[2])
    glVertex3f(v3[0], v3[1], v3[2])
    glVertex3f(v4[0], v4[1], v4[2])
    glVertex3f(v2[0], v2[1], v2[2])
    glEnd()


'''
3D çaydanlık çizdiren fonksiyon 
'''


def DrawTeapot():
    global teapot_angle_x, teapot_angle_y
    glColor3f(0, 0, 1.0)
    glTranslatef(0, 0, -5)
    glRotatef(teapot_angle_x, 1, 0, 0)
    glRotatef(teapot_angle_y, 0, 1, 0)
    glutWireTeapot(1)


'''
Küp ve çaydanlığı iki ayrı viewportta çizdiren fonksiyon.
Bu fonksiyon çalıştığı sürece küp x ekseni etrafında döner.
'''


def Draw():
    global x_angle, y_axis_rotate, z_axis_rotate
    global x_axis_translate, y_axis_translate
    global Vertexs

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glViewport(0, 0, 250, 250)
    glTranslatef(x_axis_translate, y_axis_translate, -5)
    glRotatef(x_angle, 1.0, 0.0, 0.0)
    glScale(zoom, zoom, zoom)
    # gluLookAt(5,3,2,0,0,0,0,0,1)
    DrawCubeSurface(Vertexs[0], Vertexs[1], Vertexs[2], Vertexs[3], [1, 0, 0])
    DrawCubeSurface(Vertexs[0], Vertexs[1], Vertexs[5], Vertexs[4], [0.55, 0.44, 0.33])
    DrawCubeSurface(Vertexs[0], Vertexs[3], Vertexs[7], Vertexs[4], [0.84, 0.3, 0.9])
    DrawCubeSurface(Vertexs[1], Vertexs[2], Vertexs[6], Vertexs[5], [0.7, 0.9, 0.2])
    DrawCubeSurface(Vertexs[1], Vertexs[5], Vertexs[6], Vertexs[2], [0.3, 0.3, 0.4])
    DrawCubeSurface(Vertexs[2], Vertexs[6], Vertexs[7], Vertexs[3], [0.1, 0.9, 0.8])
    DrawCubeSurface(Vertexs[2], Vertexs[6], Vertexs[7], Vertexs[3], [0.1, 0.9, 0.8])
    DrawCubeSurface(Vertexs[4], Vertexs[5], Vertexs[6], Vertexs[7], [0.46, 0.9, 0.1])
    glPopMatrix()
    x_angle += 0.03
    glPushMatrix()
    glViewport(250, 0, 250, 250)
    DrawTeapot()
    glPopMatrix()

    glutSwapBuffers()


'''
w,a,s,d tuşlarına basıldıkça küpün ileri-geri,sağ-sol hareket etmesini sağlayan fonksiyon
'''


def keyPressed(*args):
    global x_axis_translate, y_axis_translate
    if args[0] == b'w' or args[0] == b'W':
        y_axis_translate += 0.2
    if args[0] == b'a' or args[0] == b'A':
        x_axis_translate -= 0.2
    if args[0] == b's' or args[0] == b'S':
        y_axis_translate -= 0.2
    if args[0] == b'd' or args[0] == b'D':
        x_axis_translate += 0.2
    glutPostRedisplay()


'''
Farenin orta tekerleğinin çaydanlığı yakınlaştırıp uzaklaştırmayı sağlayan fonksiyon
'''


def MouseWheel(*args):
    global zoom
    print(args)
    if args[1] == -1:
        zoom -= 0.05
    if args[1] == 1:
        zoom += 0.05
    glutPostRedisplay()


'''
Fare'de sol tıka basılıp basılmadığını kontrol eden fonksiyon.
args[0]=button
args[1]=State
args[2]=Fare'nin tıklandığı yerdeki X konumu
args[3]=Fare'nin tıklandığı yerdeki Y konumu
'''
def KeepMousePosition(*args):
    global mouse_x_axis, mouse_y_axis
    mouse_x_axis = args[2]
    mouse_y_axis = args[3]
    if args[0] == 0:
        if args[1] == 0:  # Sol tıka basıldıysa
            glutMotionFunc(MouseLeftButtonHoldDown)
        elif args[1] == 1:  # Sağ tık' basıldıysa
            pass
    glutPostRedisplay()
'''
Eğer farede sol tık basılı durumdaysa çalışan fonksiyon.
Bu fonksiyon fare sol tıka basılı olduğu durumda fare nereye giderse ona göre çaydanlığın dönüş açısını ve yönünü değiştirir
args[0]=Mouse'un yeni X konumu
args[1]=Mouse'un yeni Y konumu
'''
def MouseLeftButtonHoldDown(*args):
    global teapot_angle_x,teapot_angle_y
    teapot_angle_x+=(args[1]-mouse_y_axis)*0.05
    teapot_angle_y+=(args[0]-mouse_x_axis)*0.05
    glutPostRedisplay()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('OpenGL Python Cube and Teapot')
    Init()
    glutDisplayFunc(Draw)
    glutIdleFunc(Draw)
    glutKeyboardFunc(keyPressed)
    glutMouseWheelFunc(MouseWheel)
    glutMouseFunc(KeepMousePosition)#Mouse'a tıklanıldığında tetiklenen fonksiyon kaynak:https://www.opengl.org/resources/libraries/glut/spec3/node50.html
    glutMainLoop()


main()
