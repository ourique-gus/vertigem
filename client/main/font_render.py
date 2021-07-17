import pygame
import os

class FontRender():
    def __init__(self,game,font,size, colour):
        self.game=game
        self.font=font
        self.size=size
        self.colour=colour
        self.valid_characters=''.join([chr(i) for i in range(33,127)]+[chr(i) for i in range(161,688)])
        pygame.font.init()

    def render_font(self):
        font_path=os.path.join('fonts',self.font)
        self.font_draw=pygame.font.Font(font_path,self.size)
        self.full_render=self.font_draw.render(self.valid_characters, True, self.colour)
        pygame.image.save(self.full_render,'font.png')
        
fr=FontRender(0,'arial.ttf',60,(0,0,0)) 
fr.render_font()
    
