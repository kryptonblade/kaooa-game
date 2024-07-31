"""
    turtle from python turtle library
"""
import turtle
import time

t = turtle.Turtle()
X = []
color_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
crow_neighbours = [[4, 5], [7, 8], [3, 4, 8, 9], [2, 4], [0, 2, 3, 5],
                   [0, 4, 6, 7], [5, 7], [1, 5, 6, 8], [1, 2, 7, 9],[2, 8]]
possible_captures = [[[4, 2], [5, 7]],
                     [[8, 2], [7, 5]],
                     [[8, 1], [4, 0]],
                     [[2, 8], [4, 5]],
                     [[2, 9], [5, 6]],
                     [[7, 1], [4, 3]],
                     [[5, 4], [7, 8]],
                     [[5, 0], [8, 9]],
                     [[2, 3], [7, 6]],
                     [[8, 7], [2, 4]]]
possible_traps = [[2, 4, 5, 7], [2, 5, 7, 8], [0, 1, 3, 4, 8, 9], [2, 4, 5, 8],
                  [0, 2, 3, 5, 6, 9], [0, 1, 3, 4, 6, 7], [4, 5, 7, 8],
                  [0, 1, 5, 6, 8, 9], [1, 2, 3, 6, 7, 9], [2, 4, 7, 8]]
CLICKCOUNT = 1
CROWSCOUNT = 7
MOVINGCROWFLAG = -1
VULTUREPOSITION = -1


def move_cursor_func(u, v):
    """
    places the cursor in the u,v position.
    :param u: x_coordinate.
    :param v: y_coordinate.
    :return: None
    """
    t.penup()
    t.goto(u, v)
    t.pendown()


def check_vulture():
    """
    Checks the possibility that vulture is captured
    :return:None
    """
    trapss = possible_traps[VULTUREPOSITION]
    for j in trapss:
        if (color_array[j] != 1 and color_array[j] != 2):
            return
    t.color("black")
    t.write("Crows Win", True, align="center",
            font=("arial", 60, "bold"))
    time.sleep(2)
    # pylint: disable=no-member
    turtle.bye()


def placing_crow(xx, yy):
    """
    places the crow if cursor points a valid space.
    :param xx: x_coordinate of onscreenclick.
    :param yy: y_coordinate of onscreenclick.
    :return: None.
    """
    global CLICKCOUNT
    index = 0
    for (a, b) in X:
        if (abs(a - xx) < 40) and (abs(b - yy) < 40):
            move_cursor_func(a, b)
            if color_array[index] == 0:
                t.color("red")
                t.dot(50)
                color_array[index] = 1
                CLICKCOUNT = CLICKCOUNT + 1
                check_vulture()
            break
        index = index + 1


def check_neighbours(index, prev_index):
    """
    Checks if the new position the crow wants to move to is its neighbour.
    :param index: current place where we want to move the crow.
    :param prev_index: its initial position.
    :return: 0 if the space is occupied else 1.
    """
    for space in crow_neighbours[prev_index]:
        if space == index:
            return 1
    return 0


def check_capture(final_index):
    """

    :param final_index: position of the vulture
    :return:
    """
    for item in possible_captures[VULTUREPOSITION]:
        if item[1] == final_index:
            if color_array[item[0]] == 1:
                return item[0]
    return -1


def moving_crow(u, v):
    """

    :param u: x_coordinate of onscreenclick.
    :param v: y_coordinate of onscreenclick.
    :return: None
    """
    global MOVINGCROWFLAG
    global CLICKCOUNT
    index = 0
    for (a, b) in X:
        if (abs(a - u) < 40) and (abs(b - v) < 40):
            move_cursor_func(a, b)
            if color_array[index] == 1:
                MOVINGCROWFLAG = index
            elif (color_array[index] == 0) and (MOVINGCROWFLAG != -1):
                valid = check_neighbours(index, MOVINGCROWFLAG)
                if valid == 1:
                    t.color("red")
                    t.dot(50)
                    color_array[index] = 1
                    color_array[MOVINGCROWFLAG] = 0
                    t.penup()
                    t.goto(X[MOVINGCROWFLAG])
                    t.pendown()
                    t.color("white")
                    t.dot(50)
                    MOVINGCROWFLAG = -1
                    CLICKCOUNT = CLICKCOUNT + 1
                    check_vulture()
            break
        index = index + 1


def crow_turn(u, v):
    """
    checks if all crows are to be placed or moved.
    :param u: x_coordinate of onscreenclick.
    :param v: y_coordinate of onscreenclick.
    :return: None.
    """
    if CLICKCOUNT < 14:
        placing_crow(u, v)
    else:
        moving_crow(u, v)


