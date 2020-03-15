from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class TestClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)


class TestWrapper(EWrapper):
    results_tmp = {}
    results = {}
    

class TestApp(EClient, EWrapper):
    def __init__(self):
        TestWrapper.__init__(self)
        TestClient.__init__(self, wrapper=self)


app_ib = TestApp()
app_ib.connect("127.0.0.1", 7497, clientId=0)
# ! [connect]
print("serverVersion:%s connectionTime:%s" % (app_ib.serverVersion(),                                                      app_ib.twsConnectionTime()))