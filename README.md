## Desempeño
***
Descripción de procedimiento:
* Investigo una biblioteca que extrae los datos que solicitemos de wireshark.(pyshark).
* Se genera un fichero ".py" para extraer los datos que solicitemos del paquete para comprobarlos posteriormente. "wireshar.py" contiene comentarios que explican el código.
* Por último, se crea un fichero ".py", "test_file.py" contiene las pruebas que se realizarán sobre el paquete obtenido de la captura de red. También se han añadido comentarios a este fichero.

Descripción de su ejecución.
* Nos situamos en la ruta indicada: "cd /home/kali/Test_BCNC_DanielMoraleda"
* Instalo la biblioteca (pyshark) usando el siguiente comando: "pip install pyshark".
* Utilizamos el módulo "unittest que se utiliza para pruebas unitarias con el siguiente comando: "python -m unittest test_file.py"
* El resultado obtenido es una lista enumerada de los parámetros que indicamos extraer del paquete.
