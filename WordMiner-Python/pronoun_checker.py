import csv

class Pronoun:
    def __init__(self, tree):
        self.tree = tree

    def is_pronoun(self, word):
        def _traverse(node, remaining_word):
            if not remaining_word:
                return True  # The entire word has been matched
            for prefix, child_node in node.items():
                if remaining_word.startswith(prefix):
                    if _traverse(child_node, remaining_word[len(prefix):]):
                        return True
            return False

        return _traverse(self.tree, word)
    
    def generate_pronouns(self):
        pronouns = []

        def _traverse(node, current_word, current_depth):
            if current_depth >= 2:  # Include pronouns with depth >= 2
                pronouns.append((current_word, current_depth))
            for prefix, child_node in node.items():
                _traverse(child_node, current_word + prefix, current_depth + 1)

        _traverse(self.tree, "", 0)
        return pronouns

    def view_pronouns(self, filename="Possible_pronouns.csv"):
        pronouns = self.generate_pronouns()
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["index", "pronoun", "tree_depth"])  # Write header
            for index, (pronoun, depth) in enumerate(pronouns, start=1):
                writer.writerow([index, pronoun, depth])

possessive_tree_commons = {
        'কে' : {'ই': {}, 'ও': {}},
        'র' : {'ই': {}, 'ও': {}},
        'তে' : {'ই': {}, 'ও': {}},
        'ই': {},
        'ও': {}
}

possessive_suffix_tree = {
    'টি' : {
        **possessive_tree_commons
    },
    'টা' : {
        **possessive_tree_commons
    },
    'টুকু' : {
        **possessive_tree_commons
    },
    'গুলো' : {
        **possessive_tree_commons
    },
    'গুলি' : {
        **possessive_tree_commons
    },
}
# Define the NFA with your structure
tree = {
    #first person
    'আম': {
        'ি': {'ই': {}, 'ও': {}}, 
        'ার': {
            **possessive_suffix_tree,
            'ই': {}, 
            'ও': {}
            },
        'রা': {'ই': {}, 'ও': {}},
    },
    'আমা' : {
        'য়' : {'ও': {}},
        'কে' : {'ই': {}, 'ও': {}},
        'দের' : {
            **possessive_suffix_tree,
            'কে' : {'ই': {}, 'ও': {}},
            'ই': {}, 
            'ও': {},
            },
        'দিগকে' : {'ই': {}, 'ও': {}},
    },
    'মো' : {
        'র' : {},
        'রা' : {'ই': {}, 'ও': {}},
        'দের' : {
            **possessive_suffix_tree,
            'কে' : {'ই': {}, 'ও': {}},
            'ই': {}, 
            'ও': {},
        }
    },

    #second preson
    'তুম' : {
        'ি' : {'ই': {}, 'ও': {}}
    },
    'তোম' : {
        'রা' : {'ই': {}, 'ও': {}},
        'াকে' : {'ই': {}, 'ও': {}},
        'ার': {
            **possessive_suffix_tree,
            'ই': {}, 
            'ও': {}
        },
        'াদের' : {
            **possessive_suffix_tree,
            'কে' : {'ই': {}, 'ও': {}},
            'ই': {}, 
            'ও': {},
        },
        'াদিগকে' : {'ই': {}, 'ও': {}},
    },
    'আপন' : {
        'ি' : {'ই': {}, 'ও': {}},
        'ারা': {'ই': {}, 'ও': {}},
        'াকে': {'ই': {}, 'ও': {}},
        'ার': {
            **possessive_suffix_tree,
            'ই': {}, 
            'ও': {}
        },
        'াদের' : {
            **possessive_suffix_tree,
            'কে' : {'ই': {}, 'ও': {}},
            'ই': {}, 
            'ও': {},
        },
    }
}

pronoun_detector = Pronoun(tree)

pronoun_detector.view_pronouns()

# Test words
test_words = ["আমি", "আমার", "আমরা", "আমায়", "আমিও", "আমাদেরও"]

# Check if each word is accepted
for word in test_words:
    print(f"'{word}' is a pronoun: {pronoun_detector.is_pronoun(word)}")