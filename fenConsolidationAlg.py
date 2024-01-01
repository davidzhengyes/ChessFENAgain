FEN=[[1, 1, 1, 1, 1, 1, 1, 1], ['p', 'q', 'k', 'p', 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], ['P', 'Q', 'K', 'P', 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
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

print(finalFEN)
