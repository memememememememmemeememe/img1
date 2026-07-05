import json
import os

CLUB_NAME = "ZYN Sports FC"
DATA_FILE = "stats_data.json"

# Base template if database doesn't exist yet
try:
    with open(DATA_FILE, "r") as f:
        db = json.load(f)
except Exception:
    db = {
        "Miguel":      {"club": CLUB_NAME, "matches": 0, "goals": 0, "wins": 0, "draws": 0, "losses": 0},
        "Max":         {"club": CLUB_NAME, "matches": 0, "goals": 0, "wins": 0, "draws": 0, "losses": 0},
        "Angie":       {"club": CLUB_NAME, "matches": 0, "goals": 0, "wins": 0, "draws": 0, "losses": 0},
        "Cristopher":  {"club": CLUB_NAME, "matches": 0, "goals": 0, "wins": 0, "draws": 0, "losses": 0},
        "Nelson":      {"club": CLUB_NAME, "matches": 0, "goals": 0, "wins": 0, "draws": 0, "losses": 0}
    }

def push_to_github():
    print("\n>>> Pushing fresh stats to GitHub...")
    # These run standard Git terminal commands automatically
    os.system("git add stats_data.json")
    os.system('git commit -m "Auto-update match statistics"')
    os.system("git push origin main")
    print(">>> Sync complete!")

while True:
    print("\n==============================================")
    print(f"      {CLUB_NAME} - STREAMING MANAGER")
    print("==============================================")
    for name, s in db.items():
        print(f"{name:<12} | Matches: {s['matches']} | Goals: {s['goals']} | W/D/L: {s['wins']}/{s['draws']}/{s['losses']}")
    print("==============================================")
    
    print("[1] Update a Player")
    print("[Q] Quit")
    choice = input("\nEnter command: ").strip().lower()
    
    if choice == '1':
        p_name = input("Enter player name: ").strip().capitalize()
        if p_name in db:
            try:
                goals = int(input(f"Goals scored by {p_name}: "))
                res = input("Result (W/D/L): ").strip().upper()
                
                db[p_name]["matches"] += 1
                db[p_name]["goals"] += goals
                if res == 'W': db[p_name]["wins"] += 1
                elif res == 'D': db[p_name]["draws"] += 1
                elif res == 'L': db[p_name]["losses"] += 1
                
                # Save locally inside the img1 folder
                with open(DATA_FILE, "w") as f:
                    json.dump(db, f, indent=4)
                
                # Push it straight online
                push_to_github()
                
            except Exception as e:
                print(f"Error updating stats: {e}")
        else:
            print("Player not found.")
    elif choice == 'q':
        break
