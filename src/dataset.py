import os
import torch
from torch.utils.data import Dataset
from PIL import Image

class CaptionDataset(Dataset):
    def __init__(self, captions_df, images_path, word2idx, max_length, transform=None):
        self.captions_df = captions_df
        self.images_path = images_path
        self.word2idx = word2idx
        self.max_length = max_length
        self.transform = transform

    def __len__(self):
        return len(self.captions_df)

    def __getitem__(self, idx):
        row = self.captions_df.iloc[idx]

        image_path = os.path.join(self.images_path, row["image"])
        image = Image.open(image_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        caption = row["caption"].split()

        caption_idx = [
            self.word2idx.get(word, self.word2idx["<pad>"])
            for word in caption
        ]

        if len(caption_idx) < self.max_length:
            caption_idx += [0] * (self.max_length - len(caption_idx))
        else:
            caption_idx = caption_idx[:self.max_length]

        return image, torch.tensor(caption_idx)