# Proyecto de Gestion de Productos con FastAPI y MongoDB

Este proyecto es una API RESTful para gestionar productos utilizando **FastAPI** y **MongoDB**. Incluye funcionalidades para crear, listar, buscar, actualizar y eliminar productos. El diseño del proyecto implementa el enfoque de **vertical slicing**, organizando las funcionalidades en módulos.

---

## 🚀 Características

- **Crear productos**: Agregar nuevos productos con nombre, descripción, precio, stock, y categoría.
- **Listar productos**: Recuperar todos los productos disponibles en la base de datos.
- **Buscar productos por nombre**: Filtrar productos por su nombre.
- **Eliminar productos por nombre**: Eliminar un producto específico por su nombre.
- **Conexión con MongoDB**

---

## 🔧 Configuración del Entorno

La estructura del proyecto sigue un enfoque de **vertical slicing**, organizando cada funcionalidad en módulos independientes con su propia lógica, modelos, repositorios y rutas.

```plaintext
src/
├── config/                # Configuración general del proyecto
│   ├── db_mongo/          # Configuración de la base de datos MongoDB
│   │   ├── __init__.py
│   │   └── settings.py    # Configuración de variables globales
├── middlewares/           # Middlewares globales del proyecto
│   ├── __init__.py
│   └── middleware_cors.py # Middleware para configurar CORS
├── orders/                # (En desarrollo) Funcionalidades relacionadas con órdenes
├── products/              # Módulo de productos
│   ├── models/            # Modelos y esquemas de productos
│   │   ├── __init__.py
│   │   ├── format_product.py # Formateo de datos de productos
│   │   ├── product.py        # Esquema de entrada para productos
│   │   └── product_response.py # Esquema de respuesta
│   ├── repository/        # Acceso a la base de datos relacionado con productos
│   │   └── __init__.py
│   ├── services/          # Lógica de negocio para productos
│   │   ├── __init__.py
│   │   ├── router.py       # Rutas de API relacionadas con productos
│   │   └── routes.py       # Archivo para incluir todas las rutas
├── main.py                # Punto de entrada principal de la aplicación
└── .gitignore         
```
## Instalacion de dependencias del proyecto

```bash
pip install -r requirements.txt
```
## Ejecutar programa con uvicorn
```bash
uvicorn main:app --reload
```


