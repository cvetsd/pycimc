import datetime
import logging
from logging.handlers import RotatingFileHandler
import inspect

def initlogging(argvlocal):
    global logfile 
    mynow = datetime.datetime.now()
    mytimestamp = mynow.strftime("%Y%m%d_%H%M")
    logger = logging.getLogger('mylog')
    myfmt = logging.Formatter("%(asctime)-15s @ [%(threadName)s] @ %(message)s  ")
    if '/' in argvlocal[0]:
        print(argvlocal[0])
        myfilename = argvlocal[0][argvlocal[0].rfind('/')+1:len(argvlocal[0])]
    else:
        myfilename = argvlocal[0]
    myhandler = RotatingFileHandler('logs/%s_%s.log' % (mytimestamp, myfilename[0:myfilename.find('.',2)]), maxBytes=100000,
                                  backupCount=10)
    myhandler.setFormatter(myfmt)
    logger.setLevel(logging.INFO)
    logger.addHandler(myhandler)
    #this is to print it on exit
    logfile = myhandler.baseFilename

def mylogger(mymsg):
    logger = logging.getLogger('mylog')
    logger.info(mymsg)

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno