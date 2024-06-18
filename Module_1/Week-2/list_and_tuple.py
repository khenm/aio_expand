def list_and_tuple():
    my_tuple1 = (2, 3)
    my_tuple2 = (3, 6)
    sum_tuple = (my_tuple1[0] + my_tuple2[0], my_tuple1[1] + my_tuple2[1])
    time_tuple = (my_tuple1[0] * my_tuple2[0], my_tuple1[1] * my_tuple2[1])
    print(sum_tuple)
    print(time_tuple)
    distance = ((my_tuple1[0] - my_tuple2[0])**2 +
                (my_tuple1[1] - my_tuple2[1])**2)**(1/2)
    print(distance)
    print((my_tuple1.index(3), my_tuple2.index(3)))


if __name__ == '__main__':
    list_and_tuple()
