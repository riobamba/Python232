#!/usr/bin/env python


import sys
from seiscomp3 import Client, DataModel, Core
import json



class WfqQuery(Client.Application):

  def __init__(self, argc, argv):
    Client.Application.__init__(self, argc, argv)
    self.setPrimaryMessagingGroup("LISTENER_GROUP")
    self.addMessagingSubscription("QC")
    self.setMessagingEnabled(True)
    self.setDatabaseEnabled(True, True)
    self.setAutoApplyNotifierEnabled(False)
    self.setInterpretNotifierEnabled(True)
    self.run()



  def run(self):

    self._start = '2016-06-11 00:00:00'
    self._end = '2016-06-11 01:00:00'
    self._parameter= 'availability'
    if not self.query():
      print "Sin conexion a la base de datos"
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
  
  def data(self):
      return "sirve"

app = WfqQuery(len(sys.argv), sys.argv)
sys.exit(app())