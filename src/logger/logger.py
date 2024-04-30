import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)

time = "%(asctime)s"
proc = "[%(processName)s: %(process)d]"
thread = "[%(threadName)s: %(thread)d]"
info = "[%(levelname)s] %(name)s: %(message)s"

log_formatter = logging.Formatter(f"{time} {proc} {thread} {info}")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
