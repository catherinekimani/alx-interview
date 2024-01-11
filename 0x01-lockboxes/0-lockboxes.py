#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    """
    total_boxes = len(boxes)
    visited_keys = [0]
    opened_boxes_count = 0
    current_key_idx = 0

    while current_key_idx < len(visited_keys):
        current_box = visited_keys[current_key_idx]

        for key in boxes[current_box]:
            if 0 < key < total_boxes and key not in visited_keys:
                visited_keys.append(key)
                opened_boxes_count += 1

        current_key_idx += 1

    return opened_boxes_count == total_boxes - 1
