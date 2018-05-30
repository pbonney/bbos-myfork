import logging
import osandio.fileUtils
import os
from osandio._7ZipController import _7ZipController

class BBOSConfig:
    #Gameday
    gamedayURL = 'http://gd2.mlb.com/components/game/'
    statsapiURL = 'http://statsapi.mlb.com/api/v1/game/'
    gamedayDaysBackToLoad = 2

    dbUser = 'bbos'
    dbPass = 'bbos'
    dbHost = 'localhost'
    dbPort = 3306
    dbName = 'gameday'
    mySQLLocation = os.sep + "usr" + os.sep + "local" + os.sep + "mysql" + os.sep + "bin"
    numberOfThreads = 8

    #logging
    logLocation = os.sep + "Users" + os.sep + "peter" + os.sep + "Documents" + os.sep + "baseball"
    logScreenPrintingLogLevel = logging.INFO

    #file compression
    pathTo7Zip = os.sep + "opt" + os.sep + "local" + os.sep + "bin" + os.sep + "7za"
    unzipController = _7ZipController(pathTo7Zip)

    #retrosheet
    retrosheetURL = "http://www.retrosheet.org/game.htm"
    pathToChadwick = os.sep + "usr" + os.sep + "local" + os.sep + "bin" + os.sep

    sqlAlchemyEngine = 'mysql'
    sqlAlchemyHost = 'localhost'
    sqlAlchemyDatabase = 'retrosheet'
    sqlAlchemySchema = ''
    sqlAlchemyUser = 'bbos'
    sqlAlchemyPassword = 'bbos'

    #path info *** added by me ***
    pathToBBOS = os.sep + "Users" + os.sep + "peter" + os.sep + "Documents" + os.sep + "baseball" + os.sep + "bbos"

#executed on loading of config file
osandio.fileUtils.mkdir(BBOSConfig.logLocation)
