# zona-prop-scraping

Scraper de Zonaprop.

Modo de uso:

Ejecutar archivo "zonaprop-scraping.py" seteando en la variable url la búsqueda que se quiere realizar. Entrar a la página y ejecutar una primera búsqueda con los filtros deseados y extraer la url (sacar el final ".html").

Se guardaran en el directorio "./data/" un archivo ".csv" y otro ".xls" con los datos extraídos de todas las páginas correspondientes a la búsqueda.

Análisis de datos:

Ejecutar el archivo "analysis-estates.py" seteando la variable "data_path" con la ubicación del archivo csv.

Utilizando los datos de área y precio de las propiedades se calculará un regresor lineal que prediga el precio de una propiedad dada el área de la misma.

A su vez se entrenará con estos mismos datos un red neuronal multicapa que también se utilizará para predecir los precios.

Pequeña conclusión:

Se puede ver, analizando como la red neuronal predice mayor valor a las propiedades de 3 ambientes y de 2 ambientes grandes con respecto al regresor lineal, que de alguna forma la red está entiendo la mayor demanda que hay por estas propiedades en el mercado.

Con el mismo razonamiento, la red neuronal entiende que hay menos demanda por departamentos más pequeños o excesivamente grandes.

Esto tiene cierto sentido ya que las familias de clase media buscarán alquilar propiedades que se encuentren en un rango de área de entre 50 y 80 mts cuadrados, aumentando la demanda de estas propiedades.
