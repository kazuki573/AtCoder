x_1, y_1, x_2, y_2 = [int(x) for x in input().split()]
delta_x = x_2 - x_1
delta_y = y_2 - y_1
x_3 = x_2 - delta_y
y_3 = y_2 + delta_x
x_4 = x_3 - delta_x
y_4 = y_3 - delta_y
print(str(x_3) + ' ' + str(y_3) + ' ' + str(x_4) + ' ' + str(y_4))
