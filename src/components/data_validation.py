import os
import sys
import shutil
from distutils.dir_util import copy_tree
from logger import logging
from exception import CustomException
from src.entity.config_entity import DataValidationConfig
from src.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact,
        data_validation_config: DataValidationConfig = DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise CustomException(e, sys)

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifact.extracted_data_path)

            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(
                        self.data_validation_config.data_validation_dir, exist_ok=True
                    )
                    with open(
                        self.data_validation_config.valid_status_file_dir, "w"
                    ) as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(
                        self.data_validation_config.data_validation_dir, exist_ok=True
                    )
                    with open(
                        self.data_validation_config.valid_status_file_dir, "w"
                    ) as f:
                        f.write(f"validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_validation(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_validation method of DataValidation class.")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(validation_status=status)

            logging.info(
                "Exited initiate_data_validation method of DataValidation method of DataValidation class."
            )
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            if status:
                copy_tree(
                    self.data_ingestion_artifact.extracted_data_path,
                    os.getcwd() + "\data",
                )

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e, sys)
