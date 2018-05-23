# -*- coding: utf-8 -*-
import base64
import gzip
import io
import json
from math import floor


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
    result = json.loads(decompressed_data)
    return result


def compress_op(data):
    str_2_json = json.dumps(data) + "\n"
    json_2_bytes = str_2_json.encode('utf-8')
    compressed_data = gzip.compress(json_2_bytes)
    compressed_data_2_byte = base64.standard_b64encode(compressed_data)
    result = compressed_data_2_byte.decode("utf-8")
    return result


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
    for chunk_key in chunks:
        chunk_pos = chunks[chunk_key]["position"]
        chunk_blocks = chunks[chunk_key]["blocks"]
        new_block_list = []
        chunk_block_dict = dict()
        for block in chunk_blocks:
            block_pos_y = block["position"]["y"]
            block_world_y = (chunk_pos["y"] * 16 + block_pos_y) * 0.1
            if block_world_y > avg_z + 0.2 or block_world_y < avg_z - 0.2:
                block["reliability"] = 0
            else:
                block["position"]["y"] = -floor(avg_z / 0.1)
                key = str(block["position"]["x"])+":"+str(block["position"]["y"])+":"+str(block["position"]["z"])
                if key in chunk_block_dict:
                    chunk_block_dict[key]["reliability"] += block["reliability"]
                else:
                    chunk_block_dict[key] = block
        for k in chunk_block_dict:
            new_block_list.append(chunk_block_dict[k])
        chunks[chunk_key]["blocks"] = new_block_list
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
                        if(
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
    x = floor(px / 0.1)
    y = floor(py / 0.1)
    z = floor(pz / 0.1)
    chunk_x = floor(x / 16)
    chunk_y = floor(y / 16)
    chunk_z = floor(z / 16)
    return chunk_x, chunk_y, chunk_z


def get_block(px, py, pz):
    cx, cy, cz = get_chunk(px, py, pz)
    x = floor(px / 0.1) - cx * 16
    y = floor(py / 0.1) - cy * 16
    z = floor(pz / 0.1) - cz * 16
    return x, y, z


def process(map_json, movement_json):
    avg_z = get_z_axis(map_json, movement_json)
    avg_move_z = get_avg_movement_z(movement_json)
    new_map = map_json
    new_map = apply_movement(new_map, movement_json, avg_z)
    new_map = clear_non_walkable(new_map, avg_z, avg_move_z)
    new_map = simplify(new_map, avg_z)
    new_map_json = json.dumps(new_map)
    return new_map_json
