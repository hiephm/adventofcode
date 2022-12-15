# -*- coding: utf-8 -*-
import utils
import re

input = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''

input = utils.get_input(15)

input = utils.get_multiline_str(input)


class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx = int(sx)
        self.sy = int(sy)
        self.bx = int(bx)
        self.by = int(by)
        self.radius = abs(self.sx - self.bx) + abs(self.sy - self.by)

    def __str__(self):
        return 'S:{},{}  B:{},{}  D:{}'.format(self.sx, self.sy, self.bx, self.by, self.radius)


def is_overlap(seg1, seg2):
    if seg1[1] < seg2[0] or seg2[1] < seg1[0]:
        return False
    return min(seg1[0], seg2[0]), max(seg1[1], seg2[1])


sensors = []
for line in input:
    sx, sy, bx, by = re.findall('\d+', line)
    sensors.append(Sensor(sx, sy, bx, by))


def first(target_row):
    segments = []
    for sensor in sensors:
        distance_to_target_row = abs(sensor.sy - target_row)
        cross_over = sensor.radius - distance_to_target_row
        if cross_over >= 0:
            # print(b, "Cross over:", cross_over, "Overlap range:", b.sx - cross_over, b.sx + cross_over)
            current_seg = (sensor.sx - cross_over, sensor.sx + cross_over)
            for i in range(0, len(segments)):
                if segments[i]:
                    new_seg = is_overlap(segments[i], current_seg)
                    if new_seg:
                        current_seg = new_seg
                        segments[i] = None
            segments.append(current_seg)
    total = 0
    segment_count = 0
    for seg in segments:
        if seg:
            total += seg[1] - seg[0]
            segment_count += 1
    return total, segment_count, segments


def second():
    for row in range(0, 4000000):
        total, seg_count, segments = first(row)
        if seg_count >= 2:
            print(row, seg_count, segments)
            break
    # 2634249 2 [None, None, None, (3120102, 4426606), None, None, None, None, None, (-378999, 3120100)]
    return ''


if __name__ == '__main__':
    # print('First: {}'.format(first(10)))
    print('First: {}'.format(first(2000000)))
    # print('Second: {}'.format(second()))
