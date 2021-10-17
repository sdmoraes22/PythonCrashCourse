favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'chris': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['chris', 'mike','sarah', 'john']

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"{friend.title()} thank you for responding to the list.")
    else:
        print(f"{friend.title()} didn't responded to the list.")