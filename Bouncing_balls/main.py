
import pygame, sys, pymunk  #importing pygame and systems

width, height = 600,600

def create_circle(space,pos): #invisible_circle hitbox
    body = pymunk.Body(1,100,body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 30)
    shape.elasticity = 1.5
    space.add(body, shape)
    return shape


def draw_apples(apples): #visible circle
    for apple in apples:
        if (apple.body.position.x < width and apple.body.position.x > 0 and apple.body.position.y < height and apple.body.position.y > 0):
            pos_x = int(apple.body.position.x)
            pos_y = int(apple.body.position.y)
            pygame.draw.circle(screen,(180,20,20),(pos_x, pos_y), 30)

        else:
            apples.pop(apples.index(apple))

        #print(apple.body.position)

def static_ball(space,pos):
    body = pymunk.Body(body_type= pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,30)
    shape.elasticity = 0.5
    space.add(body, shape)
    return shape

def draw_static_ball(balls): #visible circle
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)

        pygame.draw.circle(screen,(80,20,150),(pos_x, pos_y), 30)



def create_boudaries(space,width, height):
    rects = [
        [(width / 2, height), (width, 1)],
        [(width / 2, 0), (width, 1)],
        [(width, height / 2), (1, height)],
        [(0, height / 2), (1, height)],
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type = pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        space.add(body,shape)
        shape.elasticity = 0.5
        shape.friction = 0.9


pygame.init() # inintializes pygame

screen = pygame.display.set_mode((width, height)) #creating a window
pygame.display.set_caption("Simulation")
clock = pygame.time.Clock() #creating the game clock

space = pymunk.Space()
space.gravity = (0,200)

apples = []
#apples.append(create_circle(space, pos))

balls = []
balls.append(static_ball(space, (450, 100)))
balls.append(static_ball(space, (100, 400)))
balls.append(static_ball(space, (300, 450)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_circle(space,event.pos))


    screen.fill((255,255,255))
    draw_apples(apples)
    draw_static_ball(balls)
    create_boudaries(space, width, height)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120) #limiting fps to 120
