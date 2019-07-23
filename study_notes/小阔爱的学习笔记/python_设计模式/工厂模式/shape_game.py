import pygame

class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError()

    def move(self, direction):
        if direction == "up":
            self.y -= 4
        elif direction == "down":
            self.y += 4
        if direction == "left":
            self.x -= 4
        elif direction == "right":
            self.x += 4

    @staticmethod
    def factory(type):
        if type == "circle":
            return Circle(100, 100)
        if type == "square":
            return Square(100, 100)
        assert 0, "Bad shape requested: " + type

class Square(Shape):
    def draw(self):
        pygame.draw.rect(
                screen,
                (255,255,0), 
                pygame.Rect(self.x, self.y, 20, 20)
                )

class Circle(Shape):
    def draw(self):
        pygame.draw.circle(
                screen,
                (0,255,255), 
                (self.x, self.y),
                10
                )

if __name__ == "__main__":

    window_dimensions = 800,600

    pygame.init()
    screen = pygame.display.set_mode(window_dimensions)

    x = 100
    y = 100

    # square = Square(100, 100)
    # obj = square
    obj = Shape.factory("square")

    player_quits = False

    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: y -= 4
            if pressed[pygame.K_DOWN]: y += 4
            if pressed[pygame.K_LEFT]: x -= 4
            if pressed[pygame.K_RIGHT]: x += 4

            screen.fill((0,0,0))
            pygame.draw.rect(screen, (255,255,0), pygame.Rect(x,y, 20, 20))
        pygame.display.flip()


