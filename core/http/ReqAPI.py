#Author:Jason Lou
from requests import get
import json
import re
import logging


class HttpReq:
    def __init__(self, url):
        self.url = url
        print("self.url:"+self.url)
        pass

    #comm: addGoalQueueA valA;currentState running/stop
    def setCommData(self, comm, key, val):
        jsonData = get(self.url+"/"+comm+"?key="+key+"&val="+val).json()
        # logging.info(jsonData)
        return jsonData

    def getGoalState(self):
        return get(self.url+"/getGoalState").json()

    def getDelGoalState(self):
        get(self.url+"/delGoalQueue?key=GoalQueueA")
        # return get(self.url+"/delGoalAliases").json()
