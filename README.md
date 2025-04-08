# 🌴 Jungle Quest

[English](#english) | [Español](#español)

---

<a name="english"></a>
# 🌴 Jungle Quest

Welcome to **Jungle Quest**!  
A 2D adventure game developed with **Pygame**, where you take on the role of an astronaut lost in an alien jungle, facing dangers and looking for a way out before it's too late.

![Level_1](https://github.com/Ivnfdzz/Jungle_Quest/blob/d4e3ba1fc01eec9c09a2aeb2d2e165b45276a5fc/src/assets/readme/level_1.png)

---

## 🧠 Story
During a frantic alien chase, a supernova interrupts an astronaut's escape, catapulting their ship towards an unknown planet.  
The crash landing doesn't go well, and a key piece of the ship called the "**Artifact**", a gem that powers the engine, is lost in the jungle.  
Your mission: **survive, dodge enemies, find the Artifact and get off the planet in one piece**. All this while hostile creatures lurk in every corner.

---

## 🐍 Enemies
- **Trunk: ![Trunk](https://github.com/Ivnfdzz/Jungle_Quest/blob/d4e3ba1fc01eec9c09a2aeb2d2e165b45276a5fc/src/assets/readme/trunk.png)**  
  A trunk that shoots laser beams at intervals. Ideal for keeping you on the move.
  
- **Rino: ![Rino](https://github.com/Ivnfdzz/Jungle_Quest/blob/d4e3ba1fc01eec9c09a2aeb2d2e165b45276a5fc/src/assets/readme/Rino.png)**  
  An unstoppable rhinoceros that charges from right to left, destroying everything in its path.

*Each defeated enemy will add a star to your score*

---

## 🌌 Power-ups
- **Invulnerability Star: ![inv_star](https://github.com/Ivnfdzz/Jungle_Quest/blob/d4e3ba1fc01eec9c09a2aeb2d2e165b45276a5fc/src/assets/readme/invulnerability_star.png)**  
  If you find it, you can use it to become invulnerable for a few seconds. It can make the difference between victory or restart.

---

## 📺 Watch Gameplay
See Jungle Quest in action! Just click in this video where you can watch the full gameplay and how the mechanics work live.
[![Watch the gameplay on YouTube](https://img.youtube.com/vi/LDWBX3Gc_dw/0.jpg)](https://www.youtube.com/watch?v=LDWBX3Gc_dw)

---
## 🎮 Gameplay
- **Movement:**  
  `W`, `A`, `S`, `D` to move.  
  `Space` to jump (double jump included!).  
- **Attack:**  
  `Shift` to shoot.  
- **Special ability:**  
  `X` activates the **invulnerability star** (if you've obtained it).
- **Lives:**  
  You start with **5 lives**. Each hit costs you one. When you lose them all, the game restarts.
- **Score:**  
  Based on the number of **lives** of the character and the **stars** obtained. This score is saved along with the player's name to be seen later in the leaderboards section.
  
---

## 🗺️ Levels
The game has **4 unique levels**, each with its own challenges and design.  
When you die, you'll be asked for your name and the game will restart from the beginning.

---

## 🔊 Sound
Includes background music that can be **turned on or off** from the settings menu when starting the game.

---

## ⚙️ Technologies and structure
- **Libraries used:**  
  Only **Pygame**
- **tools.py:**  
  It's the **game engine**. Controls collisions, player and enemy movement, lives system, power-ups and more.
- **levels.py:**  
  Orchestrates the levels using the functions of `tools.py` as if they were pieces of a big puzzle. Each level is a function like `level_1()`.

---

### 🧑‍💻 Author
Developed by [@ivnfdzz](https://github.com/Ivnfdzz), as a personal project for university.
Completely made solo in approximately 2 weeks.

---

### 🏁 Future plans
- **Correction** of minor bugs
- **Improvement** in player **mobility**
- **Improvement** in the scoring system
- Possible **expansion** with new enemies, story or mechanics

---

## 🚀 Installation
*It is recommended to use a virtual environment*

### 1. Clone the repository:
```
git clone https://github.com/Ivnfdzz/Jungle_Quest.git
cd Jungle_Quest
```

### 2. Create a virtual environment:
```
python -m venv venv
```

### 3. Activate the virtual environment:
- On Windows:
```
venv\Scripts\activate
```
- On macOS/Linux:
```
source venv/bin/activate
```

### 4. Install pygame:
```
pip install -r requirements.txt
```

### 5. Run the game:
```
python src/main.py
```

---

<a name="español"></a>
# 🌴 Jungle Quest

¡Bienvenido a **Jungle Quest**!  
Un juego de aventuras 2D desarrollado con **Pygame**, donde tomás el rol de un astronauta perdido en una jungla alienígena, enfrentando peligros y buscando una salida antes de que sea demasiado tarde.

![Level_1](https://github.com/Ivnfdzz/Jungle_Quest/blob/d4e3ba1fc01eec9c09a2aeb2d2e165b45276a5fc/src/assets/readme/level_1.png)

---

## 🧠 Historia
Durante una frenética persecución alienígena, una supernova interrumpe la huida de un astronauta, catapultando su nave hacia un planeta desconocido.  
El aterrizaje forzoso no sale bien, y una pieza clave de la nave llamada el "**Artefacto**", una gema que alimenta el motor, se pierde en la jungla.  
Tu misión: **sobrevivir, esquivar enemigos, encontrar el Artefacto y salir en una pieza del planeta**. Todo esto mientras criaturas hostiles te acechan en cada rincón.

---

## 🐍 Enemigos
- **Trunk: ![Trunk](https://github.com/Ivnfdzz/Jungle_Quest/blob/d4e3ba1fc01eec9c09a2aeb2d2e165b45276a5fc/src/assets/readme/trunk.png)**  
  Un tronco que dispara rayos láser a intervalos. Ideal para mantenerte en movimiento.
  
- **Rino: ![Rino](https://github.com/Ivnfdzz/Jungle_Quest/blob/d4e3ba1fc01eec9c09a2aeb2d2e165b45276a5fc/src/assets/readme/Rino.png)**  
  Un rinoceronte imparable que embiste de derecha a izquierda arrasando con todo.

*Cada enemigo derrotado sumará una estrella al puntaje*

---

## 🌌 Power-ups
- **Estrella de invulnerabilidad: ![inv_star](https://github.com/Ivnfdzz/Jungle_Quest/blob/d4e3ba1fc01eec9c09a2aeb2d2e165b45276a5fc/src/assets/readme/invulnerability_star.png)**  
  Si la encontrás, la podés usar para volverte invulnerable por unos segundos. Puede marcar la diferencia entre la victoria o el reinicio.

---

## 📺 Ver Gameplay  
¡Mirá *Jungle Quest* en acción! Hace click en este video donde vas a poder ver el gameplay completo y cómo funcionan las mecánicas en vivo.  
[![Ver el gameplay en YouTube](https://img.youtube.com/vi/LDWBX3Gc_dw/0.jpg)](https://www.youtube.com/watch?v=LDWBX3Gc_dw)

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
  Basada en la cantidad de **vidas** del personaje y las **estrellas** conseguidas. Esta puntuación se guarda junto al nombre del jugador para luego poder verla en la sección de leaderboards.
  
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
- **Corrección** de bugs menores
- **Mejora** en la **movilidad** del jugador
- **Mejora** en el sistema de puntuación
- Posible **expansión** con nuevos enemigos, historia o mecánicas

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
pip install -r requirements.txt
```

### 5. Ejecutá el juego:
```
python src/main.py
```
