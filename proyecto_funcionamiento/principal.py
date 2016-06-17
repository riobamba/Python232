import sys
import consultarsnc
import multiprocessing

def funcionamiento(fecha,entrada,salida):
  app=consultarsnc.WfqQuery(len(sys.argv), sys.argv, fecha,entrada,salida)
  app()


def main():
  r = multiprocessing.Process(target=funcionamiento,args=("2016-06-14","stations.json","rsnc.txt"))
  r.start()
  a = multiprocessing.Process(target=funcionamiento,args=("2016-06-16","staacel.json","rnac.txt"))
  a.start()
  i = multiprocessing.Process(target=funcionamiento,args=("2016-06-16","stainter.json","inter.txt"))
  i.start()


main()
print ("SIGUE")

