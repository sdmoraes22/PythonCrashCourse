current_users = ['user1', 'User2', 'user3', 'User4', 'user5']
new_users = ['user9', 'user5', 'user2', 'user4', 'user9',]
current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username {new_user} has already been used.") 
    else:
        print(f"Username {new_user} is available.")