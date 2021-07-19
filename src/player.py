import pandas as pd
import random
from game_manager import GameManager

class PlayerInterface:
    def get_word(self, word):
        pass



class Player(PlayerInterface):
    def get_word(self, word, output):
        player_input = ''
        gm = GameManager()
        while True:
            player_input = input("단어를 입력하세요 : ")

            if word == '':
                break
            if word[-1] != player_input[0] or len(player_input) <= 1:
                print("단어를 다시 입력해주세요")
            elif gm.check_word(player_input):
                print("없는 단어입니다.")
            else:
                break
        output[0] = player_input


class Bot(PlayerInterface):
    def load_dict(self):
        data = pd.read_csv("./kr_korean_utf.csv")
        nouns = data[data['어미'] == '명사']
        return nouns

    
    def get_word(self, word):
        nouns = self.load_dict()
        first_same_noun = []
        for n in nouns['#NAME?']:
            if n[0] == word[-1] and len(n) > 1:
                first_same_noun += [n]

        if first_same_noun == []:
            return "FINISH"

        random_index = random.randrange(len(first_same_noun))

        return first_same_noun[random_index]    

 