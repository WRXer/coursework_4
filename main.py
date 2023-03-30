from src.engine_classes import HH, SuperJob
from src.connector import Connector


if __name__ == '__main__':
    hh = HH('python', 3)
    hh.get_request()
    sj = SuperJob('java', 2)
    sj.get_request()