def placing_vulture(u, v):
    """
    The function deals with placing the vulture.
    :param u: x_coordinate of onscreenclick.
    :param v: y_coordinate of onscreenclick.
    :return: None
    """
    global VULTUREPOSITION
    global CLICKCOUNT
    index = 0
    for (a, b) in X:
        if (abs(a - u) < 40) and (abs(b - v) < 40):
            move_cursor_func(a, b)
            if color_array[index] == 0:
                t.color("black")
                t.dot(50)
                color_array[index] = 2
                VULTUREPOSITION = index
                CLICKCOUNT = CLICKCOUNT + 1
            break
        index = index + 1


def check_vulture_win():
    """
    Checks if the vulture won.
    :return: None
    """
    if CROWSCOUNT < 4:
        t.color("black")
        t.write("Vulture Wins", True, align="center",
                font=("arial", 60, "bold"))
        time.sleep(2)
        # pylint: disable=no-member
        turtle.bye()


def moving_vulture(u, v):
    """
    this function deals with moving the vulture to a valid space.
    :param u: x_coordinate of onscreenclick.
    :param v: y_coordinate of onscreenclick.
    :return: None.
    """
    global CLICKCOUNT
    global VULTUREPOSITION
    global CROWSCOUNT
    index = 0
    for (a, b) in X:
        if (abs(a - u) < 40) and (abs(b - v) < 40):
            move_cursor_func(a, b)
            if color_array[index] == 0:
                valid_move = check_neighbours(index, VULTUREPOSITION)
                if valid_move == 1:
                    t.color("black")
                    t.dot(50)
                    color_array[index] = 2
                    t.penup()
                    t.goto(X[VULTUREPOSITION])
                    t.pendown()
                    t.color("white")
                    t.dot(50)
                    color_array[VULTUREPOSITION] = 0
                    VULTUREPOSITION = index
                    CLICKCOUNT = CLICKCOUNT + 1
                else:
                    valid_capture = check_capture(index)
                    if valid_capture != -1:
                        t.color("black")
                        t.dot(50)
                        t.penup()
                        t.goto(X[VULTUREPOSITION])
                        t.pendown()
                        t.color("white")
                        t.dot(50)
                        color_array[VULTUREPOSITION] = 0
                        t.penup()
                        t.goto(X[valid_capture])
                        t.pendown()
                        t.color("white")
                        t.dot(50)
                        color_array[index] = 2
                        color_array[valid_capture] = 0
                        CROWSCOUNT = CROWSCOUNT - 1
                        VULTUREPOSITION = index
                        CLICKCOUNT = CLICKCOUNT + 1
                        check_vulture_win()

            break
        index = index + 1


def vulture_turn(u, v):
    """
    checks if the vulture needs to be placed or moved
    :param u: x_coordinate of onscreenclick.
    :param v: y_coordinate of onscreenclick.
    :return: None.
    """
    if CLICKCOUNT < 3:
        placing_vulture(u, v)
    else:
        moving_vulture(u, v)


def kaooa_game(u, v):
    """
    checks whose turn it is currently and redirects to their corresponding functions.
    :param u: x_coordinate of onscreenclick.
    :param v: y_coordinate of onscreenclick.
    :return: None
    """
    if CLICKCOUNT % 2 == 1:
        t.color("black")
        crow_turn(u, v)
    else:
        vulture_turn(u, v)


screen = t.getscreen()
turtle.Screen().bgcolor("light green")
turtle.Screen().title("Kaooa Game")
move_cursor_func(350, 350)
t.color("red")
t.dot(50)
t.color("black")
move_cursor_func(385, 335)
t.write("Crow", False, align="left",
        font=("arial", 15, "bold"))
move_cursor_func(350, 310)
t.color("black")
t.dot(50)
move_cursor_func(385, 295)
t.write("Vulture", False, align="left",
        font=("arial", 15, "bold"))
t.pensize(16)
t.pencolor("white")
move_cursor_func(-300, 0)
for i in range(5):
    x = t.position()
    if x not in X:
        X.append(x)
    t.speed(9)
    t.forward(240)
    x = t.position()
    if x not in X:
        X.append(x)
    t.forward(120)
    x = t.position()
    if x not in X:
        X.append(x)
    t.forward(240)
    x = t.position()
    if x not in X:
        X.append(x)
    t.right(144)
X.pop(0)
X.pop(0)
X.pop(0)
X.pop(1)
X.pop(1)
X.pop(2)
# print(X)

for (x, y) in X:
    t.penup()
    t.goto(x, y)
    t.pendown()
    # t.fill()
    t.dot(50)
# pylint: disable=no-member
turtle.onscreenclick(kaooa_game, 1)
# pylint: disable=no-member
turtle.mainloop()
