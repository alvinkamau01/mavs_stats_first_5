# imports all necessary  modules
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey  
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Mavs(Base): # Creates the table for the mavs team
    __tablename__ = 'mavs' 
    # Creates columns for the table
    id = Column(Integer, primary_key=True)
    name = Column(String)
    shots_percentage = Column(Integer)
    rebounds = Column(Integer)
    assists = Column(Integer)
    games_played = Column(Integer)
    position = Column(String)
    # Initializes instances  of the class
    def __init__(self, name, shots_percentage, rebounds, assists, games_played, position):
        self.name = name
        self.shots_percentage = shots_percentage
        self.rebounds = rebounds
        self.assists = assists  
        self.games_played = games_played
        self.position = position

    def __repr__(self): #shows the representation of the class
        return f"Mavs('{self.name}', '{self.shots_percentage}', '{self.rebounds}', '{self.assists}', '{self.games_played}', '{self.position}')"


class Celtics(Base): #  Creates the table for the celtics team
    __tablename__ = 'celtics'
    #  Creates columns for the table
    id = Column(Integer, primary_key=True)
    name = Column(String)
    shots_percentage = Column(Integer)
    rebounds = Column(Integer)
    assists = Column(Integer)
    games_played = Column(Integer)
    position = Column(String, ForeignKey('mavs.position'))

    # Relationship to Mavs for position
    mavs_player = relationship("Mavs", backref="celtics_players")

    def __init__(self, name, shots_percentage, rebounds, assists, games_played, position):
        self.name = name
        self.shots_percentage = shots_percentage
        self.rebounds = rebounds
        self.assists = assists  
        self.games_played = games_played
        self.position = position

    def __repr__(self):
        return f"Celtics('{self.name}', '{self.shots_percentage}', '{self.rebounds}', '{self.assists}', '{self.games_played}', '{self.position}')"



engine = create_engine("sqlite:///players.db", echo=True)# Connects sqlite to database
Base.metadata.create_all(engine)# Adds all tables to the database

Session = sessionmaker(bind=engine)
session = Session()

# Create player instances by adding the classes arguments
player1M = Mavs('Luca Doncic', 38, 9, 10, 70, 'PG')
player1C = Celtics('Jason Tatum', 37, 8, 5, 74, 'SF')
player2M = Mavs('Kyrie Irving', 41, 9, 5, 58, 'SG')
player2C = Celtics('Jalen Brown', 35, 36, 5, 70, 'SG')
player3M = Mavs('P.J. Washington', 31, 6, 3, 29, 'PF')
player3C = Celtics('Jrue Holiday', 43, 5, 7, 69, 'PF')
player4M = Mavs('Derrick Gafford', 0, 7, 2, 29, 'C')
player4C = Celtics('Kristaps Porzingis', 38, 7, 4, 57, 'C')
player5M = Mavs('D. Jones Jr', 34, 3, 6, 76, 'SF')
player5C = Celtics('Derrick White', 40, 4, 8, 73, 'PG')

# Add all players to the session
players = [player1M, player1C, player2M, player2C, player3M, player3C, player4M, player4C, player5M, player5C]

# Add all players to the database
if players:
    session.add_all(players)
    session.commit()
else:
    print("No players to add.")
