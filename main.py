from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_injestion import DataIngestionTrainingPipeline





STAGE_NAME="Data Injestion stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
