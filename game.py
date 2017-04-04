from random import randint

class player:

    def __init__(self, number):
        self.number = number
        self.order = 1
        self.position = dict()
        self.d = dict()
        self.setPosition()
        self.makeDict()
        self.counter = 0

    def setPosition(self):
        if self.number == 2:
            self.position["1"] = (10,0), "h"
            self.position["2"] = (10,1), "h"
            self.position["3"] = (9,0), "h"
            self.position["4"] = (9,1), "h"
            self.position["A"] = (10,10), "h"
            self.position["B"] = (10,9), "h"
            self.position["C"] = (9,10), "h"
            self.position["D"] = (9,9), "h"
        if self.number == 3:
            self.position["1"] = (10,0), "h"
            self.position["2"] = (10,1), "h"
            self.position["3"] = (9,0), "h"
            self.position["4"] = (9,1), "h"
            self.position["A"] = (10,10), "h"
            self.position["B"] = (10,9), "h"
            self.position["C"] = (9,10), "h"
            self.position["D"] = (9,9), "h"
            self.position["E"] = (0,0), "h"
            self.position["F"] = (0,1), "h"
            self.position["G"] = (1,0), "h"
            self.position["H"] = (1,1), "h"
        if self.number == 4:
            self.position["1"] = (10,0), "h"
            self.position["2"] = (10,1), "h"
            self.position["3"] = (9,0), "h"
            self.position["4"] = (9,1), "h"
            self.position["A"] = (10,10), "h"
            self.position["B"] = (10,9), "h"
            self.position["C"] = (9,10), "h"
            self.position["D"] = (9,9), "h"
            self.position["E"] = (0,0), "h"
            self.position["F"] = (0,1), "h"
            self.position["G"] = (1,0), "h"
            self.position["H"] = (1,1), "h"
            self.position["I"] = (0,9), "h"
            self.position["J"] = (0,10), "h"
            self.position["K"] = (1,9), "h"
            self.position["L"] = (1,10), "h"
    
