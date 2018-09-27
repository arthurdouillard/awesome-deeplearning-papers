#!/usr/bin/env python3
import glob
import os
import operator


FOLDER = 'categories'

def get_stats(path, stats):
    with open(path) as f:
        lines = f.readlines()

    title = lines[0][2:].strip()
    stats[title] = [0, 0, 0]
    for line in lines:
        if '[X]' in line:
            stats[title][0] += 1
            stats[title][1] += 1
        elif '[ ]' in line:
            stats[title][1] += 1

        if ':star:' in line:
            stats[title][2] += 1


def get_global_stats(stats):
    read, total, star = 0, 0, 0
    for cat_read, cat_total, cat_star in stats.values():
        read += cat_read
        total += cat_total
        star += cat_star
    return read, total, star


if __name__ == '__main__':
    stats = {}
    for path in glob.iglob(os.path.join(FOLDER, '*.md')):
        get_stats(path, stats)

    global_stats = get_global_stats(stats)

    print('------ Global Statistics ------')
    print('Total papers: ', global_stats[1])
    print('Total read:   ', global_stats[0])
    print('Percentage:   ', round(100 * global_stats[0] / global_stats[1], 2))
    print(f'Nb of stars: {global_stats[2]} ({round(100 * global_stats[2] / global_stats[0], 2)})%')
    print('-------------------------------')

    stats = [(title, read, total, star) for title, (read, total, star) in stats.items()]
    stats.sort(key=operator.itemgetter(2, 1, 3), reverse=True)

    for title, read, total, _ in stats:
        print('--- {}/{}'.format(read, total).ljust(10, ' '), title)