'''
A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once.
'''
def panagram(string):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string:
            return False
        return True

panagram('the quick brown fox jumps over the lazy dog')
panagram("Back in june we delivered oxygen equipment of the same size")