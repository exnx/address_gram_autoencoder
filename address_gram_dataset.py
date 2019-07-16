from torchvision import transforms
from PIL import Image
import os
import numpy as np
import torch
from torch.utils.data.dataset import Dataset


class AddressGramDataset(Dataset):
    def __init__(self, dir_path):
        self.dir_path = dir_path

        # dataset path, e.g.
        # './font_imgs/arial'

        # get list of files in that dir and put in list
        self.img_files = []
        
        # loop thru directory and add file names to list
        for filename in os.listdir(dir_path):
            if filename.endswith(".png"):
                self.img_files.append(filename)

    def __getitem__(self, index):

        img_name = self.img_files[index]

        img_path = os.path.join(self.dir_path, img_name)

        img = Image.open(img_path)  #open img path as PIL image

                # define transforms
        transform = transforms.Compose([            #[1]

                  # resizes pil image, square
        
         transforms.ToTensor()
         ])

        # transform = transforms.Compose([
        #   # resizes pil image, square
        #  transforms.ToTensor(),
        #  transforms.Normalize(mean=[0.5, 0.5, 0.5],
        #  std=[0.5, 0.5, 0.5])
        #  ])

        img = transform(img)

        # save to normalize maybe
        
         #  transforms.Normalize(                      #[5]
         # mean=[0.485, 0.456, 0.406],                #[6]
         # std=[0.229, 0.224, 0.225]                  #[7]
         # )]

        # return img as just the tensor, no label for now
        return img, img

    def __len__(self):
        return len(self.img_files)







