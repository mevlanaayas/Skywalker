# -*- coding: utf-8 -*-
import json
import base64
import gzip
import io
from copy import deepcopy


def gzip_op(compressed_data):
    decompressed_data = ''
    checker = True
    str_compressed_data = base64.standard_b64decode(compressed_data)
    byte_compressed_data = io.BytesIO(str_compressed_data)
    with gzip.GzipFile(fileobj=byte_compressed_data) as gz:
        while checker:
            try:
                decompressed_data = gz.read()
                if decompressed_data is not None:
                    checker = False
            except OSError:
                print("gzip cart curt error")
    return decompressed_data


def map_data_op(data):
    positions = []
    for key, value in data.items():
        # data['key]['0:-1:-1']['blocks'][0]['position']
        for key1, value1 in value.items():
            for key2, value2 in value1.items():
                for temp in value2:
                    try:
                        temp_array = deepcopy(temp['position'])
                        positions.append(temp_array)
                    except TypeError:
                        print("chunk position found")
    return positions


def is_in_range(range_list, position):
    for point in range_list:
        x = point["x"]
        z = point["z"]

        pos_x = position["x"] * 0.1
        pos_z = position["z"] * 0.1

        is_x = x + 0.1 >= pos_x >= x - 0.1
        is_z = z + 0.1 >= pos_z >= z - 0.1

        if is_x and is_z:
            return True
    return False


def get_z_axis(map, movements):
    movement_pos_list = []
    for movement in movements:
        movement_pos_list.append(movement["position"])
    chunks = map["chunkCache"]
    avg = 0
    total_reliability = 0
    for chunk in chunks.values():
        chunk_pos = chunk["position"]
        chunk_blocks = chunk["blocks"]
        for block in chunk_blocks:
            if is_in_range(movement_pos_list, block["position"]):
                block_pos_y = block["position"]["y"]
                block_reliability = block["reliability"]
                avg += (chunk_pos["y"] * 16 + block_pos_y) * 0.1 * block_reliability
                total_reliability += block_reliability
    avg = avg / total_reliability
    return avg


def simplify(map, avg_z):
    chunk_del_list = []
    chunks = map["chunkCache"]
    for chunk_key, chunk in chunks.items():
        chunk_pos = chunk["position"]
        chunk_blocks = chunk["blocks"]
        new_block_list = []
        chunk_block_dict = dict()
        for block in chunk_blocks:
            block_pos_y = block["position"]["y"]
            block_world_y = (chunk_pos["y"] * 16 + block_pos_y) * 0.1
            if (
                    block_world_y > avg_z + 0.2 or
                    block_world_y < avg_z - 0.2
            ):
                block["reliability"] = 0
            else:
                block["position"]["y"] = -(int)(avg_z / 0.1)
                key = str(block["position"]["x"])+":"+str(block["position"]["y"])+":"+str(block["position"]["z"])
                if key in chunk_block_dict:
                    chunk_block_dict[key]["reliability"] += block["reliability"]
                else:
                    chunk_block_dict[key] = block
        for k in chunk_block_dict:
            new_block_list.append(chunk_block_dict[k])
        chunk["blocks"] = new_block_list
        if len(new_block_list) == 0:
            chunk_del_list.append(chunk_key)
    for c in chunk_del_list:
        del chunks[c]
    return map


def clear_non_walkable(map, avg_floor_z, avg_movement_z):
    chunks = map["chunkCache"]
    for chunk in chunks.values():
        chunk_pos = chunk["position"]
        chunk_blocks = chunk["blocks"]
        clear_list = []
        for block in chunk_blocks:
            block_pos_y = block["position"]["y"]
            block_world_y = (chunk_pos["y"] * 16 + block_pos_y) * 0.1
            key = str(block["position"]["x"]) + ":" + str(block["position"]["z"])
            if (
                    avg_floor_z + 0.2 < block_world_y < avg_movement_z and
                    key not in clear_list
            ):
                clear_list.append(key)
        for block in chunk_blocks:
            key = str(block["position"]["x"]) + ":" + str(block["position"]["z"])
            if key in clear_list:
                block["reliability"] = 0
    return map


def apply_movement(map, movements, avg_z):
    movement_pos_list = []
    for movement in movements:
        movement_pos_list.append(movement["position"])

    footprint = [[0, 0.05, 0.1, 0.05, 0],
                 [0.05, 0.1, 0.4, 0.1, 0.05],
                 [0.1, 0.4, 1, 0.4, 0.1],
                 [0.05, 0.1, 0.4, 0.1, 0.05],
                 [0, 0.05, 0.1, 0.05, 0]]
    for move in movement_pos_list:
        for i in range(-2, 3):
            for j in range(-2, 3):
                chunk_x, chunk_y, chunk_z = get_chunk(move["x"] + i*0.1, avg_z, move["z"] + j*0.1)
                chunk_key = '{x}:{y}:{z}'.format(x=chunk_x, y=chunk_y, z=chunk_z)
                block_x, block_y, block_z = get_block(move["x"] + i*0.1, avg_z, move["z"] + j*0.1)
                if chunk_key in map["chunkCache"]:
                    is_found = False
                    for block in map["chunkCache"][chunk_key]["blocks"]:
                        if (
                                block["position"]["x"] == block_x and
                                block["position"]["y"] == block_y and
                                block["position"]["z"] == block_z
                        ):
                            block["reliability"] += footprint[i+2][j+2]
                            is_found = True
                            break
                    if not is_found:
                        new_block = dict()
                        new_block["position"] = dict()
                        new_block["position"]["x"] = block_x
                        new_block["position"]["y"] = block_y
                        new_block["position"]["z"] = block_z
                        new_block["reliability"] = footprint[i+2][j+2]
                        map["chunkCache"][chunk_key]["blocks"].append(new_block)
    return map


def get_avg_movement_z(movements):
    avg = 0
    for movement in movements:
        avg += movement["position"]["y"]
    return avg / len(movements)


def get_chunk(px, py, pz):
    x = int(px / 0.1)
    y = int(py / 0.1)
    z = int(pz / 0.1)
    chunk_x = int(x / 16)
    chunk_y = int(y / 16)
    chunk_z = int(z / 16)
    return chunk_x, chunk_y, chunk_z


def get_block(px, py, pz):
    cx, cy, cz = get_chunk(px, py, pz)
    x = int(px / 0.1) - cx * 16
    y = int(py / 0.1) - cy * 16
    z = int(pz / 0.1) - cz * 16
    return x, y, z


def process(map_json, movements_json):
    movements = json.loads(movements_json)
    map = json.loads(map_json)
    avg_z = get_z_axis(map, movements)
    avg_move_z = get_avg_movement_z(movements)
    new_map = map
    new_map = apply_movement(new_map, movements, avg_z)
    new_map = clear_non_walkable(new_map, avg_z, avg_move_z)
    new_map = simplify(new_map, avg_z)
    new_map_json = json.dumps(new_map)
    file = open("new_map.json", "w")
    file.write(new_map_json)
    file.close()
    return new_map_json
