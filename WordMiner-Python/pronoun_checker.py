from pronoun import Pronoun
from pronoun_tree import tree

pronoun_detector = Pronoun(tree)
pronoun_detector.list_pronouns()

# Test words
test_words = [
    # First person
    "আমি", "আমরা", "আমাকে", "আমাদিগকে", "আমাদেরকে", "আমার", "আমাদের", "মোর", "মোরা",
    
    # Second person informal
    "তুমি", "তোমরা", "তোমাকে", "তোমাদিগকে", "তোমাদেরকে", "তোমার", "তোমাদের",
    
    # Third person informal
    "সে", "তারা", "তাহারা", "তাকে", "তাহাকে",
    
    # Second person formal
    "আপনি", "আপনারা", "আপনাকে", "আপনার", "আপনাদের",
    
    # Third person formal and literary
    "তিনি", "তাঁরা", "তাঁহারা", "তাঁদের", "তাঁহাদের", "তাঁহাদিগকে", "তাঁদেরকে", "তাঁহাদেরকে", 
    "তাঁহাকে", "তাঁকে", "ইনি", "এঁর", "এঁরা", "ইহাদের", "ইহাদেরকে", "ইহাকে", "এঁকে", 
    "উনি", "এরা", "এঁদের", "এদেরকে",
    
    # Pronouns with variants
    "ইহা", "ইহারা", "এই", "এ", "এরা", "উঁহা", "উঁহারা", "ওরা", "ওদের"
]

# Check if each word is accepted
for word in test_words:
    print(f"'{word}' is a pronoun: {pronoun_detector.is_pronoun(word)}")