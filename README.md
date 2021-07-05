**(Optional) Build the image**
    `docker build -t quantumobile/stt:1625497419 .`

**Run the application:**
    `docker-compose up -d`

**Test**
    `wget https://opus-codec.org/static/examples/samples/speech_orig.wav`
    `curl --data-binary @speech_orig.wav 'http://localhost:9000/api/predict'`
