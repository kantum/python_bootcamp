languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

s = ""

for l, c in languages.items():
    s = l + " was created by " + c
    print(s)
