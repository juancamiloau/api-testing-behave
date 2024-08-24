# Proyecto de Pruebas de API con Behave y Requests

Este proyecto es una suite de pruebas automatizadas para la API de Pet Store (`https://petstore.swagger.io/v2`) especificamente para el crud de usuarios. Utiliza `behave` para la gestión de escenarios de prueba y `requests` para realizar las solicitudes HTTP a la API.

## Estructura del Proyecto

- `features/`: Contiene los archivos `.feature` donde se definen los escenarios de prueba en lenguaje Gherkin.
- `steps/`: Contiene los archivos Python que implementan los steps definidos en los archivos `.feature`.
- `utilities/`: Contiene utilidades y configuraciones, incluyendo el archivo `properties.ini` para manejar la configuración de la URL de la API.
- `templates/`: Contiene el body para crear un usuario llamado `create_user.json` donde se configura para tener datos aleatorios en el username.

## Escenarios de Prueba

### Feature: Pet store user API

Este feature cubre tres escenarios principales para probar la creación, modificación y eliminación de un usuario en la API:

1. **Scenario: Create user**
   - Se crea un nuevo usuario en la API.
   - Se verifica que el código de estado de la respuesta sea 200.
   - Se verifica que los datos del usuario creado se puedan obtener correctamente.

2. **Scenario: Modify user**
   - Se crea un nuevo usuario en la API.
   - Se modifica la información del usuario existente.
   - Se verifica que los datos del usuario modificado se puedan obtener correctamente.

3. **Scenario: Delete user**
   - Se crea un nuevo usuario en la API.
   - Se elimina el usuario creado.
   - Se verifica que el código de estado de la respuesta sea 200.
   - Se verifica que el al consultar el usuario eliminado se retorne un código 404.

## Configuración del Proyecto

La URL de la API y otras configuraciones necesarias para las pruebas se almacenan en un archivo `properties.ini`, ubicado en la carpeta `utilities/`. Esta configuración se carga al inicio de cada escenario mediante un hook `before_scenario`.

## Requisitos
- Python 3.x
- pip (gestor de paquetes de Python)
Las siguientes dependencias instaladas:
- behave
- requests

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```
## Ejecución

Para ejecutar este suite de pruebas basta con ejecutar el siguiente comando:
```bash
behave
```
