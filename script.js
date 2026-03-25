document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Mobile menu toggle logic
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            if (navLinks.style.display === 'flex') {
                navLinks.style.display = 'none';
            } else {
                navLinks.style.display = 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '70px';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.background = '#121212';
                navLinks.style.padding = '20px';
                navLinks.style.gap = '20px';
                navLinks.style.textAlign = 'center';
            }
        });
    }

    // Scroll reveal animation for sections
    const observerOptions = { threshold: 0.1 };
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.feature-card, .intro-text, .intro-visual, .contact-form-container').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s ease-out';
        observer.observe(el);
    });

    // ─── STAT COUNTER ANIMATION ───────────────────────────────────────────────
    function animateCounter(el) {
        const targetAttr = el.getAttribute('data-target');
        const target = parseFloat(targetAttr);
        const duration = 1800;
        const step = target / (duration / 16);
        let current = 0;
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            const decimalPlaces = target % 1 !== 0 ? 1 : 0;
            el.textContent = current.toLocaleString(undefined, { 
                minimumFractionDigits: decimalPlaces,
                maximumFractionDigits: decimalPlaces 
            });
        }, 16);
    }

    const statObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                statObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    document.querySelectorAll('.stat-number').forEach(el => statObserver.observe(el));

    // ─── AUCTION COUNTDOWN TIMERS ─────────────────────────────────────────────
    function getCountdownString(endDateStr) {
        const end = new Date(endDateStr).getTime();
        const now = new Date().getTime();
        const diff = end - now;
        if (diff <= 0) return 'Ended';
        const d = Math.floor(diff / (1000 * 60 * 60 * 24));
        const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const s = Math.floor((diff % (1000 * 60)) / 1000);
        if (d > 0) return `${d}d ${h}h ${m}m`;
        return `${h}h ${m}m ${s}s`;
    }

    function updateTimers() {
        document.querySelectorAll('.auction-card__timer[data-end]').forEach(el => {
            el.textContent = getCountdownString(el.getAttribute('data-end'));
        });
    }

    updateTimers();
    setInterval(updateTimers, 1000);
});

// ─── FAQ ACCORDION ────────────────────────────────────────────────────────────
function toggleFaq(btn) {
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    // Close all open items
    document.querySelectorAll('.faq-item.open').forEach(openItem => {
        openItem.classList.remove('open');
    });
    // Open clicked item if it was closed
    if (!isOpen) {
        item.classList.add('open');
    }
}

