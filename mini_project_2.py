import re
from collections import Counter

# Common English stopwords (extend as needed)
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
    "to", "of", "in", "on", "at", "for", "with", "as", "by", "it",
    "this", "that", "these", "those", "be", "been", "being", "from",
    "i", "you", "he", "she", "we", "they", "them", "his", "her"
}


class KeywordFrequencyCounter:
    def __init__(self, stopwords=None):
        self.stopwords = stopwords if stopwords is not None else STOPWORDS

    def _tokenize(self, text: str):
        """Lowercase and extract alphabetic words."""
        return re.findall(r"[a-zA-Z']+", text.lower())

    def count(self, text: str, remove_stopwords: bool = True) -> dict:
        """Return a hash table {word: frequency}."""
        freq = {}
        for word in self._tokenize(text):
            if remove_stopwords and word in self.stopwords:
                continue
            freq[word] = freq.get(word, 0) + 1
        return freq

    def top_n(self, text: str, n: int = 5, remove_stopwords: bool = True):
        """Return the top-n most frequent keywords as (word, count) tuples."""
        freq = self.count(text, remove_stopwords)
        # Sort by count desc, then alphabetically for stable output
        return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


# ---------------- Demo ----------------
if __name__ == "__main__":
    text = """
    Python is a powerful programming language. Python is easy to learn and
    easy to read. Many developers love Python because Python is versatile.
    Learning Python opens many doors; learning any language takes practice,
    but Python makes practice fun.
    """

    counter = KeywordFrequencyCounter()

    # Full frequency table
    freq_table = counter.count(text)
    print("Full frequency table:")
    for word, count in sorted(freq_table.items()):
        print(f"  {word:15} -> {count}")

    print("\nTop 5 keywords:")
    for word, count in counter.top_n(text, n=5):
        print(f"  {word:15} -> {count}")

    # Comparison: using collections.Counter (also a hash-based approach)
    print("\n(Using collections.Counter for comparison)")
    quick = Counter(re.findall(r"[a-zA-Z']+", text.lower()))
    print("  Top 3:", quick.most_common(3))