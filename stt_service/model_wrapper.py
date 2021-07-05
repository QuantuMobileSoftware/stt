import torch
from glob import glob
import asyncio
from concurrent.futures import ThreadPoolExecutor


class ModelWrapper:
    def __init__(self):
        self.device = torch.device('cpu')
        self.model, self.decoder, self.utils = torch.hub.load(
            repo_or_dir='snakers4/silero-models',
            model='silero_stt',
            language='en',
            device=self.device
        )
        self.executor = ThreadPoolExecutor(max_workers=1)

    def predict(self, filename):
        (read_batch, split_into_batches, read_audio, prepare_model_input) = self.utils
        test_files = glob(filename)
        batches = split_into_batches(test_files, batch_size=10)

        input = prepare_model_input(read_batch(batches[0]), device=self.device)
        output = self.model(input)

        data_output = [self.decoder(text.cpu()) for text in output]
        return data_output

    async def predict_async(self, filename):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(self.executor, self.predict, filename)
