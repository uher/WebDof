import zerorpc
import logging

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name

logging.basicConfig()

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
