from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Mavs, Celtics  # Ensure this imports your models

# Create the database engine
engine = create_engine("sqlite:///players.db", echo=True)
Session = sessionmaker(bind=engine)

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

def delete_player(team, player_name):
    session = Session()
    try:
        if team.lower() == 'mavs':## Queries Mavs' table to select player to delete
            player = session.query(Mavs).filter_by(name=player_name).first()
        elif team.lower() == 'celtics':##  Queries Celtics' table to select player to delete
            player = session.query(Celtics).filter_by(name=player_name).first()
        else:
            print("Invalid team. Please specify 'mavs' or 'celtics'.") ##Prompts user to select a valid team 
            return

        if player: ## Checks if player exists in the database
            session.delete(player) ## Deletes that player if they are in the database
            session.commit()
            print(f"Player '{player_name}' deleted from {team} successfully.")
        else:
            print(f"Player '{player_name}' not found in {team}.")
    except Exception as player: ##  Handles any errors that occur during the deletion process
        session.rollback()
        print(f"Error deleting player: {player}")
    session.close()
## This conditional statement is used to determines whether the user wants to add or delete a player
if __name__ == '__main__':
    action = input("Do you want to add or delete a player? (add/delete): ").strip().lower()
    team = input("Enter the team (mavs/celtics): ").strip().lower()
    
    ## Adds players by having the user enter the player's name, stats, and position
    if action == 'add':
        name = input("Enter the player's name: ")
        shots_percentage = int(input("Enter the shooting percentage: "))
        rebounds = int(input("Enter the number of rebounds: "))
        assists = int(input("Enter the number of assists: "))
        games_played = int(input("Enter the number of games played: "))
        position = input("Enter the player's position (PG, SG, SF, PF, C): ")
        add_player(team, name, shots_percentage, rebounds, assists, games_played, position)## Function call to add_player that takes the diffrent variables as arguments
    ## Deletes players by having the player enter the players name
    elif action == 'delete':
        player_name = input("Enter the player's name to delete: ")
        delete_player(team, player_name)## Function call used to delete player
    
    else:
        print("Invalid action. Please specify 'add' or 'delete'.")
