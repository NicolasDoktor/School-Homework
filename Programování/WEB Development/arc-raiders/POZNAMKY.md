# Poznámky k projektu ARC Raiders

## Co jsem se naučil

Tento projekt mi ukázal, jak vytvořit moderní webovou stránku s několika technologiemi dohromady.

### HTML
- Používání sémantických tagů (`<nav>`, `<section>`, `<footer>`)
- Správná struktura stránky s `<head>` a `<body>`
- Meta tagy pro SEO optimalizaci
- Formuláře s různými input typy

### CSS
- Grid layout pro rozložení obsahu
- Flexbox pro navigaci a karty
- CSS proměnné (custom properties) pro barvy
- Transitions a hover efekty
- Responzivní design s media queries
- Import fontů z Google Fonts

### JavaScript
- DOM manipulace (získávání elementů pomocí `getElementById`)
- Event listeners (klikání, scrollování)
- For cykly pro procházení pole
- Dynamické vytváření HTML obsahu
- String concatenace pro sestavování HTML

### Python (Flask)
- Základní Flask aplikace
- Routing (různé URL adresy)
- JSON data handling
- CORS pro komunikaci s front-endem
- Čtení souborů v Pythonu

## Struktura kódu

### index.html
Hlavní soubor, který obsahuje všechny sekce webu. Používá jednoduchou strukturu:
- Navigace nahoře (sticky)
- Hero sekce s velkým titulkem
- Několik content sekcí
- Formulář
- Footer

### style.css
Všechny styly jsou v jednom souboru pro jednoduchost. Obsahuje:
- Reset stylů (odstranění výchozích margin/padding)
- Font nastavení
- Grid layouty pro sekce
- Hover animace
- Responzivní design pro mobily

### main.js
Základní interaktivity:
- Změna navigace při scrollování
- Mobilní hamburger menu
- Plynulé scrollování
- Animace při objevení sekcí

### data-inline.js
Načítání herních dat:
- Pole objektů s daty tříd a novinek
- Funkce pro vytvoření HTML karet
- Načtení při startu stránky

### app.py (backend)
Jednoduchý Python server:
- API endpointy pro různá data
- Čtení JSON souborů
- Zasílání odpovědí ve formátu JSON

## Důležité koncepty

### One-page web
- Všechen obsah je na jedné stránce
- Navigace scrolluje k sekcím
- Rychlé načítání

### Responsive design
- Web funguje na PC i mobilu
- Media queries pro různé velikosti obrazovek
- Mobilní menu

### Dynamické načítání
- Data nejsou pevně v HTML
- JavaScript vytváří obsah z pole objektů
- Flexibilní a snadno upravitelné

## Co bych mohl vylepšit

- Přidat víc animací
- Použít backend API místo inline dat
- Přidat galerii obrázků
- Vytvořit víc stránek (ne jen one-page)
- Přidat databázi místo JSON souborů

## Užitečné zdroje

- [MDN Web Docs](https://developer.mozilla.org/) - Dokumentace HTML, CSS, JS
- [W3Schools](https://www.w3schools.com/) - Tutoriály a příklady
- [Google Fonts](https://fonts.google.com/) - Zdarma fonty
- [Flask dokumentace](https://flask.palletsprojects.com/) - Python web framework

## Časté problémy a řešení

**Problém:** Data se nenačítají
- **Řešení:** Zkontroluj console v prohlížeči (F12), jestli nejsou chyby

**Problém:** CSS styly nefungují
- **Řešení:** Zkontroluj cestu k CSS souboru v HTML

**Problém:** Mobilní menu se neotevírá
- **Řešení:** Zkontroluj, jestli je správně načtený main.js

**Problém:** Backend API nefunguje
- **Řešení:** Ujisti se, že máš nainstalované Flask (`pip install flask flask-cors`)
