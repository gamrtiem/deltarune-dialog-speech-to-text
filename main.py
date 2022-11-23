from pygame import mixer
from vosk import Model, KaldiRecognizer
import pyaudio
import pygame
import time
pygame.init()

x = 1334
y = 376
z = "hellow \n rosld"
linebreak = 0
n = "* "
b = ""
a = ""
k = ""
change = ""

pygame.display.set_mode((x,y))

scrn = pygame.display.set_mode((x, y))
	
portrait = pygame.image.load("images\\ralsei_idle.png").convert()
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
    
mixer.init()
mixer.music.load("images\\ralsei_snd.wav")
mixer.music.set_volume(0.7)


g = 0 

pygame.display.flip()
running  = True
while running:  
    data = stream.read(8192)
    if recognizer.AcceptWaveform(data):
        text2 = recognizer.Result()
        print(f"' {text2[14:-3]} '")
        z = "*" + f" {text2[14:-3]}" 
        print(len(z) - 2)

    def print_string(sentence):
        count = 0

        while count < len(sentence):
           global k
           k = k + sentence[count]
           o = k
           text = font_1.render(o, False, (255, 255, 255))
           if dialogs == 1:
             scrn.blit(text, (337,64))
           if dialogs == 2:
             scrn.blit(text, (337,164))
           print(k)
           pygame.display.update()
           mixer.music.play()
           count += 1
           time.sleep(0.05)
           mylist = z.split()
           del mylist[1]
           
        k = ""
        o = ""

    scrn.blit(portrait, (74, 86))

    zlist = list(z)
    blist = list(b)
    alist = list(a)




    for i in range(len(z)):
        if i > 25:
            blist.append(z[i])
            if i > 50:
                del zlist[i]
            
            


    if not change == zlist:
        scrn.blit(dialog, (0, 0))
        scrn.blit(portrait, (74, 86))
        dialogs = 1
        print_string(zlist)
        dialogs = 2
        print_string(blist)
        dialogs = 3
        print_string(alist)
        change = zlist


    

    k = ""



    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False