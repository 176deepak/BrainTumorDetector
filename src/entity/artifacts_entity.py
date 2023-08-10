from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    zip_data_path:str
    extracted_data_path:str


@dataclass
class DataValidationArtifact:
    validation_status:bool


@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str
    