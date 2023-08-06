"""
tools.py
Helper functions
"""
import logging
import os

import pandas as pd
import torch
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from torch.utils.data import DataLoader


class TabularDataLoader(torch.utils.data.Dataset):
    def __init__(self, path, filename, label, scale="minmax"):

        self.path = path

        if not os.path.isfile(path + filename):
            raise RuntimeError(f"Dataset not found at {path + filename}. You can use download=True to download it")

        self.dataset = pd.read_csv(path + filename)
        self.target = label

        # Save target and predictors
        self.X = self.dataset.drop(self.target, axis=1)

        # Save feature names
        self.feature_names = self.X.columns.to_list()
        self.target_name = label

        # Transform data
        if scale == 'minmax':
            self.scaler = MinMaxScaler()
        elif scale == 'standard':
            self.scaler = StandardScaler()
        else:
            raise NotImplementedError(
                "The current version of DataLoader class only provides the following "
                "transformations: {minmax, standard}")

        self.scaler.fit_transform(self.X)

        self.data = self.scaler.transform(self.X)
        self.targets = self.dataset[self.target]

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):

        # select correct row with idx
        if isinstance(idx, torch.Tensor):
            idx = idx.tolist()

        if 'Synthetic' in self.path:
            return (self.data[idx], self.targets.values[idx], self.weights[idx], self.masks[idx],
                    self.masked_weights[idx], self.probs[idx], self.cluster_idx[idx])
        else:
            return self.data[idx], self.targets.values[idx]


def get_data(dataset: str, batch_size: int, data_path="./datasets"):
    """
    Helper function to get data-loaders for different datasets
    """
    if dataset in ["bankmarketing", "californiahousing", "electricity", "eyemovement", "magictelescope",
                   "phoneme", "telecommarketing"]:
        dataset_train = TabularDataLoader(path=f"{data_path}/{dataset}/",
                                          filename=f"{dataset}-train.csv",
                                          label="class")

        dataset_test = TabularDataLoader(path=f"{data_path}/{dataset}/",
                                         filename=f"{dataset}-test.csv",
                                         label="class")

        loader_train = DataLoader(dataset_train, batch_size=batch_size, shuffle=True)
        loader_test = DataLoader(dataset_test, batch_size=batch_size, shuffle=True)
        num_classes = 2
    elif dataset in ["corrupt-bankmarketing", "corrupt-californiahousing", "corrupt-electricity",
                     "corrupt-eyemovement", "corrupt-magictelescope",
                     "phoneme", "corrupt-telecommarketing"]:
        dataset_train = TabularDataLoader(path=f"{data_path}/{dataset[8:]}/",
                                          filename=f"{dataset[8:]}-train.csv",
                                          label="class")

        dataset_test = TabularDataLoader(path=f"{data_path}/{dataset[8:]}/",
                                         filename=f"{dataset[8:]}-test.csv",
                                         label="class")
        dataset_train.data = torch.tensor(dataset_train.data)
        dataset_test.data = torch.tensor(dataset_test.data)
        dataset_train.data = torch.concat([dataset_train.data,
                                           torch.rand_like(dataset_train.data)], dim=1)
        dataset_test.data = torch.concat([dataset_test.data,
                                          torch.rand_like(dataset_test.data)], dim=1)
        loader_train = DataLoader(dataset_train, batch_size=batch_size, shuffle=True)
        loader_test = DataLoader(dataset_test, batch_size=batch_size, shuffle=True)
        num_classes = 2
    else:
        raise ValueError(f"The dataset name {dataset} is not yet available in this repo.")

    return loader_train, loader_test, num_classes


def save_model(model, explainers, disagreement_lambda, disagreement_mu, dest):
    """
    Helper function to save the torch model to disk
    """
    logging.info(f"Saving checkpoint to {os.path.join(os.getcwd(), dest)}...")
    state_dict = {"model": model.state_dict(),
                  "explainers": explainers,
                  "lambda": disagreement_lambda,
                  "mu": disagreement_mu}
    torch.save(state_dict, dest)
