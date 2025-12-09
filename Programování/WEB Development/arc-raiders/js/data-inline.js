// ============================================
// INLINE DATA - Pro použití bez serveru
// ============================================

const INLINE_CLASSES = [
    {
        "id": 1,
        "name": "Assault",
        "description": "Heavy frontline warrior specialized in direct combat. Equipped with advanced armor and powerful weapons, the Assault class excels at taking and dealing massive damage in close to medium range engagements.",
        "image": "images/assault-class.png",
        "role": "Tank/DPS",
        "difficulty": "Medium",
        "abilities": [
            "Heavy Armor Plating",
            "Suppressive Fire",
            "Combat Shield",
            "Adrenaline Rush"
        ],
        "stats": {
            "health": 95,
            "damage": 85,
            "mobility": 60,
            "utility": 70
        }
    },
    {
        "id": 2,
        "name": "Scout",
        "description": "Agile reconnaissance specialist with superior mobility and precision. Masters of long-range combat and stealth tactics, Scouts provide critical intelligence and eliminate high-value targets from distance.",
        "image": "images/scout-class.png",
        "role": "DPS/Recon",
        "difficulty": "Hard",
        "abilities": [
            "Active Camouflage",
            "Precision Shot",
            "Motion Tracker",
            "Quick Escape"
        ],
        "stats": {
            "health": 65,
            "damage": 90,
            "mobility": 95,
            "utility": 75
        }
    },
    {
        "id": 3,
        "name": "Support",
        "description": "Vital team member focused on healing and tactical support. Equipped with advanced medical technology and defensive systems, Support class keeps the team alive and operational in the harshest conditions.",
        "image": "images/support-class.png",
        "role": "Healer/Support",
        "difficulty": "Easy",
        "abilities": [
            "Healing Field",
            "Shield Generator",
            "Ammo Supply",
            "Revive Beacon"
        ],
        "stats": {
            "health": 75,
            "damage": 60,
            "mobility": 70,
            "utility": 95
        }
    },
    {
        "id": 4,
        "name": "Engineer",
        "description": "Technical specialist capable of deploying automated defenses and hacking enemy systems. Engineers control the battlefield through strategic placement of turrets, traps, and electronic warfare.",
        "image": "images/assault-class.png",
        "role": "Support/Control",
        "difficulty": "Medium",
        "abilities": [
            "Auto-Turret Deploy",
            "EMP Blast",
            "Repair Drone",
            "Fortify Position"
        ],
        "stats": {
            "health": 70,
            "damage": 75,
            "mobility": 65,
            "utility": 90
        }
    }
];

const INLINE_NEWS = [
    {
        "id": 1,
        "date": "2025-12-05",
        "title": "Major Update 2.0 - New Class System",
        "category": "Update",
        "excerpt": "Introducing the completely revamped class system with four distinct playstyles. Each class now features unique abilities, customizable loadouts, and specialized skill trees. Balance changes across all weapons and equipment."
    },
    {
        "id": 2,
        "date": "2025-11-28",
        "title": "Patch Notes 1.8.5 - Performance Improvements",
        "category": "Patch",
        "excerpt": "Significant performance optimizations reducing loading times by 40%. Fixed critical bugs affecting multiplayer stability. Improved AI behavior for robotic enemies. Various quality-of-life improvements based on community feedback."
    },
    {
        "id": 3,
        "date": "2025-11-20",
        "title": "New Map: Industrial Wasteland",
        "category": "Content",
        "excerpt": "Explore the ruins of a massive industrial complex overrun by hostile machines. Features vertical gameplay, destructible environments, and new mission types. Available now for all players."
    },
    {
        "id": 4,
        "date": "2025-11-15",
        "title": "Community Event: Robot Uprising",
        "category": "Event",
        "excerpt": "Join forces with players worldwide in our biggest community event yet. Defend key locations against waves of increasingly difficult robotic enemies. Exclusive rewards for top performers and participants."
    },
    {
        "id": 5,
        "date": "2025-11-08",
        "title": "Developer Diary: The Future of ARC Raiders",
        "category": "News",
        "excerpt": "Our development team shares insights into upcoming features, including new enemy types, expanded crafting system, and the highly anticipated PvPvE mode. Plus a sneak peek at Year 2 content roadmap."
    },
    {
        "id": 6,
        "date": "2025-11-01",
        "title": "Weapon Balance Update",
        "category": "Patch",
        "excerpt": "Comprehensive weapon balance pass addressing community concerns. Assault rifles buffed, sniper rifles adjusted for better long-range viability. Full patch notes available on our official forums."
    }
];

