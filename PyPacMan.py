# -*- coding: utf-8 -*-

'''
Created on 2010/08/31

@author: norikazu
'''

class Player:

    def __init__(self, w, h):
        self.pos_w = w
        self.pos_h = h
        self.previous_w = w
        self.previous_h = h

    def move(self, key, F, D, score):

        if key == "h":
            if F[self.pos_h][self.pos_w -1] == 0:
                self.previous_h = self.pos_h
                self.previous_w = self.pos_w
                self.pos_w -= 1
            else:
                key = "."
        elif key == "j":
            if F[self.pos_h + 1][self.pos_w] == 0:
                self.previous_h = self.pos_h
                self.previous_w = self.pos_w
                self.pos_h += 1
            else:
                key = "."
        elif key == "k":
            if F[self.pos_h - 1][self.pos_w] == 0:
                self.previous_h = self.pos_h
                self.previous_w = self.pos_w
                self.pos_h -= 1
            else:
                key = "."
        elif key == "l":
            if F[self.pos_h][self.pos_w + 1] == 0:
                self.previous_h = self.pos_h
                self.previous_w = self.pos_w
                self.pos_w += 1
            else:
                key = "."
        else:
            key = "."
        
        if D[self.pos_h][self.pos_w] == 1:
            score += 1
            D[self.pos_h][self.pos_w] = 0

        return D, score, key
            
            
    
