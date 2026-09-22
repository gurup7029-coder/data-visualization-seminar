/* ==========================================================================
   INTERACTIVE DATA VISUALIZATION SEMINAR - SLIDE PRESENTATION JAVASCRIPT
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initPageTransitions();
  initCustomCursor();
  initBackgroundCanvas();
  initSlideDeckNavigation();
  initCommandPalette();
  initThemeToggle();
  initCodeBlocks();
  initInteractiveCharts();
});

/* --------------------------------------------------------------------------
   1. PAGE TRANSITION OVERLAY SYSTEM
   -------------------------------------------------------------------------- */
function initPageTransitions() {
  const overlay = document.createElement('div');
  overlay.className = 'page-transition-overlay';
  document.body.appendChild(overlay);

  document.querySelectorAll('a').forEach(link => {
    const href = link.getAttribute('href');
    if (href && !href.startsWith('#') && !href.startsWith('http') && !link.hasAttribute('download')) {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        overlay.classList.add('active');
        setTimeout(() => {
          window.location.href = href;
        }, 120);
      });
    }
  });
}

/* --------------------------------------------------------------------------
   2. ENHANCED TOPIC-SPECIFIC CUSTOM MAGNETIC CURSOR
   -------------------------------------------------------------------------- */
function initCustomCursor() {
  const dot = document.createElement('div');
  dot.className = 'custom-cursor-dot';
  const circle = document.createElement('div');
  circle.className = 'custom-cursor-circle';
  document.body.appendChild(dot);
  document.body.appendChild(circle);

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let circleX = mouseX;
  let circleY = mouseY;

  // Detect topic accent color for cursor
  const pagePath = window.location.pathname;
  if (pagePath.includes('3d-plotting')) {
    document.documentElement.style.setProperty('--cursor-color', '#7c3aed');
    document.documentElement.style.setProperty('--cursor-glow', 'rgba(124, 58, 237, 0.2)');
  } else if (pagePath.includes('basemap')) {
    document.documentElement.style.setProperty('--cursor-color', '#0d9488');
    document.documentElement.style.setProperty('--cursor-glow', 'rgba(13, 148, 136, 0.2)');
  } else if (pagePath.includes('seaborn')) {
    document.documentElement.style.setProperty('--cursor-color', '#e11d48');
    document.documentElement.style.setProperty('--cursor-glow', 'rgba(225, 29, 72, 0.2)');
  } else if (pagePath.includes('reference')) {
    document.documentElement.style.setProperty('--cursor-color', '#d97706');
    document.documentElement.style.setProperty('--cursor-glow', 'rgba(217, 119, 6, 0.2)');
  } else if (pagePath.includes('quiz')) {
    document.documentElement.style.setProperty('--cursor-color', '#10b981');
    document.documentElement.style.setProperty('--cursor-glow', 'rgba(16, 185, 129, 0.25)');
  } else {
    document.documentElement.style.setProperty('--cursor-color', '#2563eb');
    document.documentElement.style.setProperty('--cursor-glow', 'rgba(37, 99, 235, 0.2)');
  }

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.transform = `translate(${mouseX}px, ${mouseY}px)`;
  });

  function renderCursor() {
    circleX += (mouseX - circleX) * 0.18;
    circleY += (mouseY - circleY) * 0.18;
    circle.style.transform = `translate(${circleX}px, ${circleY}px)`;
    requestAnimationFrame(renderCursor);
  }
  requestAnimationFrame(renderCursor);

  const interactiveSelectors = 'a, button, input, select, .slide-btn, .slide-dot, .interactive-card, .btn-icon, .control-btn';
  document.addEventListener('mouseover', (e) => {
    if (e.target.closest(interactiveSelectors)) {
      document.body.classList.add('hovering-interactive');
    } else if (e.target.closest('.code-container') || e.target.closest('.colab-execution-cell')) {
      document.body.classList.add('hovering-code');
    }
  });

  document.addEventListener('mouseout', (e) => {
    if (e.target.closest(interactiveSelectors)) {
      document.body.classList.remove('hovering-interactive');
    } else if (e.target.closest('.code-container') || e.target.closest('.colab-execution-cell')) {
      document.body.classList.remove('hovering-code');
    }
  });
}

/* --------------------------------------------------------------------------
   3. UNIQUE ANIMATED BACKGROUND CANVAS PER PAGE / TOPIC
   -------------------------------------------------------------------------- */
let canvasMode = 'hero';

