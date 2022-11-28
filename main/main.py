from pygame import mixer
from vosk import Model, KaldiRecognizer
import pyaudio
import pygame
import time
import keyboard
pygame.init()

x = 1334
y = 376
z = "* hotkeys are       CTRL+1-6 to change  portrait icons"
linebreak = 0
n = "* "
b = ""
a = ""
k = ""
change = ""
portraitImage = 1

pygame.display.set_mode((x,y))

scrn = pygame.display.set_mode((x, y))

portrait = pygame.image.load("ralsei_idle.png").convert()
portrait = pygame.transform.scale(portrait, (262, 220))
scrn.blit(portrait, (91, 85))

dialog = pygame.image.load("dialog.png").convert()
scrn.blit(dialog, (0, 0))

font_1 = pygame.font.Font("determinationMono.ttf", 59)

pygame.display.set_caption('speech to deltarune')
pygame_icon = pygame.image.load('deltarune.png')
pygame.display.set_icon(pygame_icon)


model = Model(r"vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(model, 16000)
    
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
    
mixer.init()
mixer.music.load("ralsei_snd.wav")
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
             scrn.blit(text, (347,144))
           if dialogs == 3:
             scrn.blit(text, (347,224))
           print(k)
           pygame.display.update()
           mixer.music.play()
           count += 1
           time.sleep(0.04)
        k = ""
        o = ""
    

        #optimized code hours right here
    if keyboard.is_pressed("ctrl+1"):
        portraitImage = 1
        print("1")
    elif keyboard.is_pressed("ctrl+2"):
        portraitImage = 2
        print("2")
    elif keyboard.is_pressed("ctrl+3"):
        portraitImage = 3
        print("3")
    elif keyboard.is_pressed("ctrl+4"):
        portraitImage = 4
        print("4")
    elif keyboard.is_pressed("ctrl+5"):
        portraitImage = 5
        print("5")
    elif keyboard.is_pressed("ctrl+6"):
        portraitImage = 6
        print("6")

    if portraitImage == 1:
        portrait = pygame.image.load("ralsei_idle.png").convert()
        portrait = pygame.transform.scale(portrait, (262, 220))
    elif portraitImage == 2:
        portrait = pygame.image.load("ralsei_happy.png").convert()
        portrait = pygame.transform.scale(portrait, (262, 220))
    elif portraitImage == 3:
        portrait = pygame.image.load("ralsei_blush.png").convert()
        portrait = pygame.transform.scale(portrait, (262, 220))
    elif portraitImage == 4:
        portrait = pygame.image.load("ralsei_worry.png").convert()
        portrait = pygame.transform.scale(portrait, (262, 220))
    elif portraitImage == 5:
        portrait = pygame.image.load("ralsei_what.png").convert()
        portrait = pygame.transform.scale(portrait, (262, 220))
    elif portraitImage == 6:
        portrait = pygame.image.load("ralsei_smug.png").convert()
        portrait = pygame.transform.scale(portrait, (262, 220))
        
        #sadly the end of optimized code hours

    scrn.blit(portrait, (74, 86))
    zlist = list(z)
    blist = list(b)
    alist = list(a)


    if not change == z and not z == "* huh":
        scrn.blit(dialog, (0, 0))
        scrn.blit(portrait, (74, 86))
        print(zlist)
        print(change)
        blist.append("  ")
        alist.append("  ")
        if len(z) > 20:
            for i in range(len(z)):
                if i >= 20 and not i >= 40:
                    blist.append(zlist[i])
            for i in range(len(z)):
                if i >= 40 and not i >= 60:
                    alist.append(zlist[i])
            for i in range(len(z)):
                if i >= 20:
                    del zlist[20]
        change = z
        dialogs = 1
        print_string(zlist)
        dialogs = 2
        print_string(blist)
        dialogs = 3
        print_string(alist)
        change = z
        print(str(zlist))
        print(str(blist))
        print(str(alist))
        time.sleep(1)

    

    k = ""

    if g == 1:
        z = "* have fun!"
        g = 2
    if g == 0:
        z = "* remember to hold  them down or else   they wont go through"
        g = 1
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False