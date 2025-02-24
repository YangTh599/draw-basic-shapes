# These are Classes that help with on screen graphics
"""

class Text_box():

    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.text_font = pygame.font.SysFont('Comic Sans MS', 18)

    def draw_textbox(self):
        img = self.text_font.render(self.text, True, WHITE)
        pygame.draw.rect(screen_window, (50, 200, 50), self.rect)
        text_rect = img.get_rect(center=self.rect.center)
        screen_window.blit(img, text_rect)

class Image_box():

    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(join('assets','images',image))

    def draw_image(self):
        screen_window.blit(self.image, (self.x, self.y))

"""