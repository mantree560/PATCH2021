import pandas as pd
import time
from threading import Thread

class GameManager:
    def __init__(self):
        self.d = self.load_dict()
        
    def load_dict(self):
        data = pd.read_csv("./kr_korean_utf.csv")
        nouns = data[data['어미'] == '명사']
        return nouns

    def check_word(self, word):
        if len(word) <= 1:
            return False
        
        if (self.d['#NAME?'] == word).any():
            return True
        else:
            return False

    def timer(self, a):
        start = time.time()

        while True:
            end = time.time()

            if end - start >= 6:
                a[0] = False

    def game(self, p1, p2):
        p1_f = [True]
        p2_f = True
        w1 = ['']
        w2 = ''
        while True:
            th = Thread(target=p1.get_word, args=(w2, w1))
            th.start()
        
            w1 = p1.get_word(w2)
            
            th.join()

            if w1 is "FINISH":
                p1_f[0] = False
                break   

            if p1_f[0] == False:
                break   

            print(w1[0])

            
            w2 = p2.get_word(w1[0])
            if w2 is "FINISH":
                p2_f = False
                break   
            
            print(w2)

            if p2_f is False:
                break

        if p1_f[0] == True and p2_f == False:
            print("Player1 won!")
        else:
            print("Player2 won!")

if __name__ == "__main__":
    
    from player import Player, Bot
    gm = GameManager()

    p = Player()
    b = Bot()

    gm.game(p, b)