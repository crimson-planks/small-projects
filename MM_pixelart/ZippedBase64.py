import base64
import zlib

def pad_bytes_to_readable_str(b: bytes) -> str:
    rslt_list = []
    for a in b:
        rslt_list.append(hex(a)[2:].upper().zfill(2))
    return ' '.join(rslt_list)

def decode(b64data: str | bytes) -> bytes:
    b64_decoded = base64.b64decode(b64data)
    zlib_decompressed = zlib.decompress(b64_decoded)
    return zlib_decompressed

def encode(b: bytes) -> bytes:
    zlib_compressed = zlib.compress(b)
    b64_encoded = base64.b64encode(zlib_compressed)
    return b64_encoded

if __name__=="__main__":
    print(base64.b64decode(r"eJz7/x8/YGBgwIspBYTMp9R+QvoBzQifYQ=="))