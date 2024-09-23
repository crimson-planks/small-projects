from typing import NamedTuple
def NamedTuple_to_dict(nt: NamedTuple) -> dict:
    v = {}
    for i,key in enumerate(nt._fields):
        v[key] = nt[i]
    return v
class MM_Texture(NamedTuple):
    Data: str
    DataType: str
    Height: int
    ID: str
    Width: int
class MM_PixelArt(NamedTuple):
    PixelArtID: str
    Type: 6040
    X: float
    Y: float
class MM_AnimatedPixelArt(NamedTuple):
    Behavior: int
    Delay: int
    PixelArtID: str
    Scale: int
    Type: 6044
    X: float
    Y: float