import csv

class PosTagger:
    def __init__(self, dict_path, text_path):
        self.punctuations = ['.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '~', '`', '‘', '’', '“', '”', '…']
        self.noun_suffixes = self.load_noun_suffixes("./data/bangla-noun-suffixes.csv")
        self.text = self.load_text(text_path)
        self.words = self.text.split(" ")
        self.pos_tags = ["NOUN"]
        self.bangla_dict = {}
        self.load_bangla_dict(dict_path)
        self.known_words = []
        self.unknown_words = []

    def load_bangla_dict(self, file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            i = 0
            for line in file:
                self.bangla_dict.update({i: line.strip()})
                i += 1
            print("Bangla dictionary loaded successfully")

    def load_noun_suffixes(self, file_path):
        suffixes = []
        with open(file_path, "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) > 1:
                    suffixes.append(row[1].strip())
        return suffixes
            

    def get_dict(self):
        return self.bangla_dict
    
    def load_text(self, file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            text = file.read()
        return self.clean_text(text)
    
    def clean_text(self, text):
        # Remove punctuations
        for p in self.punctuations:
            text = text.replace(p, '')
        # Remove multiple spaces keeping only one
        text = ' '.join(text.split())
        return text
    
    def get_unknown_words(self):
        for word in self.words:
            if word not in self.bangla_dict.values():
                self.unknown_words.append(word)
        return self.unknown_words
    
    def get_known_words(self):
        for word in self.words:
            if word in self.bangla_dict.values():
                self.known_words.append(word)
        return self.known_words

    

    

# tagger = PosTagger("./data/bangla_word_huge_dataset.csv", "./sample-text.txt")
# bangla_dict = tagger.get_dict()

# print("Unknown count:", len(tagger.get_unknown_words()))
# print("Known count:", len(tagger.get_known_words()))

