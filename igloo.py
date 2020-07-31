import pymongo
from flask import Flask, jsonify, request, json, make_response
import xmltodict
import dict2xml

app = Flask(__name__)
conn = pymongo.MongoClient('mongodb://pss:a1234567@ds157621.mlab.com:57621/testpss?retryWrites=false')

db = conn.testpss


@app.route('/', methods=[ 'GET'])
def Test():
      return "alive and ticking"
  
@app.route('/api/device-commands', methods=['POST'])
def adduser():
    if request.headers['Content-Type'] == 'application/xml':
        info = xmltodict.parse(request.data)
        id=info['DeviceCommand']['@id']
        data=json.loads( json.dumps(info))
        # print(data)
        # print(info['DeviceCommand']['@id'])
        # print(data['DeviceCommand']['@id'])
        # print(json.dumps(info))
        db.igloo.insert({'name': id, 'content':data})
        output = {"message": "DeviceCommand inserted successfully!"}
        return jsonify(output),201
    else:
        return jsonify({'message': 'invalid request', 'out': json.dumps(info)}),401
        
      

@app.route('/api/device-commands/<id>', methods=['GET'])
def getuser(id):
    a = db.igloo.find_one({'name': id})
    if a:
        output = {'Status': '‘device commandsʼreceived Found!'}, {'name': a['content']}
        return jsonify(output),200
    else:
        output = {'message': 'device commands not Found!'}
        return jsonify(output)
    

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host= '0.0.0.0')
