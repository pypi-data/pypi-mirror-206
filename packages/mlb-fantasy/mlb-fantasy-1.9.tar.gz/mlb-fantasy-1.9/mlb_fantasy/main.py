from pybaseball import standings
import pandas as pd
import argparse

def main():

    def parse_args():
        parser = argparse.ArgumentParser(description='MLB fantasy draft optimizer')
        parser.add_argument('draft_picks_file', help='Path to draft_picks.txt file')
        # Add any other command-line arguments here
        return parser.parse_args()


    args = parse_args()
    draft_picks_file = args.draft_picks_file

    draft_picks_list = []

    with open(draft_picks_file, 'r') as file:
        for line in file:
            player_name, teams = line.strip().split(': ')
            player_teams = teams.split(',')
            while len(player_teams) < 6:
                player_teams.append('')
            draft_picks_list.append([player_name] + player_teams)

    draft_picks_df = pd.DataFrame(draft_picks_list, columns=['Name', 'Pick 1', 'Pick 2', 'Pick 3', 'Pick 4', 'Pick 5', 'Pick 6'])

    # Define the teams that each player is associated with
    player_teams = {player[0]: player[1:] for player in draft_picks_list}


    # Get current MLB standings
    mlb_standings = standings()

    # Prepare Standings DataFrame
    standings_df = pd.concat(mlb_standings)

    # Calculate the wins and losses for each player
    player_data = []
    for player_name, teams in player_teams.items():
        player_wins = 0
        player_losses = 0
        for team in teams:
            team_wins = 0
            team_losses = 0
            for df in mlb_standings:
                matching_rows = df[df['Tm'] == team]
                if not matching_rows.index.empty:
                    team_record = matching_rows.iloc[0]
                    team_wins = int(team_record['W'])
                    team_losses = int(team_record['L'])

            player_wins += team_wins
            player_losses += team_losses
        if player_wins + player_losses == 0:
            player_win_pct = 0
        else:
            player_win_pct = player_wins / (player_wins + player_losses)
        player_data.append({'Player Name': player_name, 'Wins': player_wins, 'Losses': player_losses, 'Win Percentage': player_win_pct})

    # Prepare Player Standings DataFrame
    player_standings_df = pd.DataFrame(player_data)
    player_standings_df.sort_values(by='Win Percentage', ascending=False, inplace=True)

    # Write DataFrames to Excel
    with pd.ExcelWriter('fantasy_mlb_results.xlsx', engine='openpyxl') as writer:
        draft_picks_df.to_excel(writer, sheet_name='Draft Picks', index=False)
        standings_df.to_excel(writer, sheet_name='MLB Standings', index=False)
        player_standings_df.to_excel(writer, sheet_name='Player Standings', index=False)

    print("Data successfully exported to fantasy_mlb_results.xlsx")


if __name__ == "__main__":
    main()