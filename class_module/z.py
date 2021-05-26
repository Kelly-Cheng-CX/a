username_inp = input('请输入你的用户名：')
pwd_inp = input('请输入你的密码：')

with open('user_info.txt', 'r', encoding='utf8') as fr:
    for user_info in fr:
        username, pwd = user_info.split(':')

        if username.strip() == username_inp and pwd.strip() == pwd_inp:
            print('登录成功')
            break
        else:
            continue
    else:
        print('用户名或密码错误')
