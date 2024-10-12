from pathlib import Path
import video_to_frames, quantize, remove_artifacts, write_texture_to_map, write_pixelart_to_map
file_path = Path(input("\nfile path:"))
#video_to_frames.main()
#quantize.main()
remove_artifacts.main(file_path)
write_texture_to_map.main(file_path)
write_pixelart_to_map.main(file_path)
print("Done!")