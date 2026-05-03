import itertools

# Your known components
words = ["test", "tset"]
spacers = ["", "-", "_", "$"]

def generate_combinations(word_list, spacer_list):
    # This generates pairs of words with every possible spacer between them
    # Example: test-tset, test$tset, tset_test, etc.
    combinations = []
    
    # Get all ordered pairs of words
    for pair in itertools.permutations(word_list, 2):
        for s in spacer_list:
            combinations.append(f"{pair[0]}{s}{pair[1]}")
            
    return combinations

# Generate the list
possible_passwords = generate_combinations(words, spacers)

# Print results
print(f"Generated {len(possible_passwords)} potential passwords:")
for pw in possible_passwords:
    print(pw)