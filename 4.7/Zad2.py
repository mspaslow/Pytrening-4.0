tree_height = int(input("Podaj wysokość choinki: "))
stars = 1
for row in range(1, tree_height + 1):
    print(tree_height * " ", stars * "*")
    stars += 2
    tree_height -= 1
