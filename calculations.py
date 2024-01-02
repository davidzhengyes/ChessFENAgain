import time
import pyautogui
import mouseinputhandler as mh
import math
import apptester
import requests
import chess.engine

#seems like i could have created a class operation
#so i don't have to recalculate topleft and bottomright every time.

def scanrook():

    img="newrook.PNG"

    try:
        t1=time.time()
        #a=pyautogui.locateAllOnScreen(img,grayscale=True)
        a=pyautogui.locate(img,img,grayscale=True)
        print(a)
        # for x in a:
        #     print(x)
        print("time:", time.time()-t1)

    except:
        print("Not found")
    else:

        pass #does what happens if except odesn't run, 
    #cannot put the for x in a here because will reference a again.
    
    finally: 
        print(mh.randomvar)
        pyautogui.moveTo(1150, 940)
        #https://stackoverflow.com/questions/1181464/controlling-mouse-with-python
        print(pyautogui.position()[0])
        print("Woohoo!")

def takeGeneralScreenshots(topleft,bottomright):
    width=bottomright[0]-topleft[0]
    height=bottomright[1]-topleft[1]
    #be VERY CAREFUL WITH THE EDGE ERRORS. maybe increase error or smth.
    #accounting for error, knowing that a chessboard is square
    approxDist=(width+height)//16 #screenshot requires ints.
    pieceRatio=0.7 #take the ratio, in top right so avoiding the numbers and letters.
    #just naming pieces for png files.
    pieces=("rook","knight","bishop","queen","king","bishop","knight","rook") #unique pieces.
     #for the white ones on bottom.
    

    for x in range (len(pieces)):
                                                                                    ##+- 3 on each side to avoid touching lines.
        blackloc=(topleft[0]+x*approxDist+int((1-pieceRatio)*approxDist),topleft[1]+3,int(approxDist*pieceRatio)-3,int(approxDist*pieceRatio)-3)
        whiteloc=(topleft[0]+x*approxDist+int((1-pieceRatio)*approxDist),bottomright[1]-approxDist+3,int(approxDist*pieceRatio)-3,int(approxDist*pieceRatio)-3)
        #MIGHT overflow on right side if bottom right selection is not accurate enough.
        if x%2==0:
            blackboardcolour="white"
            whiteboardcolour="black"
        else:
            blackboardcolour="black"
            whiteboardcolour="white"
        pyautogui.screenshot("black"+pieces[x]+"on"+blackboardcolour+".png",region=blackloc)
        pyautogui.screenshot("white"+pieces[x]+"on"+whiteboardcolour+".png",region=whiteloc)


   


    #screenshot width should be relative to board size.
    boardimg=pyautogui.screenshot("board.png",region=(topleft[0],topleft[1],width,height))

def extrasScreenshots(topleft,bottomright):
    width=bottomright[0]-topleft[0]
    height=bottomright[1]-topleft[1]
    approxDist=(width+height)//16 #screenshot requires ints.
    pieceRatio=0.7 #take the ratio, in top right so avoiding the numbers and letters.

    pieces=("pawn","queen","king","pawn") #unique pieces.
     #for the white ones on bottom.
   

    for x in range (len(pieces)):
                                                                                    ##+- 3 on each side to avoid touching lines.
        blackloc=(topleft[0]+x*approxDist+int((1-pieceRatio)*approxDist),topleft[1]+approxDist+3,int(approxDist*pieceRatio)-3,int(approxDist*pieceRatio)-3)
        whiteloc=(topleft[0]+x*approxDist+int((1-pieceRatio)*approxDist),bottomright[1]-approxDist*2+3,int(approxDist*pieceRatio)-3,int(approxDist*pieceRatio)-3)

        if x%2==0:
            blackboardcolour="black"
            whiteboardcolour="white"
        else:
            blackboardcolour="white"
            whiteboardcolour="black"
        pyautogui.screenshot("black"+pieces[x]+"on"+blackboardcolour+".png",region=blackloc)
        pyautogui.screenshot("white"+pieces[x]+"on"+whiteboardcolour+".png",region=whiteloc)



#if want to later speed things up by 4x, need to retake coordinates of game board
        #as anaysis board is shifted relative to game board.
#should always use top-left corner of image, default for pyatuogui's locateallonscreen.
        
#pieces will never be exactly aligned in a searched row due to 
        #pixel rounding and initialization inaccuracy.
        #still need to verify that all are the same size?
        #integer division by 16, meaning can have up to 16 pixel inaccuracy
        #also human inaccuracy giving maybe 5-10 pixels

def locateAll(topleft,bottomright): #topleft and bottomright of GAME SCREEN.
    print("parameters pass correct")
    width=bottomright[0]-topleft[0]
    height=bottomright[1]-topleft[1]
    approxDist=(width+height)//16 

    #ALSO NEED TO VERIFY THE COORDINATES OF SCREENSHOTS. THIS ASSUMES SC IS TO THE RIGHT AND DOWN OF GRIDLINE.
    #need to change this when switch to game board.
    #####
    ##########
    #############
    def coords(x,y):
        x-=topleft[0]
        y-=topleft[1]

        x=math.floor(x/approxDist)
        y=math.floor(y/approxDist)
        return(x,y)
    

    FEN=[]

    for x in range(8):
        FEN.append([1,1,1,1,1,1,1,1])

    shorthand={'pawn':'p','rook':'r','knight':'n','bishop':'b','king':'k','queen':'q'}
    piececolour=('black','white')
    pieces=('pawn','rook','knight','bishop','king','queen')
    squarecolour=('black','white')
    #finding all black pieces and putting their coordinates into a master list
    for x in piececolour:
        for y in pieces:
            for z in squarecolour:
                location=(x+y+'on'+z+'.png')
                #CAN CHANGE TO LOCATE IN BOARDIMAGE LATER.
                try:
                   
                    for pos in pyautogui.locateAllOnScreen(location,grayscale=True):
                        #maybe try catch for error msg
                        pair=coords(pos[0],pos[1])
                    
                        abbreviation=shorthand[y]
                        if x=='white':
                            abbreviation=abbreviation.upper()
                        FEN[pair[1]][pair[0]]=abbreviation
                except: 
                    print("not found",location)
                else: #not sure if this needed
                    pass
                finally:
                    pass
    print(FEN)

    #USE STACK HERE?
    for x in range(8):
        res=[]
        res.append(FEN[x][0])
        for y in range(1,8):
            
            if ("0" <= str(FEN[x][y]) <= "9") and ("0" <= str(res[-1]) <= "9"):
                res[-1]+=1
            else:
                res.append(FEN[x][y])
        FEN[x]=res

    finalFEN=''
    for x in range(8):
        for y in range(len(FEN[x])):
            finalFEN+=str((FEN[x][y]))
        if x!=7:
            finalFEN+="/"
    print(finalFEN)

    if apptester.win.radioButton.isChecked():
        board = chess.Board(finalFEN + " w - - 4 45")
    else:
        board = chess.Board(finalFEN + " b - - 4 45")

    engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-x86-64-avx2.exe")

    res=(str((engine.play(board, chess.engine.Limit(time=0.2))).move))

    engine.quit()

    
    apptester.win.showText(finalFEN+"\n"+res)



  


