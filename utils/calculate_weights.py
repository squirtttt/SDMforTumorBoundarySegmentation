import os

import torch
from tqdm import tqdm
import numpy as np

from utils.mypath import Path

#num__classes : 2 -> 3
def calculate_weights_labels(dataloader, num_classes=3):
    # Create an instance from th data loader
    z = np.zeros((num_classes,))

    # Initialize tqdm
    tqdm_batch = tqdm(dataloader)
    print('Calculating classes weights')

    for sample in tqdm_batch:
        y = sample['label']
        y = y.detach().cpu().numpy()
        mask = (y >= 0) & (y < num_classes)
        labels = y[mask].astype(np.uint8)
        count_l = np.bincount(labels, minlength=num_classes)
        z += count_l

    tqdm_batch.close()
    total_frequency = np.sum(z)

    class_weights = []
    for frequency in z:
        class_weight = 1 / (np.log(1.02 + (frequency / total_frequency)))
        class_weights.append(class_weight)

    ret = np.array(class_weights)
    class_weights_path = os.path.join(Path.pathology_root_dir(), 'classes_weights.npy')
    np.save(class_weights_path, ret)
    print("classes_weight : ", np.load('C:\\Users\\LeeYujin\\PycharmProjects\\SegmentationCode\\PathologyDataSet\\classes_weights.npy'))

    return ret

#data = np.load('C:\\Users\\LeeYujin\\PycharmProjects\\SegmentationCode\\PathologyDataSet\\SegNet\\classes_weights.npy')
#for i in data:
#   print("weight : ",i)
#print("classes_weight : ", np.load('C:\\Users\\LeeYujin\\PycharmProjects\\SegmentationCode\\PathologyDataSet\\SegNet\\classes_weights.npy'))
#print("data shape",data.shape)
#weight = torch.from_numpy(data.astype(np.float32))[:2]
#print("!!!!!!!!!!!!!", weight)
