from bbos.db.db import DB
from bbos.config import loggingSetup
loggingSetup.initializeLogging("createBBOS.py")
import logging

    
def createMLB(db):
    sqlFile = "..\\sql\\createGamedaySchema.sql"
    
    db.run(sqlFile)
    
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
    
