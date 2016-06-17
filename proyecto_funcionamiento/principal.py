import sys
import consultarsnc
import threading

def funcionamiento(fecha,entrada,salida):
  app=consultarsnc.WfqQuery(len(sys.argv), sys.argv, fecha,entrada,salida)
  sys.exit(app())

t = threading.Thread(target=funcionamiento, args=("2016-06-14","stations.json","rsnc.txt"))
t.start()
#b = threading.Thread(target=funcionamiento, args=("2016-06-14","staacel.json","rnac.txt"))
#b.start()

#app=consultarsnc.WfqQuery(len(sys.argv), sys.argv, "2016-06-14","stations.json","rsnc.txt")
#  sys.exit(app())
#funcionamiento("2016-06-14","stations.json","rsnc.txt")
#funcionamiento("2016-06-14","staacel.json","rnac.txt")

