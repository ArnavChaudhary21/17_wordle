def evaluate(target, guess):

    result = ["gray"] * len(guess)
    remaining = {}
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
        else:
            remaining[target[i]] = remaining.get(target[i], 0) + 1
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if remaining.get(ch, 0) > 0:
            result[i] = "yellow"
            remaining[ch] -= 1
    return result
