const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login')

if (registerBtn && container) {
  registerBtn.addEventListener('click', () =>{
      container.classList.add("active");
  });
}

if (loginBtn && container) {
  loginBtn.addEventListener('click', () =>{
      container.classList.remove("active");
  });
}

// Interacciones para Base2.html

document.addEventListener('DOMContentLoaded', () => {
  // Tema: init + toggle
  const root = document.documentElement;
  function applyTheme(theme) {
    root.dataset.theme = theme;
    try { localStorage.setItem('theme', theme); } catch {}
    const btn = document.getElementById('themeToggle');
    if (btn) btn.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
  }
  let saved = null;
  try { saved = localStorage.getItem('theme'); } catch {}
  if (!saved) saved = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  applyTheme(saved);
  const themeBtn = document.getElementById('themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const next = (root.dataset.theme === 'dark') ? 'light' : 'dark';
      applyTheme(next);
    });
  }

  // Filtrado por texto
  const searchInput = document.getElementById('searchInput');
  const cards = Array.from(document.querySelectorAll('.faculties-grid a'));
  function filterCards() {
    const q = (searchInput?.value || '').toLowerCase().trim();
    cards.forEach(card => {
      const title = (card.querySelector('h3')?.textContent || '').toLowerCase();
      const match = title.includes(q);
      card.hidden = !match;
    });
  }
  if (searchInput) searchInput.addEventListener('input', filterCards);

  // Reveal on scroll
  const prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!prefersReduced && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    cards.forEach(card => {
      card.classList.add('reveal');
      io.observe(card);
    });
  } else {
    cards.forEach(card => card.classList.add('visible'));
  }

  // Botón “Subir”
  const backToTop = document.getElementById('backToTop');
  function onScroll() {
    if (!backToTop) return;
    if (window.scrollY > 300) backToTop.classList.add('show');
    else backToTop.classList.remove('show');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  if (backToTop) {
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
  onScroll();
});