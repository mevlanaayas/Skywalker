# -*- coding: utf-8 -*-
from copy import deepcopy


def save_label(data):
    pass


def save_map(data):
    chunk_list = data.get('chunkCache')
    points = []
    chunk_points = []
    for key, chunk in chunk_list.items():
        points = chunk['blocks']
        chunk_points.append(key)
        for point in points:
            a = point
    print(chunk_points)
    pass


def save_movement(data):
    pass
