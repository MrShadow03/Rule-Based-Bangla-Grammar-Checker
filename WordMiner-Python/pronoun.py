import csv

# class Pronoun:
#     def __init__(self, tree):
#         self.tree = tree

#     def is_pronoun(self, word, generate_csv):
#         def _traverse(node, remaining_word):
#             if not remaining_word:
#                 return True  # The entire word has been matched
#             for prefix, child_node in node.items():
#                 if remaining_word.startswith(prefix):
#                     if _traverse(child_node, remaining_word[len(prefix):]):
#                         return True
#             return False

#         return _traverse(self.tree, word)
    
#     def generate_pronouns(self):
#         pronouns = []

#         def _traverse(node, current_word, current_depth):
#             if current_depth >= 2:  # Include pronouns with depth >= 2
#                 pronouns.append((current_word, current_depth))
#             for prefix, child_node in node.items():
#                 _traverse(child_node, current_word + prefix, current_depth + 1)

#         _traverse(self.tree, "", 0)
#         return pronouns

#     def list_pronouns(self, filename="Possible_pronouns.csv"):
#         pronouns = self.generate_pronouns()
#         with open(filename, mode='w', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             writer.writerow(["index", "pronoun", "tree_depth"])  # Write header
#             for index, (pronoun, depth) in enumerate(pronouns, start=1):
#                 writer.writerow([index, pronoun, depth])


class Pronoun:
    def __init__(self, tree):
        self.tree = tree
        self.detected = []
        self.not_detected = []

    def is_pronoun(self, word, generate_csv=False, csv_filename="Pronoun_detection.csv"):
        def _traverse(node, remaining_word):
            if not remaining_word:
                return True
            for prefix, child_node in node.items():
                if remaining_word.startswith(prefix):
                    if _traverse(child_node, remaining_word[len(prefix):]):
                        return True
            return False

        result = _traverse(self.tree, word)

        if generate_csv:
            if result:
                self.detected.append(word)
            else:
                self.not_detected.append(word)

        return result

    def generate_pronouns(self):
        pronouns = []

        def _traverse(node, current_word, current_depth):
            if current_depth >= 2:
                pronouns.append((current_word, current_depth))
            for prefix, child_node in node.items():
                _traverse(child_node, current_word + prefix, current_depth + 1)

        _traverse(self.tree, "", 0)
        return pronouns

    def list_pronouns(self, filename="Possible_pronouns.csv"):
        pronouns = self.generate_pronouns()
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["index", "pronoun", "tree_depth"])
            for index, (pronoun, depth) in enumerate(pronouns, start=1):
                writer.writerow([index, pronoun, depth])

    def write_detection_results(self, filename="Pronoun_detection.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Word", "Detected"])
            for word in self.detected:
                writer.writerow([word, True])
            for word in self.not_detected:
                writer.writerow([word, False])
