import json
from random import choice


with open("json/players.json", "r") as f:
    players_list = json.load(f)


def order_match(match):
    return tuple(sorted(match))


def generate_first_round_matches(players):
    players = sorted(players, key=lambda x: (x['rank'], x['last_name'], x['first_name']))
    return [order_match((a['id'], b['id'])) for a, b in zip(players[4:], players[:4])]


def play_match(match):
    score1 = choice((1.0, 0.5, 0.0))
    score2 = 1 - score1
    return ((match[0], score1), (match[1], score2))


def play_matches(round_matches):
    score_matches = []
    for match in round_matches:
        score_match = play_match(match)
        score_matches.append(score_match)
    return score_matches


def find_score(player_id, score_matches):
    score = 0
    for (id_p1, s1), (id_p2, s2) in score_matches:
        if id_p1 == player_id:
            score += s1
        elif id_p2 == player_id:
            score += s2
    return score


def find_opponent(p1, players, tournament_matches):
    for p2 in players:
        match = order_match((p1['id'], p2['id']))
        if match not in tournament_matches:
            players.pop(players.index(p2))
            return p2, match
    p2 = players.pop(0)
    match = order_match((p1['id'], p2['id']))
    return p2, match


def generate_next_round_matches(players, tournament_matches, score_matches):
    round_matches = []
    players = sorted(players, key=lambda x: (-find_score(x['id'], score_matches), x['rank']))
    while players:
        p1 = players.pop(0)
        p2, match = find_opponent(p1, players, tournament_matches)
        round_matches.append(match)
        tournament_matches.append(match)
    return round_matches


# liste des matchs du tournoi
tournament_matches = []

# je joue les matchs du premier tour
t0 = generate_first_round_matches(players_list)

# je génère les scores des matchs du premier tour
score_matches = play_matches(t0)

# j'ajoute les matchs du premier tour à la liste de matchs du tournoi
tournament_matches += t0

# je joue les matchs du deuxième tour
t1 = generate_next_round_matches(players_list, tournament_matches, score_matches)
score_matches += play_matches(t1)

# je joue les matchs du troisième tour
t2 = generate_next_round_matches(players_list, tournament_matches, score_matches)
score_matches += play_matches(t2)

# je joue les matchs du quatrième tour
t3 = generate_next_round_matches(players_list, tournament_matches, score_matches)
score_matches += play_matches(t3)

print(tournament_matches)
