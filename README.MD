# Basketball Players Database

This project uses SQLAlchemy and SQLite to manage a database of basketball players from the Dallas Mavericks (Mavs) and the Boston Celtics. It allows users to add player information and query the database for player comparisons based on their positions.Then outputs the better player in that position by comparing between the two teams, who's stats were better in the previous season of the NBA

## Features

- Add players from the Mavs and Celtics with stats including shooting percentage, rebounds, assists, games played, and position.
- Query the database to find the better player at a specified position between the two teams.
- Compare the stats of players at a specified position between the two teams.
- Find out the better team between Mavs and Celtics in a specific position.
- Add a player to either the mavs' or celtics' table.
- Delete a player to either mavs' or celtics' table

## Running the app
-To run the app, simply run python3 app.py. This prompts you as the user to enter a position for comparison.
-You can add players to the database by running python3 add_player.py and following the prompts.
- The first prompt asks the user to whether they want to add,delete or compare a celtic player to mavs player.
- If they choose to add a player, the user is prompted to enter the player's name, team, position, games played, rebounds, assists
- To confirm addition to the table the user is told that the player has been added to the team successfully
- If they choose to delete a player, the user is prompted to enter the player's name 
-To confrim deletion  the user is told that the player has been deleted from the team he is currently at successfully

## Technologies Used

- **Python**: Programming language used for development.
- **SQLAlchemy**: ORM for managing database operations.
- **SQLite**: Lightweight database used to store player information.
- **Alembic**: Tool for handling database migrations (optional).

   ```bash
   git clone https://github.com/yourusername/basketball-players-database.git
   cd basketball-players-database
