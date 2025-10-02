# 🧪 QA – Demo OpenCart Tests  

Este repositorio contiene un set básico de **pruebas funcionales manuales** realizadas sobre la aplicación [Demo OpenCart](https://demo.opencart.com/).  

Incluye escenarios de **Login, Carrito de Compras, Checkout** y validaciones generales.  

---

## 📋 Casos de Prueba

### 🔹 Login
| ID   | Caso de Prueba   | Pasos                                                                 | Datos de Entrada                        | Resultado Esperado                                                  | Resultado Obtenido | Estado |
|------|------------------|----------------------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------|--------------------|--------|
| TC01 | Login válido      | 1. Ir a *My Account → Login*<br>2. Ingresar usuario válido<br>3. Clic en *Login* | Email válido, contraseña válida          | Acceso exitoso, redirección al Dashboard                             | Acceso exitoso, redirección al Dashboard | ✅ |
| TC02 | Login inválido    | 1. Ir a *Login*<br>2. Ingresar email válido + contraseña incorrecta | Contraseña errónea                       | Mensaje de error: “Warning: No match for E-Mail Address and/or Password.” | El mensaje de error aparece correctamente | ✅ |

---

### 🔹 Carrito de Compras
| ID   | Caso de Prueba     | Pasos                                                                 | Datos de Entrada | Resultado Esperado                     | Resultado Obtenido | Estado |
|------|--------------------|----------------------------------------------------------------------|------------------|-----------------------------------------|--------------------|--------|
| TC03 | Agregar producto   | 1. Seleccionar un producto<br>2. Clic en *Add to Cart*                | N/A              | Producto agregado, ícono de carrito actualizado | El carrito muestra el producto agregado correctamente | ✅ |
| TC04 | Eliminar producto  | 1. Agregar producto<br>2. Ir al carrito<br>3. Clic en *Remove*        | N/A              | Producto eliminado, carrito vacío        | Producto eliminado, carrito en 0 | ✅ |

---

### 🔹 Checkout
| ID   | Caso de Prueba       | Pasos                                                                 | Datos de Entrada     | Resultado Esperado                              | Resultado Obtenido | Estado |
|------|----------------------|----------------------------------------------------------------------|----------------------|------------------------------------------------|--------------------|--------|
| TC05 | Checkout sin login   | 1. Ir al carrito<br>2. Clic en *Checkout* sin iniciar sesión          | N/A                  | Sistema pide login o registro                   | Se muestra pantalla de login/registro | ✅ |
| TC06 | Checkout con login   | 1. Iniciar sesión<br>2. Ir al carrito con producto<br>3. Proceder al checkout | Dirección válida     | Flujo completo hasta confirmación de orden      | Flujo completado hasta la confirmación de orden | ✅ |

---

### 🔹 Otros básicos
| ID   | Caso de Prueba       | Pasos                                                                 | Datos de Entrada | Resultado Esperado                   | Resultado Obtenido | Estado |
|------|----------------------|----------------------------------------------------------------------|------------------|---------------------------------------|--------------------|--------|
| TC07 | Búsqueda de producto | 1. Escribir nombre en buscador<br>2. Clic en *Search*                 | “MacBook”        | Resultados con productos coincidentes | Se muestran resultados relacionados con “MacBook” | ✅ |
| TC08 | Cambio de moneda     | 1. Seleccionar otra moneda en menú superior                          | USD, EUR, GBP    | Precios mostrados en la moneda elegida | Los precios cambian según la moneda seleccionada | ✅ |

---

## 📚 Tecnologías / Herramientas usadas
- **Google Sheets / Markdown** → Documentación de casos de prueba  
- **Demo OpenCart** → Sitio web de pruebas  
- **Postman** *(opcional)* → Para futuras pruebas de API  
- **SQL básico** *(opcional)* → Validación de datos en BD  
- **Selenium (Python)** *(opcional)* → Automatización sencilla  

---

✍️ *Este es un proyecto personal de práctica para entrevistas de QA, con el objetivo de mostrar habilidades en documentación y ejecución de pruebas funcionales.*
