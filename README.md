||  Instrucciones para ejecutar el programa de reconocimiento facial    ||

||  Requisitos previos  ||

1.	Instalación de Python: 
Hay que asegurarse de tener Python instalado en la máquina.
Si no se posee, se puede descargar desde python.org. Se recomienda utilizar Python 3.x.

2.	Instalar las dependencias: Este programa requiere algunas bibliotecas de Python para funcionar correctamente.
Para instalarlas, debe abrirse una terminal o línea de comandos y ejecutar lo siguiente:
  pip install opencv-python imutils numpy
Esto instalará OpenCV, una librería necesaria para el procesamiento de imágenes y video, así como imutils y numpy que son utilizadas por el programa.

3.	Asegurarse de tener los archivos necesarios:
El archivo haarcascade_frontalface_default.xml se utiliza para detectar los rostros. Este archivo está incluido en OpenCV, por lo que no se necesita descargar por separado.
El archivo modeloEigenFace.xml (o el modelo de preferencia) debe estar disponible en el mismo directorio que el script o se debe ajustar la ruta en el código según corresponda.

4.	Ruta de las imágenes de entrenamiento: Hay que asegurarse de tener un conjunto de imágenes de las personas que se desea reconocer. Las imágenes deben estar organizadas en carpetas dentro del directorio especificado en la variable dataPath en el código. Cada subcarpeta debe contener las imágenes de una persona, y el nombre de la subcarpeta debe ser el nombre de la persona.

||  Pasos para ejecutar el programa ||

1.	Entrenamiento del modelo: 
Si aún no se ha entrenado el modelo de reconocimiento facial, hay que seguir estos pasos:
    * Ejecutar el script EntrenandoRF.py. Este script recorrerá las imágenes almacenadas en la carpeta de entrenamiento y generará un modelo de reconocimiento facial.
    * El modelo entrenado se guardará en un archivo XML (por ejemplo, modeloEigenFace.xml), que será utilizado más tarde para reconocer las personas.

2.	Ejecutar el reconocimiento facial: 
Una vez que se tenga el modelo entrenado, se puede ejecutar el script ReconocimientoFacial.py, para ello.
    * Abrir una terminal o línea de comandos en el directorio donde se encuentra el script.
    * Ejecutar el siguiente comando para iniciar el reconocimiento facial:
        python ReconocimientoFacial.py
    * Se abrirá una ventana con la imagen capturada por tu cámara web. El programa detectará y reconocerá los rostros, comparándolos con el modelo entrenado.
    * Si se reconoce una persona, se mostrará su nombre y, si es la persona correcta (en este caso, "Jose Manuel Leyva Munguia"), se mostrará información adicional como los ingresos, ocupación y antecedentes.

3.	Finalizar el programa:
    * Es posible salir del programa en cualquier momento presionando la tecla ESC mientras la ventana de video está activa.

||  Problemas comunes   ||

* El modelo no reconoce correctamente el rostro: Revisar de que el rostro esté bien iluminado y frontalmente visible. Si el reconocimiento sigue fallando, intentar ajustar el umbral de confiabilidad del modelo o mejorar la calidad de las imágenes de entrenamiento.

* La cámara no se abre: Verificar que la cámara esté conectada y correctamente configurada en el sistema. Si se está utilizando un archivo de video, asegurarse de que la ruta del archivo sea correcta.