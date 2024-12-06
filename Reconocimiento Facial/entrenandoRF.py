import cv2
import os
import numpy as np

# Ruta donde se encuentran las imágenes de los rostros
dataPath = 'C:/Users/Josem/Desktop/PROYECTO FINAL IA/Rostros/Data' #Cambia a la ruta donde hayas almacenado Data

# Obtener lista de personas (subdirectorios) en el directorio 'Data'
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

# Inicialización de listas para las etiquetas y las imágenes de rostros
labels = []
facesData = []
label = 0

# Recorrer todas las personas y sus imágenes para entrenar el modelo
for nameDir in peopleList:
	# Ruta de la persona
	personPath = dataPath + '/' + nameDir
	print('Leyendo las imágenes')

	# Recorrer todas las imágenes dentro de cada carpeta de persona
	for fileName in os.listdir(personPath):
		print('Rostros: ', nameDir + '/' + fileName)
		# Asignar la etiqueta correspondiente a la persona
		labels.append(label)
		# Cargar la imagen en escala de grises y añadirla a facesData
		facesData.append(cv2.imread(personPath+'/'+fileName,0))
		# Imágenes de prueba (descomentarlas si se desea mostrar las imágenes mientras se leen)
		image = cv2.imread(personPath+'/'+fileName,0)
		# cv2.imshow('image',image)
		# cv2.waitKey(10)
	# Incrementar la etiqueta para la siguiente persona
	label = label + 1

# Métodos para entrenar el reconocedor (se puede elegir otro método comentando/descomentando las siguientes líneas)
face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenamiento del reconocedor de rostros seleccionado
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenamiento del modelo obtenido
face_recognizer.write('modeloEigenFace.xml')
#face_recognizer.write('modeloFisherFace.xml')
#face_recognizer.write('modeloLBPHFace.xml')
print("Modelo almacenado...")