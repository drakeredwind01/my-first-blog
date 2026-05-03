import itertools
from tqdm import tqdm

# python _USB/iterpass_logic_starters_1.py
# --- GLOBALS ---
# How many characters/symbols to add AFTER the starter
MIN_ADDITIONS = 3
MAX_ADDITIONS = 5

STARTERS = ["$", "", "black2black", "$Black2Black", "Black2Black", "black2black ", "$Black2Black ", "Black2Black "]
SYMBOLS = ["$", "_", " "]
ALPHABET = "abcdefhiklmnorstwy" 
OUTPUT_FILE = "targeted_brute.txt"

def generate_targeted_list():
    # Combine symbols and alphabet into the "filler" pool
    fillers = SYMBOLS + list(ALPHABET)
    
    # 1. Calculate Total for tqdm
    # Each starter * (fillers ^ r) for each length r
    total_combos = 0
    for r in range(MIN_ADDITIONS, MAX_ADDITIONS + 1):
        total_combos += len(STARTERS) * (len(fillers)**r)

    # 2. Generate with Progress Bar
    # ---------------------------------------------------------
    # BUFFERING NOTE: Set buffering=1 to flush lines to disk 
    # immediately, keeping RAM usage low. Set to -1 for system 
    # default (faster but uses more RAM).
    with open(OUTPUT_FILE, "w", buffering=1) as f: 
    # ---------------------------------------------------------
        with tqdm(total=total_combos, desc="Generating", unit="lines") as pbar:
            for start in STARTERS:
                # Loop through the number of additions
                for r in range(MIN_ADDITIONS, MAX_ADDITIONS + 1):
                    if r == 0:
                        f.write(f"{start}\n")
                        pbar.update(1)
                    else:
                        # Only symbols and alphabet are allowed here, no Starters
                        # Itertools.product acts as a generator, 
                        # so it doesn't store the whole list in RAM.
                        for addition in itertools.product(fillers, repeat=r):
                            f.write(start + "".join(addition) + "\n")
                            pbar.update(1)

    print(f"Done! Created {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_targeted_list()