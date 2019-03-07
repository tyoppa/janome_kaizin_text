import random
import pickle
from janome.tokenizer import Tokenizer

def make_sentence(text):
        t = Tokenizer()
        markov_chain = text
        count = 0
        num = 1
        sentence = ""
        while True:
                w1, w2 = random.choice(list(markov_chain.keys()))
                tmp = random.choice(markov_chain[(w1, w2)])
                tmp = t.tokenize(tmp)[0]
                tmp_hinnsi = tmp.part_of_speech.split(',')[0]
                tmp = tmp.surface
                if tmp_hinnsi == '名詞':
                        sentence += tmp
                        w1, w2 = w2, tmp
                        break
                elif tmp_hinnsi == '動詞':
                        sentence += tmp
                        w1, w2 = w2, tmp
                        break
        while count < num:
                tmp = random.choice(markov_chain[(w1, w2)])
                sentence += tmp
                if(tmp=='。'):
                        count += 1
                        sentence += '\n'
                w1, w2 = w2, tmp
        print(sentence)

def main():
    text = ""
    with open('janome_make.pickle', mode='rb')as f:
        text = pickle.load(f)

    return text


if __name__ == "__main__":
        text = main()
        make_sentence(text)





    