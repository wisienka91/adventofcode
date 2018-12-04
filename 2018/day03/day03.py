# -*- coding: utf-8 -*-


def get_fabric_data(data):
    fabric_data = []
    for line in data:
        line_parsed = line.rstrip().split(' ')
        id = line_parsed[0]
        top_left_corner = [int(i) for i in line_parsed[2].strip(':').split(',')]
        dimensions = [int(i) for i in line_parsed[3].split('x')]
        fabric_data.append((id, top_left_corner, dimensions))
    return fabric_data


def get_fabric_dimensions(fabric_data):
    x = 0
    y = 0
    for id_info in fabric_data:
        _x = id_info[1][0] + id_info[2][0]
        _y = id_info[1][1] + id_info[2][1]

        if _x > x:
            x = _x

        if _y > y:
            y = _y

    return (x, y)


def apply_claim(id_info, fabric):
    for i in range(id_info[1][0], id_info[1][0] + id_info[2][0]):
        for j in range(id_info[1][1], id_info[1][1] + id_info[2][1]):
            inch = "{}_{}".format(i, j)
            claims = fabric.get(inch, 0)
            if claims == 0:
                fabric[inch] = 1
            else:
                fabric[inch] += 1
    return fabric


def apply_fabric_claims(fabric_data, fabric_dimensions):
    fabric = {}
    for id_info in fabric_data:
        apply_claim(id_info, fabric)
    return fabric


def count_multiple_claims(data):
    counter = 0
    for claims in list(fabric.values()):
        if claims > 1:
            counter += 1
    return counter


def has_id_one_claim(id_info, fabric):
    one_claim = False
    highest_claim = 1
    for i in range(id_info[1][0], id_info[1][0] + id_info[2][0]):
        for j in range(id_info[1][1], id_info[1][1] + id_info[2][1]):
            inch = "{}_{}".format(i, j)
            if fabric.get(inch) > highest_claim:
                highest_claim = fabric.get(inch)
    if highest_claim == 1:
        one_claim = True
    return one_claim

def get_no_multiple_claim(fabric_data, fabric):
    no_multiple_claims_id = None
    for id_info in fabric_data:
        if has_id_one_claim(id_info, fabric):
            no_multiple_claims_id = id_info[0].strip('#')
    return no_multiple_claims_id


if __name__ == '__main__':
    input_file = open('day03.txt', 'r')
    data = input_file.readlines()
    fabric_data = get_fabric_data(data)
    fabric_dimensions = get_fabric_dimensions(fabric_data)
    fabric = apply_fabric_claims(fabric_data, fabric_dimensions)
    multiple_claims = count_multiple_claims(data)
    no_multiple_claims_id = get_no_multiple_claim(fabric_data, fabric)
    print("Overclaimed square fabric inches: {}".format(multiple_claims))
    print("Non-overlaping claim id: {}".format(no_multiple_claims_id))

