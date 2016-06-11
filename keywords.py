class Operator:
    def __init__(self):
        self.name = ""
        self.meaning = ""
        self.


dictionary = {
    "operator": ["whip", "worship", "tie up", "tickle", "penetrate", "flog", "feel up"],
    "pronoun": ["him", "himself", "her", "herself", "they", "themself", "it", "itself"],
    "control flow": ["if", "while", "until", "end if", "more please", "declare safeword"],
    "context": ["have", "make"],
    "comparison": ["is", "is over", "is under"]
}

keywords = []
for a in [b for b in dictionary.values()]:
    keywords += a
reserved_words = (" ".join(keywords)).split()