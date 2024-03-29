favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'chris': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# Os dois loops abaixo tem o mesmo comportamento sendo de escolha do desnvolvedor
# deixar o método keys() explícito ou não
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you love {language}")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take your pool")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the pool")

print("The folowing languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())

