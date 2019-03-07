from janome.tokenizer import Tokenizer
import random
import re
import pickle

def load_file(file):
    text = ""
    with open(file, 'r', encoding='utf-8')as f:
        text += f.read().strip()

    unwanted_chars = ['\r','\u3000','-','|']
    for uc in unwanted_chars:
            text = text.replace(uc, '')
    
    unwanted_patterns = [re.compile(r'《.*》'), re.compile(r'［＃.*］')]
    for up in unwanted_patterns:
            text = re.sub(up, '', text)
    
    return text

def make_dictionary(text):
    wordlist = Tokenizer().tokenize(text, wakati=True)
    markov = {}
    w1, w2 = "", ""
    for word in wordlist:
            if w1 and w2:
                    if (w1, w2) not in markov:
                            markov[(w1, w2)] = []
                    markov[(w1, w2)].append(word)
            w1, w2 = w2, word

    return markov

def main():
    load_text = load_file('kaijin_nijumenso.txt')
    splittede_text = make_dictionary(load_text)
    
    with open('janome_make.pickle', mode='wb') as f:
        pickle.dump(splittede_text, f)
    print('ok')
    
if __name__ == "__main__":
    main()