# 🌴 Jungle Quest

¡Bienvenido a **Jungle Quest**!  
Un juego de aventuras 2D desarrollado con **Pygame**, donde tomás el rol de un astronauta perdido en una jungla alienígena, enfrentando peligros y buscando una salida antes de que sea demasiado tarde.

---

## 🧠 Historia

Durante una frenética persecución alienígena, una supernova interrumpe la huida de un astronauta, catapultando su nave hacia un planeta desconocido.  
El aterrizaje forzoso no sale bien, y una pieza clave de la nave llamada el "**Artefacto**", una gema que alimenta el motor, se pierde en la jungla.  
Tu misión: **sobrevivir, esquivar enemigos, encontrar el Artefacto y salir en una pieza del planeta**. Todo esto mientras criaturas hostiles te acechan en cada rincón.

---

## 🐍 Enemigos

- **Trunk:**  
  Un tronco que dispara rayos láser a intervalos. Ideal para mantenerte en movimiento.
- **Rino:**  
  Un rinoceronte imparable que embiste de derecha a izquierda arrasando con todo.

---

## 🌌 Power-ups

- **Estrella de invulnerabilidad:**  
  Si la encontras, la podes usar para volverte invulnerable por unos segundos. Puede marcar la diferencia entre la victoria o el reinicio.

---

## 🎮 Gameplay

- **Movimiento:**  
  `W`, `A`, `S`, `D` para moverte.  
  `Space` para saltar (¡doble salto incluido!).  
- **Ataque:**  
  `Shift` para disparar.  
- **Habilidad especial:**  
  `X` activa la **estrella de invulnerabilidad** (si la conseguiste).
- **Vidas:**  
  Comenzás con **5 vidas**. Cada golpe te cuesta una. Al perder todas, el juego reinicia.
- **Puntuación:**  
  Basada en la cantidad de **vidas** del personaje y las **estrellas** conseguidas. Esta puntuacion se guarda junto al nombre del jugador para luego poder verla en la seccion de leaderboards
  
---

## 🗺️ Niveles

El juego cuenta con **4 niveles únicos**, cada uno con sus propios desafíos y diseño.  
Al morir, se te pedirá tu nombre y el juego reiniciará desde el principio.

---

## 🔊 Sonido

Incluye música de fondo que puede **activarse o desactivarse** desde el menú de configuración al iniciar el juego.

---

## ⚙️ Tecnologías y estructura

- **Librerías utilizadas:**  
  Solo **Pygame**
- **tools.py:**  
  Es el **motor del juego**. Controla colisiones, movimiento del jugador y enemigos, sistema de vidas, power-ups y más.
- **main.py:**  
  Orquesta los niveles usando las funciones de `tools.py` como si fueran piezas de un gran rompecabezas. Cada nivel es una función como `level_1()`.

---

### 🧑‍💻 Autor

Desarrollado por [@ivnfdzz](https://github.com/Ivnfdzz), como proyecto personal para la universidad.
Completamente hecho en solitario en aproximadamente 2 semanas.

---

### 🏁 Planes a futuro

**Corrección** de bugs menores
**Mejora** en la **movilidad** del jugador
**Mejora** en el sistema de puntuación
Posible **expansión** con nuevos enemigos, historia o mecánicas

---

## 🚀 Instalación

*Se recomienda usar un entorno virtual*

### 1. Cloná el repositorio:
```
git clone https://github.com/Ivnfdzz/Jungle_Quest.git
cd Jungle_Quest
```

### 2. Creá un entorno virtual:
```
python -m venv venv
```

### 3. Activá el entorno virtual:
- En Windows:
```
venv\Scripts\activate
```
- En macOS/Linux:
```
source venv/bin/activate
```

### 4. Instalá pygame:
```
pip install pygame
```

### 5. Ejecutá el juego:
```
python src/main.py
```
