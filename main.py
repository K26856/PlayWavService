from flask import Flask, request, make_response
import pyaudio
from io import BytesIO
import wave

# app initiate
app = Flask(__name__)
pa = pyaudio.PyAudio()
config = {}
config['CHUNK'] = 1024
config['OUTPUT_DEVICE'] = None

# route
@app.route("/", methods=["GET"])
def index() :
    return "Hello world"

@app.route("/play", methods=["POST"])
def play() :
    wavfile = request.files["file"]
    with wave.open(BytesIO(wavfile.read()), 'rb') as w:
        pa_stream = pa.open(
            format=pa.get_format_from_width(w.getsampwidth()),
            channels=w.getnchannels(),
            rate=w.getframerate(),
            output_device_index=config['OUTPUT_DEVICE'],
            output=True
            )
        wav_data = w.readframes(config['CHUNK'])
        while len(wav_data) > 0 :
            pa_stream.write(wav_data)
            wav_data = w.readframes(config['CHUNK'])
        pa_stream.stop_stream()
        pa_stream.close()
    return make_response("", 200)

if __name__=="__main__" :
    app.run(port=8889)