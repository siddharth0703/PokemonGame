from initializers import *

# List of tuples for mouse clicks and position
listofTuples = []
# pygame.draw.aaline(background_image,(255,0,0),(0,580),(380,580))
running = True
while running:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            pygame.draw.circle(background_image, (255, 0, 0), pygame.mouse.get_pos(), 5)
            listofTuples.append(pygame.mouse.get_pos())
            print(listofTuples)
        if event.type == MOUSEBUTTONUP:
            pass
        if event.type == KEYDOWN:
            if event.key == K_f and counter_fullscreen == 0:
                counter_fullscreen = 1;
                newscreen=(1360,760)
                screen = pygame.display.set_mode(newscreen, FULLSCREEN, 32)  # All Advanced features for Windows Display
            elif event.key == K_f and counter_fullscreen == 1:
                counter_fullscreen = 0
                screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
            elif event.key == pygame.K_ESCAPE:
                pause = True
        while pause == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = False
                elif event.type == QUIT:
                    pygame.quit()
                    exit()

# Player Movement with Mouse
    check = pygame.mouse.set_visible(False)
    x_mouse, y_mouse = pygame.mouse.get_pos();
    x_mouse -= lance.get_width() / 2
    y_mouse -= lance.get_height() / 2
    check = pygame.Rect.collidepoint(main_rectangle, x_mouse, y_mouse)
    print("The collision is : ",check)


    screen.blit(lance, (x_mouse, y_mouse))
    clock.tick(60)
    pygame.display.update()
