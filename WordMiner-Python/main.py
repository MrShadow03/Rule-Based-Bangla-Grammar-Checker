import csv

class PosTagger:
    def __init__(self, dict_path, text_path):
        self.punctuations = ['।', '.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '~', '`', '‘', '’', '“', '”', '…']
        self.sentence_terminals = ['।', '!', '?']
        self.bangla_digits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
        self.noun_suffixes = self.load_noun_suffixes("./data/bangla-noun-suffixes.csv")
        self.text = self.load_text(text_path)
        self.words = self.text.split(" ")
        self.striped_words = [self.stipe_noun_suffix(word) for word in self.words]
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

        #remove bangla digits
        for digit in self.bangla_digits:
            text = text.replace(digit, '')

        return text
    
    def get_unknown_words(self):
        for word in self.striped_words:
            if word.strip() != "" and word not in self.bangla_dict.values():
                self.unknown_words.append(word)
        return self.unknown_words
    
    def get_known_words(self):
        for word in self.striped_words:
            if word in self.bangla_dict.values():
                self.known_words.append(word)
        return self.known_words
    
    def stipe_noun_suffix(self, word):
        for suffix in self.noun_suffixes:
            if word.endswith(suffix) and len(word) > len(suffix):
                striped_word = word[:-len(suffix)]
                #create a csv file with the original word and the suffix
                with open("words_and_suffixes.csv", "a", encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([striped_word, suffix, len(word), len(suffix)])
                return striped_word
        return word

    

    

tagger = PosTagger("./data/bangla_word_huge_dataset.csv", "./sample-text.txt")
bangla_dict = tagger.get_dict()

# save the unknown words to a file
with open("unknown_words.txt", "w", encoding='utf-8') as file:
    for word in tagger.get_unknown_words():
        file.write(word + "\n")

# save the known words to a file
with open("known_words.txt", "w", encoding='utf-8') as file:
    for word in tagger.get_known_words():
        file.write(word + "\n")


print("Unknown count:", len(tagger.get_unknown_words()))
print("Known count:", len(tagger.get_known_words()))

