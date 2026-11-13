# Trabajo Práctico 2: Análisis de Datos con Python, SQL y Pandas

Este proyecto corresponde al **Trabajo Práctico N° 2**, cuyo objetivo es integrar la generación de datos ficticios, el almacenamiento relacional con **SQL (SQLite)** y la manipulación, consulta y visualización de datos utilizando **Python**, **Pandas** y **Matplotlib** dentro de un entorno **Jupyter Notebook**.

---

## 📁 Estructura del Repositorio

```text
.
├── crear_db.py                    # Script en Python para inicializar la base de datos y tablas
├── tp2_resolucion.ipynb           # Notebook principal con las consultas SQL, análisis y gráficos
├── datos_mockaroo.csv             # Dataset ficticio exportado desde Mockaroo
├── reporte_capital_categorias.csv # CSV resultante generado a partir de una consulta SQL
├── tp2_base.db                    # Base de datos SQLite local (creada tras ejecutar el script)
└── README.md                      # Documentación del proyecto
```

---

##  Requisitos Previos

Asegúrate de tener instalado [Anaconda](https://www.anaconda.com/) o [Miniconda](https://docs.conda.io/en/latest/miniconda.html) en tu sistema.

---

## Guía de Instalación y Ejecución

Sigue estos pasos desde tu terminal para clonar, configurar y ejecutar el proyecto:

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Crear y activar el entorno Conda
Creamos un entorno aislado con Python 3.11 para evitar conflictos de librerías:

```bash
# Crear entorno
conda create -n tp2_python python=3.11 -y

# Activar entorno
conda activate tp2_python
```

### 3. Instalar las dependencias
Instala los paquetes necesarios en el entorno activo:

```bash
pip install pandas matplotlib jupyter
```

### 4. Inicializar la Base de Datos
Antes de ejecutar el Notebook, ejecuta el script ejecutable para crear la estructura relacional (`categorias` y `productos` con sus respectivas claves foráneas) e insertar los registros base:

```bash
python crear_db.py
```

*Salida esperada:*
```text
Categorías iniciales insertadas.
Base de datos 'tp2_base.db' y tablas creadas exitosamente.
```

### 5. Iniciar Jupyter Notebook
Lanza la interfaz de Jupyter Notebook para abrir la solución:

```bash
jupyter notebook
```

Una vez en la interfaz web, abre el archivo **`tp2_resolucion.ipynb`** y ejecuta las celdas en orden secuencial.

---

## 📊 Descripción del Notebook (`tp2_resolucion.ipynb`)

El notebook contiene todo el flujo de trabajo del proyecto:

1. **Importación e Inserción de Datos:** Carga del CSV generado en Mockaroo (`datos_mockaroo.csv`) e inserción masiva a la tabla `productos` en la base SQLite.
2. **Consultas SQL y Visualización:**
   * **Consulta 1 (`WHERE`, `BETWEEN`, `LIKE`):** Identificación de productos con stock crítico (entre 10 y 50 unidades). Visualización mediante un gráfico de barras horizontal.
   * **Consulta 2 (`GROUP BY`, `COUNT`, `AVG`, `SUM`):** Análisis del capital invertido y desglose de productos por categoría. Visualización mediante un gráfico circular (*Pie Chart*).
   * **Consulta 3 (`MIN`, `MAX`, `CONCAT`):** Reporte gerencial formateado con los valores mínimos y máximos de precio y stock.
3. **Exportación de Resultados:** Exportación del DataFrame resultante de la Consulta 2 a un nuevo archivo CSV (`reporte_capital_categorias.csv`).
