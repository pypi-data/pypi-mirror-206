import os
import sys
from pathlib import Path

from loguru import logger as logger1

from souJpg.comm.cfg.utils import initGcf

gcfFilePath = os.getenv("gcfFilePath", None)
if gcfFilePath is None:
    logger1.error("gcfFilePath is not set")
    raise Exception("gcfFilePath is not set")


gcf = initGcf(baseConf=gcfFilePath)
