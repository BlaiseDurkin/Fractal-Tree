#fractals
import graphics
from graphics import *
import math

pie = math.pi

def drawBranch(window, leng, angle, fp, g):
    #returns end point and branch
    dx = math.cos(angle)*leng
    dy = math.sin(angle)*leng
    x_n = fp.getX() - dx
    y_n = fp.getY() - dy
    np = Point(x_n,y_n)
    line = Line(fp,np)
    color_val = int(200*math.sin(pie*g/20) + 50) #g must not excede 11
    line.setOutline(color_rgb(color_val, 0, color_val))
    line.draw(window)
    return np ,line
    
def FractalTree(base, length, generation, window, fang):
    fp = base
    igr = 1/1.61803398875
    bl = [] # (branch list) of all branches in fractal
    tdl1 = []    # (two D list) list of nodes of extending from root branch 1
    tdl2 = []    # list of nodes extending from root branch 2
    tdl3 = []    # list of nodes extending from root branch 3
    matrix1 = [] #2D list of each generations angle change
 
    for g in range(generation):
        leng = length*igr**g
        maxbr = int(2**g)
        gl1 = [] #for nodes (generation list 1)
        al1 = [] #for angles (angle list 1)
        gl2 = [] #for nodes
        al2 = [] #for angles
        gl3 = [] #for nodes
        al3 = [] #for angles
        if g == 0:
            np1, line = drawBranch(window, leng, ((fang)*pie/180), fp, g)
            gl1.append(np1)
            fp1 = np1
            al1.append(0)
            matrix1.append(al1)
            bl.append(line)
            #2
            np2, line = drawBranch(window, leng, ((fang+120)*pie/180), fp, g)
            gl2.append(np2)
            fp2 = np2
           
            bl.append(line)
            #3
            np3, line = drawBranch(window, leng, ((fang+240)*pie/180), fp, g)
            gl3.append(np3)
            fp3 = np3
  
            bl.append(line)

        else:
            for num in matrix1[g-1]:
                al1.append(num+1)
                

            for numr in reversed(matrix1[g-1]):
                al1.append(-1*(numr+1))
              

            matrix1.append(al1)
            

            branch = 0
            branchcount = 0
            for i in range(maxbr):
                ang1 = ((fang + 60*(matrix1[g][i]))*pie/180)
                np1, line = drawBranch(window, leng, ang1, tdl1[g-1][branch], g)
                gl1.append(np1)
                bl.append(line)

                ang2 = ((fang+120 + 60*(matrix1[g][i]))*pie/180)
                np2, line = drawBranch(window, leng, ang2, tdl2[g-1][branch], g)
                gl2.append(np2)
                bl.append(line)
    
                ang3 = ((fang-120 + 60*(matrix1[g][i]))*pie/180)
                np3, line = drawBranch(window, leng, ang3, tdl3[g-1][branch], g)
                gl3.append(np3)
                bl.append(line)

                branchcount += 1
                if branchcount %2 == 0:
                    branch +=1
                    
        tdl1.append(gl1)
        tdl2.append(gl2)
        tdl3.append(gl3)
        
    for line in bl:
        line.undraw()
        
def main():
    base = Point(450,400)
    length = 100
    generation = 10
    window = GraphWin("Fractal Tree",900,800)
    window.setBackground("black")
    
    
    for i in range(8):
        #draw several trees and rotate by 30 degrees each time
        FractalTree(base, length, generation, window,(i*30 + 90)) 
    
    window.getMouse()
    window.close()
main()
    
