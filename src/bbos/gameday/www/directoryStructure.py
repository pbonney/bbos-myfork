from www.page import Page
import re
from datetime import date
from datetime import timedelta
from regularExpressions import pattern
import logging

class GamedayDirectoryStructure:
    def __init__(self, rootURL, league):
        self.rootURL = rootURL + league

    def getGameURLsForGame(self, gameName):
        """gid_2008_09_24_pitmlb_milmlb_1"""
        """http://gd2.mlb.com/components/game/mlb/year_2007/month_08/day_17/"""

        year = gameName[4:8]
        month = gameName[9:11]
        day = gameName[12:14]

        gameURL = self.__buildDayURL__(year, month, day) + "/" + gameName

        return [gameURL]

    def __buildDayURL__(self, year, month, day):
        monthString = str(month)

        if month < 10:
            monthString = '%02d' % month

        dayString = str(day)

        if day < 10:
            dayString = '%02d' % day

        dayURL = self.rootURL + "/year_" + str(year) + "/month_" + monthString + "/day_" + \
            dayString

        return dayURL

    def getGameURLsForDay(self, dateTuple):
        (year, month, day) = dateTuple

        dayURL = self.__buildDayURL__(year, month, day)

        gameURLs = self.__getGameURLsForDay__(dayURL)

        return gameURLs

    def getGameURLsForYear(self, year):
        yearURLs = self.__getGameURLsForYear__(year)

        return yearURLs

    def getGameURLsForMonth(self, yearMonthTuple):
        (year, month) = yearMonthTuple

        logging.debug("gameURLsForMonth:"+str(yearMonthTuple))

        yearURLs = self.__getGameURLsForMonth__(year, month)

        return yearURLs

    def getGameURLsForLastNumberOfDays(self, daysBack):
        gameURLs = []

        oneday = timedelta(days=1)

        yesterday = date.today() - oneday

        for days in range(0,daysBack):
            dayToLoad = yesterday - (days * oneday)

            year = str(dayToLoad.year)
            month = str(dayToLoad.month)
            day = str(dayToLoad.day)
            if len(month) < 2: month = '0%s' % month
            if len(day) < 2: day = '0%s' % day

            dayURL = self.__buildDayURL__(year, month, day) + "/"

            daysURLs = self.__getGameURLsForDay__(dayURL)

            gameURLs.extend(daysURLs)

        return gameURLs

    def _getGameURLsForMonth(self, monthURL):
        dayURLsForMonth = self.__getDayURLsForMonth__(monthURL)

        gameURLs = []

        for dayURL in dayURLsForMonth:
            gameURLsForDay = self.__getGameURLsForDay__(dayURL)

            gameURLs.extend(gameURLsForDay)

        return gameURLs

    def __getGameURLsForMonth__(self, year, month):
        yearURL = self.__getYearURL__(year)

        logging.debug("year URL:"+yearURL)

        dayURLs = []

        monthURLs = [yearURL + "/month_" + str(month).zfill(2)]

        for monthURL in monthURLs:
            dayURLsForMonth = self.__getDayURLsForMonth__(monthURL)

            dayURLs.extend(dayURLsForMonth)

        gameURLs = []

        for dayURL in dayURLs:
            gameURLsForDay = self.__getGameURLsForDay__(dayURL)

            gameURLs.extend(gameURLsForDay)

        return gameURLs

    def __getGameURLsForYear__(self, year):
        yearURL = self.__getYearURL__(year)
        logging.debug("year URL:"+yearURL)

        monthURLs = self.__getMonthURLsForYear__(yearURL)

        dayURLs = []

        for monthURL in monthURLs:
            dayURLsForMonth = self.__getDayURLsForMonth__(monthURL)

            dayURLs.extend(dayURLsForMonth)

        gameURLs = []

        for dayURL in dayURLs:
            gameURLsForDay = self.__getGameURLsForDay__(dayURL)

            gameURLs.extend(gameURLsForDay)

        return gameURLs

    def __getGameURLsForDay__(self, dayURL):
        gameURLs = []

        logging.debug("dayURL"+dayURL)

        if (self.__dateInFuture__(dayURL)): return []

        gameIDs = self.__parseGameIDs__(dayURL)

        for gameID in gameIDs:
            gameURL = dayURL + "/" + gameID
            logging.debug("game URL:"+gameURL)

            gameURLs.append(gameURL)

        gameURLs = self.__filterGameURLsForFullGames__(gameURLs)

        return gameURLs

    def __dateInFuture__(self, dayURL):
        #"hlb/year_2008/month_09/day_24/
        logging.debug("dayURL:"+str(dayURL))

        year = int(pattern.capture("year_(\d\d\d\d)", dayURL))
        month = int(pattern.capture("month_(\d\d)", dayURL))
        day = int(pattern.capture("day_(\d\d)", dayURL))

        today = date.today()

        yearNow = today.year
        monthNow = today.month
        dayNow = today.day

        yearGreaterThanCurrentYear = (year > yearNow)
        yearEqualToCurrentYearButMonthGreaterThanCurrentMonth = (year == yearNow and month > monthNow)
        yearEqualAndMonthEqualButDayGreaterThanCurrentDay = (year == yearNow and month == monthNow and day > dayNow)

        return yearGreaterThanCurrentYear or yearEqualToCurrentYearButMonthGreaterThanCurrentMonth \
            or yearEqualAndMonthEqualButDayGreaterThanCurrentDay

    def __filterGameURLsForFullGames__(self, gameURLs):
        filteredURLs = []

        for url in gameURLs:
            logging.debug("gameURL:" + url)

            hitURL = url + "/inning/inning_hit.xml"

            hitXML = Page(hitURL).getContent()

            if hitXML.find("404 Not Found") == -1 and hitXML.find("NoSuchKey") == -1:
                filteredURLs.append(url)
            else:
                logging.debug("incomplete game info found, skipping URL:"+url)
                logging.debug("no content found at URL:"+hitURL)

        return filteredURLs

    def __parseGameIDs__(self, dayURL):

        dayURLContent = Page(dayURL).getContent()
        #<li><a href="gid_2007_08_17_kcamlb_oakmlb_1/"> gid_2007_08_17_kcamlb_oakmlb_1/</a></li>

        pattern = re.compile('gid_\d\d\d\d_\d\d_\d\d_\w*_\w*_\d\/\">')

        gameIDs = pattern.findall(dayURLContent)

        gameIDs = [gID[0:-3] for gID in gameIDs]

        return gameIDs


    def __getDayURLsForMonth__(self, monthURL):
        dayURLs = []

        days = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', \
                '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', \
                '25', '26', '27', '28', '29', '30', '31')

        for day in days:
            dayURL = monthURL + '/day_' + day
            logging.debug("day URL:"+dayURL)

            dayURLs.append(dayURL)

        return dayURLs

    def __getMonthURLsForYear__(self, yearURL):
        monthURLs = []

        months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')

        for month in months:
            monthURL = yearURL + '/month_' + month
            logging.debug("month URL:"+monthURL)

            monthURLs.append(monthURL)

        return monthURLs

    def __getYearURL__(self, year):
        yearURL = self.rootURL + '/year_' + str(year)

        return yearURL


