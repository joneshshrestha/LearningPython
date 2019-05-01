def search4vowels(word):
    """dispaly any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
            print(vowel)