function initBackgroundCanvas() {
  const canvas = document.getElementById('bgCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let width, height;

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  const pagePath = window.location.pathname;
  if (pagePath.includes('3d-plotting')) canvasMode = '3d';
  else if (pagePath.includes('basemap')) canvasMode = 'basemap';
  else if (pagePath.includes('seaborn')) canvasMode = 'seaborn';
  else if (pagePath.includes('reference')) canvasMode = 'reference';
  else canvasMode = 'hero';

  // Hero Constellation Particles
  const heroParticles = Array.from({ length: 45 }, () => ({
    x: Math.random() * window.innerWidth,
    y: Math.random() * window.innerHeight,
    vx: (Math.random() - 0.5) * 0.8,
    vy: (Math.random() - 0.5) * 0.8,
    radius: Math.random() * 2 + 1
  }));

  // Reference Matrix Nodes
  const refNodes = Array.from({ length: 30 }, () => ({
    x: Math.random() * window.innerWidth,
    y: Math.random() * window.innerHeight,
    size: Math.random() * 4 + 2,
    alpha: Math.random()
  }));

  let time = 0;

  function animate() {
    ctx.clearRect(0, 0, width, height);
    time += 0.015;

    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

    if (canvasMode === 'hero') {
      // 1. HOME / LANDING: Interactive Constellation Particle Mesh
      ctx.strokeStyle = isDark ? 'rgba(59, 130, 246, 0.15)' : 'rgba(37, 99, 235, 0.12)';
      ctx.fillStyle = isDark ? 'rgba(59, 130, 246, 0.4)' : 'rgba(37, 99, 235, 0.3)';

      heroParticles.forEach((p, i) => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0 || p.x > width) p.vx *= -1;
        if (p.y < 0 || p.y > height) p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();

        for (let j = i + 1; j < heroParticles.length; j++) {
          const p2 = heroParticles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 130) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      });
    } else if (canvasMode === '3d') {
      // 2. 3D PLOTTING: Rotating 3D Wireframe Hyper-Cube & Sine Mesh Grid
      ctx.strokeStyle = isDark ? 'rgba(124, 58, 237, 0.25)' : 'rgba(124, 58, 237, 0.18)';
      ctx.lineWidth = 1;

      const gridSize = 30;
      const rows = 16;
      const cols = 22;
      const startX = width / 2 - (cols * gridSize) / 2;
      const startY = height / 2 - 40;

      for (let r = 0; r < rows; r++) {
        ctx.beginPath();
        for (let c = 0; c < cols; c++) {
          const x = startX + c * gridSize;
          const dist = Math.sqrt(Math.pow(c - cols / 2, 2) + Math.pow(r - rows / 2, 2));
          const z = Math.sin(dist * 0.4 - time) * 22;
          const y = startY + r * gridSize + z;
          if (c === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
      }
    } else if (canvasMode === 'basemap') {
      // 3. BASEMAP: Geodesic Latitude/Longitude Coordinate Grid & City Beacons
      ctx.strokeStyle = isDark ? 'rgba(13, 148, 136, 0.25)' : 'rgba(13, 148, 136, 0.18)';
      ctx.lineWidth = 1;
      const cx = width / 2;
      const cy = height / 2;
      const radius = Math.min(width, height) * 0.38;

      ctx.beginPath();
      ctx.arc(cx, cy, radius, 0, Math.PI * 2);
      ctx.stroke();

      for (let i = -60; i <= 60; i += 20) {
        ctx.beginPath();
        const y = cy + (i / 90) * radius;
        const rx = Math.sqrt(Math.max(0, radius * radius - Math.pow((i / 90) * radius, 2)));
        ctx.ellipse(cx, y, rx, rx * (0.2 + 0.1 * Math.sin(time)), 0, 0, Math.PI * 2);
        ctx.stroke();
      }
    } else if (canvasMode === 'seaborn') {
      // 4. SEABORN: Flowing Gaussian KDE Smooth Density Curves
      ctx.lineWidth = 2.5;
      for (let w = 0; w < 3; w++) {
        ctx.strokeStyle = w % 2 === 0
          ? (isDark ? 'rgba(225, 29, 72, 0.2)' : 'rgba(225, 29, 72, 0.15)')
          : (isDark ? 'rgba(217, 119, 6, 0.2)' : 'rgba(217, 119, 6, 0.15)');
        ctx.beginPath();
        for (let x = 0; x < width; x += 20) {
          const y = height * 0.65 + Math.sin(x * 0.004 + time + w) * 55 + Math.cos(x * 0.002 - time * 0.4) * 35;
          if (x === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
      }
    } else if (canvasMode === 'reference') {
      // 5. REFERENCE: Dynamic Digital Data Matrix Nodes
      ctx.fillStyle = isDark ? 'rgba(217, 119, 6, 0.3)' : 'rgba(217, 119, 6, 0.2)';
      refNodes.forEach(node => {
        node.alpha += 0.02;
        ctx.globalAlpha = (Math.sin(node.alpha) + 1) / 2 * 0.4 + 0.1;
        ctx.fillRect(node.x, node.y, node.size, node.size);
      });
      ctx.globalAlpha = 1.0;
    }

    requestAnimationFrame(animate);
  }

  animate();
}

/* --------------------------------------------------------------------------
   4. PRESENTATION SLIDE DECK NAVIGATION
   -------------------------------------------------------------------------- */
let currentSlideIndex = 0;
let totalSlides = 0;
let slideSections = [];

function initSlideDeckNavigation() {
  slideSections = Array.from(document.querySelectorAll('.slide-section'));
  totalSlides = slideSections.length;
  if (totalSlides === 0) return;

  const progressFill = document.querySelector('.top-progress-fill');
  const slideIndicator = document.querySelector('.slide-indicator');
  const prevBtn = document.querySelector('.slide-btn-prev');
  const nextBtn = document.querySelector('.slide-btn-next');
  const slideDotsContainer = document.querySelector('.slide-dots');

  if (slideDotsContainer) {
    slideDotsContainer.innerHTML = '';
    slideSections.forEach((_, idx) => {
      const dot = document.createElement('div');
      dot.className = `slide-dot ${idx === 0 ? 'active' : ''}`;
      dot.addEventListener('click', () => goToSlide(idx));
      slideDotsContainer.appendChild(dot);
    });
  }

  function launchFireworksConfetti() {
    let canvas = document.getElementById('confettiCanvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'confettiCanvas';
      canvas.style.position = 'fixed';
      canvas.style.top = '0';
      canvas.style.left = '0';
      canvas.style.width = '100vw';
      canvas.style.height = '100vh';
      canvas.style.pointerEvents = 'none';
      canvas.style.zIndex = '99999';
      document.body.appendChild(canvas);
    }

    const ctx = canvas.getContext('2d');
    const width = canvas.width = window.innerWidth;
    const height = canvas.height = window.innerHeight;

    const particles = [];
    const colors = ['#2563eb', '#7c3aed', '#0d9488', '#d97706', '#e11d48', '#10b981', '#f59e0b', '#ec4899', '#3b82f6'];

    const burstPoints = [
      { x: width * 0.2, y: height * 0.4 },
      { x: width * 0.5, y: height * 0.3 },
      { x: width * 0.8, y: height * 0.4 },
      { x: width * 0.35, y: height * 0.25 },
      { x: width * 0.65, y: height * 0.25 }
    ];

    burstPoints.forEach(pt => {
      for (let i = 0; i < 70; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 14 + 4;
        particles.push({
          x: pt.x,
          y: pt.y,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - Math.random() * 5,
          size: Math.random() * 9 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          rSpeed: (Math.random() - 0.5) * 16,
          gravity: 0.22,
          alpha: 1.0,
          decay: Math.random() * 0.014 + 0.007,
          shape: Math.random() > 0.35 ? 'rect' : 'circle'
        });
      }
    });

    const startTime = performance.now();

    function renderConfetti(now) {
      const elapsed = now - startTime;
      ctx.clearRect(0, 0, width, height);

      let activeCount = 0;
      particles.forEach(p => {
        if (p.alpha <= 0) return;
        activeCount++;

        p.x += p.vx;
        p.y += p.vy;
        p.vy += p.gravity;
        p.vx *= 0.98;
        p.rotation += p.rSpeed;
        p.alpha -= p.decay;

        ctx.save();
        ctx.globalAlpha = Math.max(0, p.alpha);
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.fillStyle = p.color;

        if (p.shape === 'rect') {
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 1.6);
        } else {
          ctx.beginPath();
          ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.restore();
      });

      if (activeCount > 0 && elapsed < 4500) {
        requestAnimationFrame(renderConfetti);
      } else {
        if (canvas && canvas.parentNode) canvas.parentNode.removeChild(canvas);
      }
    }

    requestAnimationFrame(renderConfetti);
  }

  function updateSlideState() {
    slideSections.forEach((slide, idx) => {
      if (idx === currentSlideIndex) {
        slide.style.display = 'flex';
        setTimeout(() => slide.classList.add('active'), 20);

        // Lazy-initialize interactive charts only for the active slide
        initChartForActiveSlide(slide);

        // Trigger Crackers Confetti Blast ONLY on the final Thank You slide
        const titleText = slide.querySelector('.slide-title')?.textContent.toLowerCase() || '';
        const isThankYouSlide = titleText.includes('thank you') || (slide.id === 'slide-8' && window.location.pathname.includes('seaborn'));
        if (isThankYouSlide) {
          setTimeout(launchFireworksConfetti, 100);
        }
      } else {
        slide.classList.remove('active');
        slide.style.display = 'none';
      }
    });

    if (progressFill) {
      const percent = ((currentSlideIndex + 1) / totalSlides) * 100;
      progressFill.style.width = `${percent}%`;
    }

    if (slideIndicator) {
      slideIndicator.textContent = `Slide ${String(currentSlideIndex + 1).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
    }

    if (prevBtn) prevBtn.disabled = currentSlideIndex === 0;
    if (nextBtn) nextBtn.disabled = currentSlideIndex === totalSlides - 1;

    const dots = document.querySelectorAll('.slide-dot');
    dots.forEach((d, idx) => {
      d.classList.toggle('active', idx === currentSlideIndex);
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function goToSlide(index) {
    if (index >= 0 && index < totalSlides) {
      currentSlideIndex = index;
      updateSlideState();
    }
  }
  window.goToSlide = goToSlide;

  if (prevBtn) prevBtn.addEventListener('click', () => goToSlide(currentSlideIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => goToSlide(currentSlideIndex + 1));

  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
      e.preventDefault();
      goToSlide(currentSlideIndex + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      e.preventDefault();
      goToSlide(currentSlideIndex - 1);
    }
  });

  // Check URL hash or query param for initial slide (e.g. #slide-2 or ?slide=2)
  const hash = window.location.hash;
  const urlParams = new URLSearchParams(window.location.search);
  if (hash && hash.startsWith('#slide-')) {
    const slideNum = parseInt(hash.replace('#slide-', ''), 10);
    if (!isNaN(slideNum) && slideNum >= 1 && slideNum <= totalSlides) {
      currentSlideIndex = slideNum - 1;
    }
  } else if (urlParams.has('slide')) {
    const slideNum = parseInt(urlParams.get('slide'), 10);
    if (!isNaN(slideNum) && slideNum >= 1 && slideNum <= totalSlides) {
      currentSlideIndex = slideNum - 1;
    }
  }

  updateSlideState();
}

/* --------------------------------------------------------------------------
   5. THEME TOGGLE & COMMAND PALETTE
   -------------------------------------------------------------------------- */
function initThemeToggle() {
  const themeBtn = document.getElementById('themeToggleBtn');
  if (!themeBtn) return;

  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  themeBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
  });
}

function updateThemeIcon(theme) {
  const themeBtn = document.getElementById('themeToggleBtn');
  if (themeBtn) {
    themeBtn.innerHTML = theme === 'dark'
      ? `<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><path d="M12 1v2m0 18v2M4.22 4.22l1.42 1.42m12.72 12.72l1.42 1.42M1 12h2m18 0h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>`
      : `<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>`;
  }
}

function initCommandPalette() {
  const backdrop = document.getElementById('cmdPaletteBackdrop');
  const input = document.getElementById('cmdInput');
  const list = document.getElementById('cmdResultsList');
  if (!backdrop || !input || !list) return;

  window.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      backdrop.classList.toggle('active');
      if (backdrop.classList.contains('active')) input.focus();
    } else if (e.key === 'Escape') {
      backdrop.classList.remove('active');
    }
  });

  backdrop.addEventListener('click', (e) => {
    if (e.target === backdrop) backdrop.classList.remove('active');
  });

  const searchItems = [
    { title: 'Home - Landing Slide Deck', page: 'index.html', slide: 0 },
    { title: 'Home - Seminar Overview & Definitions', page: 'index.html', slide: 1 },
    { title: 'Home - Dataset Reference Table (All Datasets)', page: 'index.html', slide: 2 },
    { title: 'Home - Learning Objectives & Navigation', page: 'index.html', slide: 3 },
    { title: '3D Plotting - Axes & Coordinate Systems', page: '3d-plotting.html', slide: 0 },
    { title: '3D Plotting - 3D Points & Lines (Helix)', page: '3d-plotting.html', slide: 1 },
    { title: '3D Plotting - Iris 3D Species Scatter', page: '3d-plotting.html', slide: 2 },
    { title: '3D Plotting - Contour3D & Level Control', page: '3d-plotting.html', slide: 3 },
    { title: '3D Plotting - view_init Camera Angle Control', page: '3d-plotting.html', slide: 4 },
    { title: '3D Plotting - Wireframe vs Surface', page: '3d-plotting.html', slide: 5 },
    { title: '3D Plotting - Surface Triangulation (plot_trisurf)', page: '3d-plotting.html', slide: 6 },
    { title: '3D Plotting - Flights 3D Passenger Surface', page: '3d-plotting.html', slide: 7 },
    { title: '3D Plotting - Categorical 3D Bar Plot (ax.bar3d)', page: '3d-plotting.html', slide: 8 },
    { title: 'Basemap - Introduction & Setup', page: 'basemap.html', slide: 0 },
    { title: 'Basemap - Drawing Map Background Functions', page: 'basemap.html', slide: 1 },
    { title: 'Basemap - Interactive Projection Families', page: 'basemap.html', slide: 2 },
    { title: 'Basemap - Perspective & Conic Projections', page: 'basemap.html', slide: 3 },
    { title: 'Basemap - World Cities Population Overlay', page: 'basemap.html', slide: 4 },
    { title: 'Basemap - Great Circle Flight Arcs Chennai', page: 'basemap.html', slide: 5 },
    { title: 'Basemap - Migration to Cartopy', page: 'basemap.html', slide: 6 },
    { title: 'Seaborn - Why Use Seaborn Over Matplotlib', page: 'seaborn.html', slide: 0 },
    { title: 'Seaborn - Side-by-Side Code Comparison', page: 'seaborn.html', slide: 1 },
    { title: 'Seaborn - Histograms & KDE Densities', page: 'seaborn.html', slide: 2 },
    { title: 'Seaborn - Pair Plots (sns.pairplot)', page: 'seaborn.html', slide: 3 },
    { title: 'Seaborn - Faceted Histograms & Jointplot', page: 'seaborn.html', slide: 4 },
    { title: 'Seaborn - Factor Plots & catplot', page: 'seaborn.html', slide: 5 },
    { title: 'Seaborn - 2D Heatmaps (sns.heatmap)', page: 'seaborn.html', slide: 6 },
    { title: 'Reference - API Cheat Sheet & Notebook Download', page: 'reference.html', slide: 0 }
  ];

  function renderSearch(query = '') {
    list.innerHTML = '';
    const filtered = searchItems.filter(item => item.title.toLowerCase().includes(query.toLowerCase()));
    filtered.forEach(item => {
      const li = document.createElement('li');
      li.className = 'cmd-result-item';
      li.innerHTML = `<span>${item.title}</span><span style="font-size:0.8rem; opacity:0.6;">Jump ↵</span>`;
      li.addEventListener('click', () => {
        backdrop.classList.remove('active');
        if (window.location.pathname.includes(item.page)) {
          if (typeof goToSlide === 'function') goToSlide(item.slide);
        } else {
          window.location.href = `${item.page}?slide=${item.slide}`;
        }
      });
      list.appendChild(li);
    });
  }

  input.addEventListener('input', (e) => renderSearch(e.target.value));
  renderSearch('');
}

/* --------------------------------------------------------------------------
   6. CODE BLOCK ACTIONS (Copy & Colab Launcher)
   -------------------------------------------------------------------------- */
function initCodeBlocks() {
  document.querySelectorAll('.code-container, .colab-execution-cell').forEach(block => {
    const copyBtn = block.querySelector('.btn-copy-code');
    const colabBtn = block.querySelector('.btn-colab-code');

    if (copyBtn) {
      copyBtn.addEventListener('click', () => {
        const codeText = block.querySelector('code').innerText;
        navigator.clipboard.writeText(codeText).then(() => {
          copyBtn.innerHTML = `<span>✓ Copied!</span>`;
          setTimeout(() => {
            copyBtn.innerHTML = `Copy`;
          }, 2000);
        });
      });
    }

    if (colabBtn) {
      colabBtn.addEventListener('click', () => {
        window.open('https://colab.research.google.com/', '_blank');
      });
    }
  });
}

/* --------------------------------------------------------------------------
   7. INTERACTIVE PLOTLY & D3 CHART ENGINES (LAZY-INITIALIZED ON SLIDE DEMAND)
   -------------------------------------------------------------------------- */
const chartInitRegistry = {
  'helix3dChart': init3DHelixChart,
  'contour3dChart': initContourChart,
  'viewInitChart': initViewInitCameraChart,
  'wireframeSurfaceChart': initWireframeSurfaceChart,
  'triangulation3dChart': initTriangulationChart,
  'basemapD3Chart': initBasemapProjections,
  'worldCitiesMapChart': initWorldCitiesMap,
  'seabornKdeChart': initSeabornKdeChart,
};

const initializedChartIds = new Set();

function initChartForActiveSlide(slideElement) {
  if (!slideElement) return;
  for (const [id, initFunc] of Object.entries(chartInitRegistry)) {
    const el = slideElement.querySelector('#' + id);
    if (el) {
      if (!initializedChartIds.has(id)) {
        initializedChartIds.add(id);
        requestAnimationFrame(() => {
          setTimeout(() => {
            try {
              initFunc();
              setTimeout(() => {
                if (typeof Plotly !== 'undefined' && el.data) {
                  Plotly.Plots.resize(el);
                }
              }, 60);
            } catch (err) {
              console.warn('Lazy chart init notice for ' + id, err);
            }
          }, 30);
        });
      } else if (typeof Plotly !== 'undefined' && el.data) {
        requestAnimationFrame(() => {
          setTimeout(() => {
            try {
              Plotly.Plots.resize(el);
            } catch(e) {}
          }, 20);
        });
      }
    }
  }
}

function initInteractiveCharts() {
  init3DChartActionControls();
  const activeSlide = document.querySelector('.slide-section.active') || slideSections[0];
  if (activeSlide) {
    initChartForActiveSlide(activeSlide);
  }
}

function init3DHelixChart() {
  const container = document.getElementById('helix3dChart');
  if (!container || typeof Plotly === 'undefined') return;

  const z = [], x = [], y = [];
  for (let i = 0; i < 300; i++) {
    const t = (i / 300) * 15;
    z.push(t);
    x.push(Math.sin(t));
    y.push(Math.cos(t));
  }

  const traceLine = {
    type: 'scatter3d', mode: 'lines',
    x: x, y: y, z: z,
    line: { width: 6, color: '#7c3aed' },
    name: '3D Spiral Line'
  };

  const traceScatter = {
    type: 'scatter3d', mode: 'markers',
    x: x.filter((_, i) => i % 3 === 0),
    y: y.filter((_, i) => i % 3 === 0),
    z: z.filter((_, i) => i % 3 === 0),
    marker: { size: 5, color: z.filter((_, i) => i % 3 === 0), colorscale: 'Viridis', opacity: 0.8 },
    name: 'Scatter Points'
  };

  const layout = {
    autosize: true,
    height: 315,
    margin: { l: 0, r: 0, b: 0, t: 0 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    scene: {
      aspectmode: 'cube',
      camera: {
        eye: { x: 1.45, y: 1.45, z: 1.15 },
        center: { x: 0, y: 0, z: 0.15 }
      },
      xaxis: { title: 'X = sin(z)', gridcolor: '#e2e8f0' },
      yaxis: { title: 'Y = cos(z)', gridcolor: '#e2e8f0' },
      zaxis: { title: 'Z (linspace)', gridcolor: '#e2e8f0' }
    }
  };

  Plotly.newPlot(container, [traceLine, traceScatter], layout, { responsive: true, displayModeBar: false });
}

function initContourChart() {
  const container = document.getElementById('contour3dChart');
  const slider = document.getElementById('contourLevelSlider');
  const levelVal = document.getElementById('contourLevelVal');
  if (!container || typeof Plotly === 'undefined') return;

  function generateContourData(nLevels = 50) {
    const n = 40;
    const x = [], y = [], z = [];
    for (let i = 0; i < n; i++) {
      x.push(-6 + (12 * i) / n);
      y.push(-6 + (12 * i) / n);
    }
    for (let i = 0; i < n; i++) {
      const row = [];
      for (let j = 0; j < n; j++) {
        row.push(Math.sin(Math.sqrt(x[i] * x[i] + y[j] * y[j])));
      }
      z.push(row);
    }

    const surfaceTrace = {
      type: 'surface',
      x: x, y: y, z: z,
      colorscale: 'Portland',
      colorbar: { len: 0.75, y: 0.5, thickness: 14 },
      contours: {
        z: {
          show: true,
          usecolormap: true,
          highlightcolor: "#4299e1",
          project: { z: true },
          start: -1,
          end: 1,
          size: 2 / Math.max(5, nLevels)
        }
      }
    };

    return [surfaceTrace];
  }

  const layout = {
    autosize: true,
    height: 315,
    margin: { l: 0, r: 0, b: 0, t: 0 },
    paper_bgcolor: 'transparent',
    scene: {
      aspectmode: 'cube',
      camera: {
        eye: { x: 1.5, y: 1.5, z: 1.2 },
        center: { x: 0, y: 0, z: 0.12 }
      },
      xaxis: { title: 'X' },
      yaxis: { title: 'Y' },
      zaxis: { title: 'Z = sin(√(x²+y²))' }
    }
  };

  Plotly.newPlot(container, generateContourData(50), layout, { responsive: true, displayModeBar: false });

  if (slider && levelVal) {
    slider.addEventListener('input', (e) => {
      const val = parseInt(e.target.value);
      levelVal.textContent = val;
      Plotly.react(container, generateContourData(val), layout);
    });
  }
}

function initViewInitCameraChart() {
  const container = document.getElementById('viewInitChart');
  const elevSlider = document.getElementById('elevSlider');
  const azimSlider = document.getElementById('azimSlider');
  const elevVal = document.getElementById('elevVal');
  const azimVal = document.getElementById('azimVal');
  const codeSpan = document.getElementById('viewInitCodeSnippet');
  if (!container || typeof Plotly === 'undefined') return;

  const n = 30;
  const x = [], y = [], z = [];
  for (let i = 0; i < n; i++) {
    x.push(-5 + (10 * i) / n);
    y.push(-5 + (10 * i) / n);
  }
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      row.push(Math.sin(x[i]) * Math.cos(y[j]));
    }
    z.push(row);
  }

  const trace = { type: 'surface', x: x, y: y, z: z, colorscale: 'Viridis', colorbar: { len: 0.75, y: 0.5, thickness: 14 } };
  const layout = {
    autosize: true,
    height: 315,
    margin: { l: 0, r: 0, b: 0, t: 0 },
    paper_bgcolor: 'transparent',
    scene: {
      aspectmode: 'cube',
      camera: {
        eye: { x: 1.5, y: 1.5, z: 1.2 },
        center: { x: 0, y: 0, z: 0.12 }
      }
    }
  };

  Plotly.newPlot(container, [trace], layout, { responsive: true, displayModeBar: false });

  function updateCamera() {
    const elev = parseInt(elevSlider.value);
    const azim = parseInt(azimSlider.value);
    if (elevVal) elevVal.textContent = elev;
    if (azimVal) azimVal.textContent = azim;

    const radElev = (elev * Math.PI) / 180;
    const radAzim = (azim * Math.PI) / 180;
    const r = 2.0;

    const eyeX = r * Math.cos(radElev) * Math.cos(radAzim);
    const eyeY = r * Math.cos(radElev) * Math.sin(radAzim);
    const eyeZ = r * Math.sin(radElev);

    Plotly.relayout(container, {
      'scene.camera.eye': { x: eyeX, y: eyeY, z: eyeZ },
      'scene.camera.center': { x: 0, y: 0, z: 0.12 }
    });

    if (codeSpan) {
      codeSpan.innerHTML = `ax.view_init(<span class="token-highlight">elev=${elev}, azim=${azim}</span>)`;
    }
  }

  if (elevSlider) elevSlider.addEventListener('input', updateCamera);
  if (azimSlider) azimSlider.addEventListener('input', updateCamera);
}

