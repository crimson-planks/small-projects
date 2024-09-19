from typing import NamedTuple
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
    y: float