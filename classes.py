import pygame

#Define Classes
class Game():
    """A class to manage gameplay"""

    def __init__(self):
        """Initialize the game"""
        pass

    def update(self):
        """Update the game"""
        pass

    def draw(self):
        """Draw the game HUD"""
        pass

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
        pass

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
        for i in range (1, 11):
            img = pygame.image.load(f"./zombie_knight_assets/images/ruby/crystal{i}.png").convert_alpha()
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

    def __init__(self):
        """Initialize the portal"""
        pass

    def update(self):
        """Update the portal"""
        pass

    def animate(self):
        """Animate the portal"""
        pass
