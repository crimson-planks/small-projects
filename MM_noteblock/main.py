#get midi file and a table of midi instrument to MM instrument
import dataclasses
import enum
#notecontraption: the contraption that plays the same note multiple times
@dataclasses.dataclass(slots = True)
class MM_notecontraption:
    note: int
    instrument: int

with open("music.mid") as input_midi_file:
    pass
playing_CEtemplate = {
    "Behavior" : 0,
    "CanPlayerStandOn" : True,
    "HitBoxHeight" : 16,
    "HitBoxWidth" : 48,
    "ID" : None,
    "PixelArtID" : "0",
    "TransformCondition" : 2,
    "TransformConditionValue" : 18,
    "TransformDelay" : 0,
    "TransformID" : None
},
not_playing_CEtemplate = {
    "Behavior" : 0,
    "CanPlayerStandOn" : True,
    "HitBoxHeight" : 16,
    "HitBoxWidth" : 16,
    "ID" : None,
    "PixelArtID" : "1",
    "TransformCondition" : 2,
    "TransformConditionValue" : 7,
    "TransformDelay" : 0,
    "TransformID" : None
},
end_CEtemplate = {
    "Behavior" : 0,
    "CanHurtPlayer" : False,
    "CanInteractWithEnemies" : False,
    "ID" : "end",
    "PixelArtID" : "b"
}
lengths = [(),(),()]
onenote_rslt = []
onenote_rslt.append(notplaying_CE.copy())