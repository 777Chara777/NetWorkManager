import unittest

from Manager.utility.Logger.logger import Logger, LoggerLevel

class TestLogger(unittest.TestCase):
    
    # def test_logger_create(self):
    #     Logger("main")
    
    def test_logger(self):
        d = Logger("main")
        d.info("1 tests")
        # d.set_format("tess")
        # d.info("2 tests")


        test = Logger("name")
        message = test._log("tests", LoggerLevel("Test Debug", 9, True))
        # self.assertEqual(message, None, "Сообщение не корекное ")
        pass