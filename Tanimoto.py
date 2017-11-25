# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:14:04 2017

@author: David
"""

"""
Created on Mon Nov 20 07:53:22 2017

@author: David
"""
import csv
import thread
import threading
import pandas as pd
import time
global timetotal
datos=pd.read_csv('ZINC.csv')
datos1=pd.read_csv('ZINC.csv')
dr=pd.DataFrame(datos)
do=pd.DataFrame(datos1)
list=[]
print 'Componente_a\t\t','Componente_b\t\t','Value'
vmax_hilos={}

def formulas(a,b): 
  
  for i in range(a,b):
   for j in range(0,len(do)):
      
      hola=dr.loc[i,'SMILES']
     
      hola1=do.loc[j,'SMILES']
      
      Na=0.0
      Nb=0.0
      Nc=0.0
      T=0.0
      diccionario={}
      diccionario2={}
      diccionario3={}
      for letra in hola:
                if diccionario.has_key(letra) :
                         diccionario[letra]=diccionario[letra]+1
                         if diccionario.has_key('@')==True:
                             diccionario['@']=1
                else:
                            diccionario[letra]=1
      
       
                        
      for letra1 in hola1:
                if diccionario2.has_key(letra1):
                         diccionario2[letra1]=diccionario2[letra1]+1  
                         if diccionario2.has_key('@')==True:
                             diccionario2['@']=1
                else:
                            diccionario2[letra1]=1  
      
     
      #print diccionario
      #print diccionario2
      for letra in diccionario:
         for letra1 in diccionario2:
           
           if letra==letra1:
               if(diccionario[letra]<diccionario2[letra1]):
                diccionario3[letra]=diccionario[letra]
               else:
                diccionario3[letra]=diccionario2[letra1]
      #print diccionario3
      
      for letra1 in diccionario2:
       Na+=diccionario2[letra1]
      #print Na
      for letra in diccionario:
       Nb+=diccionario[letra]
      #print Nb
      for letra in diccionario3:
       Nc+=diccionario3[letra]
      #print Nc
      T= Nc/(Na+Nb-Nc)
      #list.insert(i,dr.loc[i,'chemical_id'])
      #list.sort()
      list.insert(1,(dr.loc[i,'chemical_id'] ,  do.loc[j,'chemical_id'],  round(T,2) ))
      list.sort()
      
      print (dr.loc[i,'chemical_id'],"" ,  do.loc[j,'chemical_id'],"",  round(T,2)) 
      
      final = open('salida.csv', 'w')#poner cualquier nombre para el archivo de salida
      salida = csv.writer(final)
      salida.writerow(['COMPONENTE_A', 'COMPONENTE_B','VALUE'])
      salida.writerows(list)
      del salida
      final.close()
  
start=time.time()

hilo1 = threading.Thread(target=formulas,args=(0,6072 ))
hilo2 = threading.Thread(target=formulas,args=(6073, 8587))
hilo3 = threading.Thread(target=formulas,args=(8588,10517 ))
hilo4 = threading.Thread(target=formulas,args=(10518, 12144))
#hilo3 = threading.Thread(target=formulas,args=(len(dr)*2/3, len(dr)))
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
#hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()
#hilo3.join()
end=time.time()
timetotal=end-start

print 'tiempo es', timetotal
#try:
 
 #thread.start_new_thread( formulas, ( 0,0,len(dr)/2 ) )
 #thread.start_new_thread( formulas, ( 1,len(dr)/2, len(dr)) )
 
#except:
 #  print "Error: unable to start thread"

#while 1:
 #  pass  
#end=time.time()
#print 'tiempo',(end-start)   

#formulas(2)      
#print list    
#th=[]
#for i in range (0,2) :
 #   th.append(threading.Thread(target=formulas))
  #  th[i].start()

#print threads