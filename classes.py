import pygame, random
from settings import *

#Define Classes
class Game():
    """A class to manage gameplay"""

    def __init__(self, player, display_surface):
        """Initialize the game"""
        #Set constants
        self.STARTING_ROUND_TIME = 30

        #Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME

        #Load fonts
        self.title_font = pygame.font.Font("./zombie_knight_assets/fonts/Poultrygeist.ttf", 48)
        self.HUD_font = pygame.font.Font("./zombie_knight_assets/fonts/Pixel.ttf", 24)

        #Connect the player object
        self.player = player

        #Connect the display surface
        self.display_surface = display_surface

    def update(self):
        """Update the game"""
        #Update the round time every second
        self.frame_count += 1
        if self.frame_count % FPS == 0:
            self.round_time -= 1
            self.frame_count = 0

    def draw(self):
        """Draw the game HUD"""
        #Set text
        self.score_text = self.HUD_font.render("Score: " + str(self.score), True, WHITE)
        self.score_rect = self.score_text.get_rect(topleft= (10, WINDOW_HEIGHT - 50))

        self.health_text = self.HUD_font.render("Health: " + str(self.player.health), True, WHITE)
        self.health_rect = self.health_text.get_rect(topleft= (10, WINDOW_HEIGHT - 25))

        self.title_text = self.title_font.render("Zombie Knight", True, GREEN)
        self.title_rect = self.title_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT - 25))

        self.round_text = self.HUD_font.render("Night: " + str(self.round_number), True, WHITE)
        self.round_rect = self.round_text.get_rect(topright= (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50))

        self.time_text = self.HUD_font.render("Sunrise in: " + str(self.round_time), True, WHITE)
        self.time_rect = self.time_text.get_rect(topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25))

        #Draw the HUD
        self.display_surface.blit(self.score_text, self.score_rect)
        self.display_surface.blit(self.health_text, self.health_rect)
        self.display_surface.blit(self.title_text, self.title_rect)
        self.display_surface.blit(self.round_text, self.round_rect)
        self.display_surface.blit(self.time_text, self.time_rect)

    def add_zombie(self):
        """Add a zombie to the game"""
        pass

    def check_collisions(self):
        """Check collisions that affect gameplay"""
        pass

    def check_round_completion(self):
        """Check if the player survived a single night"""
        pass

    def check_game_over(self):
        """Check to see if the player lost the game"""
        pass

    def start_new_round(self):
        """Start a new night"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def reset_game(self):
        "Reset the game"
        pass

class Tile(pygame.sprite.Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, x, y, tile_int, main_group, sub_group = ""):
        """Initialize the tile"""
        super().__init__()
        #Load in the correct image and add it to the correct sub group
        if tile_int == 1:
            self.image = pygame.transform.scale(pygame.image.load("./zombie_knight_assets/images/tiles/Tile (1).png"),
                                                (32,32)).convert_alpha()
        #Platform Tiles
        elif tile_int == 2:
            self.image = pygame.transform.scale(pygame.image.load("./zombie_knight_assets/images/tiles/Tile (2).png"),
                                                (32, 32)).convert_alpha()
            sub_group.add(self)
        elif tile_int == 3:
            self.image = pygame.transform.scale(pygame.image.load("./zombie_knight_assets/images/tiles/Tile (3).png"),
                                                (32, 32)).convert_alpha()
            sub_group.add(self)
        elif tile_int == 4:
            self.image = pygame.transform.scale(pygame.image.load("./zombie_knight_assets/images/tiles/Tile (4).png"),
                                                (32, 32)).convert_alpha()
            sub_group.add(self)
        elif tile_int == 5:
            self.image = pygame.transform.scale(pygame.image.load("./zombie_knight_assets/images/tiles/Tile (5).png"),
                                                (32, 32)).convert_alpha()
            sub_group.add(self)
        #Add every tile to main group
        main_group.add(self)

        #Get the rect of the image and position it within the grid
        self.rect = self.image.get_rect(topleft = (x,y))

class Player(pygame.sprite.Sprite):
    """A class the user can control"""

    def __init__(self):
        """Initialize the player"""
        super().__init__()
        self.health = 100

    def update(self):
        """Update the player"""
        pass

    def move(self):
        """Move the player"""

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        pass

    def check_animations(self):
        """Check to see if the jump/fire animations should run"""
        pass

    def jump(self):
        """Jump upwards if on a platform"""
        pass

    def fire(self):
        """Fire a projectile from sword"""
        pass

    def reset(self):
        """reset the player's position"""
        pass

    def animate(self):
        """Animate the player's actions"""
        pass

class Projectile(pygame.sprite.Sprite):
    """A projectile launched by the player"""

    def __init__(self):
        """Initialize the projectile"""
        pass

    def update(self):
        """Update the projectile"""
        pass

class Zombie(pygame.sprite.Sprite):
    """A class to create enemy zombies that move across the screen"""

    def __init__(self):
        """Initialize the zombie"""
        pass

    def update(self):
        """Update the zombie"""
        pass

    def move(self):
        """Move the zombie"""

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        pass

    def check_animations(self):
        """Check to see if the death/rise animations should run"""
        pass

    def animate(self):
        """Animate the zombie's actions"""
        pass

class RubyMaker(pygame.sprite.Sprite):
    """A tile that is animated. A ruby will be generated here"""

    def __init__(self, x, y, main_group):
        """Initialize the ruby maker"""
        super().__init__()

        #Animation Frames
        self.rubymaker_sprites = []

        #Rotating Animation
        for i in range (7):
            img = pygame.image.load(f"./zombie_knight_assets/images/ruby/tile00{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (64,64))
            self.rubymaker_sprites.append(img)

        #Load image and get rect
        self.current_sprite = 0
        self.image = self.rubymaker_sprites[self.current_sprite]
        self.rect = self.image.get_rect(bottomleft = (x,y))

        #Add to the main group for drawing purposes
        main_group.add(self)

    def update(self):
        """Update the ruby maker"""
        self.animate(self.rubymaker_sprites, .2)

    def animate(self, sprite_list, speed):
        """Animate the ruby maker"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]

class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self):
        """Initialize the ruby"""
        pass

    def update(self):
        """Update the ruby"""
        pass

    def move(self):
        """Move the ruby"""
        pass

    def check_collisions(self):
        """Check to see if the ruby has collided with platforms and portals"""
        pass

    def animate(self):
        """Animate the ruby"""
        pass

class Portal(pygame.sprite.Sprite):
    """A class to create portals that will transport you if you collide with it"""

    def __init__(self, x, y, color, portal_group):
        """Initialize the portal"""
        super().__init__()

        #Create animation frames list
        self.portal_sprites = []

        #Load portal animation frames
        for i in range(22):
            if i < 10:
                img = pygame.image.load(f"./zombie_knight_assets/images/portals/{color}/tile00{i}.png").convert_alpha()
            else:
                img = pygame.image.load(f"./zombie_knight_assets/images/portals/{color}/tile0{i}.png").convert_alpha()
            self.portal_sprites.append(img)

        #Load an image and get a rect
        self.current_sprite = random.randint(0,len(self.portal_sprites) - 1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect(bottomleft = (x,y))

        #Add to the portal group
        portal_group.add(self)

    def update(self):
        """Update the portal"""
        self.animate(self.portal_sprites, .2)

    def animate(self, sprite_list, speed):
        """Animate the portal"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]
