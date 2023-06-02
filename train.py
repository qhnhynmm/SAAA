import argparse

from configs.utils import get_config
from builders.task_builder import build_task
from utils.logging_utils import setup_logger

logger = setup_logger()

parser = argparse.ArgumentParser()
parser.add_argument("--config-file", type=str, required=True)

args = parser.parse_args()

config = get_config(args.config_file)
config.TRAINING.VERBOSE_SCORES = ["CIDEr", "BLEU", "ROUGE"]  # Thay đổi các giá trị tùy theo yêu cầu
task = build_task(config)
task.start()
task.get_predictions()
logger.info("Task done.")