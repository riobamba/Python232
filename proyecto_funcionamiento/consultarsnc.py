#!/usr/bin/env python


import sys
from seiscomp3 import Client, DataModel, Core
import json
import sqlite3



class WfqQuery(Client.Application):

  def __init__(self, argc, argv,fecha,entrada,salida):
    self._fecha=fecha
    self._entrada=entrada
    self._salida=salida
    Client.Application.__init__(self, argc, argv)
    self.setPrimaryMessagingGroup("LISTENER_GROUP")
    self.addMessagingSubscription("QC")
    self.setMessagingEnabled(True)
    self.setDatabaseEnabled(True, True)
    self.setAutoApplyNotifierEnabled(False)
    self.setInterpretNotifierEnabled(True) 




  def run(self):
    self._start=self._fecha+' 00:00:00'
    self._end=self._fecha+' 23:00:00'
    self._parameter= 'availability'
    conn = sqlite3.connect('disponiblidad.db')
    cursor = conn.cursor()
    if not self.query():
      print "Sin conexion a la base de datos"
      return False
    else:
      print "Conexion a la base de datos"
    #Creacion de un archivo 
    #outfile = open(self._salida, 'w')
    
    with open(self._entrada) as data_file:    
      result = json.load(data_file)
      for station in result['stations']:
        net=str(station['net'])
        sta=str(station['sta'])
        loc=str(station['loc'])
        cha=str(station['cha'])
        lat=str(station['lat'])
        lon=str(station['long'])
        #print sta
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
        #print sta+" "+str(val)
        cursor.execute('''INSERT INTO funcionamiento (net,sta,loc,lat,lon,fun,tipo,fecha)
                  VALUES(?,?,?,?,?,?,?,?)''', (net,sta,loc,lat,lon,str(val), self._parameter,self._fecha))
        #outfile.write(sta+" "+str(val)+"\n")
               
    outfile.close()
    conn.commit()
    print "TERMINADO"
    return True



