from vosk import Model, KaldiRecognizer
import pyaudio
import pygame
pygame.init()

x = 1334
y = 376
z = "hello wrold"

pygame.display.set_mode((x,y))

scrn = pygame.display.set_mode((x, y))
	
portrait = pygame.image.load("images\\ralsei_happy.png").convert()
portrait = pygame.transform.scale(portrait, (262, 220))
scrn.blit(portrait, (91, 85))

dialog = pygame.image.load("images\\dialog.png").convert()
scrn.blit(dialog, (0, 0))

font_1 = pygame.font.Font("font\\determinationMono.ttf", 59)


model = Model(r"vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(model, 16000)
    
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
    



pygame.display.flip()
running  = True
while running:  

    text = font_1.render(z, True, (255, 255, 255))
    scrn.blit(text, (337,64))

    pygame.display.update()
    data = stream.read(4096)
        
    scrn.blit(dialog, (0, 0))
    scrn.blit(portrait, (74, 86))
    if recognizer.AcceptWaveform(data):
        text2 = recognizer.Result()
        print(f"' {text2[14:-3]} '")
        z = "*" + f" {text2[14:-3]} "


    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False