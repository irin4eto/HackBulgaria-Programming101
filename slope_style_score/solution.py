def slope_style_score(scores):
    scores.remove(min(scores))
    scores.remove(max(scores))
    scores = int(sum(scores) / len(scores) * 100)

    return scores / 100
