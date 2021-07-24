import json
from random import choice


with open("json/players.json", "r") as f:
    players_list = json.load(f)


def order_match(match):
    return tuple(sorted(match))


def generate_first_round_matches(players):
    players = sorted(players, key=lambda p: (p['rank'], p['last_name'], p['first_name']))
    return [order_match((a['id'], b['id'])) for a, b in zip(players[4:], players[:4])]


def find_score(player_id, played_matches):
    score = 0
    for (id_p1, s1), (id_p2, s2) in played_matches:
        if id_p1 == player_id:
            score += s1
        elif id_p2 == player_id:
            score += s2
    return score


def find_opponent(p1, players, matches):
    for p2 in players:
        match = order_match((p1['id'], p2['id']))
        if match not in matches:
            return p2, match


def generate_next_round_matches(players, matches, played_matches):
    matches = []
    players = sorted(players, key=lambda p: (-find_score(p['id'], played_matches), p['rank']))
    while players:
        p1 = players.pop(0)
        p2, match = find_opponent(p1, players, matches)
        players.pop(players.index(p2))
        played_matches.append(match)
        matches.append(match)
    return matches


def play_match(match):
    score1 = choice((1.0, 0.5, 0.0))
    score2 = 1 - score1
    return ((match[0], score1), (match[1], score2))


def play_matches(matches):
    played_matches = []
    for match in matches:
        played_match = play_match(match)
        played_matches.append(played_match)
    return played_matches


matches = []
t0 = generate_first_round_matches(players_list)
matches += t0

played_matches = []
played_matches += play_matches(matches)

t1 = generate_next_round_matches(players_list, matches, played_matches)
matches += t1

t2 = generate_next_round_matches(players_list, matches, played_matches)
print(t2)