import os 
from dataclasses import dataclass
from datetime import datetime
from src.constants.training_constants import *


@dataclass
class TrainingPipelineConfig:
    artifacts_dir:str = ARTIFACTS_DIR

training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR) 

    extracted_data_path:str = os.path.join(data_ingestion_dir, DATA_INGESTION_EXTRACTED_DATA_DIR)

    data_download_url:str = DATA_DOWNLOAD_URL


@dataclass
class DataValidationConfig:
    data_validation_dir:str = os.path.join(training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR)

    valid_status_file_dir:str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)

    required_file_list = DATA_VALIDATION_REQUIRED_FILES

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR)

    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME

    no_epochs = MODEL_TRAINER_NO_EPOCHS