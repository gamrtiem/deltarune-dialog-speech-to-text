import pygame
pygame.init()

x = 296
y = 82

pygame.display.set_mode((x,y))

scrn = pygame.display.set_mode((x, y))
	

imp = pygame.image.load("images\\dialog.png").convert()
scrn.blit(imp, (0, 0))


font_1 = pygame.font.Font("font\\determinationsansweb-webfont.ttf", 20)
text = font_1.render("Hello world!", True, (255, 255, 255))

pygame.display.flip()
running  = True
while running:  
    for event in pygame.event.get():  

        if event.type == pygame.QUIT:  

            running = False
    scrn.blit(text, (0, 0))
    pygame.display.update()