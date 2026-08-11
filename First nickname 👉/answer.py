nickname_user = input()

while True:
    if '_' in nickname_user:
        nickname_user = input()
    else:
        print(nickname_user)
        break
