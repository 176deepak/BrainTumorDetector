import os
import sys
import zipfile
import gdown
from logger import logging
from exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(
        self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()
    ):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)

    def download_extract_data(self) -> str:
        try:
            url = self.data_ingestion_config.data_download_url

            ZIP_FILE_DIR = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(ZIP_FILE_DIR, exist_ok=True)
            ZIP_FILE_NAME = "data.zip"
            ZIP_FILE_PATH = os.path.join(ZIP_FILE_DIR, ZIP_FILE_NAME)

            DATA_PATH = self.data_ingestion_config.extracted_data_path
            os.makedirs(DATA_PATH, exist_ok=True)

            logging.info(
                f"Downloading data from url {url} into the file {ZIP_FILE_PATH}"
            )
            file_id = url.split("/")[-2]
            prefix = "https://drive.google.com/uc?id="

            gdown.download(prefix + file_id, ZIP_FILE_PATH)

            logging.info(f"Extracting data from url {url} into the file {DATA_PATH}")
            with zipfile.ZipFile(ZIP_FILE_PATH, "r") as zip_ref:
                zip_ref.extractall(DATA_PATH)

            return ZIP_FILE_PATH, DATA_PATH

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Data ingestion starts...")
        try:
            ZIP_FILE_PATH, DATA_PATH = self.download_extract_data()
            data_ingestion_artifact = DataIngestionArtifact(
                zip_data_path=ZIP_FILE_PATH, extracted_data_path=DATA_PATH
            )

            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class."
            )
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)
