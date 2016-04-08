import sys
from . import graph


def find_plates(input_string):
    start, end = graph.START, graph.END
    next_vertex = None
    plate_start = 0
    plates = []
    for i, c in enumerate(input_string + ' '):
        if not next_vertex:
            next_vertex = graph.get_next_vertex(start, c)
            plate_start = i if next_vertex else 0
        elif next_vertex.pk == end.pk:
            plates.append((plate_start, i-1))
            next_vertex = graph.get_next_vertex(next_vertex, c)
        else:
            next_vertex = graph.get_next_vertex(next_vertex, c)

    return plates


def get_result(input_string, plates):
    for plate in plates:
        input_string = input_string.replace(input_string[plate[0]:plate[1]+1], '<PLATE>')
    return input_string


if __name__ == '__main__':
    input_string = sys.argv[1]
    print(get_result(input_string, find_plates(input_string)))