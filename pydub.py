import urllib.request
from pydub import AudioSegment
from pydub.playback import play
# Download an audio file
urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
# Load into PyDub
loop = AudioSegment.from_wav("metallic-drums.wav")
# Play the result
play(loop)

# Download another loop
urllib.request.urlretrieve("https://tinyurl.com/yx3k5kw5", "beat.wav")
# Load into PyDub
beat = AudioSegment.from_wav("beat.wav")
# Mix with our original loop
mixed = beat[:length].overlay(loop2)