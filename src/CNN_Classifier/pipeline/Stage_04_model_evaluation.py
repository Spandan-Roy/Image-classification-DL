from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.mode_evaluation import Evaluation
from CNN_Classifier import logger


STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        eval_config=config.get_evaluation_config()
        evaluation=Evaluation()
        evaluation.save_score()
        #evaluation.log_into_mlflow()
        
if __name__=="__main__":
    try:
        logger.info(f"*********")
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n \n")
    except Exception as e:
        logger.exception(e)
        raise e