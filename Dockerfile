FROM python:3.8-slim-buster

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN pip3 install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
RUN python -c "import torch; torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_stt', language='en', device='cpu')"

COPY . /code/
RUN python -m compileall -b . && find -name '*.py' -exec rm {} \;

EXPOSE 9000
CMD ["python", "-m", "server"]