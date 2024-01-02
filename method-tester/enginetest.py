import chess.engine
import chess
import requests
#works
board = chess.Board("8/8/8/2k5/4K3/8/8/8 w - - 4 45")
engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-x86-64-avx2.exe")

print(str((engine.play(board, chess.engine.Limit(time=0.1))).move))

engine.quit()

# res=requests.get("https://stockfish.online/api/stockfish.php?fen=r2q1rk1/ppp2ppp/3bbn2/3p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 11&depth=5&mode=bestmove")
# print(res.content)
# print(res.content[0:5])
