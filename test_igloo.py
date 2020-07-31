
import unittest
import os
import json

from igloo import app



class DevicesTest(unittest.TestCase):
  """
  Users Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = app
    self.client = self.app.test_client
    self.device = "<DeviceCommand id=e0ec28d4-27f5-86a2-a20e-b68b330abb89><DCCRoleID>EIS</DCCRoleID><DeviceID>0F-0B-6B-01-00-0D-0C-CD</DeviceID><DeviceType>ESME</DeviceType><Body><UpdateDeviceLog><DeviceID>3F-EB-5A-FF-FF-2D-77-17</DeviceID><RequestType>Add</RequestType><AddDeviceToSystem><JoinTimePeriod>3600</JoinTimePeriod><InstallCode>015156FD96159409C973701EC28703EB</InstallCode><ImportMPxN>20000321321232</ImportMPxN></AddDeviceToSystem></UpdateDeviceLog></Body><SchemaVersion>3.0</SchemaVersion><SubmittedDeviceType>CHF</SubmittedDeviceType><SMETSV>2</SMETSV></DeviceCommand>"


  
#   def test_device_creation(self):
#     """ test devise post """
#     res = self.client().post('/api/device-commands', headers={'Content-Type': 'application/xml'}, data=self.device)
#     json_data = json.loads(res.data)
#     self.assertTrue(json_data.get('message'))
#     # self.assertEqual(res.status_code, 201)




  def test_device_get(self):
    """ test device get"""
    
    res = self.client().get('/api/device-commands/e0ec28d4-27f5-86a2-a20e-b68b330abb89')
    json_data = json.loads(res.data)
    self.assertTrue(json_data)
    self.assertEqual(res.status_code, 200)
   


if __name__ == "__main__":
  unittest.main() 
