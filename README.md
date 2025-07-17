# Self-Training for Boundary-Aware Tumor Segmentation via Signed Distance Map

## Description
<img src="./imgs/overall_pipeline.jpg" alt="Overall pipeline"></img><br/>
We propose a self-training-based pseudo labeling to address the scarcity of annotated histopathology data. Further, the proposed architecture incorporates the concept of the Signed Distance Map (SDM) to facilitate robust boundary learning in complex pathological structures. 

Examples are shown below. The proposed method accurately captures complex boundaries, especially in ther lower-right area of each samples.
<img src="./imgs/segmentation result-breast7.jpg" alt="visualization"></img><br/>
## Environment Setup

    conda env create -f pseudo-u.yaml
    conda activate pseudo-u


## Data setup
The BCSS dataset used in this paper is from [Kaggle-Breast Cancer Semantic Segmentation (BCSS)](https://www.kaggle.com/datasets/whats2000/breast-cancer-semantic-segmentation-bcss?resource=download-directory&select=gtruth_codes_512.tsv).
The patch image size of 256*256 is cropped from BCSS_512, and we selectively used a subset of annotation labels(tumor, stroma, dcis). The remaining labels were treated as background.
Preprocessing code is available in BCSS_preprocess.ipynb.

## Usage
Follow the semi_sdm_unet.py
