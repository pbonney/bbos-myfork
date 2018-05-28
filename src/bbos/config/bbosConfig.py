import logging
import osandio.fileUtils
import os
from osandio._7ZipController import _7ZipController

class BBOSConfig:
    #Gameday
    gamedayURL = 'http://gd2.mlb.com/components/game/'
    gamedayDaysBackToLoad = 2
    dbUser = 'bbos'
    dbPass = 'bbos'
    dbHost = 'localhost'
    #    dbHost='127.0.0.1'
    dbPort = 3306
    dbName = 'gameday'
    #    mySQLLocation = 'C:\\Program Files\\MySQL\\MySQL Server 5.5\\bin'
    mySQLLocation = os.sep + "usr" + os.sep + "local" + os.sep + "mysql" + os.sep + "bin"
    numberOfThreads = 6
    
    #logging
    #    logLocation = 'c:\\temp'
    logLocation = os.sep + "Users" + os.sep + "peter" + os.sep + "Documents" + os.sep + "baseball"
    logScreenPrintingLogLevel = logging.INFO
    
    #file compression
    #    pathTo7Zip = ".." + os.sep + "tools" + os.sep + "7-Zip" + os.sep + "7za.exe"
    pathTo7Zip = os.sep + "opt" + os.sep + "local" + os.sep + "bin" + os.sep + "7za"
    #    unzipController = _7ZipController(os.path.abspath(pathTo7Zip))
    unzipController = _7ZipController(pathTo7Zip)
    
    #retrosheet
    retrosheetURL = "http://www.retrosheet.org/game.htm"
    #    pathToChadwick = ".." + os.sep + "tools" + os.sep + "retrosheet" + os.sep
    pathToChadwick = os.sep + "usr" + os.sep + "local" + os.sep + "bin" + os.sep
    
    #    sqlAlchemyEngine = 'mysql+pymysql'
    #    sqlAlchemyEngine = 'mysql+MySQLdb'
    sqlAlchemyEngine = 'mysql'
    sqlAlchemyHost = 'localhost'
    #    sqlAlchemyHost = '127.0.0.1'
    sqlAlchemyDatabase = 'retrosheet'
    sqlAlchemySchema = ''
    sqlAlchemyUser = 'bbos'
    sqlAlchemyPassword = 'bbos'

    #path info *** added by me ***
    pathToBBOS = os.sep + "Users" + os.sep + "peter" + os.sep + "Documents" + os.sep + "baseball" + os.sep + "bbos"

#executed on loading of config file
osandio.fileUtils.mkdir(BBOSConfig.logLocation)    