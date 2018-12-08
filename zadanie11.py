x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if x < 10 and y < 10:
    print("Gracz znajduje się w lewym dolnym rogu")
elif x > 10 and x < 90 and y < 10:
    print("Gracz znajduje się w dolnej krawędzi")
elif x > 90 and x < 100 and y < 10:
    print("Gracz znajduje się w prawym dolnym rogu")
elif x > 10 and x < 90 and y > 10 and y < 90:
    print("Gracz znajduje się w centrum")
elif x < 10 and y > 10 and y < 90:
    print("Gracz znajduje się w lewej krawędzi")
elif x < 10 and y > 10 and y < 90:
    print("Gracz znajduje się w lewej krawędzi")