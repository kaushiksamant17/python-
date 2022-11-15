import logging
logging.basicConfig(filename ="trail.log",level=logging.WARNING,format ="%(asctime)s %(levelname)s %(name)s %(message)s")

logging.info("this is just an information")
logging.warning("this is just a warning")
logging.debug("this is debug")

try :
     f= open("abc.txt","w")
     f.write("this is trying")
     f.append("i am trying")

except Exception as e:
    logging.error(e)
    logging.exception(e)
finally:
    logging.critical("this one is critical")
    f.close()
