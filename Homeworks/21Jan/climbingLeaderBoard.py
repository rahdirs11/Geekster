def climbingLeaderboard(ranked, player):
    output = []
    ranked = sorted(list(set(ranked)), reverse=True)
    for p in player:
        while ranked and p >= ranked[-1]:
            ranked.pop()
        output.append(len(ranked) + 1)
    
    return output