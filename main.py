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
        
        self.counter_on = True

        self.start_screen = True
        


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

    def put_none(self,line,column,valeur):

        self.grille[line][column] =valeur




class game:

    def __init__(self):
        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption('Tic Tac Toe ')
        self.jeu_en_cours = True
        self.grille = grille(self.screen)
        self.player_X = 'X'
        self.player_O = "O"
        self.counter = 0
        self.start_screen = True


    def principal_function(self):

        while self.jeu_en_cours:

            while self.start_screen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.start_screen = False    
                self.screen.fill((230,230,230))
                
                self.message('grande', 'Tic Tac Toe', [200, 30, 200, 50], (0, 0, 0))
                self.message('petite', "Ce jeu se joue à deux et chaqu'un se verra attribuer un symbole ",[50, 130, 400, 50], (0, 0, 0))
                self.message('petite', 'X ou O', [220, 150, 100, 100], (0, 0, 0))
                self.message('petite', 'Le premier joueur qui reussi à aligner 3 de ses symboles gagne',[50, 170, 200, 50], (0, 0, 0))
                self.message('moyenne', 'Pour recommencer le jeu , appuyer sur Enter', [70, 350, 200, 50],(0, 0, 0))
                self.message('moyenne', 'Appuyer sur Espace pour commencer le jeu ', [70, 400, 200, 50],(0, 0, 0))
                self.message('moyenne', 'Pour revenir a cette ecran , appuyer sur ESC ', [70, 450, 200, 50],(0, 0, 0))
                pygame.display.flip()

                    
            for event in pygame.event.get():
                

                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() [0]:
                    
                    position = pygame.mouse.get_pos()
                    position_x , position_y = position[0]//200 , position[1]//200
                    print(position_x,position_y)


                    if self.counter %2 ==0 :
                       self.grille.valeur(position_x,position_y,self.player_X) 

                    else:
                        self.grille.valeur(position_x,position_y,self.player_O) 
                    
                    if self.grille.counter_on: 
                        self.counter += 1    
                        print(self.counter)                 
                        self.grille.counter_on = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.play_again()
                   
                             

                self.grille.print_grille()    


                liste_X=[]
                liste_O =[]
                liste_lines_X =[]
                liste_columns_X =[]
                liste_lines_O =[]
                liste_columns_O =[]    


                for line in range(0,len(self.grille.grille)):
                    for column in range(0,len(self.grille.grille)):

                        if self.grille.grille[line][column] == 'X':

                            X_position = (line,column)
                            liste_X.append(X_position)

                        elif self.grille.grille[line][column] == 'O':

                            O_position = (line,column)
                            liste_O.append(O_position)
                print(liste_X)
                if len(liste_X) >= 3 :
                    for (line,column) in liste_X:
                        liste_lines_X.append(line)
                        liste_columns_X.append(column)

                    if liste_lines_X.count(0) ==3 or liste_lines_X.count(1)==3 or liste_lines_X.count(2)==3:
                        print("X a gagné!") 
                    if liste_columns_X.count(0) ==3 or liste_columns_X.count(1)==3 or liste_columns_X.count(2)==3:
                        print("X a gagné!")    
                    if liste_lines_X == liste_columns_X or liste_lines_X == liste_columns_X[::-1]:
                        print("X a gagné!")
                
                if len(liste_O) >= 3 :
                    for (line,column) in liste_O:
                        liste_lines_O.append(line)
                        liste_columns_O.append(column)

                    if liste_lines_O.count(0) ==3 or liste_lines_O.count(1)==3 or liste_lines_O.count(2)==3:
                        print("O a gagné!") 
                    if liste_columns_O.count(0) ==3 or liste_columns_O.count(1)==3 or liste_columns_O.count(2)==3:
                        print("O a gagné!")               
                    if liste_lines_O == liste_columns_O or liste_lines_O == liste_columns_O[::-1]:
                        print("O a gagné!") 



            
                self.screen.fill((240,240,240))
                self.grille.afficher()
                pygame.display.flip()

    def play_again(self):

        for line in range(0,len(self.grille.grille)):
                    for column in range(0,len(self.grille.grille)):
                        self.grille.put_none(line,column,None)

    def message(self,font,message,message_rectangle,color):
        if font == "petite":

            font = pygame.font.SysFont("lato",20,False)

        if font ==  "moyenne":

            font = pygame.font.SysFont("lato",30,False)    
        elif font == "grande":
            font = pygame.font.SysFont("lato",40,True)

        message = font.render(message,False,color)

        self.screen.blit(message,message_rectangle)    


if __name__=="__main__":
    pygame.init()
    game().principal_function()
    pygame.quit()