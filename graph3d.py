import  pygame

from OpenGL.GL import *
from OpenGL.GLU import *


class Graph3D(object):
    def __init__(self, width=600, height=600):
        pygame.init()
        display = (width, height)

        pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL| pygame.OPENGLBLIT)
        gluPerspective(45, display[0] / display[1], 0.1, 50.0)
        glTranslatef(0.0, 0.0, -7.0)

        glEnable(GL_DEPTH_TEST)

        self.x = 0
        self.y = 0

        self.points = []

    def invalidate(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        glRotatef(self.x, 0, 1, 0)
        glRotatef(self.y, 0, 0, 1)

        # draw X-axis
        self.draw_line((0.0, 0.0, 0.0), (3.0, 0.0, 0.0), (1.0, 0.0, 0.0))

        # draw Y-axis
        self.draw_line((0.0, 0.0, 0.0), (0.0, 3.0, 0.0), (0.0, 1.0, 0.0))

        # draw Z-axis
        self.draw_line((0.0, 0.0, 0.0), (0.0, 0.0, 3.0), (0.0, 0.0, 1.0))

        for point in self.points:
            self.draw_cube(point['coord'], point['color'])

        glPopMatrix()

    def add_point(self, coord, color=(1.0, 1.0, 1.0)):
        self.points.append({'coord': coord, 'color': color})

    def show(self):
        quit = False

        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = 1
                else:
                    self.handle_event(event)

            self.invalidate()

            pygame.display.flip()
            pygame.time.wait(10)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            rel = pygame.mouse.get_rel()

            self.x = self.x + rel[0]
            self.y = self.y + rel[1]
        else:
            print(event)

    def draw_line(self, f, t, c=(1.0, 1.0, 1.0)):
        glBegin(GL_LINES)
        glColor3fv(c)
        glVertex3fv(f)
        glVertex3fv(t)
        glEnd()

    def draw_cube(self, coord, color):
        glPushMatrix()
        glTranslatef(coord[0], coord[1], coord[2])
        glScalef(0.2, 0.2, 0.2)

        # FRONT
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()

        # BACK
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glEnd()

        # RIGHT
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glEnd()

        # LEFT
        glBegin(GL_POLYGON);
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()

        # TOP
        glBegin(GL_POLYGON)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glEnd();

        # BOTTOM
        glBegin(GL_POLYGON)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()

        glPopMatrix()

    def __delete__(self):
        pygame.quit()


if __name__ == "__main__":
    g = Graph3D()

    g.add_point((1.0, 1.0, 1.0))
    g.add_point((1.5, 1.5, 1.5))
    g.add_point((2.0, 2.0, 2.0))
    
    g.add_point((-1.0, -1.0, -1.0))

    g.show()
