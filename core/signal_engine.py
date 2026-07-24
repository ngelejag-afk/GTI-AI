"""
GTI AI
Signal Engine
Version 1.0
"""


def generate_signal(
    decision: str,
    confidence: int,
    explanation: str,
) -> str:
    """
    Generate the final GTI AI trading signal.
    """

    return f"""
==============================
GTI AI SIGNAL
==============================

Decision   : {decision}

Confidence : {confidence}%

------------------------------

{explanation}

==============================
"""
