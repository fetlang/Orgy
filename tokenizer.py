import shlex


# After splitting into semi-meaningful words, the code is split into Token objects
class Token:
    pass


class Tokenizer:
    # Take in raw source code
    def __init__(self, sourcecode):
        self.raw_text = sourcecode
        self._split()
        self._remove_gags()
        print(self.words)

    # Split self.raw_text into lines, and lines into semi-meaningful words
    # That is, words separated by spaces, and quotes
    def _split(self):
        # Split into lines
        lines = self.raw_text.split("\n")

        self.words = []
        for line in lines:
            # Prepare shlexer thing
            shlexer = shlex.shlex(line)
            shlexer.quotes = '"'
            shlexer.whitespace_split = True
            shlexer.commenters = ''  # Comments exist, but in nontraditional way (GAG - UNGAG)

            # Add splat line to words
            self.words.append(list(shlexer))

    # Remove comments(gags) from self.words
    # Orgy programs always start gagged
    def _remove_gags(self):
        new_words = []
        gagged = True

        # Go through self.words and add only ungagged words to new_words
        for line in self.words:
            new_words.append([])
            for word in line:
                if gagged:
                    if word.lower() == "ungag":
                        gagged = False
                else:
                    if word.lower() == "gag":
                        gagged = True
                    else:
                        new_words[-1].append(word)

        # Update self.words
        self.words = new_words

# Test
if __name__ == "__main__":
    Tokenizer("bla bla blbla bla UNGAG hi everybody \"hi buddy\" GAG what")
