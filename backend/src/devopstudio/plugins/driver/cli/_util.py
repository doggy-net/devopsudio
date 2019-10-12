import re
from array import array


def to_bytes(obj):
    if isinstance(obj, bytes):
        return obj

    if isinstance(obj, str):
        return obj.encode()

    if isinstance(obj, re.Pattern):
        if isinstance(obj.pattern, str):
            return re.compile(obj.encode(), obj.flags)
        return obj

    return str(obj).encode()


# Handle control character
def handle_ctrlchr(self, ori_text):
    ori_arr = array('b')
    ori_arr.frombytes(ori_text)
    new_arr = array('b')
    for chr in ori_arr:
        if chr == 8:  # [BS] (backspace)
            if new_arr:
                new_arr.pop()
        else:
            new_arr.append(chr)
    return new_arr.tobytes().decode()
