from bbos.db.db import DB
from bbos.config import loggingSetup
from bbos.config.bbosConfig import BBOSConfig
loggingSetup.initializeLogging("createBBOS.py")
import logging
import os
    
def createMLB(db):
    #    sqlFile = "..\\sql\\createGamedaySchema.sql"
    sqlFile = BBOSConfig.pathToBBOS + os.sep + "sql" + os.sep + "createGamedaySchema.sql"
    logging.info("test: " + sqlFile)
    db.run(sqlFile)
    logging.info("test")

def create():
    db = DB()
    
    createMLB(db)
    
def main():
    create()    
    

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        logging.info(e.message)
        raise Exception(e)
    
