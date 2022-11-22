from vosk import Model, KaldiRecognizer
import pyaudio
import pygame
pygame.init()

x = 296
y = 82
z = "hello wrold"

pygame.display.set_mode((x,y))

scrn = pygame.display.set_mode((x, y))
	

imp = pygame.image.load("images\\dialog.png").convert()
scrn.blit(imp, (0, 0))

font_1 = pygame.font.Font("font\\determinationsansweb-webfont.ttf", 20)


model = Model(r"vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(model, 16000)
    
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
    



pygame.display.flip()
running  = True
while running:  

    text = font_1.render(z, True, (255, 255, 255))
    scrn.blit(text, (0, 0))

    pygame.display.update()
    data = stream.read(4096)
        
    scrn.blit(imp, (0, 0))

    if recognizer.AcceptWaveform(data):
        text2 = recognizer.Result()
        print(f"' {text2[14:-3]} '")
        z = f" {text2[14:-3]} "


    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False