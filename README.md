# zona-prop-scraping

Scraper de Zonaprop.

## Modo de uso:

1- setear version de python con pyenv 
```bash
pyenv local 3.12
```

2- crear venv con poetry
```bash
poetry shell
```

3-
```bash 
poetry install
```


4- Ejecutar el script `zonaprop-scraping.py` pasando como argumento la url de la página de Zonaprop que se desea scrapear (por default se utilizará la url: https://www.zonaprop.com.ar/departamentos-alquiler.html):

```bash
python zonaprop_scraper/zonaprop-scraping.py <url>
```

Por ejemplo:

```bash
python zonaprop_scraper/zonaprop-scraping.py https://www.zonaprop.com.ar/departamentos-alquiler.html
```

5- El script generará un archivo `.csv` en el directorio `data` con los datos de los inmuebles obtenidos.

## Análisis de los datos:

Se puede ver un análisis de los datos obtenidos por el scraper en el archivo `/analysis/exploratory-analysis.ipynb`.

Tomar este análisis como un ejemplo de cómo se puede utilizar el scraper para obtener datos y analizarlos.
