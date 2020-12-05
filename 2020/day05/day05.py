# -*- coding: utf-8 -*-


def get_seat_data():
    seat_data = []
    data_file = open('day05.txt', 'r')

    for line in data_file.readlines():
        seat_data.append(line.strip())

    data_file.close()
    return seat_data


def _get_mid(data, down, up):
    for i in data:
        if i in ['F', 'L']:
            up = (down + up) // 2
        elif i in ['B', 'R']:
            down = (down + up) // 2 + 1
    if up == down:
        return down


def get_seat_coord(seat):
    row_data = seat[:7]
    col_data = seat[7:]
    seat_row = _get_mid(row_data, 0, 127)
    seat_col = _get_mid(col_data, 0, 7)
    return (seat_row, seat_col)


def get_seats():
    highest_seat_id = 0
    seat_data = get_seat_data()
    seats = []

    for seat in seat_data:
        seat_row, seat_col = get_seat_coord(seat)
        seat_id = seat_row * 8 + seat_col
        seats.append(seat_id)
    return seats


def my_seat(seats):
    my_seat = [i for i in range(min(seats), max(seats)) if i not in seats][0]
    return my_seat


if __name__ == '__main__':
    seats = get_seats()
    print('The highest seat ID is {}...'.format(max(seats)))
    print('My seat ID is {}...'.format(my_seat(seats)))

