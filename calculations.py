import time
import pyautogui
import mouseinputhandler as mh
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
    blackpieces=("rook","knight","bishop","queen","king","bishop","knight","rook") #unique pieces.
     #for the white ones on bottom.
    whitepieces=("rook","knight","bishop","king","queen","bishop","knight","rook")

    for x in range (len(blackpieces)):
                                                                                    ##+- 3 on each side to avoid touching lines.
        blackloc=(topleft[0]+x*approxDist+int((1-pieceRatio)*approxDist),topleft[1]+3,int(approxDist*pieceRatio)-3,int(approxDist*pieceRatio)-3)
        whiteloc=(topleft[0]+x*approxDist+int((1-pieceRatio)*approxDist),bottomright[1]-approxDist+3,int(approxDist*pieceRatio)-3,int(approxDist*pieceRatio)-3)

        if x%2==0:
            blackboardcolour="white"
            whiteboardcolour="black"
        else:
            blackboardcolour="black"
            whiteboardcolour="white"
        pyautogui.screenshot("black"+blackpieces[x]+"on"+blackboardcolour+".png",region=blackloc)
        pyautogui.screenshot("white"+whitepieces[x]+"on"+whiteboardcolour+".png",region=whiteloc)


   


    #screenshot width should be relative to board size.
    boardimg=pyautogui.screenshot("board.png",region=(topleft[0],topleft[1],width,height))

def extrasScreenshots(topleft,bottomright):
    width=bottomright[0]-topleft[0]
    height=bottomright[1]-topleft[1]
    print("extras Gone whoooo")

