import pygame as pg
from pygame.locals import *

WINDOWWIDTH = 1000
WINDOWHEIGHT = 629
FPS = 30

def main():
    global WINDOWHEIGHT, WINDOWWIDTH,FPSCLOCK
    pg.init()
    FPSCLOCK = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),HWSURFACE | DOUBLEBUF|RESIZABLE)
    pg.display.set_caption('Scroll Tester')
    pg.display.update()
    screen = pg.image.load('images/screens/menu_screen_1.jpg')
    qsurf = pg.image.load('images/DMTB_QUEST.png')
    qheight = qsurf.get_height()
    qwidth = qsurf.get_width()
    qRect = qsurf.get_rect(topleft = (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 200 ))

    scrollSurf = pg.Surface((qwidth,4*qheight))
    scrollSurf.set_alpha(255)
    scrollSurf.fill((255,255,255))
    DISPLAYSURF.blit(screen, (0,0))

    DISPLAYSURF.blit(scrollSurf, (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 500 ) )
    scrollSurf.blit(qsurf, (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 500 ))

    while True:

        for event in pg.event.get():
            if event.type == MOUSEBUTTONUP:
                if qRect.collidepoint(event.pos):
                    print('Hello')
                else:
                    DISPLAYSURF.blit(screen, (0,0))
    
                    scrollSurf.blit(qsurf,(WINDOWWIDTH/2 - int(qwidth/2), qRect.y -int(WINDOWHEIGHT/10)))
                    DISPLAYSURF.blit(scrollSurf, (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 500 ) )

                    qRect = qsurf.get_rect(topleft = (WINDOWWIDTH/2 - int(qwidth/2), qRect.y -qheight ))



        pg.display.update()


if __name__ == '__main__':
    main()
                
                
                
