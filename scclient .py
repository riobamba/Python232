import sys, traceback, seiscomp3.Client

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
            #######################################
            #### Include your custom code here ####
            print "event.publicID = %s" % event.publicID()
            #######################################
        except:
            info = traceback.format_exception(*sys.exc_info())
            for i in info: sys.stderr.write(i)

    def updateObject(self, parentID, object):
        # called if an updated object is received
        event = seiscomp3.DataModel.Event.Cast(object)
        if event:
            print "received update for event %s" % event.publicID()
            self.doSomethingWithEvent(event)

    def addObject(self, parentID, object):
        # called if a new object is received
        event = seiscomp3.DataModel.Event.Cast(object)
        if event:
            print "received new event %s" % event.publicID()
            self.doSomethingWithEvent(event)

    def run(self):
        # needs not be re-implemented
        print "Hi! The EventListener is now running."
        return seiscomp3.Client.Application.run(self)

app = EventListener()
sys.exit(app())
