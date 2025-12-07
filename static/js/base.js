// static/js/base.js

// Mobile menu toggle
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        menuToggle.classList.toggle('active');
    });
}

// Close flash messages
document.querySelectorAll('.flash-close').forEach(button => {
    button.addEventListener('click', function() {
        this.closest('.flash-message').style.display = 'none';
    });
});

// Auto-hide flash messages after 5 seconds
setTimeout(() => {
    document.querySelectorAll('.flash-message').forEach(message => {
        message.style.opacity = '0';
        message.style.transform = 'translateY(-10px)';
        setTimeout(() => message.style.display = 'none', 300);
    });
}, 5000);