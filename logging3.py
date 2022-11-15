import logging
logging.basicConfig(filename="test3.log",level = logging.INFO,format = "%(asctime)s  %(levelname)s  %(name)s  %(message)s")

def divq(a,b):
    logging.info("information entered are : "+str(a)+"and"+str(b))
    return(a/b)

print(divq(4,5))

try:
    print(divq(4,0))
except Exception as e:
    logging.exception(e)
