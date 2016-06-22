import operators

dictionary = {
	"objective pronouns": ["him", "her", "they", "it"],
	"reflexive pronouns": ["himself","herself", "themself", "itself"],
	"possessive pronouns": ["his", "her", "their", "its"],
	"possessive reflexive pronouns": ["his own", "her own", "their own", "its own"],
	"control flow": ["if", "while", "until", "end if", "more please", "declare safeword", "with safeword"],
	"context": ["have", "make", "times"],
}

# Add list of operators (primary and secondary names) to dictionary
dictionary += {"operators": [a.name for a in operators.operators]+[a.alt for a in filter(
	lambda b: b is not None, operators.operators)]}

# Add list of comparison operator (primary and secondary names) to dictionary
dictionary += {"comparison operators": [a.name for a in operators.comparison_operators]+[a.alt for a in filter(
	lambda b: b is not None, operators.comparison_operators)]}

# The list version of the dictionary: keywords
keywords = []
for a in [b for b in dictionary.values()]:
	keywords += a

# Every actual word that could be part of a meaning
base_words = (" ".join(keywords)).split()