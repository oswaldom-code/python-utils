# Docker Scripts

Este directorio contiene scripts útiles para interactuar y gestionar contenedores Docker. Estos scripts están diseñados para simplificar tareas comunes y proporcionar análisis de información sobre contenedores en ejecución.

## Contenido

- `docker-inspector.py`: Un script que lista y analiza la configuración de los contenedores en ejecución. Proporciona información sobre el uso de CPU, memoria, volúmenes, redes, y otros datos relevantes. La información se puede exportar en formatos JSON y CSV, así como generar gráficos interactivos en formato SVG.

## Requisitos

- Python 3.x
- Bibliotecas requeridas:
  - `docker`
  - `pandas`
  - `plotly`

Puedes instalar las bibliotecas requeridas usando pip:

```bash
pip install docker pandas plotly
```

## Uso

Para ejecutar un script, simplemente navega al directorio donde se encuentra el script y usa el siguiente comando:

python3 docker-inspector.py

Este script generará archivos `container_info.json` y `container_info.csv` con la información de los contenedores, además de crear un gráfico `container_usage.svg` con estadísticas visuales de uso.
