import pandas as pd

class GameManager:
    def __init__(self):
        self.d = self.load_dict()
        
    def load_dict(self):
        data = pd.read_csv("./kr_korean_utf.csv")
        nouns = data[data['어미'] == '명사']
        nouns["#NAME?"] = nouns["#NAME?"].str.replace(pat=r'[^\w]', repl=r'', regex=True)
        return nouns

    def check_word(self, word):
        if len(word) <= 1:
            return False
        
        if (self.d['#NAME?'] == word).any():
            return True
        else:
            return False


    def game(self, p1, p2):
        p1_f = True
        p2_f = True
        w1 = ''
        w2 = ''
        w_list = []
        while True:
            w1 = p1.get_word(w2, w_list)

            if w1.lower() == "finish":
                p1_f = False
                break   

            if p1_f == False:
                break   

            print(w1)

            w_list += [w1]
            
            w2 = p2.get_word(w1, w_list)
            if w2 is "FINISH":
                p2_f = False
                break   
            
            print(w2)

            w_list += [w2]

            if p2_f is False:
                break

        if p1_f == True and p2_f == False:
            print("Player1 won!")
        else:
            print("Player2 won!")

if __name__ == "__main__":
    
    from player import Player, Bot
    gm = GameManager()

    p = Player()
    b = Bot()

    gm.game(p, b)