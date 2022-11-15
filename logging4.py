import logging
logging.basicConfig(filename = "lk4.log",level = logging.ERROR,format =" %(asctime)s %(levelname)s %(message)s")

try :
    logging.info("successfully created in try")
    with open("abc.txt","r"):
        logging.info("successfully create")
except Exception as e:
    logging.error(e)