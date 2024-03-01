#Backtracking sudoku solver

#examples
"""
530 070 000
600 195 000
098 000 060
800 060 003
400 803 001
700 020 006
060 000 280
000 419 005
000 080 079"""


"""really hard one
800 000 000
003 600 000
070 090 200
050 007 000
000 045 700
000 100 030
001 000 068
008 500 010
090 000 400
"""


'''
030 010 060
750 030 048
006 984 300
003 000 800
912 000 674
004 000 500
001 675 200
680 090 015
090 040 030
'''
import termcolor
def inputSudoku():
  Sudoku = []
  global SudokuHints
  SudokuHints=[]
  print('enter numbers as numbers 1-9 and use zeroes for blank boxes')
  print('Use the below format for the sudoku')
  print('for example, use:')
  print("""
030 010 060
750 030 048
006 984 300
003 000 800
912 000 674
004 000 500
001 675 200
680 090 015
090 040 030
  """)
  print('for the sudoku:')
  PrintSudoku(['030 010 060','750 030 048','006 984 300','003 000 800','912 000 674','004 000 500','001 675 200','680 090 015','090 040 030'])
  message = (("input row {}").format(1))
  print('Enter your sudoku or press "e" for example:')
  val=(input())
  Sudoku.append(val)
  SudokuHints.append(val)
  if Sudoku[0] == 'e':
      Sudoku = ['030 010 060','750 030 048','006 984 300','003 000 800','912 000 674','004 000 500','001 675 200','680 090 015','090 040 030']
      SudokuHints =['030 010 060','750 030 048','006 984 300','003 000 800','912 000 674','004 000 500','001 675 200','680 090 015','090 040 030']
      #['000 700 000','100 000 000','000 430 200','000 000 006','000 509 000','000 000 418','000 081 000','002 000 050','040 000 300'] 
      #['530 070 000','600 195 000','098 000 060','800 060 003','400 803 001','700 020 006','060 000 280','000 419 005','000 080 079']
  else:
    for n in range(8):
      message = (("input row {}").format(n+2))
      val=(input())
      Sudoku.append(val)
      SudokuHints.append(val)
  print('you have entered the sudoku:')
  PrintSudoku(Sudoku)
  print('if this is correct press enter, otherwise enter q to try inputing the sudoku again')
  redo = input()
  if redo == 'q':
    Sudoku = inputSudoku()
  
  return Sudoku
def PrintSudoku(rows):
  for n in range(9):
    printVariable = rows[n]
    for n2 in range(len(printVariable)):
      if printVariable[n2] != '0':
        color = 'green'
      else:
        color = 'red'
      termcolor.cprint(printVariable[n2],color,end =' ')
    print()
    if (n+1)//3 == (n+1)/3:
      print()

def HelpfulVariables(Sudoku):
  global rows
  global SudokuByCollumns
  global SudokuBySquairs
  SudokuBySquairs = []
  rows=Sudoku
  SudokuByCollumns = []
  
  for n in range(11):
    collumn = ''
    for n2 in range(9):
      collumn=collumn+(rows[n2][n])
    SudokuByCollumns.append(collumn)
  n=0
  n2=0
  Squair = ''
  for t in range(3):
    
    for n in range(9):
      
      if (n)//3 == (n)/3:
        Squair = ''
      x=t*4
      for n2 in range(3):
        Squair += Sudoku[n][n2+x]
      if (n+1)//3 == (n+1)/3:
        
        SudokuBySquairs.append(Squair)
def RowCorrect(num,x):
  if num in rows[x]:
    return(False)
  else:
    return(True)
    
def CollumnCorrect(num,x):
  if num in SudokuByCollumns[x]:
    return(False)
  else:
    return(True)
def SquairCorrect(num,x):
  if num in SudokuBySquairs[x]:
    return(False)
  else:
    return(True)
def calculatePosition(x,y):
    if x == 0 or x == 1 or x ==2:
      squairX = 1
    elif x == 3 or x==4 or x ==5:
      squairX = 2
    else:
      squairX = 3

    if y == 0 or y == 1 or y ==2:
      squairY = 1
    elif y == 4 or y==5 or y ==6:
      squairY = 2
    else:
      squairY = 3

    if squairX == 1 and squairY == 1:
      squair=0
    elif squairX == 2 and squairY == 1:
      squair=1
    elif squairX == 3 and squairY == 1:
      squair=2
    elif squairX == 1 and squairY == 2:
      squair=3
    elif squairX == 2 and squairY == 2:
      squair=4
    elif squairX == 3 and squairY == 2:
      squair=5
    elif squairX == 1 and squairY == 3:
      squair=6
    elif squairX == 2 and squairY == 3:
      squair=7
    else:
      squair=8
    return squair
Sudoku = inputSudoku()
HelpfulVariables(Sudoku)

solved = False

T = 0
x=0
y=0
position = 0
num = 1
while solved == False:
  HelpfulVariables(Sudoku)
  if y==11:
    x+= 1
    if x == 9:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print ('the solution to your sudoku:')
        PrintSudoku(SudokuHints)
        print('is:')
        PrintSudoku(Sudoku)
        break
    y = 0
  if SudokuHints[x][y]=='0' or num>9:
    
    if num > 9:
      Sudoku[x] = Sudoku[x][0:y]+'0'+Sudoku[x][y+1:]
      unsolved = True
      while unsolved:
        HelpfulVariables(Sudoku)
        if y>0 or x>0:
          y-= 1
        else: 
          print('this sudoku has no solution, are you sure you entered it correctly?')
          PrintSudoku(SudokuHints)
          while True:
            pass
          
        if y<0 and x>0:
          y = 10
          x -=1
          
        #cannot change a hint
        if Sudoku[x][y] !=' ' and SudokuHints[x][y] =='0':
           num = int(Sudoku[x][y])+1

           if num>10:
             pass
           else:
            
            Sudoku[x] = Sudoku[x][0:y]+'0'+Sudoku[x][y+1:]
            if num > 9:
              pass
            else:
              unsolved = False
            HelpfulVariables(Sudoku)
            
            
        else: 
          pass
          
        
      
      
    squair = calculatePosition(x,y)
    
    if RowCorrect(str(num),x):
      if CollumnCorrect(str(num),y):
        if SquairCorrect(str(num),squair):
          
          Sudoku[x] = Sudoku[x][0:y]+str(num)+Sudoku[x][y+1:]
          #HelpfulVariables(Sudoku)
          T += 1
          #end graphics if processing takes too long (even though I really like the graphics)
          if T<1000 and T//1== T/1:
            print('\n\n')
            PrintSudoku(Sudoku)
          elif T==3000 or T//15000== T/15000:
            print('\n\n')
            PrintSudoku(Sudoku)
            print('To increase processing speed, numbers will no longer be shown regularly')
            

          num = 1
          y+=1
        else:
          num += 1
          
      else:
        num += 1
        
    else:
       num += 1
       
    
  else:
    y+= 1
    if y> 10:
      x+= 1
      y = 0
      if x==9:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print ('the solution to your sudoku:')
        PrintSudoku(SudokuHints)
        print('is:')
        PrintSudoku(Sudoku)
        break