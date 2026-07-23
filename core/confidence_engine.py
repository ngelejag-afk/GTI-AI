"""
GTI AI Confidence Engine
"""


def calculate_confidence(score: int) -> int:
    """
    Returns confidence score between 0 and 100.
    """
    if score < 0:
        return 0

    if score > 100:
        return 100

    return score
