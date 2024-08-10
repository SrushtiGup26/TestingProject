def detect_spam(text):
    # A simple heuristic-based spam detection
    spam_keywords = ["win", "free", "prize", "click", "subscribe"]
    if any(keyword in text.lower() for keyword in spam_keywords):
        return "This message is SPAM."
    return "This message seems to be legitimate."
