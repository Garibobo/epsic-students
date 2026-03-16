/* ========================================
   INSTALLATIONS ÉLECTRIQUES - JAVASCRIPT
   Créé par Amir Garibovic - 2026
   ======================================== */

// Attendre que le DOM soit chargé
document.addEventListener('DOMContentLoaded', function() {
    
    // Créer la bulle "Merci Denis"
    createTributeBubble();
    
    // Ajouter le bouton retour en haut
    createBackToTop();
    
    // Animations au scroll
    initScrollAnimations();
    
    // Message console
    showWelcomeMessage();
});

// ========================================
// BULLE "MERCI DENIS"
// ========================================
function createTributeBubble() {
    const bubble = document.createElement('div');
    bubble.className = 'tribute-bubble';
    bubble.innerHTML = `
        <a href="https://tchapatch-stack.github.io/installations/" target="_blank" title="Visiter le site original de Denis (DS_de_Mo)">
            Merci Denis
        </a>
    `;
    
    // Ajouter les styles inline
    const style = document.createElement('style');
    style.textContent = `
        .tribute-bubble {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1000;
            animation: floatBubble 3s ease-in-out infinite;
        }
        
        .tribute-bubble a {
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            color: #333;
            padding: 15px 25px;
            border-radius: 50px;
            box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
            text-decoration: none;
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            font-weight: 600;
            border: 3px solid #FFD700;
            transition: all 0.3s ease;
        }
        
        .tribute-bubble a:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(255, 215, 0, 0.6);
            background: linear-gradient(135deg, #FFA500 0%, #FFD700 100%);
        }
        
        @keyframes floatBubble {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        
        @media (max-width: 768px) {
            .tribute-bubble {
                top: 10px;
                left: 10px;
            }
            .tribute-bubble a {
                padding: 12px 20px;
                font-size: 14px;
            }
        }
    `;
    
    document.head.appendChild(style);
    document.body.appendChild(bubble);
    
    console.log('✨ Bulle "Merci Denis" créée avec lien vers site original !');
}

// ========================================
// BOUTON RETOUR EN HAUT
// ========================================
function createBackToTop() {
    const button = document.createElement('button');
    button.className = 'back-to-top';
    button.innerHTML = '↑';
    button.setAttribute('aria-label', 'Retour en haut');
    
    // Styles
    const style = document.createElement('style');
    style.textContent = `
        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #0066CC, #0099FF);
            color: white;
            border: none;
            border-radius: 50%;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 102, 204, 0.3);
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 999;
        }
        
        .back-to-top.visible {
            opacity: 1;
            visibility: visible;
        }
        
        .back-to-top:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(0, 102, 204, 0.4);
        }
        
        @media (max-width: 768px) {
            .back-to-top {
                bottom: 20px;
                right: 20px;
                width: 45px;
                height: 45px;
                font-size: 20px;
            }
        }
    `;
    
    document.head.appendChild(style);
    document.body.appendChild(button);
    
    // Afficher/masquer selon le scroll
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            button.classList.add('visible');
        } else {
            button.classList.remove('visible');
        }
    });
    
    // Retour en haut au clic
    button.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ========================================
// ANIMATIONS AU SCROLL
// ========================================
function initScrollAnimations() {
    const sections = document.querySelectorAll('.content-section');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1
    });
    
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
}

// ========================================
// MESSAGE DE BIENVENUE
// ========================================
function showWelcomeMessage() {
    console.log('%c⚡ INSTALLATIONS ÉLECTRIQUES', 'color: #0066CC; font-size: 24px; font-weight: bold;');
    console.log('%c━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', 'color: #0099FF;');
    console.log('%c✨ Site modernisé par Amir Garibovic - 2026', 'color: #0066CC; font-size: 14px;');
    console.log('%c❤️  Basé sur le travail original de Denis (DS_de_Mo)', 'color: #FFD700; font-size: 14px;');
    console.log('%c📚 Site original accessible via la bulle "Merci Denis"', 'color: #0066CC; font-size: 14px;');
    console.log('%c━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', 'color: #0099FF;');
}

// ========================================
// SMOOTH SCROLL POUR LES LIENS D'ANCRAGE
// ========================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
