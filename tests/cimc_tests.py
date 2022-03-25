import unittest
import pycimc
import testConfig
import cveLogger
import sys
import random
cveLogger.initlogging(sys.argv) 

class cimcTest(unittest.TestCase):

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
    
    def testGetMgmtIf(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myResp = myServer.getMgmtIf()
        myServer.logout()
        self.assertTrue(myResp)

    def testSetMgmtIfMode(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.getMgmtIf()
        if 'nicMode' in dir(testConfig):
            myResp = myServer.setMgmtIfMode(nicMode = testConfig.nicMode, nicRedundancy = testConfig.nicRedundancy)
        else:
            myResp = myServer.setMgmtIfMode()
        myServer.logout()
        self.assertTrue(myResp)

    def testSetMgmtIpAddress(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.getMgmtIf()
        if 'newIp' in dir(testConfig):
            myResp = myServer.setMgmtIp(testConfig.newIp, testConfig.newSubnet, testConfig.newGw)
        else:
            staticIp = myServer.inventory["mgmtIf"].get('extIp')
            staticMask = myServer.inventory["mgmtIf"].get('extMask')
            staticGw = myServer.inventory["mgmtIf"].get('extGw')
            myResp = myServer.setMgmtIp(staticIp, staticMask, staticGw)
        myServer.logout()
        self.assertTrue(myResp)

    def testSetDriveIdToUnconfigGood(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.get_drive_inventory()
        if 'driveIds' in dir(testConfig):
            for driveId in testConfig.driveIds:
                myResp = myServer.setDriveAsUnconfigGood(driveId)
        else:
            myResp = myServer.setDriveAsUnconfigGood(3)
        myServer.logout()
        self.assertTrue(myResp)

    def testGetStorageControllerInventory(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myResp = myServer.getStorageControllerInventory()
        self.assertTrue(myResp)
    
    def testMakeVirtualDriveBootable(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.get_drive_inventory()
        myResp = myServer.setVirtualDriveAsBootable(testConfig.virtualDriveName)
        myServer.logout()
        self.assertTrue(myResp)

    def testCreateVirtualDrive(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myServer.getStorageControllerInventory()
        controllerDn = myServer.inventory.get('storageControllers')[0].get('dn')
        drives = f'{str(testConfig.driveId1)},{str(testConfig.driveId2)}'
        myResp = myServer.create_virtual_drive(controllerDn, testConfig.virtualDriveName, "1", testConfig.virtualDriveSize,
                drives, "write-through", "64k", force=True)
        myServer.logout()
        self.assertTrue(myResp)

    def testCreateUser(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        if 'myNewUname' in dir(testConfig):
            myResp = myServer.createUser(testConfig.myNewUname, testConfig.myNewPword)
        else:
            cveLogger.mylogger("'myUname' not found in testConfig module")
        myServer.logout()
        self.assertTrue(myResp)
    
    def testGetUsers(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        myResp = myServer.get_users()
        myServer.logout()
        self.assertTrue(myResp)
    
    def testChangeUserSettings(self):
        myServer = pycimc.UcsServer(testConfig.myUcsIp, testConfig.myUname, testConfig.myPword)
        myServer.login()
        if 'myUname' in dir(testConfig):
            myResp = myServer.changeUserSettings(testConfig.myUname, testConfig.myNewPword)
        else:
            cveLogger.mylogger("'myUname' not found in testConfig module")
        myServer.logout()
        self.assertTrue(myResp)
    


if __name__ == "__main__":
    import sys
    cveLogger.initlogging(sys.argv) 
    unittest.main()