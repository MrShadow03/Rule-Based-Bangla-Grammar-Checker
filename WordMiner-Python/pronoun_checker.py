from pronoun import Pronoun
from pronoun_tree import tree

pronoun_detector = Pronoun(tree)
pronoun_detector.list_pronouns()

# Test words
test_words = ["আমি", "আমার", "আমরা", "আমায়", "আমিও", "আমাদেরও"]

# Check if each word is accepted
for word in test_words:
    print(f"'{word}' is a pronoun: {pronoun_detector.is_pronoun(word)}")