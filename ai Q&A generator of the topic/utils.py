def categorize_difficulty(level: int) -> str:
    if level <= 3:
        return "easy"
    elif level <= 6:
        return "medium"
    else:
        return "hard"
