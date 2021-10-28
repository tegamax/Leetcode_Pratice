class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        magazine_counts = collections.Counter(magazine)
        ransom_note_counts = collections.Counter(ransomNote)

        # For each *unique* character in the ransom note:
        for char, count in ransom_note_counts.items():
            # Check that the count of char in the magazine is equal
            # or higher than the count in the ransom note.
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False

        # If we got this far, we can successfully build the note.
        return True

    
            '''''''''
            # Check for obvious fail case.
            if len(ransomNote) > len(magazine): return False

            # In Python, we can use the Counter class. It does all the work that the
            # makeCountsMap(...) function in our pseudocode did!
            letters = collections.Counter(magazine)

            # For each character, c, in the ransom note:
            for c in ransomNote:
                # If there are none of c left, return False.
                if letters[c] <= 0:
                    return False
                # Remove one of c from the Counter.
                letters[c] -= 1
            # If we got this far, we can successfully build the note.
            return True
            '''''''''
