import os

ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant 
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://github.com/raghavpatel2507/Datasets/raw/main/Sign%20Language%20Detection.v1i.yolov5pytorch.zip"


"""
Data Validation realted contant 
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]


"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 60 #i am run the model 60 epochs you can try more ephochs and more eccuracy.

MODEL_TRAINER_BATCH_SIZE: int = 16