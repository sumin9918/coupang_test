import logging

# 공통 로그 설정
logging.basicConfig(
    filename="test.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# 각 파일에서 logger를 import해서 사용하도록 설정
logger = logging.getLogger(__name__)
