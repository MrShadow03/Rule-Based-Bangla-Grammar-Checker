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

    def list_pronouns(self, filename="Possible_pronouns.csv"):
        pronouns = self.generate_pronouns()
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["index", "pronoun", "tree_depth"])  # Write header
            for index, (pronoun, depth) in enumerate(pronouns, start=1):
                writer.writerow([index, pronoun, depth])