function initWireframeSurfaceChart() {
  const container = document.getElementById('wireframeSurfaceChart');
  const select = document.getElementById('colormapSelect');
  const modeSelect = document.getElementById('renderModeSelect');
  if (!container || typeof Plotly === 'undefined') return;

  const n = 35;
  const x = [], y = [], z = [];
  for (let i = 0; i < n; i++) {
    x.push(-6 + (12 * i) / n);
    y.push(-6 + (12 * i) / n);
  }
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      const r = Math.sqrt(x[i] * x[i] + y[j] * y[j]);
      row.push(Math.sin(r));
    }
    z.push(row);
  }

  function getTraces(colormap = 'Viridis', mode = 'both') {
    const traces = [];

    // Surface trace
    if (mode === 'surface' || mode === 'both') {
      traces.push({
        type: 'surface',
        x: x, y: y, z: z,
        colorscale: colormap,
        opacity: mode === 'both' ? 0.85 : 1.0,
        showscale: false
      });
    }

    // Wireframe grid lines trace
    if (mode === 'wireframe' || mode === 'both') {
      traces.push({
        type: 'surface',
        x: x, y: y, z: z,
        colorscale: [[0, '#000000'], [1, '#000000']],
        hidesurface: mode === 'wireframe',
        contours: {
          x: { show: true, color: '#0f172a', width: 2 },
          y: { show: true, color: '#0f172a', width: 2 },
          z: { show: true, color: '#0f172a', width: 1 }
        },
        showscale: false
      });
    }

    return traces;
  }

  const layout = {
    autosize: true,
    height: 315,
    margin: { l: 0, r: 0, b: 0, t: 0 },
    paper_bgcolor: 'transparent',
    scene: {
      aspectmode: 'cube',
      camera: {
        eye: { x: 1.5, y: 1.5, z: 1.2 },
        center: { x: 0, y: 0, z: 0.12 }
      },
      xaxis: { title: 'X', gridcolor: '#cbd5e1' },
      yaxis: { title: 'Y', gridcolor: '#cbd5e1' },
      zaxis: { title: 'Z = sin(√(x²+y²))', gridcolor: '#cbd5e1' }
    }
  };

  Plotly.newPlot(container, getTraces('Viridis', 'both'), layout, { responsive: true, displayModeBar: false });

  function updatePlot() {
    const colormap = select ? select.value : 'Viridis';
    const mode = modeSelect ? modeSelect.value : 'both';
    Plotly.react(container, getTraces(colormap, mode), layout);
  }

  if (select) select.addEventListener('change', updatePlot);
  if (modeSelect) modeSelect.addEventListener('change', updatePlot);
}

