def showBoard(board):
    for i in range(len(board)):
        print(board[i])


def getInput(prompt):
    x = int(input(prompt))
    y = int(input(prompt))
    xy = (x,y)
    return xy


def express(prompt):
    print(prompt)



def Pygame():
    import sys, pygame
    pygame.init()

    size = width, height = 900, 600
    black = 0,0,0
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Free Punjabi Movie 2020")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, black, [400,300,50,50])

        pygame.display.update()