class Ghost:
    def __init__(self, w, h):
        self.pos_w = w
        self.pos_h = h
        self.previous_w = w
        self.previous_h = h
        self.type = "g"
        self.LRswitch = "L"

    def move_basic(self, F):
        if F[self.pos_h + 1][self.pos_w] == 0:
            self.previous_h = self.pos_h
            self.previous_w = self.pos_w
            self.pos_h += 1
        elif F[self.pos_h][self.pos_w - 1] == 0:
            self.previous_h = self.pos_h
            self.previous_w = self.pos_w
            self.pos_w -= 1
        elif F[self.pos_h - 1][self.pos_w] == 0:
            self.previous_h = self.pos_h
            self.previous_w = self.pos_w
            self.pos_h -= 1
        elif F[self.pos_h][self.pos_w + 1] == 0:
            self.previous_h = self.pos_h
            self.previous_w = self.pos_w
            self.pos_w += 1

    def move_passage(self, F):
        if F[self.pos_h + 1][self.pos_w] == 0 \
            and not ( self.previous_h == self.pos_h + 1 and self.previous_w == self.pos_w ):
            self.previous_h = self.pos_h
            self.previous_w = self.pos_w
            self.pos_h += 1
        elif F[self.pos_h][self.pos_w - 1] == 0 \
            and not ( self.previous_h == self.pos_h and self.previous_w == self.pos_w - 1 ):
            self.previous_h = self.pos_h
            self.previous_w = self.pos_w
            self.pos_w -= 1
        elif F[self.pos_h - 1][self.pos_w] == 0 \
            and not ( self.previous_h == self.pos_h - 1 and self.previous_w == self.pos_w ):
            self.previous_h = self.pos_h
            self.previous_w = self.pos_w
            self.pos_h -= 1
        elif F[self.pos_h][self.pos_w + 1] == 0 \
            and not ( self.previous_h == self.pos_h and self.previous_w == self.pos_w + 1 ):
            self.previous_h = self.pos_h
            self.previous_w = self.pos_w
            self.pos_w += 1

    def move_typeV(self, P, F):
        moved = False
        dx, dy = P.pos_w - self.pos_w, P.pos_h - self.pos_h 
        if dy != 0 and not moved:
            if dy > 0:
                if F[self.pos_h + 1][self.pos_w] == 0:
                    self.previous_h = self.pos_h
                    self.previous_w = self.pos_w
                    self.pos_h += 1
                    moved = True
            else:
                if F[self.pos_h - 1][self.pos_w] == 0:
                    self.previous_h = self.pos_h
                    self.previous_w = self.pos_w
                    self.pos_h -= 1
                    moved = True

        if dx != 0 and not moved:
            if dx > 0:
                if F[self.pos_h][self.pos_w + 1] == 0:
                    self.previous_h = self.pos_h
                    self.previous_w = self.pos_w
                    self.pos_w += 1
                    moved = True
            else:
                if F[self.pos_h][self.pos_w - 1] == 0:
                    self.previous_h = self.pos_h
                    self.previous_w = self.pos_w
                    self.pos_w -= 1
                    moved = True

        if not moved:
            self.move_basic(F)

    def move_typeH(self, P, F):
        moved = False
        dx, dy = P.pos_w - self.pos_w, P.pos_h - self.pos_h 

        if dx != 0 and not moved:
            if dx > 0:
                if F[self.pos_h][self.pos_w + 1] == 0:
                    self.previous_h = self.pos_h
                    self.previous_w = self.pos_w
                    self.pos_w += 1
                    moved = True
            else:
                if F[self.pos_h][self.pos_w - 1] == 0:
                    self.previous_h = self.pos_h
                    self.previous_w = self.pos_w
                    self.pos_w -= 1
                    moved = True

        if dy != 0 and not moved:
            if dy > 0:
                if F[self.pos_h + 1][self.pos_w] == 0:
                    self.previous_h = self.pos_h
                    self.previous_w = self.pos_w
                    self.pos_h += 1
                    moved = True
            else:
                if F[self.pos_h - 1][self.pos_w] == 0:
                    self.previous_h = self.pos_h
                    self.previous_w = self.pos_w
                    self.pos_h -= 1
                    moved = True

        if not moved:
            self.move_basic(F)

    def move_typeL(self, P, F):
        moved = False
        movingtable =[
                        [[[ 0, 0],[ 0, 0],[ 0, 0]], [[ 0, 1],[-1, 0],[ 0,-1]], [[ 0, 0],[ 0, 0],[ 0, 0]]],
                        [[[-1, 0],[ 0,-1],[ 1, 0]], [[ 0, 0],[ 0, 0],[ 0, 0]], [[ 1, 0],[ 0, 1],[-1, 0]]],
                        [[[ 0, 0],[ 0, 0],[ 0, 0]], [[ 0,-1],[ 1, 0],[ 0, 1]], [[ 0, 0],[ 0, 0],[ 0, 0]]]
                    ]

        dx, dy = self.pos_w - self.previous_w + 1, self.pos_h - self.previous_h + 1 

        for vec in movingtable[dx][dy]:
            if F[self.pos_h + vec[1]][self.pos_w + vec[0]] == 0 and not moved:
                self.previous_h = self.pos_h
                self.previous_w = self.pos_w
                self.pos_w += vec[0]
                self.pos_h += vec[1]
                moved = True

        if not moved:
            self.move_basic(F)

    def move_typeR(self, P, F):
        moved = False
        movingtable =[
                        [[[ 0, 0],[ 0, 0],[ 0, 0]], [[ 0,-1],[-1, 0],[ 0, 1]], [[ 0, 0],[ 0, 0],[ 0, 0]]],
                        [[[ 1, 0],[ 0,-1],[-1, 0]], [[ 0, 0],[ 0, 0],[ 0, 0]], [[-1, 0],[ 0, 1],[ 1, 0]]],
                        [[[ 0, 0],[ 0, 0],[ 0, 0]], [[ 0, 1],[ 1, 0],[ 0,-1]], [[ 0, 0],[ 0, 0],[ 0, 0]]]
                    ]

        dx, dy = self.pos_w - self.previous_w + 1, self.pos_h - self.previous_h + 1 

        for vec in movingtable[dx][dy]:
            if F[self.pos_h + vec[1]][self.pos_w + vec[0]] == 0 and not moved:
                self.previous_h = self.pos_h
                self.previous_w = self.pos_w
                self.pos_w += vec[0]
                self.pos_h += vec[1]
                moved = True


        if not moved:
            self.move_basic(F)

    def move_intersection(self, P, F):
        if self.type == "V":
            self.move_typeV(P, F)

        if self.type == "H":
            self.move_typeH(P, F)

        if self.type == "L":
            self.move_typeL(P, F)

        if self.type == "R":
            self.move_typeR(P, F)

        if self.type == "J":
            if self.LRswitch == "L":
                self.move_typeL(P, F)
                self.LRswitch = "R"
            else:
                self.move_typeR(P, F)
                self.LRswitch = "L"

    def move(self, P, F, t):
        if t == 0:
            self.move_basic(F)
            return
        
        canproceed = 0
        if F[self.pos_h + 1][self.pos_w] == 0:
            canproceed += 1
        if F[self.pos_h][self.pos_w - 1] == 0:
            canproceed += 1
        if F[self.pos_h - 1][self.pos_w] == 0:
            canproceed += 1
        if F[self.pos_h][self.pos_w + 1] == 0:
            canproceed += 1

        if canproceed == 1:
            #deadend
            self.move_basic(F)

        elif canproceed == 2:
            #passage
            self.move_passage(F)

        else:
            #intersection
            self.move_intersection(P, F)



class GhostV(Ghost):
    """ Ghost Type V """
    def __init__(self, *av):
        Ghost.__init__(self, *av)
        self.type = "V"

    def move(self, *av):
        Ghost.move(self, *av)
        

