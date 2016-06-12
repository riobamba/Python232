#!/usr/bin/env python


import sys
import re
from seiscomp3 import Client, IO, DataModel, Core
import json
import requests


class WfqQuery(Client.Application):

  def __init__(self, argc, argv):
    Client.Application.__init__(self, argc, argv)

    self.setPrimaryMessagingGroup("LISTENER_GROUP")
    self.addMessagingSubscription("QC")
    self.setMessagingEnabled(True)
    self.setDatabaseEnabled(True, True)
    self.setAutoApplyNotifierEnabled(False)
    self.setInterpretNotifierEnabled(True)


  def createCommandLineDescription(self):
    self.commandline().addGroup("Query")
    self.commandline().addStringOption("Query", "startTime,b", "start time: YYYY-MM-DD hh:mm:ss")
    self.commandline().addStringOption("Query", "endTime,e", "end time: YYYY-MM-DD hh:mm:ss")

    return True


  def validateParameters(self):
    self._outfile = 'xmx.xml'
    self._streamID = 'CM.BRR.00.HHZ'

    self._parameter = "availability"
    print (self._parameter)
    self._start = self.commandline().optionString("startTime")
    self._end = self.commandline().optionString("endTime")

    return True

  def run(self):
    if not self.query():
      print "No database connection"
      return False
    #Creacion de un archivo 
    outfile = open('texto.txt', 'w')
    
    response = requests.get("http://10.100.100.232:8081/query/stations.json")
    if response.status_code == 200:
      results = response.json()
      for result in results['Inventory']['network']:
        for station in result['station']:
          for location in station['sensorLocation']:
            for channel in location['stream']:
              print result['code'],station['code'],location['code'],channel['code']
              net=str(result['code'])
              sta=str(station['code'])
              loc=str(location['code'])
              cha=str(channel['code'])
              outfile.write(net+" "+sta+" "+loc+" "+cha+"\n")
             # it = self.query().getWaveformQuality(DataModel.WaveformStreamID(net,sta,loc,cha, ""),
              #                                               self._parameter,
               #                                              Core.Time.FromString(self._start,"%Y-%m-%d %H:%M:%S"),
                #                                             Core.Time.FromString(self._end,"%Y-%m-%d %H:%M:%S"))
              #while it.get():
                #se debe realzar el Cast para poder acceder a los atributos de la clase WaveformQuality como .value() mas en  http://www.seiscomp3.org/doc/seattle/2013.274/base/api-python.html#api-python-datamodel-waveformquality
                #wfq = DataModel.WaveformQuality.Cast(it.get())
                #print wfq.start() #muestra la fecha de inicio
                #print wfq.value() #muestra el procentaje
                #outfile.write(net+" "+sta+" "+loc+" "+cha+" "+str(wfq.value())+"\n")
               
                          
                #it.step()
    else:
        print "Error code %s" % response.status_code

    



    outfile.close()
    return True


app = WfqQuery(len(sys.argv), sys.argv)
sys.exit(app())