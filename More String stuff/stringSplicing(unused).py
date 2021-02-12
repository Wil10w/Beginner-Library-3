def create_username(name):
    username = ''
    space = name.find(' ')
    first_name = name[0:space]
    last_name = name[1 + space:]
    if len(first_name) <= 3:
        username += first_name
    else:
        username += first_name[0]
        username += first_name[(len(first_name) -1)// 2]
        username += first_name[len(first_name) - 1]

    username += last_name
    return username