function initTriangulationChart() {
  const container = document.getElementById('triangulation3dChart');
  if (!container || typeof Plotly === 'undefined') return;

  const n = 360;
  const x = [], y = [], z = [];
  let seed = 42;
  function pseudoRandom() {
    seed = (seed * 9301 + 49297) % 233280;
    return seed / 233280;
  }

  for (let i = 0; i < n; i++) {
    const theta = 2 * Math.PI * pseudoRandom();
    const r = 6 * pseudoRandom();
    const px = r * Math.sin(theta);
    const py = r * Math.cos(theta);
    const pz = Math.sin(Math.sqrt(px * px + py * py));
    x.push(px);
    y.push(py);
    z.push(pz);
  }

  let currentCmap = 'Viridis';

  function getTrisurfData(cmap) {
    const meshTrace = {
      type: 'mesh3d',
      x: x, y: y, z: z,
      intensity: z,
      colorscale: cmap,
      colorbar: { len: 0.75, y: 0.5, thickness: 14 },
      delaunayaxis: 'z',
      opacity: 0.92,
      showscale: true,
      name: 'Triangulated Mesh'
    };

    const scatterTrace = {
      type: 'scatter3d',
      mode: 'markers',
      x: x, y: y, z: z,
      marker: {
        size: 3,
        color: '#0f172a',
        opacity: 0.75
      },
      name: 'Raw Sample Points'
    };

    return [meshTrace, scatterTrace];
  }

  const layout = {
    autosize: true,
    height: 315,
    margin: { l: 0, r: 0, b: 0, t: 0 },
    paper_bgcolor: 'transparent',
    scene: {
      aspectmode: 'cube',
      camera: {
        eye: { x: 1.45, y: 1.45, z: 1.25 },
        center: { x: 0, y: 0, z: 0.12 }
      },
      xaxis: { title: 'X = r·sin(θ)', gridcolor: '#cbd5e1' },
      yaxis: { title: 'Y = r·cos(θ)', gridcolor: '#cbd5e1' },
      zaxis: { title: 'Z = sin(√(x²+y²))', gridcolor: '#cbd5e1' }
    }
  };

  Plotly.newPlot(container, getTrisurfData(currentCmap), layout, { responsive: true, displayModeBar: false });

  // Colormap toggle pills as requested in Audio 2
  const pills = document.querySelectorAll('#trisurfColormapBtns .colormap-pill');
  const activeLabel = document.getElementById('activeTrisurfColormap');

  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      const cmap = pill.getAttribute('data-cmap');
      currentCmap = cmap;
      if (activeLabel) activeLabel.textContent = cmap;
      Plotly.react(container, getTrisurfData(cmap), layout);
    });
  });
}

