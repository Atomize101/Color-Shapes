import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        self.height = random.randint(20, 70)
        self.width = random.randint(20, 70)
        self.change_x = random.randint(-3, 3)
        self.change_y = random.randint(-3, 3)
        self.color = [random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)]
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        #self.height += self.change_x
        #self.width += self.change_y

class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y,self.width,self.height], 0)



pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Color Shapes")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
my_list = []

for i in range(500):
    my_object = Rectangle()
    my_list.append(my_object)

for i in range(500):
    my_object = Ellipse()
    my_list.append(my_object)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(BLACK)

    for my_object in my_list:
        my_object.draw()
        my_object.move()
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()