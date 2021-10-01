def order_match(match):
    return tuple(sorted(match))


def generate_first_round_matches(players):
    players = sorted(players, key=lambda x: (x.rank, x.last_name, x.first_name))
    return [order_match((a.id, b.id)) for a, b in zip(players[4:], players[:4])]


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
        match = order_match((p1.id, p2.id))
        if match not in tournament_matches:
            players.pop(players.index(p2))
            return p2, match
    p2 = players.pop(0)
    match = order_match((p1.id, p2.id))
    return p2, match


def generate_next_round_matches(players, tournament_matches, score_matches):
    round_matches = []
    players = sorted(players, key=lambda x: (-find_score(x.id, score_matches), x.rank))
    while players:
        p1 = players.pop(0)
        p2, match = find_opponent(p1, players, tournament_matches)
        round_matches.append(match)
        tournament_matches.append(match)
    return round_matches


def generate_round_matches(players, tournament_matches, score_matches, number_round):
    if number_round == 1:
        return generate_first_round_matches(players)
    else:
        return generate_next_round_matches(players, tournament_matches, score_matches)