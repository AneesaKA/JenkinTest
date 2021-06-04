import os
import sys
# Get current folder path
sFilepath = os.path.split(__file__)[0].split('\\')
sBasePath = '\\'.join(sFilepath[:-1]) 
sCommonPath = sBasePath + '\\Common'
sLoginPath = sBasePath + '\\Login'
sys.path.insert(0, sCommonPath)
sys.path.insert(0,sLoginPath)

# Import Login and Common modules
from login import doLogin
from seleniumHelper import seleniumHelper
from seleniumHelper import dataSheet

# Get full file path of Datasheet
sFilePath =  os.path.split(__file__)[0] + '\\lgSummitDS.csv'
# Create seleniumHelper and Datasheet object
ds = dataSheet()
shLgSummit = seleniumHelper(sFilePath)

# Define Navigation Method
def Navigation(shLgSummit,eachLine):
    # Declare driver
    global driver        
    # Open the given Url
    driver = shLgSummit.openUrl(eachLine.Url)
    driver.implicitly_wait(10)
    # Calls doLogin function in login module
    doLogin(shLgSummit,driver,eachLine.Username,eachLine.Password)
    return driver

def doSummitLogin():
    # Get each line of data from Datasheet
    for eachLine in ds.readDataSheet(sFilePath,shLgSummit):
        # Do navigation to the Url given in current line of Data
        try:
            Navigation(shLgSummit,eachLine)
            time.sleep(5)
            logo_found = shLgSummit.check_exists(driver,'xpath','/html/body/form/div[7]/header/div[1]') 
            driver.quit()
            if (logo_found == True):
                status = 'Pass'
            else:
                status = 'Fail'
            datasheetResult = Status
            with open(os.path.split(__file__)[0] + '\\Result.csv','a+') as the_file:
                the_file.write(datasheetResult +'\n')
                the_file.close()
        except Exception as e:            
            driver.quit()



