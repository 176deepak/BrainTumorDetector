import os
import sys
import zipfile
import shutil
from ultralytics import YOLO
from exception import CustomException
from logger import logging
from src.entity.artifacts_entity import ModelTrainerArtifact
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, model_trainer_config=ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(
        self,
    ) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class.")

        try:
            logging.info("Pretrained model downloading starts!")
            logging.info("Model training starts!")
            os.system(
                f"yolo task=detect mode=train model={self.model_trainer_config.weight_name} data=src\config\data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true"
            )

            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)

            shutil.copy(
                r"E:\Projects\Tumor_detector\runs\detect\train\weights\best.pt",
                r"models\trained_models",
            )
            shutil.copy(
                r"E:\Projects\Tumor_Detector\yolov8n.pt", r"models\pretrained_models"
            )
            os.remove(r"E:\Projects\Tumor_Detector\yolov8n.pt")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="artifacts/model_trainer/best.pt"
            )
            logging.info("Exited initiate_model_trainer method of ModelTrainer class.")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)
