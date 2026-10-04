# ANALISIS

1. El método agregarArchivo se encarga de:  
Recibir una instancia de Carpeta junto con el tipo, nombre y tamaño de un archivo, decidir qué tipo de objeto crear (ArchivoPDF o ArchivoTexto), e insertarlo directamente en la lista de archivos de esa carpeta.

2. Method obtenerTamanio se encarga de:  
Sumar primero el tamaño de todos los archivos contenidos en el nivel actual y luego recorrer e invocar la misma función sobre cada una de las subcarpetas de su lista.

3. El método enviarResultado se encarga de:  
Calcular el tamaño total de la carpeta, crear el correo (CorreoLegacy) y mandar el mensaje al destinatario.

4. Identifiquen tres problemas concretos. Para cada uno indiquen: dónde aparece, qué cambio sería difícil y qué clase o interfaz podría hacerse responsable.  

Problema 1: La carpeta guarda archivos y subcarpetas en dos listas separadas.
- Dónde aparece: en la clase Carpeta (las listas archivos y subcarpetas) y en obtenerTamanio, que tiene un for para cada lista.
- Qué cambio sería difícil: si algún día hay un tercer tipo de cosa dentro de una carpeta (por ejemplo, un acceso directo), habría que crear otra lista y otro for, y cambiar todo el código que usa la carpeta.
- Qué debería hacerse responsable: una interfaz común llamada Elemento, con el método obtenerTamanio(). Archivo y Carpeta la usarían, y la carpeta tendría una sola lista de elementos (patrón Composite).

Problema 2: Un solo lugar decide qué tipo de archivo crear, con if/else.
- Dónde aparece: en el método agregarArchivo, que revisa si el tipo es "pdf" o "txt".
- Qué cambio sería difícil: si queremos un tercer tipo de archivo (por ejemplo, "docx"), hay que abrir ese método y modificarlo. Eso se repite con cada tipo nuevo. Además, el mismo método mezcla dos trabajos: crear el archivo y guardarlo.
- Qué debería hacerse responsable: una clase CreadorArchivo con un creador para cada tipo (CreadorPDF y CreadorTexto). Cada uno sabe construir su propio archivo (patrón Factory Method).

Problema 3: El programa depende directamente del correo viejo.
- Dónde aparece: en enviarResultado, que crea un CorreoLegacy y llama a send_email.
- Qué cambio sería difícil: si cambiamos de proveedor de correo y su método se llama distinto, hay que reescribir enviarResultado. Tampoco se puede probar sin usar el correo real.
- Qué debería hacerse responsable: una interfaz Notificador con el método enviar(), y una clase AdaptadorCorreo que traduzca enviar() a send_email() (patrón Adapter).

## Cambios realizados

### Etapa 3: Composite
- Se creó la clase Elemento. Todo Elemento sabe decir su tamaño con obtener_tamanio().
- Archivo y Carpeta usan Elemento.
- Carpeta ahora tiene una sola lista (elementos) en lugar de dos.
- El cálculo del tamaño pasó de la función suelta a un método de Carpeta.
  Ya no se pregunta si algo es archivo o carpeta: cada uno responde su
  propio tamaño.

### Etapa 4: Factory Method
- Se creó CreadorArchivo, con dos creadores: CreadorPDF y CreadorTexto.
- Cada creador sabe construir un solo tipo de archivo y lo devuelve.
- Se borró la función agregar_archivo y su if/elif. Ahora la carpeta solo guarda archivos; ya no los crea.
- Si hubiera un tercer tipo de archivo, solo se agregaría un creador nuevo, sin tocar el código que ya existe.

### Cambio extra del equipo
- Se agregó validación: Elemento no acepta nombres vacíos y Archivo no acepta tamaños negativos (lanzan ValueError).
