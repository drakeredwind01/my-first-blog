import itertools
import math

# --- Configuration ---
words = [
         "open",
         "sesame",
         "seed",
         "it was the best of times",
         "it was the worst of times",
         "bert",
        ]
spacers = ["", "_", "$", " "]
starters = ["$", "", "black2black", "$Black2Black", "Black2Black", "black2black ", "$Black2Black ", "Black2Black "] # Added the empty string if you want no starter too
depth = 4  # Number of words in the sequence

output_file = "brute_wordlist.txt"

def calculate_total(w_list, s_list, start_list, d):
    # Math: Starters * (Words^Depth) * (Spacers^(Depth-1))
    word_combos = len(w_list) ** d
    spacer_combos = len(s_list) ** (d - 1)
    return len(start_list) * word_combos * spacer_combos

def generate_to_file():
    total = calculate_total(words, spacers, starters, depth)
    print(f"Total potential passwords to generate: {total}")
    
    count = 0
    with open(output_file, "w") as f:
        # Loop through each possible starter
        for prefix in starters:
            # Generate every possible combination of words for the given depth
            for word_combo in itertools.product(words, repeat=depth):
                # Generate every possible combination of spacers to go BETWEEN the words
                for spacer_combo in itertools.product(spacers, repeat=depth - 1):
                    
                    # Construct the string
                    current_pass = prefix
                    for i in range(len(spacer_combo)):
                        current_pass += word_combo[i] + spacer_combo[i]
                    
                    # Add the final word
                    current_pass += word_combo[-1]
                    
                    f.write(current_pass + "\n")
                    count += 1
                    
                    # Progress update every 10,000 lines
                    if count % 10000 == 0:
                        print(f"Progress: {count}/{total} written...")

    print(f"Done! Wordlist saved to {output_file}")

if __name__ == "__main__":
    generate_to_file()


'''
$ python iterpass_2.py 

$ john --wordlist="/home/drake/Documents/github/my-first-blog/_USB/brute_wordlist.txt" "/home/drake/Documents/hack/zip_hash.txt"


# --- Configuration ---
words = [
         "open",
         "sesame",
         "seed",
         "IHSS",
         "bert",
        ]
spacers = ["", "_", "$", " "]
starters = ["$", "", "black2black", "$Black2Black", "Black2Black", "black2black ", "$Black2Black ", "Black2Black "] # Added the empty string if you want no starter too
depth = 4  # Number of words in the sequence



# --- Configuration ---
words = [
         "open",
         "sesame",
         "seed",
         "IHSS",
         "bert",
        ]
spacers = ["", "_", "$", " "]
starters = ["$", "",] # Added the empty string if you want no starter too
depth = 4  # Number of words in the sequence




'''

