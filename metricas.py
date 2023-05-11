import csv
import numpy
# opening the CSV file
with open('Movie_Ratings.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  datos = []
  cola1 = {}
  movie = []
  for lines in csvFile:
        datos.append(lines)

  for l in range(1,len(datos[0])):
    a = 0 
    cola = {}
    for i in range(1,len(datos)):
      movie.append(datos[i][l])
      cola[datos[i][0]]=movie[a]
      a +=  1
    cola1[datos[0][l]]=cola
    movie.clear()

  
  # Eliminar las subclaves con valor igual a cero
  for key, sub_dict in cola1.items():
      for subkey, value in list(sub_dict.items()):
          if value == '':
              del cola1[key][subkey]

def eucledian(rating1, users):
    distance = 0
    commonRatings = False
    Cola = {}

    for rating2 in users:
        a = users[rating2]
        if a != rating1:
            distance = 0
            common_keys = set(rating1.keys()) & set(a.keys())  # Obtener las claves comunes
            for key in common_keys:
                distance += (float(rating1[key]) - float(a[key]))**2
            Cola[rating2]=numpy.sqrt(distance)
            commonRatings = True
    
    if commonRatings:
        print(Cola)
        return min(Cola, key=Cola.get)
    else:
        return -1 
    
def manhattan(rating1, users):
    
    distance = 0
    commonRatings = False
    Cola = {}

    for rating2 in users:
        a = users[rating2]
        if a != rating1:
            distance = 0
            common_keys = set(rating1.keys()) & set(a.keys())  # Obtener las claves comunes
            for key in common_keys:
                distance += abs(float(rating1[key]) - float(a[key]))
            Cola[rating2]=distance
            commonRatings = True
    
    if commonRatings:
        print(Cola)
        return min(Cola, key=Cola.get)
    else:
        return -1 
    
def pearson(rating1, users):
  
    commonRatings = False
    Cola = {}

    for rating2 in users:
        a = users[rating2]
        if a != rating1:
            sum_xy = 0
            sum_x = 0
            sum_y = 0
            sum_x2 = 0
            sum_y2 = 0
            n = 0
            distance = 0
            common_keys = set(rating1.keys()) & set(a.keys())  # Obtener las claves comunes
            for key in common_keys:
                n += 1
                x = float(rating1[key])
                y = float(a[key])
                sum_xy += x*y
                sum_x += x
                sum_y += y
                sum_x2 += x**2
                sum_y2 += y**2
            denominator = numpy.sqrt(sum_x2-(sum_x**2)/n) * numpy.sqrt(sum_y2-(sum_y**2)/n)
            if denominator == 0:
                distance = 0
            else:
                distance = (sum_xy - (sum_x*sum_y)/n)/denominator
            Cola[rating2]=distance
            commonRatings = True
    
    if commonRatings:
        print(Cola)
        return min(Cola, key=Cola.get)
    else:
        return -1 

def coseno(rating1, users):
    
    distance = 0
    commonRatings = False
    Cola = {}

    for rating2 in users:
        a = users[rating2]
        if a != rating1:
            _dot = 0
            _norm_r1=0
            _norm_a=0
            common_keys = set(rating1.keys()) & set(a.keys())  # Obtener las claves comunes
            for key in common_keys:
                _dot += float(rating1[key])*float(a[key])
                _norm_r1 += float(rating1[key])**2
                _norm_a += float(a[key])**2
            distance = _dot / (numpy.sqrt(_norm_r1)*numpy.sqrt(_norm_a))
            Cola[rating2]=distance
            commonRatings = True
    
    if commonRatings:
        print(Cola)
        return min(Cola, key=Cola.get)
    else:
        return -1 
    

print(manhattan(cola1['Katherine'],cola1))

  

