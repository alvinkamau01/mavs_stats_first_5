from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Mavs, Celtics  

# Create the database engine
engine = create_engine("sqlite:///players.db", echo=True)
Session = sessionmaker(bind=engine)

def compare_players(position):
    session = Session()

    # Query players by position
    mavs_player = session.query(Mavs).filter_by(position=position).order_by(Mavs.shots_percentage.desc()).first()
    celtics_player = session.query(Celtics).filter_by(position=position).order_by(Celtics.shots_percentage.desc()).first()

    session.close()

    comparison = {}

    if mavs_player:
        comparison['Mavericks'] = {
            "name": mavs_player.name,
            "shots_percentage": mavs_player.shots_percentage,
            "rebounds": mavs_player.rebounds,
            "assists": mavs_player.assists,
            "games_played": mavs_player.games_played
        }

    if celtics_player:
        comparison['Celtics'] = {
            "name": celtics_player.name,
            "shots_percentage": celtics_player.shots_percentage,
            "rebounds": celtics_player.rebounds,
            "assists": celtics_player.assists,
            "games_played": celtics_player.games_played
        }

    if not comparison:
        return "No players found for this position."
    # Determine which player is better by comparing shooting percentages
    if mavs_player and celtics_player:
        better_team = 'Mavericks' if mavs_player.shots_percentage > celtics_player.shots_percentage else 'Celtics'
        comparison['Better Player'] = better_team

    return comparison
#Adds player to Table
def add_player(team, name, shots_percentage, rebounds, assists, games_played, position):
    session = Session()
    try:
        if team.lower() == 'mavs':
            new_player = Mavs(name=name, shots_percentage=shots_percentage, rebounds=rebounds, assists=assists, games_played=games_played, position=position)
            session.add(new_player)
        elif team.lower() == 'celtics':
            new_player = Celtics(name=name, shots_percentage=shots_percentage, rebounds=rebounds, assists=assists, games_played=games_played, position=position)
            session.add(new_player)
        else:
            print("Invalid team. Please specify 'mavs' or 'celtics'.")
            return
        session.commit()
        print(f"Player '{name}' added to {team} successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding player: {e}")
    session.close()
## Deletes plsyer from table
def delete_player(team, player_name):
    session = Session()
    try:
        if team.lower() == 'mavs':
            player = session.query(Mavs).filter_by(name=player_name).first()
        elif team.lower() == 'celtics':
            player = session.query(Celtics).filter_by(name=player_name).first()
        else:
            print("Invalid team. Please specify 'mavs' or 'celtics'.")
            return

        if player:
            session.delete(player)
            session.commit()
            print(f"Player '{player_name}' deleted from {team} successfully.")
        else:
            print(f"Player '{player_name}' not found in {team}.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting player: {e}")
    session.close()

#determines whether the user wants to add or delete a player or do a comparison between which player is better and which team is best in that position
if __name__ == '__main__':
    action = input("Do you want to add, delete a player, or do a comparison? (add/delete/compare): ").strip().lower()
    
    if action == 'add' or action == 'delete':
        team = input("Enter the team (mavs/celtics): ").strip().lower()
    
        if action == 'add':
            name = input("Enter the player's name: ")
            shots_percentage = int(input("Enter the shooting percentage: "))
            rebounds = int(input("Enter the number of rebounds: "))
            assists = int(input("Enter the number of assists: "))
            games_played = int(input("Enter the number of games played: "))
            position = input("Enter the player's position (PG, SG, SF, PF, C): ")
            add_player(team, name, shots_percentage, rebounds, assists, games_played, position)

        elif action == 'delete':
            player_name = input("Enter the player's name to delete: ")
            delete_player(team, player_name)

    elif action == 'compare':
        position = input("Enter the position (e.g., PG, SG, SF, PF, C): ")
        result = compare_players(position)
        print(result)

    else:
        print("Invalid action. Please choose 'add', 'delete', or 'compare'.")
