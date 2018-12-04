from collections import defaultdict
from time import strptime
import re


def both():
    d = defaultdict(lambda: [0]*60)
    with open('input') as f:
        curr_time = None
        curr_gid = None
        result_1 = 0
        result_2 = 0

        data = f.read().splitlines()
        data.sort(key=lambda x: strptime(x.strip().split(']')[0], r'[%Y-%m-%d %H:%M'))

        mx = 0
        for line in data:
            t, event = line.strip().split(']')
            t = strptime(t, r'[%Y-%m-%d %H:%M')

            if 'begins' in event:
                gid = int(re.search(r'#(\d+)', event).group()[1:])
                curr_gid = gid
            else:
                gid = curr_gid

            if 'falls' in event:
                curr_time = t
            elif 'wakes' in event:
                if curr_time.tm_yday != t.tm_yday:
                    curr_time = t.replace(tm_min=0)

                for i in range(curr_time.tm_min, t.tm_min):
                    d[gid][i] += 1
                    if d[gid][i] > mx:
                        mx = d[gid][i]
                        result_2 = i * gid

        mx = 0
        for k, v in d.items():
            s = sum(v)
            if s > mx:
                mx = s

                result_1 = k * v.index(max(v))

        return result_1, result_2


def main():
    print('Both:', *both())


if __name__ == '__main__':
    main()