class game(player):

    def __init__(self, players = 2):
        if players > 4:
            print("Privela hracov, max su 4")
            return None
        self.players = players
        self.gameMap = []
        self.loadMap()
        super().__init__(players)
        self.turn = 0
        self.numMove = 0
    

    def loadMap(self):
        self.gameMap = []
        with open('map.txt') as file:
            for line in file:
                foo = []
                for char in line:
                    if char == ',':
                        foo.append(" ")
                    elif char != '\n':
                        foo.append(char)
                self.gameMap.append(foo)

    def __str__(self):
        s = ""
        arr = []
        for name in self.position:
            arr.append(self.position[name][0])
        for i in range(len(self.gameMap)):
            for j in range(len(self.gameMap[i])):
                if (i,j) in arr:
                    for name in self.position:
                        if self.position[name][0] == (i,j): s += name + " "
                else: s += self.gameMap[i][j] + " "
                
            s += "\n"
        return s

    def throwCube(self):
        self.numMove = randint(1,6)
        return self.numMove

    def checkPlayer(self):
        return self.order

    def nextPlayer(self):
        if self.players == 2:
            self.order += 1
            if self.order == 3:
                self.order = 1
        if self.players == 3:
            self.order += 1
            if self.order == 4:
                self.order = 1
        if self.players == 4:
                self.order += 1
                if self.order == 5:
                    self.order = 1

    def checkAllHome(self, player):
        count = 0
        if player == 1:
            if self.position["1"][1] == "h": count += 1
            if self.position["2"][1] == "h": count += 1
            if self.position["3"][1] == "h": count += 1
            if self.position["4"][1] == "h": count += 1
            return count==4
        if player == 2:
            if self.position["A"][1] == "h": count += 1
            if self.position["B"][1] == "h": count += 1
            if self.position["C"][1] == "h": count += 1
            if self.position["D"][1] == "h": count += 1
            return count==4
        if player == 3:
            if self.position["E"][1] == "h": count += 1
            if self.position["F"][1] == "h": count += 1
            if self.position["G"][1] == "h": count += 1
            if self.position["H"][1] == "h": count += 1
            return count==4
        if player == 4:
            if self.position["I"][1] == "h": count += 1
            if self.position["J"][1] == "h": count += 1
            if self.position["K"][1] == "h": count += 1
            if self.position["L"][1] == "h": count += 1
            return count==4

    def checkHome(self, player):
        s = ""
        if player == 1:
            if self.position["1"][1] != "h": s += "1, "
            if self.position["2"][1] != "h": s += "2, "
            if self.position["3"][1] != "h": s += "3, "
            if self.position["4"][1] != "h": s += "4, "
            return s
        if player == 2:
            if self.position["A"][1] != "h": s += "A, "
            if self.position["B"][1] != "h": s += "B, "
            if self.position["C"][1] != "h": s += "C, "
            if self.position["D"][1] != "h": s += "D, "
            return s
        if player == 3:
            if self.position["E"][1] != "h": s += "E, "
            if self.position["F"][1] != "h": s += "F, "
            if self.position["G"][1] != "h": s += "G, "
            if self.position["H"][1] != "h": s += "H, "
            return s
        if player == 4:
            if self.position["I"][1] != "h": s += "I, "
            if self.position["J"][1] != "h": s += "J, "
            if self.position["K"][1] != "h": s += "K, "
            if self.position["L"][1] != "h": s += "L, "
            return s

    def makeDict(self):
        self.d[1] = (10,4)
        self.d[2] = (9,4)
        self.d[3] = (8,4)
        self.d[4] = (7,4)
        self.d[5] = (6,4)
        self.d[6] = (6,3)
        self.d[7] = (6,2)
        self.d[8] = (6,1)
        self.d[9] = (6,0)
        self.d[10] = (5,0)
        self.d[11] = (4,0)
        self.d[12] = (4,1)
        self.d[13] = (4,2)
        self.d[14] = (4,3)
        self.d[15] = (4,4)
        self.d[16] = (3,4)
        self.d[17] = (2,4)
        self.d[18] = (1,4)
        self.d[19] = (0,4)
        self.d[20] = (0,5)
        self.d[21] = (0,6)
        self.d[22] = (1,6)
        self.d[23] = (2,6)
        self.d[24] = (3,6)
        self.d[25] = (4,6)
        self.d[26] = (4,7)
        self.d[27] = (4,8)
        self.d[28] = (4,9)
        self.d[29] = (4,10)
        self.d[30] = (5,10)
        self.d[31] = (6,10)
        self.d[32] = (6,9)
        self.d[33] = (6,8)
        self.d[34] = (6,7)
        self.d[35] = (6,6)
        self.d[36] = (7,6)
        self.d[37] = (8,6)
        self.d[38] = (9,6)
        self.d[39] = (10,6)
        self.d[40] = (10,5)

    def newFromHome(self,player, cube):
        a = input("Vyber si jedneho z domceka: ")
        if ( not self.checkCorrectPLayer(player, a)):
            print("premrhal si svoje sance zlou figurkou! Ide dalsi")
            self.nextPlayer()
            return
        if(player == 1):
            self.position[a] = (self.d[1][0], self.d[1][1]), "n"
        if(player == 2):
            self.position[a] = (self.d[39][0],self.d[39][1]), "n"
        if(player == 3):
            self.position[a] = (self.d[19][0],self.d[19][1]), "n"
        if(player == 4):
            self.position[a] = (self.d[21][0],self.d[21][1]), "n"
        self.counter = 0
        print(g)
        self.nextPlayer()

    def checkLose(self, player):
        count = 0
        if player == 1:
            if self.position["1"][0] == (-1000,-1000): count += 1
            if self.position["2"][0] == (-1000,-1000): count += 1
            if self.position["3"][0] == (-1000,-1000): count += 1
            if self.position["4"][0] == (-1000,-1000): count += 1
            return count == 4
        if player == 2:
            if self.position["A"][0] == (-1000,-1000): count += 1
            if self.position["B"][0] == (-1000,-1000): count += 1
            if self.position["C"][0] == (-1000,-1000): count += 1
            if self.position["D"][0] == (-1000,-1000): count += 1
            return count == 4
        if player == 3:
            if self.position["E"][0] == (-1000,-1000): count += 1
            if self.position["F"][0] == (-1000,-1000): count += 1
            if self.position["G"][0] == (-1000,-1000): count += 1
            if self.position["H"][0] == (-1000,-1000): count += 1
            return count == 4
        if player == 4:
            if self.position["I"][0] == (-1000,-1000): count += 1
            if self.position["J"][0] == (-1000,-1000): count += 1
            if self.position["K"][0] == (-1000,-1000): count += 1
            if self.position["L"][0] == (-1000,-1000): count += 1
            return count == 4
        
    
    def move(self,player, cube):
        print("na vyber mas tycho hracov: " + self.checkHome(player))
        a = input("Vyber si jedneho: ")
        if ( not self.checkCorrectPLayer(player, a)):
            print("premrhal si svoje sance zlou figurkou! Ide dalsi")
            self.nextPlayer()
            return
        poz = self.position[a][0]
        it = list(self.d.keys())[list(self.d.values()).index(poz)]
        it = it + cube
        if (it > 40): it = it - 40
        self.position[a] = (self.d[it][0], self.d[it][1]), "n"
        for name in self.position:
            if ( name != a and self.position[name][0] == self.position[a][0] ):
                print("vyhodil si figurku: " + name)
                print("hrac s touto figurkou uz dalej nemoze hybat")
                self.position[name] = (-1000,-1000), "h"
                if(self.checkLose(player)):
                    print("Hrac s cislom " + str(player) + " prehral")
                    sys.exit(0)
                    return
        print(g)
        self.nextPlayer()

    def checkCorrectPLayer(self, player, s):
        if(player == 1):
            if (s in "1234"): return True
        if(player == 2):
            if (s in "ABCD"): return True
        if(player == 3):
            if (s in "EFGH"): return True
        if(player == 4):
            if (s in "IJKL"): return True
        
    def play(self):
        player = self.checkPlayer()
        cube = self.throwCube()
        if(self.counter == 3):
            print("Vycerpal si vsetky pokusy ide dalsi")
            self.nextPlayer()
            self.counter = 0
            return
        print("Na rade je hrac " + str(player))
        print("Hrac hodil cislo:" + str(cube))
        if(cube != 6 and self.checkAllHome(player)):
            self.counter += 1
            print("Mas vsetkych v domceku a nehodil si cislo 6, otava ti: " + str(3- self.counter) + " pokusy")
            
        elif ( cube == 6 and self.checkAllHome(player)):
            self.newFromHome(player,cube)
        elif ( cube == 6 and not self.checkAllHome(player)):
            a = input("Hodil si cislo 6 chces pokracovat alebo dat novu figurku a/n: ")
            if ( a != "a" and a != "n" ):
                print("Vyber spravnu moznost!")
                a = input("Hodil si cislo 6 chces pokracovat alebo dat novu figurku a/n: ")
            if (a == "a"):
                print("zvolil si dat novu figurku")
                self.newFromHome(player,cube)
            elif ( a == "n" ):
                self.move(player,cube)
        else:
            self.move(player,cube)
            
                    
        




a = input("Zadaj pocet hracov: ")
if int(a) < 5:
    g = game(int(a))
    print(g)
    g.play()
else:
    print("Zadal si vela hracov, max su 4")



                
                
        
