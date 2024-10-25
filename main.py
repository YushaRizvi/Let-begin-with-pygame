#to import the pygame module
import pygame

#to initialise the pygame
pygame.init()

#setup the window with dimensions in a variable
screen = pygame.display.set_mode((500,500))

#to change the bg color
screen.fill("lightblue")

#while playing the game
while True:

    #to get all the events in pygame
    for event in pygame.event.get():

        #if the type of event is pygame.QUIT
        if event.type==pygame.QUIT:

            #close the window
            pygame.quit()
    
    #to make the changes visible on the screen
    pygame.display.flip()
    