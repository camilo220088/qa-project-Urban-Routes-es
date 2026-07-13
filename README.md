# Urban Routes – Pruebas Automatizadas E2E

## Descripción del proyecto

Este proyecto contiene un conjunto de pruebas automatizadas end-to-end (E2E) para **Urban Routes**, una aplicación web de pedido de taxis. Las pruebas cubren el flujo completo de un usuario al solicitar un viaje: desde la configuración de la ruta hasta la asignación de un conductor, pasando por la selección de tarifa, el registro de un método de pago, y la solicitud de servicios adicionales.

El objetivo es validar que cada paso del flujo de pedido funciona correctamente de forma end-to-end, simulando la interacción real de un usuario con la interfaz.

### Flujo cubierto por las pruebas

1. Configuración de la dirección de origen y destino.
2. Selección de la tarifa **Comfort**.
3. Registro y verificación del número de teléfono (incluye confirmación por código SMS).
4. Registro de una tarjeta de crédito (incluye verificación por código y validación del campo CVV).
5. Envío de un mensaje para el conductor.
6. Solicitud de manta y pañuelos.
7. Solicitud de 2 helados.
8. Verificación de que aparece el modal de búsqueda de taxi.
9. *(Opcional)* Espera y verificación de la asignación de un conductor, incluyendo la lectura de la información del viaje (placa del vehículo).

## Tecnologías y herramientas utilizadas

- **Python** — lenguaje base del proyecto.
- **Selenium WebDriver** — automatización de la interacción con el navegador (Chrome).
- **pytest** — framework de ejecución y organización de las pruebas.
- **Page Object Model (POM)** — patrón de diseño utilizado para separar la lógica de interacción con la interfaz (`Pages/`) de la lógica de las pruebas (`tests/`), mejorando la mantenibilidad y legibilidad del código.

## Técnicas de automatización aplicadas

- **Esperas explícitas (`WebDriverWait`)** con condiciones de `expected_conditions` (`element_to_be_clickable`, `presence_of_element_located`, `visibility_of_element_located`), evitando el uso de esperas fijas (`time.sleep`) que hacen las pruebas lentas y poco confiables.
- **Esperas dinámicas personalizadas** mediante funciones `lambda`, usadas para esperar cambios de estado que no se ajustan a una condición estándar de Selenium (por ejemplo, esperar a que el texto del modal cambie de "Buscar automóvil" a la información del conductor asignado).
- **Interacción vía JavaScript (`execute_script`)** como estrategia de respaldo para casos donde el clic estándar de Selenium es interceptado por elementos superpuestos (overlays) o donde el elemento objetivo no es visualmente "clickeable" según los criterios de Selenium, aunque exista y sea funcional en el DOM.
- **Simulación de eventos de teclado (`Keys.TAB`)** para disparar eventos de pérdida de foco (`blur`) necesarios para habilitar controles condicionados por validación de formulario (por ejemplo, el botón de confirmación de tarjeta de crédito).
- **Locators específicos por contexto (scoped selectors)** para resolver ambigüedades cuando múltiples elementos comparten la misma clase CSS en distintas secciones del DOM.
- **Separación de datos de prueba** (`Data/data.py`) de la lógica de las pruebas, facilitando el mantenimiento y la reutilización de valores.
- **Interceptación de código de verificación** mediante una función auxiliar (`Helpers/retrive_code.py`) que recupera el código SMS enviado durante el flujo de verificación telefónica.

## Estructura del proyecto

```
qa-project-Urban-Routes-es/
│
├── Pages/
│   └── Urban_routes_page.py     # Locators y métodos de interacción (Page Object)
│
├── tests/
│   └── tests_urban_routes.py    # Casos de prueba (TestUrbanRoutes)
│
├── Data/
│   └── data.py                  # Datos de prueba (direcciones, teléfono, tarjeta, etc.)
│
├── Helpers/
│   └── retrive_code.py          # Función para interceptar el código de confirmación telefónica
│
└── README.md
```

## Cómo ejecutar las pruebas

### Requisitos previos

- Python 3.x instalado.
- Google Chrome instalado (las pruebas se ejecutan sobre este navegador).
- Un entorno virtual con las dependencias del proyecto instaladas (Selenium, pytest).

### Pasos

1. **Activa el entorno virtual** del proyecto (en PyCharm, se activa automáticamente al abrir la terminal integrada si el intérprete está bien configurado; en caso de hacerlo manualmente en Windows):
   ```
   .venv\Scripts\activate
   ```

2. **Instala las dependencias** (si aún no están instaladas):
   ```
   pip install selenium pytest
   ```

3. **Ejecuta todas las pruebas** desde la raíz del proyecto:
   ```
   pytest tests/tests_urban_routes.py -v
   ```

   El flag `-v` (verbose) muestra el detalle de cada test ejecutado individualmente.

4. **Ejecutar una prueba específica** (por ejemplo, solo el paso 4):
   ```
   pytest tests/tests_urban_routes.py::TestUrbanRoutes::test_4_add_credit_card -v
   ```

### Resultado esperado

Al finalizar la ejecución, la terminal debe mostrar los 9 casos de prueba pasando correctamente (`9 passed`), confirmando que el flujo completo de pedido de taxi —desde la configuración de la ruta hasta la asignación del conductor— funciona como se espera.

## Notas

- El paso 9 (espera de asignación del conductor) puede tardar hasta ~40 segundos en completarse, ya que depende del tiempo real que la aplicación toma en asignar un conductor.
- Los datos de prueba (número de tarjeta, teléfono, direcciones) se encuentran centralizados en `Data/data.py` para facilitar su actualización sin modificar la lógica de las pruebas.
