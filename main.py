import pygame 
import random
pygame.init()
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800,800
screen = pygame.display.set_mode((SIZE))
clock = pygame.time.Clock()


class tile:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.color = 1
    def Change(self):
        if self.color==0:
            self.color = 1
        elif self.color==1:
            self.color = 0
    def draw(self,display):
        pygame.draw.rect(display , (self.color*255,self.color*255,self.color*255), [self.x,self.y, 1, 1])

    def color_check(self):
        return self.color



class Board:
    def __init__(self, size):
        self.size = size
        self.draw_list = []
        self.screen = pygame.Surface((800,800))
    def draw_All(self):
        for x in range(len(self.draw_list)):
            for y in range(len(self.draw_list[x])):
                self.draw_list[x][y].draw(self.screen)
        
        screen.blit(self.screen, (0,0))
    def draw_one(self, x, y):
        self.draw_list[x][y].draw(self.screen)
    
    def start(self):
        for i in range(self.size):
            self.draw_list.append([])
            for x in range(self.size):
                self.draw_list[i].append(tile(i,x))

        self.draw_All()

    




class Ant:
    def __init__(self, start_x,start_y, board):
        self.board = board
        self.x = start_x
        self.y = start_y
        self.move_y = 1
        self.move_x = 0
        self.check_color()
    def move(self):
        self.x +=self.move_x
        self.y += self.move_y
        self.draw()
        self.check_color()
    def turn(self, turn_value):
        if turn_value ==1:
            if self.move_x == 0 and self.move_y == 1:
                self.move_x = 1
                self.move_y = 0
               
            elif self.move_x == 1 and self.move_y == 0:
                self.move_x = 0
                self.move_y = -1
              
            elif self.move_x == 0 and self.move_y == -1:
                self.move_x = -1
                self.move_y = 0
              
            elif self.move_x == -1 and self.move_y == 0:
                self.move_x = 0
                self.move_y = 1
             
        

        elif turn_value == -1:
            if self.move_x == 0 and self.move_y == 1:
                self.move_x = -1
                self.move_y = 0
           
            elif self.move_x == 1 and self.move_y == 0:
                self.move_x = 0
                self.move_y = 1
                
            elif self.move_x == 0 and self.move_y == -1:
                self.move_x = 1
                self.move_y = 0
                
            elif self.move_x == -1 and self.move_y == 0:
                self.move_x = 0
                self.move_y = -1
                
    def check_color(self):
        if self.board.draw_list[self.x][self.y].color == 1:
            self.board.draw_list[self.x][self.y].Change()
            self.board.draw_one(self.x,self.y)
            self.turn(1)

        elif self.board.draw_list[self.x][self.y].color == 0:
            self.board.draw_list[self.x][self.y].Change()
            self.board.draw_one(self.x,self.y)
            self.turn(-1)

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), [self.x, self.y, 1, 1])




board = Board(800)

board.start()

player = Ant(200,200, board)


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(board.screen, (0,0))
    player.move()
    player.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(1200)
    pygame.display.update()
pygame.quit()