import os

ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant 
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://github.com/raghavpatel2507/Datasets/raw/main/data.zip"


"""
Data Validation realted contant 
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test","valid", "data.yaml"]


"""
MODEL TRAINER related constant 
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 130 #you can go for more epochs

MODEL_TRAINER_BATCH_SIZE: int = 16