class GhostH(Ghost):
    """ Ghost Type H """
    def __init__(self, *av):
        Ghost.__init__(self, *av)
        self.type = "H"

class GhostL(Ghost):
    """ Ghost Type L """
    def __init__(self, *av):
        Ghost.__init__(self, *av)
        self.type = "L"

class GhostR(Ghost):
    """ Ghost Type R """
    def __init__(self, *av):
        Ghost.__init__(self, *av)
        self.type = "R"

class GhostJ(Ghost):
    """ Ghost Type J """
    def __init__(self, *av):
        Ghost.__init__(self, *av)
        self.type = "J"

class game():
    """ game main class """
    def __init__(self, stage):
        """ ゲームの初期化 """
        self.stage = stage
        self.score = 0
        self.T = 0
        self.inputs = ""

        datafilename = "stage"+str(self.stage)+".dat"
        f = open(datafilename, "r")
    
        line = f.readline()
        self.Tlimit = int(line)
        line = f.readline()
        self.W, self.H = line.split()
        self.W, self.H = int(self.W), int(self.H)
    
        self.screen = (self.H+1)*[(self.W+1)*[' ']] #screen
        for i in range(0, self.H+1):
            self.screen[i] = (self.W+1)*[' ']
        self.F = (self.H+1)*[(self.W+1)*[0]] #Field
        self.D = (self.H+1)*[(self.W+1)*[0]] #Dots
        self.E = []     #Enemys
        self.P = None   #Player

        line = f.readline().strip()
        hcount = 1
        while line:
            fline = (self.W+1)*[0]
            dline = (self.W+1)*[0]
            wcount = 1
            for point in line:
                if point == '#':
                    fline[wcount] = 1
                elif point == '.':
                    dline[wcount] = 1
                else:
                    if point == '@':
                        self.P = Player(wcount, hcount)
                    elif point == 'V':
                        self.E.append(GhostV(wcount,hcount))
                    elif point == 'H':
                        self.E.append(GhostH(wcount,hcount))
                    elif point == 'L':
                        self.E.append(GhostL(wcount,hcount))
                    elif point == 'R':
                        self.E.append(GhostR(wcount,hcount))
                    elif point == 'J':
                        self.E.append(GhostJ(wcount,hcount))
    
                wcount += 1
            
            self.F[hcount] = fline
            self.D[hcount] = dline
                
            line = f.readline().strip()
            hcount += 1
    
        f.close()

    def render(self):
        self.screen = (self.H+1)*[(self.W+1)*[' ']] #screen
        for i in range(0, self.H+1):
            self.screen[i] = (self.W+1)*[' ']

        for hcount in range(1, self.H+1):
            for wcount in range(1, self.W+1):
                if self.F[hcount][wcount] == 1:
                    self.screen[hcount][wcount] = "#"
                if self.D[hcount][wcount] == 1:
                    self.screen[hcount][wcount] = "."
        for ghost in self.E:
            self.screen[ghost.pos_h][ghost.pos_w] = ghost.type

        self.screen[self.P.pos_h][self.P.pos_w] = "@"




    def disp(self):
        cls()
        print "T", self.T
        print "score", self.score
        print "inputs", self.inputs
        for hcount in range(1, self.H+1):
            for wcount in range(1, self.W+1):
                print self.screen[hcount][wcount],
            print ""

    def move(self, key):
        for ghost in self.E:
            ghost.move(self.P, self.F, self.T)

        self.D, self.score, key = self.P.move(key, self.F, self.D, self.score)
        
        return key
    
    def detection(self):
        conflict = False
        for g in self.E:
            if g.pos_h == self.P.pos_h and g.pos_w == self.P.pos_w:
                conflict = True
                print g.type, g.pos_h, g.pos_w, "@", self.P.pos_h, self.P.pos_w
                break

            if ( g.pos_h == self.P.previous_h and g.pos_w == self.P.previous_w ) \
            and ( g.previous_h == self.P.pos_h and g.previous_w == self.P.pos_w ):
                print g.type, g.pos_h, g.pos_w, "@", self.P.pos_h, self.P.pos_w
                conflict = True
                break

        return conflict

    def start(self):
        inline = ""
        s = ""
        for self.T in range(0, self.Tlimit):
            self.render()
            self.disp()
            if len(inline) == 0:
                inline = raw_input('?>')

            s = inline[0]
            inline = inline[1:]
            
            self.inputs += self.move(s)
            conflict = self.detection()

            if conflict:
                print "GAME OVER"
                break

def cls():
    import os, sys
    if sys.platform == "win32":
        os.system("CLS")
    else:
        os.system("clear")

def main():
    cls()
    stage = raw_input('stage?(1-3)>')
    g = game(int(stage))
    g.start()

if __name__ == '__main__':
    main()