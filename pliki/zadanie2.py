from collections import defaultdict

def prepare_line(napis):
    # napis = "login-1'LOGIN;456\n"
    login, akcja, czas = napis.split(";")
    czas = int(czas)
    return login, akcja, czas

def my_key(item):
    return int(item[0].split("-")[-1])

last_login_time = {}
user_total_time = defaultdict(int)

try:
    with open("logs.txt") as f:
        for line in f:
            login, action, time = prepare_line(line)
            if action == "LOGIN":
                last_login_time[login] = time
            elif action == "LOGOUT":
                session_time = time - last_login_time[login]
                user_total_time[login] += session_time
    print("Czas przebywania w systemie: ")
    for login, time in sorted(user_total_time.items(), key=my_key):
        print(f"{login}: {time} s")
except FileNotFoundError:
    print("Nie ma takiego pliku")


