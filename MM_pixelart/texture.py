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
    X: float
    Y: float
    Type: int = 6040
class MM_AnimatedPixelArt(NamedTuple):
    AnimationBase: int
    Behavior: int
    Delay: int
    IsFront: bool
    PixelArtID: str
    Scale: int
    X: float
    Y: float
    Type: int = 6044
class MM_CustomEnemy(NamedTuple):
    PixelArtID : str
    TemplateID : str
    X : float
    Y : float
    Type : int = 3068

def main():
    print(NamedTuple_to_dict(MM_PixelArt("e3",100.,200.)))
if __name__=="__main__":
    main()