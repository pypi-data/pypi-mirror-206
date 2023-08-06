import pygame
import math

def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)

def normalize(num, min_value, max_value):
    return (num - min_value) / (max_value - min_value)

class Button:
    def __init__(self,
                 pos_tuple,
                 dim_tuple, text,
                 toggle = False,
                 disabled = False,
                 normal_color = (100, 100, 100),
                 hover_color = (69, 69, 69),
                 pressed_color = (42, 42, 42),
                 font_color = (255, 255, 255),
                 font_family = 'arial',
                 font_size = 32,
                 border_radius = 0):
        
        self.x, self.y = pos_tuple
        self.width, self.height = dim_tuple
        self.text = text
        self.toggle = toggle
        self.disabled = disabled
        
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        
        self.font_color = font_color
        self.font_family = font_family
        self.font_size = font_size
        self.border_radius = border_radius

        self.pressed = False

        self.button_rect = pygame.Rect(0, 0, 0, 0)
        self.font = pygame.font.SysFont(self.font_family, self.font_size)

    def is_pressed(self):
        if self.disabled:
            return False
        
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            return pygame.mouse.get_pressed()[0]
        else:
            return False

        #return pygame.mouse.get_pressed()[0] if self.button_rect.collidepoint(pygame.mouse.get_pos()) else False

        #if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            #if pygame.mouse.get_pressed()[0]:
                #self.pressed = not self.pressed
                #return self.pressed
        #else:
            #return self.pressed

    def is_hovering(self):
        return self.button_rect.collidepoint(pygame.mouse.get_pos())
        
    def draw(self, screen):
        self.screen = screen

        if self.is_pressed():
            self.color = self.pressed_color
        elif self.is_hovering():
            self.color = self.hover_color
        else:
            self.color = self.normal_color
        
        self.button_rect = pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height), border_radius = self.border_radius)    
        self.button_text = self.font.render(self.text, True, self.font_color)
        self.screen.blit(self.button_text, (self.x+math.floor((self.width/2) - (self.font.size(self.text)[0]/2)),
                                            (self.y+math.floor((self.height/2) - (self.font.get_height()/2)))))



class Slider:
    def __init__(self, pos, length, min_value, max_value):
        self.x, self.y = pos
        self.length = length
        self.min_value, self.max_value = min_value, max_value

        self.bob_x = self.x
        self.value = self.x

        self.font = pygame.font.SysFont('arial', 20)
        self.slider_bob = pygame.Rect(0, 0, 0, 0)

    def move_slider(self):
        if self.slider_bob.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.bob_x = pygame.mouse.get_pos()[0]
                self.bob_x = clamp(self.bob_x, self.x, self.x+self.length)
        return math.floor(normalize(self.bob_x, self.x, self.x+self.length) * self.max_value)

    def draw(self, screen):
        self.screen = screen
        self.value = self.move_slider()
        self.slider_rect = pygame.draw.rect(self.screen, (100, 100, 100), pygame.Rect(self.x, self.y, self.length, 20), border_radius=100)    
        self.slider_bob = pygame.draw.circle(self.screen, (216, 100, 0), (self.bob_x, self.y+10), 15)
        self.slider_value_text = self.font.render(str(self.value), True, (255, 255, 255))
        self.screen.blit(self.slider_value_text, (self.x+self.length+10, self.y))
    

if __name__ == "__main__":

    # cd /d "D:\SHEJIN\Projects\Python\Pygame GUI"

    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Shejin's GUI Package For Pygame")
    clock = pygame.time.Clock()

    button = Button((50, 100), (200, 100), "My Button", border_radius=100)
    button1 = Button((200, 250), (250, 150), "Hehe", normal_color=(255, 0, 0), hover_color=(0, 255, 0), pressed_color=(0, 0, 255))
    slider = Slider((300, 80), 150, -50, 50)

    run = True

    while run:
        clock.tick(60)
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        button.draw(screen)
        button1.draw(screen)
        slider.draw(screen)
        
        pygame.display.update()
        
    pygame.quit()
    quit()
