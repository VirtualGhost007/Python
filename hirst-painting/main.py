# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# all_rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     all_rgb.append(rgb)
import turtle as t

color_list = [(219, 254, 237), (84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (244, 248, 254), (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]
tim = t.Turtle()
t.colormode(255)
t.speed("fastest")
y = -300
for _ in range(16):
    t.setx(-400)
    t.sety(y)
    y += 100
    for i in range(int(len(color_list) / 2)):
        t.dot(25, color_list[i])
        t.penup()
        t.fd(50)
        t.pendown()
















screen = t.Screen()
screen.exitonclick()