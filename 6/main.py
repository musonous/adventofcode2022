import sys


def find_message_marker(packet: str):
    i = 0
    marker = []
    for c in packet:
        i += 1
        marker.append(c)
        if len(marker) > 14:
            marker = marker[1:]
            marker_set = set(marker)
            if len(marker) == len(marker_set):
                return i
    return i


def find_packet_marker(packet: str):
    i = 0
    marker = []
    for c in packet:
        i += 1
        marker.append(c)
        if len(marker) > 4:
            marker = marker[1:]
            if not (marker[0] == marker[1] or
                    marker[0] == marker[2] or
                    marker[0] == marker[3] or
                    marker[1] == marker[2] or
                    marker[1] == marker[3] or
                    marker[2] == marker[3]):
                return i
    return i


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.txt'

with open(filename) as f:
    line = f.readline()
    packet = line.strip()

    r = find_packet_marker(packet)
    print(r)

    r = find_message_marker(packet)
    print(r)
