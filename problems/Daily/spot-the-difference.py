def difference(s, t):
    # Making sure lengths are right
    if len(t) - len(s) != 1:
        return 'Lenghts not right!'
    
    exists = {}
    
    # Putting all the characters in the string s into a dictionary
    for letter in s:
        if exists.get(letter) is not None:
            exists[letter] += 1
        else:
            exists[letter] = 1
            
    # Checking if the characters in the string t are in the dictionary
    for letter in t:
        if letter not in exists or exists[letter] == 0:
            return letter
        else:
            exists[letter] -= 1
    
    # If not, return ''
    return ''
            
s = 'rfedd'
t = 'rfeddf'

print(difference(s, t))