document.addEventListener('DOMContentLoaded', function() {
    // Toggle Navigation
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    navToggle.addEventListener('click', function() {
        navMenu.classList.toggle('active');
    });

    // Search Functionality
    const searchInput = document.getElementById('search-input');
    const mangaItems = document.querySelectorAll('.manga-item');

    searchInput.addEventListener('input', function() {
        const searchTerm = searchInput.value.toLowerCase();

        mangaItems.forEach(item => {
            const title = item.querySelector('h3').textContent.toLowerCase();
            if (title.includes(searchTerm)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });

    // Form Validation (Example)
    const contactForm = document.querySelector('#contact form');
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const nameInput = contactForm.querySelector('#name');
        const emailInput = contactForm.querySelector('#email');
        const messageInput = contactForm.querySelector('#message');

        if (nameInput.value.trim() === '' || emailInput.value.trim() === '' || messageInput.value.trim() === '') {
            alert('Please fill in all fields.');
            return;
        }

        // Additional validation logic for email format, etc.

        // If all validations pass, you can submit the form via AJAX or perform other actions.
        // For demonstration purposes, you can just log the form data.
        console.log('Name:', nameInput.value);
        console.log('Email:', emailInput.value);
        console.log('Message:', messageInput.value);

        // Reset form fields after submission (optional)
        contactForm.reset();
    });

    // Smooth Scrolling (Example)
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            window.scrollTo({
                top: targetSection.offsetTop - 50,
                behavior: 'smooth'
            });
        });
    });
});
