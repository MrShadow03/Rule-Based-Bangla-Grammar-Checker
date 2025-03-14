class NFA:
    def __init__(self, transitions, start_state):
        self.transitions = transitions  # Structured NFA transition table
        self.start_state = start_state  # Start state

    def accepts(self, word, state=None):
        """Recursively check if the NFA accepts the given word."""
        if state is None:
            state = self.start_state  # Start from the initial state
        
        if not word:  # If we've processed all characters
            return state in {'ই', 'ও'}  # Check if it's a valid final state
        
        for key in self.transitions.get(state, {}):  # Check available transitions
            if word.startswith(key):  # If the word matches a transition
                next_part = word[len(key):]  # Remove the matched part
                next_states = self.transitions[state][key]  # Get possible next states
                
                if isinstance(next_states, set):  # Direct final states
                    if any(self.accepts(next_part, next_state) for next_state in next_states):
                        return True
                
                elif isinstance(next_states, dict):  # Nested transitions
                    for sub_state, sub_next_states in next_states.items():
                        if next_part.startswith(sub_state):
                            sub_remaining = next_part[len(sub_state):]
                            if any(self.accepts(sub_remaining, final_state) for final_state in sub_next_states):
                                return True
        return False


# Define the NFA with your structure
nfa_transitions = {
    'আম': {
        'ই': {'ই', 'ও'}, 
        'ার': {'ই', 'ও'}, 
        'া': {
            'য়': {'ই', 'ও'}, 
            'রা': {'ই', 'ও'}
        }
    }
}

# Create an NFA instance
nfa = NFA(nfa_transitions, 'আম')

# Test words
test_words = ["আমি", "আমার", "আমরা", "আমায়", "আমিও"]

# Check if each word is accepted
for word in test_words:
    print(f"'{word}' is a pronoun: {nfa.accepts(word)}")
