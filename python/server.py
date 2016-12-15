import zerorpc
from engine import BMEngine
# from engine_sample import BMEngine

import logging
import imp
import os

logging.basicConfig()

bmEngine = BMEngine()

class ListenerRPC(object):

    def send(self, name):
        print("receive message: " + name)
        # bmEngine.receiveFeedback
        return "from RPC message: " + name

    def getTrack(self, message):
        print('get track called. message: ' + message)
        trackId = bmEngine.getTrack()
        return trackId

    def receiveFeedback(self, feedback, trackId):

        print('feedback: ' + feedback + ", trackId: " + trackId)
        # print('receivedFeedback. message: ' + message)
        msg = bmEngine.receiveFeedback(feedback, trackId)
        return msg

    def reloadEngine(self, moduleName, fileName):

        print('Current path : ' + os.getcwd())

        try:
            newModule = imp.load_source(moduleName, fileName)
            bmEngine = newModule.NewEngine()
        except Exception:
            print("Input Error. moduleName: " + moduleName + ", fileName: " + fileName)
            return '-0.1'
        
        print('Succeed reload engine! Version : ' + bmEngine.version)
        
        return bmEngine.version



s = zerorpc.Server(ListenerRPC())


#s.bind("tcp://0.0.0.0:8080")
s.bind("tcp://0.0.0.0:4242")


#s.bind("tcp://127.0.0.1:4242")

print("python server is running")
try:
    s.run();
except Exception, e:
    print ('Exception error: ' + e);



# class HelloRPC(object):
#     def hello(self, name):
#         print('receive message: ' + name)
#         return "Hello, %s" % name

# s = zerorpc.Server(HelloRPC())
# s.bind("tcp://0.0.0.0:4242")
