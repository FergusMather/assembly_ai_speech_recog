#audio file formats
#.mp3 information can be lost in compression
#.flac compresses but allows perfect reconstruction
#.wav does not compress = best audio & largest files

import wave

# Explain
# - wave file structure
# - number of channels
# - sample width
# - framerate/sample_rate
# - number of frames
# - values of a frame

obj = wave.open("01-basics/output.wav","rb")

print("Number of channels",obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("number of frames", obj.getnframes())
print("parameters",obj.getparams())

# time of audio total frames / frame rate
t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames))

obj.close()

obj_new = wave.open("output_new.wave", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000)

obj_new.writeframes(frames)

obj_new.close()