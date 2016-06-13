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
    self._parameter = "availability"
    self._start = self.commandline().optionString("startTime")
    self._end = self.commandline().optionString("endTime")

    return True

  def run(self):
    if not self.query():
      print "No database connection"
      return False
    #Creacion de un archivo 
    outfile = open('texto.txt', 'w')
    
    with open('stations.json') as data_file:    
      result = json.load(data_file)
      for station in result['stations']:
        net=str(station['net'])
        sta=str(station['sta'])
        loc=str(station['loc'])
        cha=str(station['cha'])
        lat=str(station['lat'])
        lon=str(station['long'])
        print sta
        it = self.query().getWaveformQuality(DataModel.WaveformStreamID(net,sta,loc,cha, ""),
                                                       self._parameter,
                                                       Core.Time.FromString(self._start,"%Y-%m-%d %H:%M:%S"),
                                                       Core.Time.FromString(self._end,"%Y-%m-%d %H:%M:%S"))
        val=0;
        while it.get():
          #se debe realzar el Cast para poder acceder a los atributos de la clase WaveformQuality como .value() mas en  http://www.seiscomp3.org/doc/seattle/2013.274/base/api-python.html#api-python-datamodel-waveformquality
          wfq = DataModel.WaveformQuality.Cast(it.get())
          #print wfq.value() #muestra la fecha de inicio
          val += wfq.value() 
          it.step()
        val=(val/24)
        print val
        outfile.write(sta+" "+str(val)+"\n")
               
    outfile.close()
    return True


app = WfqQuery(len(sys.argv), sys.argv)
sys.exit(app())