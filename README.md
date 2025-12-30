# Final - Lenguaje de Programación II
<table>
  <tr>
    <td style="padding-right: 20px;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Unalm_logo.png" width="115" />
    </td>
    <td style="vertical-align: top; font-size: 20px; line-height: 1.0;">
      <strong>Universidad Nacional Agraria La Molina</strong><br><br>
      Facultad de Economía y Planificación<br><br>
      Departamento de Estadística e Informática
    </td>
  </tr>
</table>

**Docente:** Ana Cecilia Vargas Paredes  
📧 *anavargas@lamolina.edu.pe*  
🕒 *Horario de atención:* Martes y jueves, 11:00 – 12:00 h  
🏫 *Oficina:* N.º 13, Facultad de Economía y Planificación  

---

## 🧮 Evaluación Grupal 2 

### **Análisis de precios y disponibilidad de libros académicos**  
Proyecto que consiste en recopilar automáticamente información de distintas plataformas en línea sobre precios, stock y formatos de libros académicos, con el fin de comparar costos, identificar disponibilidad y apoyar la toma de decisiones de estudiantes e instituciones educativas.

**Relevancia:**  
Facilita la comparación de precios para estudiantes, de modo que la busqueda de libros sea mas eficiente y amena.

**Producto:**  
Conjunto de datos con precios, autores y editoriales. 

**Objetivos:**
Objetivo General: Desarrollar un sistema integral de extracción y procesamiento de datos bibliográficos que combine el consumo de APIs abiertas con técnicas de Web Scraping, con el fin de centralizar información académica y proporcionar una herramienta automatizada de comparación de precios en tiempo real entre librerías locales (SBS y Crisol), facilitando así la toma de decisiones económicas y de investigación para el usuario.

Objetivos Específicos:

- Automatización de Fuentes Académicas: Implementar scripts en Python para la consulta masiva de APIs (OpenLibrary, OpenAlex, Crossref), estructurando metadatos clave (título, autor, DOI, editorial) en formatos estandarizados (JSON/CSV) para su posterior análisis.

- Herramienta de Ahorro (Scraping): Desarrollar un bot de navegación web (Selenium) que busque simultáneamente en catálogos comerciales, extrayendo y comparando precios de libros específicos (Caso de estudio: "Pinocho") para identificar la opción de compra más económica.

- Integración y Visualización: Unificar fuentes de datos heterogéneas en un dataset coherente que permita al usuario visualizar tablas comparativas y métricas de disponibilidad de forma clara y directa.

**Fecha de entrega:** 16 de diciembre  
**Fecha de presentación:** 23 o 30 de diciembre  

---

## 👥 Integrantes del grupo

| Integrante   | Usuario   | Código   |
|---------------|----------|----------|
| Malvacedo Quiñonez, Jean Franco  | Solitario03  | 20231496  |
| Mejia Auccapoma, Piero Cesar     | PC-011  | 20230399  |
|Ferro Choque, Alvaro  |	Lupinthethird2 | 20221398  |

---
## 📚 Fuentes de Datos

### 🌐 Web Scraping

<ol>
  <li>
    <strong>SBS Librería Internacional</strong><br>
    <a href="https://www.sbs.com.pe/" target="_blank">https://www.sbs.com.pe</a><br>
    Tienda online de librería y material educativo. Se extraerán datos relacionados con
    precios, descuentos, disponibilidad en tienda física y virtual, categorías de libros
    (académicos, literatura, idiomas) y detalles editoriales de cada producto.
  </li>
  <br>
  <li>
    <strong>Crisol Librerías</strong><br>
    <a href="https://www.crisol.com.pe" target="_blank">https://www.crisol.com.pe</a><br>
    Tienda online especializada en libros técnicos y universitarios. Se extraerán datos
    relacionados con precios promocionales, disponibilidad en tienda física y virtual,
    así como detalles editoriales de cada libro.
  </li>
</ol>

---

### 🔗 API Pública

<ol start="3">
  <li>
    <strong>Open Library API</strong><br>
    <a href="https://openlibrary.org/developers/api" target="_blank">
      https://openlibrary.org/developers/api
    </a><br>
    API pública mantenida por Internet Archive que permite acceder a información
    detallada sobre libros, incluyendo títulos, ediciones, autores, materias e ISBN.
    En este proyecto se utilizará para obtener datos de libros académicos mediante
    búsquedas por título, autor o ISBN, complementando los datos extraídos por web scraping
    con información estructurada en formato JSON.
  </li>
</ol>

<ol start="4">
  <li>
    <strong>OpenAlex API</strong><br>
    <a href="https://docs.openalex.org/" target="_blank">
      https://docs.openalex.org/
    </a><br>
    API pública orientada a datos académicos que proporciona información estructurada
    sobre autores, trabajos científicos, instituciones y áreas de estudio.
    En este proyecto se utilizará para obtener datos de autores académicos,
    como nombre, afiliación institucional y número de publicaciones,
    permitiendo enriquecer la información obtenida desde la API de libros
    y el web scraping, en formato JSON.
  </li>
</ol>

<ol start="5">
  <li>
    <strong>Crossref API</strong><br>
    <a href="https://api.crossref.org/" target="_blank">
      https://api.crossref.org/
    </a><br>
    API pública que permite consultar metadatos bibliográficos de publicaciones
    académicas mediante identificadores como DOI e ISBN.
    En este proyecto se utilizará para obtener información estandarizada
    de libros y capítulos académicos, como editorial, fecha de publicación
    y referencias, complementando los datos obtenidos desde Open Library
    y el web scraping, en formato JSON.
  </li>
</ol>



---

### 📖 Referencias complementarias

<ul>
  <li>
    <a href="https://www.datacamp.com/es/blog/web-scraping-projects" target="_blank">
      https://www.datacamp.com/es/blog/web-scraping-projects
    </a><br>
    Artículo que presenta ejemplos y buenas prácticas en proyectos de web scraping,
    útil como guía técnica para el diseño y desarrollo del proyecto.
  </li>

  <li>
    <a href="https://www.octoparse.es/blog/70-fuentes-de-datos-gratuitas-en-2020" target="_blank">
      https://www.octoparse.es/blog/70-fuentes-de-datos-gratuitas-en-2020
    </a><br>
    Recurso informativo sobre fuentes de datos gratuitas en la web, que apoya la
    selección de plataformas y APIs adecuadas para la extracción de información.
  </li>

  <li>
    <a href="https://colorwhistle-com.translate.goog/api-importance-in-educational-website/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc" target="_blank">
      https://colorwhistle-com.translate.goog/api-importance-in-educational-website/
    </a><br>
    Artículo que explica la importancia del uso de APIs en sitios web educativos,
    reforzando el enfoque del proyecto en la integración de datos automatizada.
  </li>
</ul>





