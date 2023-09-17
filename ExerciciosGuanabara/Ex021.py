from pydub import AudioSegment

path = r"C:\Users\Paulo\Downloads\SONG"

song = AudioSegment.from_mp3(path)
play(song)