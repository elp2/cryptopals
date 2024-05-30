# Scoring functions for text


def score_english_ascii_simple(chars):
    ENGLISH_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!.?' "
    ret = 0
    for c in chars:
        if c in ENGLISH_CHARS:
            ret += 1
    return ret / len(chars)

