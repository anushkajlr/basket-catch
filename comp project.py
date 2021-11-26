import pygame,random,sys,time

points = 0
add = 0
screenx  = 700
screeny = 500
pygame.init()
window = pygame.display.set_mode([screenx,screeny])
window.fill([155,0,255])
black = [0,0,0]


font = pygame.font.SysFont(None, 30)
def start(msg,color):
    
    screen_text = font.render(msg, True , color)
    window.blit(screen_text, [0,250])
def score():
    scoretext = font.render("SCORE:"+str(points) ,True,black)
    window.blit(scoretext , [0,0])
    

window.fill([155,155,155])
messagetoscreen = font.render(' WELCOME TO BASKET CATCH ', True,black)
window.blit(messagetoscreen, [0,250])
pygame.display.update()
pygame.time.delay(1000)


#for the moving object
x = 0
width = 50
height = 10
y = screeny -height
vel = 10
catchcolor = [50,0,50]
#for good object


widthgood = 10
heightgood = 10

xgood = 250
ygood = 0
velgood = 10
goodcolor= [100,0,0]


    





run = True
while run:
    xgoodran = random.randint(0,screenx-widthgood)
    ygood+= velgood
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= 10:
        x-= vel
        

        
    if keys[pygame.K_RIGHT] and x<=screenx - width-10:
        x+= vel
        

    if ygood > 500:
        ygood = 0
        xgood = xgoodran
        
    

    window.fill([155,0,255])
    rect1 = pygame.draw.rect(window, ( catchcolor) ,(x,y,width,height))
    rect2 = pygame.draw.rect(window,(goodcolor),(xgood,ygood,widthgood,heightgood))
    pygame.display.update()
    score()
    pygame.display.update()              
                
                   
        
        
   

    
   
    
        
        
    if rect1.colliderect(rect2) == False and ygood == 500 - height:
        run = False
   
    if rect1.colliderect(rect2) == True:
        points+=1
        
        ygood = 0
        xgood = xgoodran    

start('GAME OVER, SCORE:'+str(points) , black)
pygame.display.update()



time.sleep(2)


pygame.quit
quit()
