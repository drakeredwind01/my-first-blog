
# it might say starters but it can't tell what is a starter
# therefore it will generate all combinations of the starters and symbols up to the specified depth

import itertools

# --- GLOBALS ---
MIN_PLACES = 1  
MAX_PLACES = 4  
STARTERS = ["$", "", "black2black", "$Black2Black", "Black2Black", "black2black ", "$Black2Black ", "Black2Black "]
SYMBOLS = ["$", "_", " "]
# Filtered: Removed q, u, z, p, g, v (Matching your latest list)
ALPHABET = "abcdefhiklmnorstwy" 
OUTPUT_FILE = "targeted_brute.txt"

def generate_targeted_list():
    with open(OUTPUT_FILE, "w") as f:
        print(f"Generating wordlist from {MIN_PLACES} to {MAX_PLACES} places...")
        
        # 1. Generate combinations of keywords and symbols
        for r in range(MIN_PLACES, MAX_PLACES + 1):
            for combo in itertools.product(STARTERS, repeat=r):
                # Plain merge (e.g., black2black$)
                f.write("".join(combo) + "\n")
                
                # Merged with symbols (e.g., black2black_$)
                for sym in SYMBOLS:
                    joined = sym.join(combo)
                    f.write(joined + "\n")
                    # REMOVED: The block that was adding "quotes"

        # 2. Add single characters from alphabet + symbols
        for word in STARTERS:
            for char in ALPHABET:
                for sym in SYMBOLS:
                    f.write(f"{word}{sym}{char}\n")
                    f.write(f"{char}{sym}{word}\n")

    print(f"Done! Created {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_targeted_list()