/* --------------------------------------------------------------------------
   GLOBAL 3D CAMERA ACTION CONTROLS: ZOOM IN, ZOOM OUT, RESET
   -------------------------------------------------------------------------- */
function init3DChartActionControls() {
  const defaultCameras = {
    helix3dChart: { eye: { x: 1.45, y: 1.45, z: 1.15 }, center: { x: 0, y: 0, z: 0.15 } },
    contour3dChart: { eye: { x: 1.5, y: 1.5, z: 1.2 }, center: { x: 0, y: 0, z: 0.12 } },
    viewInitChart: { eye: { x: 1.5, y: 1.5, z: 1.2 }, center: { x: 0, y: 0, z: 0.12 } },
    wireframeSurfaceChart: { eye: { x: 1.5, y: 1.5, z: 1.2 }, center: { x: 0, y: 0, z: 0.12 } },
    triangulation3dChart: { eye: { x: 1.45, y: 1.45, z: 1.25 }, center: { x: 0, y: 0, z: 0.12 } }
  };

  document.querySelectorAll('.btn-zoom-in').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const chartId = btn.getAttribute('data-chart');
      zoomPlotlyScene(chartId, 0.78);
    });
  });

  document.querySelectorAll('.btn-zoom-out').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const chartId = btn.getAttribute('data-chart');
      zoomPlotlyScene(chartId, 1.28);
    });
  });

  document.querySelectorAll('.btn-reset-view').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const chartId = btn.getAttribute('data-chart');
      resetPlotlyScene(chartId, defaultCameras[chartId]);
    });
  });
}

