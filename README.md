-Adaptado a Windows-

HOLA AMIGO@ GODÍN!
Es probable que hayas notado que hay muchas pequeñas tareas de tu trabajo que consumen mucho tiempo, a pesar de que podrían no ser las más importantes de tu día a día.
Me refiero a los pequeños detalles, como abrir archivos, leerlos, validarlos, renombrarlos, etc.

En el caso de l@s que trabajamos con facturas CFDI -por cobrar, por pagar, de nómina, etc.- solemos encontrarnos que quienes las emiten (o su software de facturación) lo hacen de una manera no estandarizada que
incluso puede no decirnos nada acerca de los datos que contiene o, peor aún, inducirnos al error. Más aún si esto no obliga a manipularlas una por una de manera "manual", lo que también nos quita mucho tiempo 
para otras cosas más importantes (¡como descansar los ojos!)

En México, el SAT volvió obligatorio durante mayo de 2023 el uso de las facturas electrónicas (CFDI) en su versión 4.0. Lo cual facilita su procesamiento y análisis con Excel (Power Query) pero también con Python.
Este código en particular, sólo hace lo siguiente:

1) En el foder de "input", busca el UUID (ese valor alfa-numérico de 32 digitos único e indistiguible) de cada factura XML y la renombra con él en letras mayúsuculas.
2) Si ya existe un archivo con ese nombre en el mismo folder, le añade un "_2" o "_3", "_4"...etc. a los archivos repetidos para que los puedas eliminar antes de cargarlos a tus bases de datos y/o hojas de Excel,
   lo cual  mejora ENORMEMENTE la calidad y CONFIABILIDAD de los datos que le metes a, por ejemplo, tus tablas dinámicas.
3) Crea un reporte en Excel que resume lo que fue renombrado, así como cualquier error que pudiera haber surgido durante su procesamiento. Recomiendo siempre echarle un ojo antes de usar los archivos para cualquier
   otro fin. Igual es buena idea guardar todos los reportes en una carpeta de tu preferencia durante un tiempo razonable, quizás 1-2 meses, antes de eliminarlos.

Instrucciones:
1) Descarga el archivo .py y guárdalo en donde prefieras, recomiendo crear una nueva carpeta en la ruta de tu editor de código Python (ahí suelen guardarse los proyetos de manera predeterminada).
2) Abre tu editor de código Python y carga el archivo.
3) El folder_path es la ruta a tu carpeta con los archivos a procesar. Debes copiarlos del explorador de archivos y pegarlos entre las comillas simples ('').
   Ejemplo: r'C:\Users\aquí va tu ruta al folder con los archivos' (Aquí mismo estarán los archivos renombrados).
5) Define el output_path para el reporte de Excel, que puede ser el mismo de arriba o donde tu quieras.
6) Ejecuta el código, valida en el reporte de Excel que todo haya salido bien, y carga tus archivos ya renombrados a tu Excel con Power Query, o a tu SQL, tu ERP, etc.

NOTAS FINALES:
-También cree una versión para renombrar las versiones PDF de estos mismos archivos XML, y funciona casi a la perfección (PDF es un formato muy conflictivo por desgracia) aunque de manera un poco más lenta.

-Siéntete libre de proponer mejoras al código porque, de hecho, podría ampliarse su alcance mucho más allá de su UUID. Y porque no soy un experto en programación, es más: no sabía nada y a través de meses, durante mis tiempos libres en el trabjo, pude desarrollar esto con ayuda de herramientas de IA y la documentación oficial de Python.

-El código tiene notas en inglés, pues así suelo trabajar (es más conciso que el español) y porque es el lenguaje que usa Python.

-Este código tiene una licencia opensource por lo que puedes hacer con ello casi lo que quieras...sólo no olvides darme crédito.

