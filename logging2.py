import logging
logging.basicConfig(filename="test2.log",level = logging.DEBUG,format= "%(asctime)s %(levelname)s %(name)s  %(message)s")
logging.debug("this is logging")
# logging.info("this is messagikng")