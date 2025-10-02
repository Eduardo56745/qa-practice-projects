# 🧪 QA Practice Projects  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium)
![Postman](https://img.shields.io/badge/Postman-API-orange?logo=postman)
![MySQL](https://img.shields.io/badge/SQL-Validation-lightgrey?logo=mysql)

Este repositorio contiene ejercicios prácticos de **Quality Assurance (QA)** realizados como parte de mi aprendizaje y preparación.  
Incluye pruebas **manuales de aplicación web (OpenCart)**, **pruebas de API (JSONPlaceholder)**, **validaciones SQL** y **automatizaciones con Selenium**.  

---

## 📑 Tabla de Contenido
- [📂 Contenido](#-contenido)
- [🔹 OpenCart Tests (Web App)](#-opencart-tests-pruebas-funcionales--web-app)
- [🌐 Postman Tests (API)](#-postman-tests-api--jsonplaceholder)
- [💾 SQL Validations](#-sql-validations)
- [🤖 Selenium Automation](#-selenium-automation-básico)

---

## 📂 Contenido
- **OpenCart Tests** → Pruebas funcionales manuales en [Demo OpenCart](https://demo.opencart.com/)  
- **Postman Tests (API)** → Pruebas de API usando [JSONPlaceholder](https://jsonplaceholder.typicode.com/)  
- **SQL Validations** → Consultas SQL básicas para validar datos en BD  
- **Selenium Scripts** → Automatizaciones simples en Python con Selenium  

---

## 🔹 OpenCart Tests (Pruebas Funcionales – Web App)

### Login
| ID   | Caso de Prueba   | Pasos                                                                 | Datos de Entrada                        | Resultado Esperado                                                  | Resultado Obtenido | Estado |
|------|------------------|----------------------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------|--------------------|--------|
| TC01 | Login válido      | 1. Ir a *My Account → Login*<br>2. Ingresar usuario válido<br>3. Clic en *Login* | Email válido, contraseña válida          | Acceso exitoso, redirección al Dashboard                             | Acceso exitoso, redirección al Dashboard | ✅ |
| TC02 | Login inválido    | 1. Ir a *Login*<br>2. Ingresar email válido + contraseña incorrecta | Contraseña errónea                       | Mensaje de error: “Warning: No match for E-Mail Address and/or Password.” | El mensaje de error aparece correctamente | ✅ |

### Carrito de Compras
| ID   | Caso de Prueba     | Pasos                                                                 | Datos de Entrada | Resultado Esperado                     | Resultado Obtenido | Estado |
|------|--------------------|----------------------------------------------------------------------|------------------|-----------------------------------------|--------------------|--------|
| TC03 | Agregar producto   | 1. Seleccionar un producto<br>2. Clic en *Add to Cart*                | N/A              | Producto agregado, ícono de carrito actualizado | El carrito muestra el producto agregado correctamente | ✅ |
| TC04 | Eliminar producto  | 1. Agregar producto<br>2. Ir al carrito<br>3. Clic en *Remove*        | N/A              | Producto eliminado, carrito vacío        | Producto eliminado, carrito en 0 | ✅ |

### Checkout
| ID   | Caso de Prueba       | Pasos                                                                 | Datos de Entrada     | Resultado Esperado                              | Resultado Obtenido | Estado |
|------|----------------------|----------------------------------------------------------------------|----------------------|------------------------------------------------|--------------------|--------|
| TC05 | Checkout sin login   | 1. Ir al carrito<br>2. Clic en *Checkout* sin iniciar sesión          | N/A                  | Sistema pide login o registro                   | Se muestra pantalla de login/registro | ✅ |
| TC06 | Checkout con login   | 1. Iniciar sesión<br>2. Ir al carrito con producto<br>3. Proceder al checkout | Dirección válida     | Flujo completo hasta confirmación de orden      | Flujo completado hasta la confirmación de orden | ✅ |

### Otros básicos
| ID   | Caso de Prueba       | Pasos                                                                 | Datos de Entrada | Resultado Esperado                   | Resultado Obtenido | Estado |
|------|----------------------|----------------------------------------------------------------------|------------------|---------------------------------------|--------------------|--------|
| TC07 | Búsqueda de producto | 1. Escribir nombre en buscador<br>2. Clic en *Search*                 | “MacBook”        | Resultados con productos coincidentes | Se muestran resultados relacionados con “MacBook” | ✅ |
| TC08 | Cambio de moneda     | 1. Seleccionar otra moneda en menú superior                          | USD, EUR, GBP    | Precios mostrados en la moneda elegida | Los precios cambian según la moneda seleccionada | ✅ |

---

## 🌐 Postman Tests (API – JSONPlaceholder)

Se realizaron pruebas básicas de **CRUD** sobre el recurso `/posts`.  

| ID   | Método | Endpoint   | Descripción                    | Código Esperado | Resultado Obtenido | Estado |
|------|--------|------------|--------------------------------|-----------------|--------------------|--------|
| API01 | GET    | /posts     | Obtener todas las publicaciones | 200 OK          | 200 OK (lista de 100 posts con `userId`, `id`, `title`, `body`) | ✅ |
| API02 | GET    | /posts/1   | Obtener un post específico      | 200 OK          | 200 OK (JSON con `userId`, `id`, `title`, `body`) | ✅ |
| API03 | POST   | /posts     | Crear una nueva publicación     | 201 Created     | 201 Created (JSON con `userId`, `title`, `body`, `id` generado) | ✅ |
| API04 | PUT    | /posts/1   | Actualizar publicación existente | 200 OK          | 200 OK (JSON con datos actualizados) | ✅ |
| API05 | DELETE | /posts/1   | Eliminar una publicación        | 200 OK          | 200 OK (respuesta vacía `{}`) | ✅ |

### 🔹 Ejemplo de body para POST
```json
{
  "userId": 1,
  "title": "Prueba QA",
  "body": "Este es un post de prueba"
}

```

---

## 💾 SQL Validations

Ejemplos de consultas SQL básicas para validar datos en una base de datos:

### Validar usuarios duplicados
```SQL
SELECT email, COUNT(*) 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;
```
### Validar productos sin precio asignado
```SQL
SELECT product_id, name 
FROM products 
WHERE price IS NULL OR price <= 0;
```

---

## 🤖 Selenium Automation (Básico)

Se añadieron scripts de **automatización UI con Selenium en Python**, como parte del aprendizaje en QA.

### Script: `selenium/google_search.py`
- Abre **Google**.
- Busca **“laptops”**.
- Hace clic en el primer resultado orgánico.
- Imprime en consola el título y URL de la página abierta.

> Nota: Google puede mostrar el mensaje *“I’m not a robot”* por medidas anti-bot. El script se deja como ejemplo de automatización básica.

---

### Script: `selenium/mercadolibre_search.py`
- Abre **MercadoLibre México**.
- Cierra el banner de cookies (si aparece).
- Busca **“laptops”** en el buscador.
- Espera la rejilla de resultados.
- Imprime en consola el número de resultados visibles y el título del primero.

Este script demuestra un flujo realista de automatización sobre un e-commerce.

---

## Conclusión

Este repositorio reúne ejercicios prácticos de Quality Assurance que abarcan pruebas manuales, validaciones de API, consultas SQL y ejemplos de automatización con Selenium.
Su objetivo es demostrar conocimientos fundamentales en QA funcional, pruebas de backend y automatización básica, aplicados en escenarios reales como e-commerce y consumo de APIs.