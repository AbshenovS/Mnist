import pandas as pd
import numpy as np
import cv2

import torch
from torch.utils.data import Dataset

class Dataset(Dataset):

	def __init__(self):
		self.csv = pd.read_csv('./mnist_train.csv')

	def __len__(self):
		return len(self.csv)

	def __getitem__(self, ind):
		X = self.csv.iloc[ind][1:].values
		Y = self.csv.iloc[ind][0]

		X = torch.from_numpy(X).float()

		return X, Y

