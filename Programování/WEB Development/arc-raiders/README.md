# ARC Raiders - Web Presentation

Moderní webová prezentace zaměřená na hru ARC Raiders. One-page web s futuristickým designem, dynamickým načítáním obsahu a responzivním layoutem.

## 🎮 O Projektu

Webová stránka představuje hru ARC Raiders - futuristickou kooperativní akci odehrávající se v postapokalyptickém světě napadeném roboty. Stránka obsahuje informace o hře, herních mechanikách, třídách, zbraních a aktuálních novinkách.

## 🚀 Technologie

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python (Flask)
- **Data**: JSON
- **AJAX**: Dynamické načítání obsahu
- **Design**: Futuristická sci-fi estetika s glassmorphism efekty

## 📁 Struktura Projektu

```
arc-raiders/
├── index.html              # Hlavní HTML soubor
├── css/
│   └── style.css          # Design systém a styly
├── js/
│   ├── main.js            # Hlavní JavaScript funkce
│   └── ajax.js            # AJAX načítání dat
├── data/
│   ├── classes.json       # Data herních tříd
│   ├── weapons.json       # Data zbraní a vybavení
│   └── news.json          # Novinky a aktualizace
├── images/                # Obrázky a grafika
├── backend/
│   ├── app.py            # Flask server
│   └── requirements.txt  # Python závislosti
└── README.md
```

## 🎨 Funkce

- ✨ **Futuristický design** s gradientami a animacemi
- 📱 **Plně responzivní** pro všechna zařízení
- 🔄 **Dynamické načítání** obsahu přes AJAX
- 🎯 **Smooth scrolling** navigace
- 💫 **Scroll reveal** animace
- 📝 **Kontaktní formulář** s validací
- 🎮 **Easter egg** (zkuste Konami kód!)

## 🛠️ Instalace a Spuštění

### Varianta 1: Pouze Frontend (bez backendu)

Stačí otevřít `index.html` v prohlížeči. Data se načtou z lokálních JSON souborů.

### Varianta 2: S Python Backendem

1. **Instalace Python závislostí:**
```bash
cd backend
pip install -r requirements.txt
```

2. **Spuštění serveru:**
```bash
python app.py
```

3. **Otevření v prohlížeči:**
```
http://localhost:5000
```

4. **Změna režimu v ajax.js:**
V souboru `js/ajax.js` změňte:
```javascript
const USE_LOCAL_FILES = false;
```

## 📡 API Endpointy

- `GET /api/classes` - Získat všechny třídy
- `GET /api/classes/<id>` - Získat konkrétní třídu
- `GET /api/weapons` - Získat všechny zbraně
- `GET /api/weapons/<id>` - Získat konkrétní zbraň
- `GET /api/news` - Získat novinky
- `GET /api/news/<id>` - Získat konkrétní novinku
- `POST /api/contact` - Odeslat kontaktní formulář
- `GET /api/stats` - Získat statistiky

## 🎯 Obsahové Sekce

1. **Hero** - Úvodní sekce s call-to-action
2. **O hře** - Představení světa a příběhu
3. **Herní mechaniky** - Popis gameplay prvků
4. **Třídy** - Dynamicky načítané herní třídy
5. **Novinky** - Aktualizace a patch notes
6. **Kontakt** - Formulář a odkazy na komunitu

## 🎨 Design Systém

### Barevná Paleta
- **Primární pozadí**: `#0a0e17`
- **Sekundární pozadí**: `#111827`
- **Accent Cyan**: `#00d9ff`
- **Accent Orange**: `#ff6b35`
- **Accent Purple**: `#a855f7`

### Typografie
- **Nadpisy**: Orbitron (Google Fonts)
- **Tělo textu**: Rajdhani (Google Fonts)

### Efekty
- Glassmorphism
- Gradient overlays
- Smooth transitions
- Hover animations
- Scroll reveal

## 📱 Responzivita

Stránka je optimalizována pro:
- 🖥️ Desktop (1920px+)
- 💻 Laptop (1024px - 1919px)
- 📱 Tablet (768px - 1023px)
- 📱 Mobile (320px - 767px)

## 🔧 Customizace

### Změna barev
Upravte CSS proměnné v `css/style.css`:
```css
:root {
  --color-accent-cyan: #00d9ff;
  --color-accent-orange: #ff6b35;
  /* ... další barvy */
}
```

### Přidání nového obsahu
Upravte JSON soubory v složce `data/`:
- `classes.json` - Přidat novou třídu
- `weapons.json` - Přidat novou zbraň
- `news.json` - Přidat novinku

## 🐛 Známé Problémy

- Backend vyžaduje Python 3.8+
- CORS může způsobit problémy při lokálním testování (použijte backend nebo Live Server)

## 📝 Licence

Školní projekt - volně použitelné pro vzdělávací účely.

## 👨‍💻 Autor

Vytvořeno jako školní projekt pro předmět Webový vývoj.

## 🎮 Easter Egg

Zkuste zadat Konami kód na klávesnici: ↑ ↑ ↓ ↓ ← → ← → B A

---

**Vytvořeno s ❤️ pro fanoušky ARC Raiders**