// ============================================
// DATA LOADING - Použije inline data
// ============================================

/**
 * Load and render character classes
 */
function loadClasses() {
    const classesGrid = document.getElementById('classesGrid');

    try {
        const classes = INLINE_CLASSES;

        classesGrid.innerHTML = classes.map(classData => `
            <div class="class-card reveal">
                <img src="${classData.image}" alt="${classData.name}" class="class-image">
                <div class="class-info">
                    <h3 class="class-name">${classData.name}</h3>
                    <p class="class-description">${classData.description}</p>
                    
                    <div class="class-stats">
                        <span class="stat-badge">Role: ${classData.role}</span>
                        <span class="stat-badge">Obtížnost: ${classData.difficulty}</span>
                    </div>
                    
                    <div class="mt-1">
                        <strong style="color: var(--color-accent-cyan);">Schopnosti:</strong>
                        <ul style="margin-top: 0.5rem; padding-left: 1.5rem; color: var(--color-text-secondary);">
                            ${classData.abilities.map(ability => `<li>${ability}</li>`).join('')}
                        </ul>
                    </div>
                    
                    <div class="mt-1">
                        <strong style="color: var(--color-accent-cyan);">Statistiky:</strong>
                        <div style="margin-top: 0.5rem;">
                            ${renderStatBar('Health', classData.stats.health)}
                            ${renderStatBar('Damage', classData.stats.damage)}
                            ${renderStatBar('Mobility', classData.stats.mobility)}
                            ${renderStatBar('Utility', classData.stats.utility)}
                        </div>
                    </div>
                </div>
            </div>
        `).join('');

        // Trigger reveal animations
        setTimeout(revealElements, 100);

    } catch (error) {
        console.error('Error loading classes:', error);
        classesGrid.innerHTML = '<p class="text-center">Chyba při načítání tříd.</p>';
    }
}

/**
 * Render a stat bar
 * @param {string} label - Stat label
 * @param {number} value - Stat value (0-100)
 * @returns {string} - HTML for stat bar
 */
function renderStatBar(label, value) {
    return `
        <div style="margin-bottom: 0.5rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                <span style="font-size: 0.9rem; color: var(--color-text-muted);">${label}</span>
                <span style="font-size: 0.9rem; color: var(--color-accent-cyan);">${value}</span>
            </div>
            <div style="width: 100%; height: 6px; background: var(--color-bg-tertiary); border-radius: 3px; overflow: hidden;">
                <div style="width: ${value}%; height: 100%; background: var(--gradient-primary); transition: width 1s ease;"></div>
            </div>
        </div>
    `;
}

/**
 * Load and render news articles
 */
function loadNews() {
    const newsGrid = document.getElementById('newsGrid');

    try {
        const news = INLINE_NEWS;

        newsGrid.innerHTML = news.map(article => `
            <div class="news-card reveal">
                <p class="news-date">${formatDate(article.date)} • ${article.category}</p>
                <h3 class="news-title">${article.title}</h3>
                <p class="news-excerpt">${article.excerpt}</p>
            </div>
        `).join('');

        // Trigger reveal animations
        setTimeout(revealElements, 100);

    } catch (error) {
        console.error('Error loading news:', error);
        newsGrid.innerHTML = '<p class="text-center">Chyba při načítání novinek.</p>';
    }
}

/**
 * Format date to Czech locale
 * @param {string} dateString - ISO date string
 * @returns {string} - Formatted date
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('cs-CZ', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

/**
 * Reveal elements with scroll animation
 */
function revealElements() {
    const reveals = document.querySelectorAll('.reveal');

    reveals.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;

        if (elementTop < window.innerHeight - elementVisible) {
            element.classList.add('active');
        }
    });
}

/**
 * Submit contact form
 * @param {Event} event - Form submit event
 */
function submitContactForm(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    console.log('Form submitted:', data);

    // Show success message
    alert('Zpráva byla odeslána (demo režim).\n\nOdeslaná data:\n' + JSON.stringify(data, null, 2));
    form.reset();
}

// ============================================
// INITIALIZATION
// ============================================

// Load data when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 Loading ARC Raiders data...');
    loadClasses();
    loadNews();

    // Setup contact form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', submitContactForm);
    }

    console.log('✅ Data loaded successfully!');
});
