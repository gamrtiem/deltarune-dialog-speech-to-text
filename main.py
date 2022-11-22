from vosk import Model, KaldiRecognizer
import pyaudio
import pygame
import time
pygame.init()

x = 1334
y = 376
z = "hellow rosld"
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
           scrn.blit(text, (337,64))
           print(k)
           pygame.display.update()
           count += 1
           time.sleep(0.05)
    


    

    g = 0
    if g == 0:
        
        g = 1

    scrn.blit(portrait, (74, 86))

        

  #  for i in range(0, len(z) - 2):
  #      if i > 25 and not i > 50:
  #          b[i - 24] = z[i]
  #          if i > 50 and not i > 75:
  #              a[i - 49] = z[i]
  #              if i > 75 and not i > 100:
  #                  z[i] = " "
  #          z[i] = " "
    if not change == z:
        scrn.blit(dialog, (0, 0))
        scrn.blit(portrait, (74, 86))
        print_string(z)
        print_string(b)
        print_string(a)
        change = z


    

    k = ""



    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False