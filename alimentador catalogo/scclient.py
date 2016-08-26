import sys, traceback, seiscomp3.Client
from seiscomp3 import  IO
import os, sys, subprocess, traceback
import seiscomp3.Client, seiscomp3.Seismology, seiscomp3.System

class EventListener(seiscomp3.Client.Application):

    def __init__(self):
        seiscomp3.Client.Application.__init__(self, len(sys.argv), sys.argv)
        self.setMessagingEnabled(True)
        self.setDatabaseEnabled(True, True)
        self.setPrimaryMessagingGroup(seiscomp3.Communication.Protocol.LISTENER_GROUP)
        self.addMessagingSubscription("EVENT")
#       self.addMessagingSubscription("LOCATION")

    def doSomethingWithEvent(self, event):
        try:

            print "event.publicID = %s" % event.publicID()

        except:
            info = traceback.format_exception(*sys.exc_info())
            for i in info: sys.stderr.write(i)

    def updateObject(self, parentID, object):
        event = seiscomp3.DataModel.Event.Cast(object)
        origin = seiscomp3.DataModel.Origin.Cast(object)
        if event:

            print "fecha %s" % origin.publicID()
            print "Acatualizacion de evento %s" % event.publicID()
            self.doSomethingWithEvent(event)


    def addObject(self, parentID, object):
        event = seiscomp3.DataModel.Event.Cast(object)
        if event:
            print "Nuevo evento resgistrado %s" % event.publicID()
            self.doSomethingWithEvent(event)

    def run(self):
        print "Monitor activado"
        return seiscomp3.Client.Application.run(self)

app = EventListener()
sys.exit(app())

