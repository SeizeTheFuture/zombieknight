import pygame, random, sys
from classes import *
from levels import *

#Use 2D vectors
vector = pygame.math.Vector2

#Initialize pygame
pygame.init()

#Set the display surface (tile size is 32x32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles high
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Knight")

#Set the FPS and clock
FPS = 60
clock = pygame.time.Clock()
tan = random.randint(1,5)


#Create Sprite Groups
main_tile_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
ruby_group = pygame.sprite.Group()


#Generate tile objects from the tile map
for row in range(len(tile_map)):
    for col in range(len(tile_map[row])):
        #Dirt tile
        if tile_map[row][col] == 1:
            Tile(col*32, row*32, 1, main_tile_group)
        #Platform tiles
        elif tile_map[row][col] == 2:
            Tile(col*32, row*32, 2, main_tile_group, platform_group)
        elif tile_map[row][col] == 3:
            Tile(col*32, row*32, 3, main_tile_group, platform_group)
        elif tile_map[row][col] == 4:
            Tile(col*32, row*32, 4, main_tile_group, platform_group)
        elif tile_map[row][col] == 5:
            Tile(col*32, row*32, 5, main_tile_group, platform_group)
        #Ruby Maker
        elif tile_map[row][col] == 6:
            RubyMaker(col*32, row*32, main_tile_group)
        #Portals
        elif tile_map[row][col] == 7:
            pass
        #Zombies
        elif tile_map[row][col] == 8:
            pass
        #Player
        elif tile_map[row][col] == 9:
            pass



#Load and resize the background
bg_image = pygame.transform.scale(pygame.image.load("./zombie_knight_assets/images/background.png"), (1280, 736)).convert_alpha()
bg_rect = bg_image.get_rect(topleft = (0,0))

#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit the background to the screen
    display_surface.blit(bg_image, bg_rect)

    ##Update our main tile group and draw our tiles
    main_tile_group.update()
    main_tile_group.draw(display_surface)

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()