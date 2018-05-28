from bbos.config import loggingSetup
loggingSetup.initializeLogging("install.py")
import logging
import shutil 
from bbos.config.bbosConfig import BBOSConfig
from osandio.fileCompression import Unzipper
import os

#   *** Note: for OS X install these libraries using pip (sudo easy_install pip), not with this script ***
#   See: http://stackoverflow.com/a/18178419
#   Actually this one seemed to work better: http://stackoverflow.com/a/13867261

def main():
    logging.info("Starting bbos install!")
    
    from distutils.sysconfig import get_python_lib
    pythonLibDir = get_python_lib()
    
    copyAndUnzip(getSQLAlchemyLocation(), pythonLibDir, getSQLAlchemyFileName())
    
    copyAndUnzip(getPyMySQLLocation(), pythonLibDir, getPyMySQLFileName())

def getSQLAlchemyFileName():
    return "sqlalchemy.7z"

def getSQLAlchemyLocation():
    return ".." + os.sep + "tools" + os.sep + "sqlAlchemy" + os.sep + getSQLAlchemyFileName()

def getPyMySQLFileName():
    return "pymysql.7z"

def getPyMySQLLocation():
    return ".." + os.sep + "tools" + os.sep + "pymysql" + os.sep + getPyMySQLFileName()

def copyAndUnzip(toMove, destinationDir, zipFileName):
    destinationFileName = destinationDir + os.sep + zipFileName
    
    shutil.copy(toMove, destinationFileName)
    
    unzipper = Unzipper(BBOSConfig.unzipController)
    
    unzipper.unzip(destinationFileName, destinationDir)

if __name__ == '__main__': 
    main()
    
