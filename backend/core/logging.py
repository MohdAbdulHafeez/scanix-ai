"""
SCANIX AI
Production Logging System
"""

import logging
import sys
from pathlib import Path

from loguru import logger

from core.settings import settings


LOG_DIR = Path("logs")
LOG_DIR.mkdir(
    exist_ok=True
)

LOG_FILE = (
    LOG_DIR
    / "scanix.log"
)


class InterceptHandler(
    logging.Handler
):

    def emit(
        self,
        record,
    ):

        try:

            level = logger.level(
                record.levelname
            ).name

        except Exception:

            level = (
                record.levelno
            )

        frame = (
            logging.currentframe()
        )

        depth = 2

        while (
            frame
            and frame.f_code.co_filename
            == logging.__file__
        ):

            frame = (
                frame.f_back
            )

            depth += 1

        logger.opt(
            depth=depth,
            exception=record.exc_info,
        ).log(
            level,
            record.getMessage(),
        )


def setup_logging():

    logger.remove()

    logger.add(
        sys.stdout,
        level=settings.LOG_LEVEL,
        colorize=True,
        enqueue=True,
        backtrace=True,
        diagnose=settings.DEBUG,
        format=(
            "<green>{time:HH:mm:ss}</green> | "
            "<level>{level}</level> | "
            "<cyan>{name}</cyan> | "
            "{message}"
        ),
    )

    logger.add(
        LOG_FILE,
        rotation="10 MB",
        retention="14 days",
        compression="zip",
        level="INFO",
        enqueue=True,
        backtrace=True,
    )

    logging.root.handlers = [
        InterceptHandler()
    ]

    logging.root.setLevel(
        settings.LOG_LEVEL
    )

    return logger


app_logger = (
    setup_logging()
)