function zoomPlotlyScene(containerId, factor) {
  const el = document.getElementById(containerId);
  if (!el || typeof Plotly === 'undefined') return;

  let eye = { x: 1.5, y: 1.5, z: 1.25 };
  if (el._fullLayout && el._fullLayout.scene && el._fullLayout.scene._scene && el._fullLayout.scene._scene.camera) {
    const curEye = el._fullLayout.scene._scene.camera.eye;
    if (Array.isArray(curEye) && curEye.length >= 3) {
      eye = { x: curEye[0], y: curEye[1], z: curEye[2] };
    }
  } else if (el.layout && el.layout.scene && el.layout.scene.camera && el.layout.scene.camera.eye) {
    eye = { ...el.layout.scene.camera.eye };
  }

  const newEye = {
    x: eye.x * factor,
    y: eye.y * factor,
    z: eye.z * factor
  };

  Plotly.relayout(el, { 'scene.camera.eye': newEye });
}

function resetPlotlyScene(containerId, defaultCam) {
  const el = document.getElementById(containerId);
  if (!el || typeof Plotly === 'undefined') return;

  const targetCam = defaultCam || { eye: { x: 1.5, y: 1.5, z: 1.1 }, center: { x: 0, y: 0, z: 0.22 } };
  Plotly.relayout(el, {
    'scene.camera': {
      eye: targetCam.eye,
      center: targetCam.center || { x: 0, y: 0, z: 0.22 },
      up: { x: 0, y: 0, z: 1 }
    }
  });

  // If this is viewInitChart, also reset sliders to default (elev=60, azim=35)
  if (containerId === 'viewInitChart') {
    const elevSlider = document.getElementById('elevSlider');
    const azimSlider = document.getElementById('azimSlider');
    const elevVal = document.getElementById('elevVal');
    const azimVal = document.getElementById('azimVal');
    const codeSpan = document.getElementById('viewInitCodeSnippet');
    if (elevSlider) elevSlider.value = 60;
    if (azimSlider) azimSlider.value = 35;
    if (elevVal) elevVal.textContent = '60';
    if (azimVal) azimVal.textContent = '35';
    if (codeSpan) codeSpan.innerHTML = 'ax.view_init(<span class="token-highlight">elev=60, azim=35</span>)';

    const radElev = (60 * Math.PI) / 180;
    const radAzim = (35 * Math.PI) / 180;
    const r = 2.0;
    Plotly.relayout(el, {
      'scene.camera.eye': {
        x: r * Math.cos(radElev) * Math.cos(radAzim),
        y: r * Math.cos(radElev) * Math.sin(radAzim),
        z: r * Math.sin(radElev)
      }
    });
  }
}

