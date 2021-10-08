from utils.player_manager import pm
from utils.tournament_manager import tm
from utils.router import router
from controllers import (
    main_ctrl,
    quit_ctrl,
    players_ctrl,
    players_create_ctrl,
    players_all_rank_ctrl,
    players_all_name_ctrl,
    players_edit_ctrl,
    tournaments_ctrl,
    tournaments_create_ctrl,
    tournaments_play_ctrl,
    tournaments_all_ctrl
    )


pm.load_from_db("json/players.json")

tm.load_from_db("json/tournaments.json")

router.add_route("/", main_ctrl)
router.add_route("/quit", quit_ctrl)
router.add_route("/players", players_ctrl)
router.add_route("/tournaments", tournaments_ctrl)
router.add_route("/players/create", players_create_ctrl)
router.add_route("/players/list/by-rank", players_all_rank_ctrl)
router.add_route("/players/list/by-name", players_all_name_ctrl)
router.add_route("/players/edit", players_edit_ctrl)
router.add_route("/tournaments/create", tournaments_create_ctrl)
router.add_route("/tournaments/play", tournaments_play_ctrl)
router.add_route("/tournaments/list/by-id", tournaments_all_ctrl)


router.navigate("/")
