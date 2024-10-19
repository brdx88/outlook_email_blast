// script.js
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// // This script will handle the background hover effect
// document.body.addEventListener('mousemove', function(e) {
//     const x = e.clientX;
//     const y = e.clientY;
//     const lightSize = 200; // radius size of the light effect
//     const gradientX = (x / window.innerWidth) * 100;
//     const gradientY = (y / window.innerHeight) * 100;
    
//     document.body.style.background = `radial-gradient(circle at ${gradientX}% ${gradientY}%, rgba(17, 34, 64, 0.3), #0a192f ${lightSize}px)`;
// });

// JavaScript to add 'sticky-active' class to section headers when they stick
document.addEventListener("scroll", function() {
    const sections = document.querySelectorAll('.section-header');
    
    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 0 && rect.bottom >= 0) {
            section.classList.add('sticky-active');
        } else {
            section.classList.remove('sticky-active');
        }
    });
});

// // Open modal function
// function openModal(modalId) {
//     document.getElementById(modalId).style.display = "block";
// }

// // Close modal function
// function closeModal(modalId) {
//     document.getElementById(modalId).style.display = "none";
// }

document.querySelectorAll('.custom-link').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelector('.custom-link.active')?.classList.remove('active');
        this.classList.add('active');
    });
});

// JavaScript to highlight the nav when a section is in view
// Select all sections and navigation links
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.custom-link');

// Set up Intersection Observer
const observerOptions = {
    threshold: 0.6  // 60% of the section must be visible
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const currentSection = entry.target.id;

            // Remove 'active' class from all nav links
            navLinks.forEach(link => {
                link.classList.remove('active');
            });

            // Add 'active' class to the nav link corresponding to the visible section
            const activeLink = document.querySelector(`.custom-link[href="#${currentSection}"]`);
            activeLink.classList.add('active');
        }
    });
}, observerOptions);

// Observe each section
sections.forEach(section => {
    observer.observe(section);
});

