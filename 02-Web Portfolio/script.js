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
