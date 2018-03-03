import pygame
from pygame.locals import *
class Champion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._health = 100
        self._damage = 10
        self._level = 1
class Fin(Champion):
    def __init__(self):
        Champion.__init__(self)
class Tower:
    def __init__(self,xpos,ypos):
        self._xpos = xpos
        self._ypos = ypos
class Map:
    def __init__(self):
        self._map_image_filename = ""
        self._map_towers = []
        self._map_monsters = []
    def on_init(self):
        self._image = pygame.image.load(self._map_image_filename).convert()
    def on_render(self,oDisplay):
        oDisplay.blit(self._image,(0,0))
class SummonersRift(Map):
    def __init__(self):
        Map.__init__(self)
        self._map_image_filename = "summonersriftmap.jpg"
        self._map_towers.append(Tower(40,40))
        self._map_towers.append(Tower(80,80))
class App:
    def __init__(self):
        self._running = True
        self._oDisplay = None
        self._oMap = SummonersRift()
        self.size = self.weight, self.height = 732, 732
    def on_init(self):
        pygame.init()
        self._oDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._oMap.on_init()
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        self._oMap.on_render(self._oDisplay)
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()