import pygame

pygame.init()

screen = pygame.display.set_mode((400,800))

pygame.display.set_caption("Pygame Practice")

clock = pygame.time.Clock()

player = pygame.image.load("./player.png")
player_Rect = player.get_rect()

player_Rect.centerx = round(200)
player_Rect.centery = round(400)

font = pygame.font.SysFont("arial", 30, True, False)
black = (0,0,0)

playing = True

while playing:
    #quit process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

    #main play code
    dx=0
    dy=0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dx = -5
        if event.key == pygame.K_RIGHT:
            dx = 5
        if event.key == pygame.K_UP:
            dy = -5
        if event.key == pygame.K_DOWN:
            dy = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            dx = 0
        if event.key == pygame.K_RIGHT:
            dx = 0
        if event.key == pygame.K_UP:
            dy = 0
        if event.key == pygame.K_DOWN:
            dy = 0


    #coordinate X
    player_Rect.x += dx
    #coordinate Y
    player_Rect.y += dy

    #err fix
    if player_Rect.left <= 0:
        player_Rect.left = 0
        text= font.render("LEFT", True, black)
        screen.blit(text,[200,400])
    if player_Rect.right >= 400:
        player_Rect.right = 400
        text= font.render("RIGHT", True, black)
        screen.blit(text,[200,400])
    if player_Rect.top <= 0:
        player_Rect.top = 0
        text= font.render("TOP", True, black)
        screen.blit(text,[200,400])
    if player_Rect.bottom >= 800:
        player_Rect.bottom = 800
        text= font.render("BOTTOM", True, black)
        screen.blit(text,[200,400])

    #background
    screen.fill((255,255,255))
    screen.blit(player,player_Rect)
    #UPdate
    pygame.display.flip()

    #fps=60
    clock.tick(60)