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
Facilita la comparación de precios para estudiantes

**Fuentes:**  
Tiendas online de libros + APIs de comercio electrónico. 

**Producto:**  
Conjunto de datos con precios, autores y editoriales. 

**Fecha de entrega:** 16 de diciembre  
**Fecha de presentación:** 23 o 30 de diciembre  

---

## 👥 Integrantes del grupo

| Integrante   | Usuario   | Código   |
|---------------|----------|----------|
| Malvacedo Quiñonez, Jean Franco  | Solitario03  | 20231496  |
| Mejia Auccapoma, Piero Cesar     | PC-011  | 20230399  |

---
## 📚 Fuentes de Datos

### 🌐 Web Scraping

<ol>
  <li>
    <strong>Buscalibre Perú</strong><br>
    <a href="https://www.buscalibre.com.pe" target="_blank">https://www.buscalibre.com.pe</a><br>
    Plataforma de comercio electrónico que ofrece un amplio catálogo de libros académicos.
    Se extraerá información como título del libro, autor, editorial, precio, disponibilidad,
    stock y reseñas. Para la recolección de datos se utilizará <em>BeautifulSoup</em> en páginas
    estáticas y <em>Selenium</em> para el manejo de filtros dinámicos.
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
    <strong>PublicAPIs.dev</strong><br>
    <a href="https://publicapis.dev/" target="_blank">
      https://publicapis.dev/
    </a><br>
    Directorio colaborativo que reúne más de 1400 APIs públicas gratuitas para desarrolladores,
    organizadas por categorías como Libros, Educación, Noticias y Gobierno. En este proyecto
    se utilizará como fuente de referencia para identificar y seleccionar APIs relacionadas
    con libros académicos (por ejemplo, APIs de libros, autores e ISBN), las cuales
    complementarán la información obtenida mediante web scraping con datos estandarizados
    y estructurados en formato JSON.
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
