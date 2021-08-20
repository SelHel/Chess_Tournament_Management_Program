from models.player import player_manager as pm
from models.tournament import tournament_manager as tm
from utils.router import router
from controllers import main_ctrl
from controllers import players_ctrl
from controllers import players_create_ctrl
from controllers import players_all_rank_ctrl
from controllers import players_all_name_ctrl
from controllers import players_edit_ctrl
from controllers import tournaments_ctrl
from controllers import tournaments_create_ctrl
from controllers import tournaments_play_ctrl
from controllers import tournaments_all_ctrl


pm.load_from_json("json/players.json")

tm.load_from_json("json/tournaments.json")

router.add_route("/", main_ctrl)
router.add_route("/players", players_ctrl)
router.add_route("/tournaments", tournaments_ctrl)
router.add_route("/players/create", players_create_ctrl)
router.add_route("/players/all/rank", players_all_rank_ctrl)
router.add_route("/players/all/name", players_all_name_ctrl)
router.add_route("/players/edit", players_edit_ctrl)
router.add_route("/tournaments/create", tournaments_create_ctrl)
router.add_route("/tournaments/play", tournaments_play_ctrl)
router.add_route("/tournaments/all", tournaments_all_ctrl)


router.navigate("/")
