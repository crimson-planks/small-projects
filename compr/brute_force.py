import sys
data_list = [b'\x00',b'\x08',b'\x08']
def get_loss(v1: int, v2: int):
    return (v1 ^ v2).bit_count()
print(sys.version_info)
print((2).bit_length)
for q0 in range(0,0x10):
    s = 0
    for data in data_list:
        s += get_loss(int.from_bytes(data,'big'),q0)
    print(s)