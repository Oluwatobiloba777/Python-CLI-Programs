# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(Fstring,Sstring):
    Fstring = Fstring.strip()
    Sstring = Sstring.strip()
    if sorted(Fstring) == sorted(Sstring):
        return True
    return False
print(find_anagrams("carnivorous","coronavirus"))

