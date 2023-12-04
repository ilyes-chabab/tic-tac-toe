import pygame
import sys

class grille:

    def __init__(self,screen):
        self.screen = screen
        self.lines = [((200,0),(200,600)),
        ((400,0),(400,600)),
        ((0,200),(600,200)),
        ((0,400),(600,400)),]

        self.grille = [[None for x in range(0,3)] for y in range(0,3)]
        self.counter_on = False

    def afficher(self):

        for line in self.lines:

            pygame.draw.line(self.screen,(0,0,0),line[0],line[1],2)

        for y in range(0,len(self.grille)):
            for x in range(0,len(self.grille)):
                if self.grille[y][x] == "X":

                    pygame.draw.line(self.screen,(0,0,0),(x * 200 , y * 200),(200+(x*200),200 + (y*200)),3)
                    pygame.draw.line(self.screen,(0,0,0),((x * 200 ),200+ (y * 200)),(200 + (x*200),(y*200)),3) 

                elif self.grille[y][x]== "O":

                    pygame.draw.circle(self.screen,(0,0,0),(100+(x*200),100+(y*200)),100,3)   

    def print_grille(self):
        print(self.grille)

    def valeur(self,x,y,valeur):
        if self.grille[y][x] == None:
            self.grille[y][x] = valeur
            self.counter_on = True




class game:

    def __init__(self):
        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption('Tic Tac Toe ')
        self.jeu_en_cours = True
        self.grille = grille(self.screen)
        self.player_X = 'X'
        self.player_O = "O"
        self.counter = 0


    def principal_function(self):

        while self.jeu_en_cours:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() [0]:
                    
                    position = pygame.mouse.get_pos()
                    position_x , position_y = position[0]//200 , position[1]//200
                    print(position_x,position_y)

                    self.grille.valeur(position_x,position_y,'X')

                    if self.counter %2 ==0 :
                       self.grille.valeur(position_x,position_y,self.player_X) 
                    else:
                        self.grille.valeur(position_x,position_y,self.player_O) 
                    
                    if self.grille.counter_on == True:
                        self.counter +=1    
                        self.grille.counter_on = False

                self.grille.print_grille()    

            self.screen.fill((240,240,240))
            self.grille.afficher()

            pygame.display.flip()


if __name__=="__main__":
    pygame.init()
    game().principal_function()
    pygame.quit()