function initBasemapProjections() {
  const container = document.getElementById('basemapD3Chart');
  if (!container || typeof Plotly === 'undefined') return;

  function renderGlobe(projType = 'ortho') {
    const data = [{
      type: 'scattergeo',
      mode: 'markers+text',
      text: WORLD_CITIES_DATA.map(c => c.city),
      textposition: 'top center',
      textfont: { family: 'Inter', size: 10, color: '#0f172a' },
      lat: WORLD_CITIES_DATA.map(c => c.lat),
      lon: WORLD_CITIES_DATA.map(c => c.lon),
      marker: {
        size: WORLD_CITIES_DATA.map(c => Math.max(7, Math.sqrt(c.pop) / 550)),
        color: '#e11d48',
        opacity: 0.85,
        line: { color: '#ffffff', width: 1.5 }
      }
    }];

    const layout = {
      margin: { l: 0, r: 0, b: 0, t: 0 },
      paper_bgcolor: 'transparent',
      geo: {
        projection: {
          type: projType === 'ortho' ? 'orthographic' : (projType === 'moll' ? 'mollweide' : 'equirectangular'),
          rotation: { lon: -10, lat: 20 }
        },
        showland: true,
        landcolor: '#e2e8f0',
        showocean: true,
        oceancolor: '#e0f2fe',
        showcountries: true,
        countrycolor: '#94a3b8',
        showcoastlines: true,
        coastlinecolor: '#0284c7',
        showlakes: true,
        lakecolor: '#bae6fd'
      }
    };

    Plotly.newPlot(container, data, layout, { responsive: true, displayModeBar: false });
  }

  renderGlobe('ortho');

  document.querySelectorAll('.proj-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.proj-tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderGlobe(btn.dataset.proj);
    });
  });
}

