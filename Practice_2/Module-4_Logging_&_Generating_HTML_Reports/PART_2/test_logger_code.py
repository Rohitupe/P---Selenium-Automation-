import pytest
from .import BaseLogger  # file is not taking its name becod of Module-4 folder name


@pytest.mark.usefixtures("loadData")
class TestLogger(BaseLogger):
    def test_logger_testing(self, loadData):
        log = self.test_logger
        log.info("Hello")
        log.critical(loadData)
