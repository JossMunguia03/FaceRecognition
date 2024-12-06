import cv2
import os
import imutils

# Nombre de la persona a capturar el rostro
personName = 'Jose Manuel Leyva Munguia'
# Ruta donde se guardarán las imágenes de los rostros
dataPath = 'C:/Users/Josem/Desktop/PROYECTO FINAL IA/Rostros/Data' #Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName

# Crear carpeta para almacenar las imágenes si no existe
if not os.path.exists(personPath):
	print('Carpeta creada: ',personPath)
	os.makedirs(personPath)

# Inicializar la captura de video desde la cámara
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video.mp4') # Usar esta línea para capturar desde un archivo de video

# Cargar el clasificador Haar para detección de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# Contador de imágenes capturadas
count = 0
# Bucle para capturar video y detectar rostros
while True:
	# Leer un frame del video
	ret, frame = cap.read()
	if ret == False: break
	
	# Redimensionar la imagen para mejorar el rendimiento
	frame =  imutils.resize(frame, width=640)
	
	# Convertir la imagen a escala de grises
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()
	
	# Detectar rostros en la imagen
	faces = faceClassif.detectMultiScale(gray,1.3,5)

	# Dibujar rectángulos alrededor de los rostros detectados y guardar las imágenes
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
		count = count + 1
	# Mostrar el frame con los rostros detectados
	cv2.imshow('frame',frame)
	
	# Esperar a presionar 'Esc' o capturar 300 imágenes para terminar
	k =  cv2.waitKey(1)
	if k == 27 or count >= 300:
		break

# Liberar recursos y cerrar ventanas
cap.release()
cv2.destroyAllWindows()