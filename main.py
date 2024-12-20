from src.CNN_Classifier import logger
from CNN_Classifier.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_Classifier.pipeline.Stage_02_prepare_model import PrepareBaseModelTrainingPipeline
from CNN_Classifier.pipeline.Stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<< \n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Prepare Base Model"
try:
    logger.info(f"*********")
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n \n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Train Model"
try:
    logger.info(f"*********")
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n \n")
except Exception as e:
    logger.exception(e)
    raise e

