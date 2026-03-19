// Scroll reveal animation using Intersection Observer
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.content-reveal').forEach(el => {
  observer.observe(el);
});

// Add revealed class style to CSS dynamically for simplicity (could be in style.css too)
const style = document.createElement('style');
style.textContent = `
  .content-reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .content-reveal.revealed {
    opacity: 1;
    transform: translateY(0);
  }
`;
document.head.appendChild(style);

console.log("Sruthi's portfolio initialized! ✨");
