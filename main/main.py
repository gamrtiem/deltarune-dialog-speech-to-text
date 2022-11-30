from pygame import mixer
import speech_recognition as sr
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
zstring = ""
bstring = ""
astring = ""
counter = ""
oneusevariable = 1

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
    
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
    
mixer.init()
mixer.music.load("ralsei_snd.wav")
mixer.music.set_volume(0.7)


g = 0 
r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)

pygame.display.flip()
running  = True
while running:
    
    if g == 3:
        with sr.Microphone() as source:
            print("say anything : ")
            audio= r.listen(source)
            try:
                z = r.recognize_google(audio)
                z = "* " + z
            except:
                z = "* could not recognize "


    def print_string(sentence):
        count = 0
        #sentence = str(sentence)
        while count < len(sentence):
           global k
           k = k + sentence[count]
           o = k
           text = font_1.render(o, False, (255, 255, 255))
           if dialogs == 1:
             scrn.blit(text, (337,64))
           if dialogs == 2:
             scrn.blit(text, (407,144))
           if dialogs == 3:
             scrn.blit(text, (407,224))
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
    zlist = z.split()
    blist = list(b)
    alist = list(a)


    if not change == z and not z == "* huh":
        scrn.blit(dialog, (0, 0))
        scrn.blit(portrait, (74, 86))
        for i in range(1, len(z.split())):
            zlist.insert(i + (i - 1), " ")
        for i in range(len(zlist)):
            counter = counter + zlist[i]
            if len(counter) >= 25 and not len(counter) >= 50:
                blist.append(zlist[i])
            if len(counter) >= 50 and not len(counter) >= 75:
                alist.append(zlist[i])
        counter = ""
        for i in range(len(zlist)):
            if not len(counter) >=25:
                counter = counter + zlist[i]
            if len(counter) >= 25:
                if i < len(zlist):
                    del zlist[i]
        counter = ""



        for i in range(len(zlist)):
            zstring = zstring + zlist[i]
        for i in range(len(blist)):
            bstring = bstring + blist[i]
        for i in range(len(alist)):
            astring = astring + alist[i]

        change = z
        dialogs = 1
        print_string(zstring)
        dialogs = 2
        print_string(bstring)
        dialogs = 3
        print_string(astring)
        change = z
        zstring = ""
        bstring = ""
        astring = ""

        print(zstring)
        print(bstring)
        print(astring)
        time.sleep(1)
        counter = ""

    

    k = ""


    if g == 2:
        g = 3
    if g == 1:
        z = "* have fun!"
        g = 2
    if g == 0:
        z = "* remember to hold  them down or else   they wont go through"
        g = 1
    





    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False