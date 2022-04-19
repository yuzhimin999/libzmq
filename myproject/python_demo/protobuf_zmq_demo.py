import protocolbufTest_pb2
import time
import os
import zmq

def set_zmq(topic, url, requestPort, responsePort):
    # ctx = zmq.Context().instance()
    # recvsocket = ctx.socket(zmq.SUB)
    # recvsocket.subscribe(topic)
    # requestUrl = "tcp://{}:{}".format(url, requestPort)
    # recvsocket.connect(requestUrl)
    # print('recvsocket bind to', requestUrl)

    # sendsocket = ctx.socket(zmq.PUB)
    # responseUrl = "tcp://{}:{}".format(url, responsePort)
    # sendsocket.connect(responseUrl)
    # print('sendsocket bind to', responseUrl)

    # return sendsocket, recvsocket
    ctx = zmq.Context().instance()
    recvsocket = ctx.socket(zmq.REP)
    recvsocket.bind("tcp://*:5555")
    return recvsocket

def serialize(data):
    send_event = protocolbufTest_pb2.Information()        #创建一个detection检测事件
    send_event.ip = data["ip"]
    send_event.port = int(data["port"])  #协议定义的int64
    send_event.type = data["type"]

    bytesdata = send_event.SerializeToString()   #最后将整个事件序列化为字节
    return bytesdata


def deserialize(message):
    deserialize_event = protocolbufTest_pb2.Information()  # 创建一个detection检测事件
    deserialize_event.ParseFromString(message)
    return deserialize_event

if __name__ == "__main__":
    topic = "animal.detection"
    url = "127.0.0.1"
    requestPort = 4601
    responsePort = 4600
    recvsocket = set_zmq(topic, url, requestPort, responsePort)

    while True:
        message = recvsocket.recv()
        recv_data = deserialize(message)
        print("收到消息：{}".format(recv_data))
        data = {"ip": "127.0.0.1", "port": 9966, "type": "string"} 
        send_message=serialize(data)
        recvsocket.send(send_message)   #发送消息，字节码消息