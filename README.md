# Data Aike

Iniciativa de comunicación de datos regionales centrada en Santa Cruz, Patagonia argentina. El proyecto combina análisis cuantitativo, visualizaciones editoriales y comunicación audiovisual de formato breve.

## Investigaciones

- [¿Cómo fueron los últimos 22 años de Santa Cruz?](stories/santa-cruz-2004-2026/): análisis histórico de la economía, la producción, el empleo y las finanzas públicas.
- [Análisis demográfico de Santa Cruz](https://github.com/gastonchalub/santa-cruz-demographic-analysis): proyecciones poblacionales por departamento y comparaciones por grupos de edad.
- [Análisis y proyección de la ganadería ovina de Santa Cruz](https://github.com/gastonchalub/santa-cruz-livestock-forecast): existencias ovinas históricas y modelos exploratorios de series temporales.

## Metodología editorial

Verificación de fuentes → limpieza de datos → análisis exploratorio → validación estadística → elaboración del guion → diseño visual → narración → edición audiovisual → publicación.

## Identidad visual

Formato vertical 9:16, tipografía de alto contraste, animaciones dinámicas y legibles, unidades y fechas explícitas, y distinción clara entre datos observados y proyecciones. Se documentan las fuentes y la incertidumbre de los pronósticos cuando corresponde.

## Ejemplo de visualización

El programa incluido genera un gráfico vertical en formato PNG a partir de la serie histórica de existencias ovinas recuperada. Es una implementación ilustrativa, no el código original de producción audiovisual.

```bash
pip install -r requirements.txt
python src/story_chart.py
```

El ejemplo no fue ejecutado como parte de esta publicación. Los archivos audiovisuales originales y los códigos de animación no están incluidos actualmente en el repositorio. Consultar la documentación de cada investigación para conocer su disponibilidad y limitaciones.
