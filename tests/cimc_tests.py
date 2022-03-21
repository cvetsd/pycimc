import unittest
import pycimc
import testConfig
import cveLogger
import sys
import random
cveLogger.initlogging(sys.argv) 

class cimcTest(unittest.TestCase):

    def testChangeIpAddress(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.getMgmtIf()
        if 'newIp' in dir(testConfig):
            myResp = myServer.setMgmtIp(testConfig.newIp, testConfig.newSubnet, testConfig.newGw)
        else:
            myResp = myServer.setMgmtIp("myServer.inventory.get('mgmtIf').get('extIp')", 
                myServer.inventory.get('mgmtIf').get('extMask'), myServer.inventory.get('mgmtIf').get('extGw'))
        myServer.logout()
        self.assertTrue(myResp) 

    def testChangeHostname(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.getMgmtIf()
        if 'newHostname' in dir(testConfig):
            myResp = myServer.setHostname(testConfig.newHostname)
        else:
            myResp = myServer.setHostname(f"test{random.randrange(1,99)}")
        myServer.logout()
        self.assertTrue(myResp)      

    def testEnableDhcp(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.getMgmtIf()
        myResp = myServer.setEnableDhcp()
        myServer.logout()
        self.assertTrue(myResp)
    
    def testGetBootOrder(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myResp = myServer.getBootOrder()
        myServer.logout()
        self.assertTrue(myResp)
    
    def testSetMgmtIfMode(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.getMgmtIf()
        if 'nicMode' in dir(testConfig):
            myResp = myServer.setMgmtIfMode(nicMode = testConfig.nicMode)
        else:
            myResp = myServer.setMgmtIfMode()
        myServer.logout()
        self.assertTrue(myResp)

    def testSetDriveIdToUnconfigGood(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.get_drive_inventory()
        if 'driveId' in dir(testConfig):
            myResp = myServer.setDriveAsUnconfigGood(testConfig.driveId)
        else:
            myResp = myServer.setDriveAsUnconfigGood(3)
        myServer.logout()
        self.assertTrue(myResp)

if __name__ == "__main__":
    import sys
    cveLogger.initlogging(sys.argv) 
    unittest.main()