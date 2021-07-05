**(Optional) Build the image**

    docker build -t quantumobile/stt:1625497419 .

**Run the application:**

    docker-compose up -d

Or

    docker run --rm -p 9000:9000 quantumobile/stt:1625497419

**Test**

    wget https://opus-codec.org/static/examples/samples/speech_orig.wav
    curl --data-binary @speech_orig.wav 'http://localhost:9000/api/stt'
