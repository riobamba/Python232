#!/usr/bin/env python

import sys, traceback, seiscomp3.Client

class ListStreamsApp(seiscomp3.Client.Application):

    def __init__(self, argc, argv):
        seiscomp3.Client.Application.__init__(self, argc, argv)
        self.setMessagingEnabled(False)
        self.setDatabaseEnabled(True, True)
        self.setLoggingToStdErr(True)
        self.setDaemonEnabled(False)
#       self.setLoadInventoryEnabled(True)

    def validateParameters(self):
        try:
            if seiscomp3.Client.Application.validateParameters(self) == False:
                return False
            return True

        except:
            info = traceback.format_exception(*sys.exc_info())
            for i in info: sys.stderr.write(i)
            sys.exit(-1)

    def run(self):
        try:
            dbr = seiscomp3.DataModel.DatabaseReader(self.database())
            now = seiscomp3.Core.Time.GMT()
            inv = seiscomp3.DataModel.Inventory()
            dbr.loadNetworks(inv)
        
            result = []
            
            for inet in xrange(inv.networkCount()):
                network = inv.network(inet)
                dbr.load(network);
                for ista in xrange(network.stationCount()):
                    station = network.station(ista)
                    try:
                        start = station.start()
                    except:
                        continue
        
                    try:
                        end = station.end()
                        if not start <= now <= end:
                            continue
                    except:
                        pass
                
                    for iloc in xrange(station.sensorLocationCount()):
                        location = station.sensorLocation(iloc)
                        for istr in range(location.streamCount()):
                            stream = location.stream(istr)
        
                            result.append( (network.code(), station.code(), location.code(), stream.code()) )
        
            for net, sta, loc, cha in result:
                print "%-2s %-5s %-2s %-3s" % (net, sta, loc, cha)
                
            return True

        except:
            info = traceback.format_exception(*sys.exc_info())
            for i in info: sys.stderr.write(i)
            sys.exit(-1)
        

def main():
    app = ListStreamsApp(len(sys.argv), sys.argv)
    app()

if __name__ == "__main__":
    main()
