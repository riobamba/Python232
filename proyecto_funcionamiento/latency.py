#!/usr/bin/env python


import sys
from seiscomp3 import Client, DataModel, Core
import json
import sqlite3


class WfqQuery(Client.Application):
    def __init__(self, argc, argv):
        self._fecha = '2016-08-02'
        print self._fecha
        self._entrada = 'stations1.json'
        Client.Application.__init__(self, argc, argv)
        self.setPrimaryMessagingGroup("LISTENER_GROUP")
        self.addMessagingSubscription("QC")
        self.setMessagingEnabled(True)
        self.setDatabaseEnabled(True, True)
        self.setAutoApplyNotifierEnabled(False)
        self.setInterpretNotifierEnabled(True)

    def run(self):
        self._start = self._fecha + ' 01:00:00'
        self._end = self._fecha + ' 10:00:00'
        self._parameter = 'latency'
        #conn = sqlite3.connect('disponibilidad.db')
        #cursor = conn.cursor()
        if not self.query():
            print
            "Sin conexion a la base de datos"
            return False
        else:
            print
            "Conexion a la base de datos"
        # Creacion de un archivo
        # outfile = open(self._salida, 'w')

        with open(self._entrada) as data_file:
            result = json.load(data_file)
            for station in result['stations']:
                ide = str(station['id'])
                sta = str(station['estacion'])
                loc = str(station['localizador'])
                cha = str(station['canal'])
                lat = str(station['latitud'])
                lon = str(station['longitud'])
                net = str(station['red'])
                print sta
                it = self.query().getWaveformQuality(DataModel.WaveformStreamID(net, sta, loc, cha, ""),
                                                     self._parameter,
                                                     Core.Time.FromString(self._start, "%Y-%m-%d %H:%M:%S"),
                                                     Core.Time.FromString(self._end, "%Y-%m-%d %H:%M:%S"))
                val = 0;

                while it.get():
                    # se debe realzar el Cast para poder acceder a los atributos de la clase WaveformQuality como .value() mas en  http://www.seiscomp3.org/doc/seattle/2013.274/base/api-python.html#api-python-datamodel-waveformquality
                    wfq = DataModel.WaveformQuality.Cast(it.get())
                    print "%s %s"%(wfq.created(),wfq.value()) #muestra la fecha de inicio
                    #val += wfq.value()
                    it.step()
                #val = (val / 24)
                # print sta+" "+str(val)
                #cursor.execute('''INSERT INTO funcionamiento (net,sta,loc,lat,lon,fun,tipo,fecha)
                 # VALUES(?,?,?,?,?,?,?,?)''', (net, sta, loc, lat, lon, str(val), self._parameter, self._fecha))
                # outfile.write(sta+" "+str(val)+"\n")

        # outfile.close()
        #conn.commit()
        print "TERMINADO"
        return True

app = WfqQuery(len(sys.argv), sys.argv)
sys.exit(app())