# mlb-fantasy
A MLB fantasy league tracker setup using MLB scores

# How To Use
This is still a work in progress but you fill out the draft_picks.txt like you see with all the players playing in the fantasy league and their picks.  Ensure you use full team names like you see in the file already.

After this is done you will want to use python3 to setup the env:

`python3 -m venv .venv` To setup the virtual env.  This may just be `python` for you depending on your version.

`source .venv/bin/activate` If on Linux to activate virtual env

`.\.venv\Scripts\activate.bat` If on windows to activate virtual env.

Now we can install our requirements:

`pip install -r requirements.txt`

Now we can run the script via:

`python fantasy_mlb.py` and it should generate a .xlsx file for us.  This file will have 3 tabs along the bottom for the Draft Picks, the actual MLB Standings from the live data, and the actual Player Standings data based on the MLB Standings and their picks.