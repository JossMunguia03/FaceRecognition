import cv2
import os

# Datos ficticios de "Jose Manuel Leyva Munguia"
person_data = {
    'Jose Manuel Leyva Munguia': {
        'Ingresos': '$50,000 USD',
        'Ocupacion': 'Programador',
        'Antecedentes Penales': 'Ninguno'
    }
}

# Ruta donde se encuentran las imágenes de los rostros
dataPath = 'C:/Users/Josem/Desktop/PROYECTO FINAL IA/Rostros/Data' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

# Crear un objeto reconocedor de rostros utilizando EigenFaces (se puede elegir otro método comentando/descomentando las líneas correspondientes)
face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo entrenado
face_recognizer.read('modeloEigenFace.xml')
#face_recognizer.read('modeloFisherFace.xml')
#face_recognizer.read('modeloLBPHFace.xml')

# Iniciar la captura de video desde la cámara
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video.mp4') # Usar esta línea para capturar desde un archivo de video

# Cargar el clasificador de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def put_text(image, text, position, font, font_scale, color, thickness, line_type):
	"""
    Función para poner texto en una imagen.
    
    :param image: Imagen donde se va a escribir el texto.
    :param text: Texto que se va a mostrar.
    :param position: Posición (x, y) donde se va a colocar el texto.
    :param font: Tipo de fuente para el texto.
    :param font_scale: Escala del texto.
    :param color: Color del texto en formato BGR.
    :param thickness: Grosor de las letras.
    :param line_type: Tipo de línea para el texto.
    """
	cv2.putText(image, text, position, font, font_scale, color, thickness, line_type)
while True:
	# Captura de fotograma
	ret,frame = cap.read()
	if ret == False: break
	
	# Convertir a escala de grises
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()
	
	# Detectar rostros en el fotograma
	faces = faceClassif.detectMultiScale(gray,1.3,5)
	# Recorrer los rostros detectados
	for (x,y,w,h) in faces:
		rostro = auxFrame[y:y+h,x:x+w] # Extraer la región del rostro
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC) # Redimensionar rostro
		# Predecir la persona utilizando el modelo entrenado
		result = face_recognizer.predict(rostro)
		
		# Obtener el nombre de la persona reconocida
		recognized_name = imagePaths[result[0]]
		
		# Si se seleccionó EigenFaces como método y el resultado es confiable (dependiendo del umbral)
		if result[1] < 5700:
			font = cv2.FONT_HERSHEY_SIMPLEX
			font_scale = 0.5
			color = (255, 255, 255)
			thickness = 1
			put_text(frame, recognized_name, (x, y - 5), font, font_scale, color, thickness, cv2.LINE_AA)
			
			# Si la persona es "Jose Manuel Leyva Munguia", mostrar información adicional
			if recognized_name == 'Jose Manuel Leyva Munguia':
				info = person_data.get('Jose Manuel Leyva Munguia', {})
				text_height = y + h + 20

				put_text(frame, f'Ingresos: {info["Ingresos"]}', (x, text_height), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
				
				text_height += 30
				put_text(frame, f'Ocupacion: {info["Ocupacion"]}', (x, text_height), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
				
				text_height += 30
				put_text(frame, f'Antecedentes Penales: {info["Antecedentes Penales"]}', (x, text_height), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
				
			# Dibujar un rectángulo alrededor del rostro detectado
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else:
			# Si el rostro no es reconocido, marcarlo como "Desconocido"
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		
		'''
		# Si se seleccionó FisherFace como método
		if result[1] < 500:
			cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else:
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		'''

		'''
		# Si se seleccionó LBPHFace como método
		if result[1] < 70:
			cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else:
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		'''
	# Mostrar el fotograma con los resultados
	cv2.imshow('frame',frame)
	k = cv2.waitKey(1)
	if k == 27: # Salir si se presiona la tecla ESC
		break
# Liberar recursos
cap.release()
cv2.destroyAllWindows()