import pygame 
from pygame.locals import *

class Champion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._health = 100
        self._damage = 1
        self._level = 1 
class Fin(Champion):
    def __init__(self):
        Champion.__init__(self)
        self.sprite_sheet = pygame.image.load("sprite/healer_m.png").convert()
        self.image = pygame.Surface([32, 35]).convert()
        self.image.blit(self.sprite_sheet, (0, 0), (0, 0, 32, 35))
        self.image.set_colorkey(( 255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

class Maurice(Champion):
    def __init__(self):
        Champion.__init__(self)
        self.sprite_sheet = pygame.image.load("sprite/warrior_m.png").convert()
        self.image = pygame.Surface([32, 35]).convert()
        self.image.blit(self.sprite_sheet, (0, 0), (0, 0, 32, 35))
        self.image.set_colorkey(( 255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

class Tower(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        pygame.sprite.Sprite.__init__(self)
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
        self.all_sprites_list = pygame.sprite.Group()
        self.size = self.weight, self.height = 732, 732
    def on_init(self):
        pygame.init()
        self._oDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._oMap.on_init()
        self.all_sprites_list.add(Fin())
        self.all_sprites_list.add(Maurice())
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        self._oMap.on_render(self._oDisplay)
        self.all_sprites_list.draw(self._oDisplay)
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