// World cities data embedded inline
const WORLD_CITIES_DATA = [{"city":"Chennai","lat":13.0827,"lon":80.2707,"pop":11500000,"country":"India"},{"city":"Tokyo","lat":35.6762,"lon":139.6503,"pop":37400000,"country":"Japan"},{"city":"New York","lat":40.7128,"lon":-74.006,"pop":19300000,"country":"USA"},{"city":"London","lat":51.5074,"lon":-0.1278,"pop":9000000,"country":"UK"},{"city":"Paris","lat":48.8566,"lon":2.3522,"pop":11000000,"country":"France"},{"city":"Sydney","lat":-33.8688,"lon":151.2093,"pop":5300000,"country":"Australia"},{"city":"Cairo","lat":30.0444,"lon":31.2357,"pop":20400000,"country":"Egypt"},{"city":"Rio de Janeiro","lat":-22.9068,"lon":-43.1729,"pop":13300000,"country":"Brazil"},{"city":"Moscow","lat":55.7558,"lon":37.6173,"pop":12500000,"country":"Russia"},{"city":"Beijing","lat":39.9042,"lon":116.4074,"pop":21500000,"country":"China"},{"city":"Mumbai","lat":19.076,"lon":72.8777,"pop":20900000,"country":"India"},{"city":"Dubai","lat":25.2048,"lon":55.2708,"pop":3300000,"country":"UAE"},{"city":"Singapore","lat":1.3521,"lon":103.8198,"pop":5700000,"country":"Singapore"},{"city":"Los Angeles","lat":34.0522,"lon":-118.2437,"pop":10000000,"country":"USA"},{"city":"Toronto","lat":43.6532,"lon":-79.3832,"pop":6200000,"country":"Canada"},{"city":"Berlin","lat":52.52,"lon":13.405,"pop":3700000,"country":"Germany"},{"city":"Cape Town","lat":-33.9249,"lon":18.4241,"pop":4600000,"country":"South Africa"},{"city":"Buenos Aires","lat":-34.6037,"lon":-58.3816,"pop":15100000,"country":"Argentina"},{"city":"Istanbul","lat":41.0082,"lon":28.9784,"pop":15500000,"country":"Turkey"},{"city":"Seoul","lat":37.5665,"lon":126.978,"pop":9700000,"country":"South Korea"}];

function initWorldCitiesMap() {
  const tableContainer = document.getElementById('worldCitiesTableContainer');
  const mapContainer = document.getElementById('worldCitiesMapChart');

  if (tableContainer) {
    const data = WORLD_CITIES_DATA;
    let html = `<table style="width:100%; border-collapse:collapse; font-size:0.875rem;">
      <thead>
        <tr style="border-bottom:2px solid var(--border-light); background:var(--bg-secondary); text-align:left;">
          <th style="padding:8px;">City</th>
          <th style="padding:8px;">Country</th>
          <th style="padding:8px;">Lat</th>
          <th style="padding:8px;">Lon</th>
          <th style="padding:8px;">Population</th>
        </tr>
      </thead>
      <tbody>`;
    data.forEach(c => {
      html += `<tr style="border-bottom:1px solid var(--border-light);">
        <td style="padding:8px; font-weight:700;">${c.city}</td>
        <td style="padding:8px;">${c.country}</td>
        <td style="padding:8px;">${c.lat.toFixed(2)}°</td>
        <td style="padding:8px;">${c.lon.toFixed(2)}°</td>
        <td style="padding:8px; color:var(--accent-teal); font-weight:700;">${(c.pop / 1000000).toFixed(1)}M</td>
      </tr>`;
    });
    html += `</tbody></table>`;
    tableContainer.innerHTML = html;
  }

  if (mapContainer && typeof Plotly !== 'undefined') {
    const mapData = [{
      type: 'scattergeo',
      mode: 'markers',
      lat: WORLD_CITIES_DATA.map(c => c.lat),
      lon: WORLD_CITIES_DATA.map(c => c.lon),
      text: WORLD_CITIES_DATA.map(c => `${c.city}, ${c.country}: ${(c.pop / 1000000).toFixed(1)}M`),
      marker: {
        size: WORLD_CITIES_DATA.map(c => Math.max(6, Math.sqrt(c.pop) / 450)),
        color: WORLD_CITIES_DATA.map(c => c.pop),
        colorscale: 'Reds',
        opacity: 0.85
      }
    }];
    const mapLayout = {
      margin: { l: 0, r: 0, b: 0, t: 0 },
      paper_bgcolor: 'transparent',
      geo: {
        projection: { type: 'equirectangular' },
        showland: true, landcolor: '#f1f5f9',
        showocean: true, oceancolor: '#e0f2fe',
        showcountries: true, countrycolor: '#cbd5e1'
      }
    };
    Plotly.newPlot(mapContainer, mapData, mapLayout, { responsive: true, displayModeBar: false });
  }
}

function initSeabornKdeChart() {
  const container = document.getElementById('seabornKdeChart');
  const slider = document.getElementById('bandwidthSlider');
  const bwVal = document.getElementById('bwVal');
  if (!container || typeof Plotly === 'undefined') return;

  function getKdeData(bw = 1.0) {
    const x = [], y = [];
    for (let i = -4; i <= 4; i += 0.1) {
      x.push(i);
      const val = Math.exp(-0.5 * Math.pow(i / bw, 2)) / (bw * Math.sqrt(2 * Math.PI));
      y.push(val);
    }
    return {
      x: x, y: y,
      type: 'scatter', mode: 'lines', fill: 'tozeroy',
      line: { color: '#e11d48', width: 3 },
      fillcolor: 'rgba(225, 29, 72, 0.15)',
      name: `KDE (bw=${bw})`
    };
  }

  const layout = {
    margin: { l: 40, r: 20, b: 40, t: 20 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    xaxis: { title: 'Value', gridcolor: '#e2e8f0' },
    yaxis: { title: 'Density', gridcolor: '#e2e8f0' }
  };

  Plotly.newPlot(container, [getKdeData(1.0)], layout, { responsive: true, displayModeBar: false });

  if (slider && bwVal) {
    slider.addEventListener('input', (e) => {
      const bw = parseFloat(e.target.value);
      bwVal.textContent = bw;
      Plotly.react(container, [getKdeData(bw)], layout);
    });
  }
}
