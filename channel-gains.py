#!/usr/bin/env python

import traceback, sys, seiscomp3.Client, seiscomp3.DataModel

class InvApp(seiscomp3.Client.Application):
    def __init__(self, argc, argv):
        seiscomp3.Client.Application.__init__(self, argc, argv)
        self.setMessagingEnabled(False)
        self.setDatabaseEnabled(True, True)
        self.setLoggingToStdErr(True)

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
        now = seiscomp3.Core.Time.GMT()
        try:
            lines = []
            dbq = seiscomp3.DataModel.DatabaseQuery(self.database())
            inv = seiscomp3.DataModel.Inventory()
            dbq.loadNetworks(inv) 
            nnet = inv.networkCount()
            for inet in xrange(nnet):
                network = inv.network(inet)
                sys.stderr.write("\rworking on network %2s" % network.code())
                dbq.load(network);
                nsta = network.stationCount()
                for ista in xrange(nsta):
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

                    # now we know that this is an operational station
                    for iloc in xrange(station.sensorLocationCount()):
                        location = station.sensorLocation(iloc)
                        for istr in range(location.streamCount()):
                            stream = location.stream(istr)
                            
                            line = "%-2s %-5s %-2s %-3s %g" % (network.code(), station.code(), location.code(), stream.code(), stream.gain())
                            lines.append(line)

            lines.sort()
            for line in lines:
                print line

            return True
        except:
            info = traceback.format_exception(*sys.exc_info())
            for i in info: sys.stderr.write(i)
            sys.exit(-1)

def main():
    app = InvApp(len(sys.argv), sys.argv)
    app()

if __name__ == "__main__":
    main()

