from utils import Manager
from models.player import player_manager as pm
from models.tournament import tournament_manager as tm


pm.load_from_json("json/players.json")

tm.load_from_json("json/tournaments.json")

print(tm.find_by_id(1))