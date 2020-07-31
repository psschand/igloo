to build the container
>>>docker-compose build 

to bring up the container
>>>docker-compose up



GET request
C:\Users\surya\Desktop\N\ig>curl http://192.168.99.100:3000/api/device-commands/e0ec28d4-27f5-86a2-a20e-b68b330abb89
[{"Status":"\u2018device commands\u02bcreceived Found!"},{"name":{"DeviceCommand":{"@id":"e0ec28d4-27f5-86a2-a20e-b68b330abb89","Body":{"UpdateDeviceLog":{"AddDeviceToSystem":{"ImportMPxN":"20000321321232","InstallCode":"015156FD96159409C973701EC28703EB","JoinTimePeriod":"3600"},"DeviceID":"3F-EB-5A-FF-FF-2D-77-17","RequestType":"Add"}},"DCCRoleID":"EIS","DeviceID":"0F-0B-6B-01-00-0D-0C-CD","DeviceType":"ESME","SMETSV":"2","SchemaVersion":"3.0","SubmittedDeviceType":"CHF"}}}]


POST request
C:\Users\surya\Desktop\N\ig>curl -X POST -H "Content-Type:application/xml"  http://192.168.99.100:3000/api/device-commands
-d @device-command.xml
{"message":"DeviceCommand inserted successfully!"}