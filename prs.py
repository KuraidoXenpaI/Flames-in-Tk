def parse(name1, name2):
    flms = ['Friends', 'Lovers', 'Admirers', 'Married', 'Enemies', 'Secret Lovers']
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    output = 0

    for char in name1.lower():
        output += alphabet.index(char)
    for char in name2.lower():
        output += alphabet.index(char)
    
    output = (output%6)-1
    return flms[output]
    