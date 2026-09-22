/**
 * Data Visualization Seminar - Interactive Quiz & Assessment Engine
 * Questions directly extracted from: Data_Visualization_Seminar_Quiz_QA.pdf
 */

const QUIZ_QUESTIONS = [
  // ==========================================
  // SECTION 1: MULTIPLE CHOICE QUESTIONS (MCQs)
  // ==========================================
  {
    id: 1,
    category: "mcq",
    categoryLabel: "1. Multiple Choice Questions",
    question: "Which Python library is mainly used for plotting graphs?",
    options: [
      "NumPy",
      "Matplotlib",
      "Pandas",
      "Requests"
    ],
    correctAnswerText: "Matplotlib",
    explanation: "Matplotlib is the foundational, multi-platform 2D and 3D data plotting library in Python."
  },
  {
    id: 2,
    category: "mcq",
    categoryLabel: "1. Multiple Choice Questions",
    question: "Which plot shows the relationship between two numerical variables?",
    options: [
      "Pie chart",
      "Histogram",
      "Scatter plot",
      "Box plot"
    ],
    correctAnswerText: "Scatter plot",
    explanation: "A scatter plot maps individual (x, y) coordinates to reveal correlations and relationships between two continuous variables."
  },
  {
    id: 3,
    category: "mcq",
    categoryLabel: "1. Multiple Choice Questions",
    question: "Which plot is commonly used to visualize a correlation matrix?",
    options: [
      "Heatmap",
      "Rug plot",
      "Bar plot",
      "Line plot"
    ],
    correctAnswerText: "Heatmap",
    explanation: "Heatmaps visualize 2D tabular numerical intensity using color gradients, making them ideal for correlation matrices."
  },
  {
    id: 4,
    category: "mcq",
    categoryLabel: "1. Multiple Choice Questions",
    question: "Which plot displays data in three dimensions?",
    options: [
      "2D plot",
      "Pie plot",
      "Count plot",
      "3D plot"
    ],
    correctAnswerText: "3D plot",
    explanation: "3D plots (such as ax.plot3D, ax.scatter3D, ax.contour3D) display data across three spatial axes (X, Y, Z)."
  },
  {
    id: 5,
    category: "mcq",
    categoryLabel: "1. Multiple Choice Questions",
    question: "Which Seaborn plot can show the distribution of a numerical variable?",
    options: [
      "Lmplot",
      "Histogram",
      "Pairplot",
      "Jointplot"
    ],
    correctAnswerText: "Histogram",
    explanation: "Histograms bin continuous numerical observations to display the underlying frequency distribution."
  },
  {
    id: 6,
    category: "mcq",
    categoryLabel: "1. Multiple Choice Questions",
    question: "Which plot helps identify outliers using quartiles?",
    options: [
      "Line plot",
      "Heatmap",
      "Box plot",
      "Contour plot"
    ],
    correctAnswerText: "Box plot",
    explanation: "Box plots (box-and-whisker) display quartiles, the median, IQR, and mark individual outliers beyond the 1.5 × IQR whiskers."
  },
  {
    id: 7,
    category: "mcq",
    categoryLabel: "1. Multiple Choice Questions",
    question: "Which library is designed for statistical data visualization?",
    options: [
      "Flask",
      "Tkinter",
      "Requests",
      "Seaborn"
    ],
    correctAnswerText: "Seaborn",
    explanation: "Seaborn is built on Matplotlib and provides high-level APIs specifically tailored for statistical data graphics."
  },
  {
    id: 8,
    category: "mcq",
    categoryLabel: "1. Multiple Choice Questions",
    question: "Which route represents a shortest path over a spherical Earth?",
    options: [
      "Great-circle route",
      "Straight line",
      "Grid line",
      "Contour line"
    ],
    correctAnswerText: "Great-circle route",
    explanation: "On a spherical surface like Earth, the geodesic arc of a great circle represents the shortest navigation distance between two points."
  },

  // ==========================================
  // SECTION 2: ODD ONE OUT
  // ==========================================
  {
    id: 9,
    category: "odd_one_out",
    categoryLabel: "2. Odd One Out",
    question: "Identify the Odd One Out: Which item does not belong with the others?",
    options: [
      "Matplotlib",
      "NumPy",
      "Seaborn",
      "Cartopy"
    ],
    correctAnswerText: "NumPy",
    explanation: "NumPy is a numerical computation library; the others (Matplotlib, Seaborn, Cartopy) are specialized for data and geographic visualization."
  },
  {
    id: 10,
    category: "odd_one_out",
    categoryLabel: "2. Odd One Out",
    question: "Identify the Odd One Out: Which item does not belong with the others?",
    options: [
      "Histogram",
      "KDE",
      "Great-circle route",
      "Rug plot"
    ],
    correctAnswerText: "Great-circle route",
    explanation: "Great-circle route represents a geographic navigation path on a sphere; the others visualize univariate data distributions."
  },
  {
    id: 11,
    category: "odd_one_out",
    categoryLabel: "2. Odd One Out",
    question: "Identify the Odd One Out: Which plot type does not belong with the others?",
    options: [
      "Heatmap",
      "Box plot",
      "Violin plot",
      "Strip plot"
    ],
    correctAnswerText: "Heatmap",
    explanation: "Heatmaps visualize 2D tabular matrix correlations; Box plot, Violin plot, and Strip plot display distributions across categories."
  },
  {
    id: 12,
    category: "odd_one_out",
    categoryLabel: "2. Odd One Out",
    question: "Identify the Odd One Out: Which function does not belong with the others?",
    options: [
      "plot3D",
      "scatter3D",
      "bar3d",
      "pairplot"
    ],
    correctAnswerText: "pairplot",
    explanation: "pairplot is a Seaborn 2D matrix exploration function; plot3D, scatter3D, and bar3d are Matplotlib 3D plotting functions."
  },
  {
    id: 13,
    category: "odd_one_out",
    categoryLabel: "2. Odd One Out",
    question: "Identify the Odd One Out: Which term does not belong with the others?",
    options: [
      "Latitude",
      "Histogram",
      "Longitude",
      "Map projection"
    ],
    correctAnswerText: "Histogram",
    explanation: "Histogram is a statistical distribution plot; Latitude, Longitude, and Map projection are fundamental geographic cartography concepts."
  },
  {
    id: 14,
    category: "odd_one_out",
    categoryLabel: "2. Odd One Out",
    question: "Identify the Odd One Out: Which parameter/technique does not belong with the others?",
    options: [
      "Elevation",
      "Azimuth",
      "KDE",
      "Camera view"
    ],
    correctAnswerText: "KDE",
    explanation: "KDE (Kernel Density Estimation) is a statistical smoothing method; Elevation, Azimuth, and Camera view configure 3D camera angles in ax.view_init."
  },

  // ==========================================
  // SECTION 3: MATCH THE FOLLOWING (SINGLE UNIFIED QUESTION)
  // ==========================================
  {
    id: 15,
    category: "match",
    categoryLabel: "3. Match the Following",
    question: "Match the items in Column A with their correct corresponding roles in Column B:",
    matchColumns: {
      colA: [
        { num: "1.", text: "Matplotlib" },
        { num: "2.", text: "Seaborn" },
        { num: "3.", text: "GeoPandas" },
        { num: "4.", text: "Heatmap" },
        { num: "5.", text: "Pairplot" },
        { num: "6.", text: "Basemap" }
      ],
      colB: [
        { num: "A.", text: "Geographic data" },
        { num: "B.", text: "Statistical visualization" },
        { num: "C.", text: "Multiple pairwise relationships" },
        { num: "D.", text: "Mapping toolkit" },
        { num: "E.", text: "General plotting" },
        { num: "F.", text: "Correlation matrix visualization" }
      ]
    },
    options: [
      "1–B, 2–E, 3–D, 4–A, 5–F, 6–C",
      "1–E, 2–A, 3–B, 4–C, 5–F, 6–D",
      "1–E, 2–B, 3–A, 4–F, 5–C, 6–D",
      "1–D, 2–B, 3–A, 4–E, 5–C, 6–F"
    ],
    correctAnswerText: "1–E, 2–B, 3–A, 4–F, 5–C, 6–D",
    explanation: "Correct Mappings:\n• 1. Matplotlib ➔ E. General plotting\n• 2. Seaborn ➔ B. Statistical visualization\n• 3. GeoPandas ➔ A. Geographic data\n• 4. Heatmap ➔ F. Correlation matrix visualization\n• 5. Pairplot ➔ C. Multiple pairwise relationships\n• 6. Basemap ➔ D. Mapping toolkit"
  },

  // ==========================================
  // SECTION 4: TRUE OR FALSE
  // ==========================================
  {
    id: 16,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "A histogram is used to show the distribution of numerical data.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "True",
    explanation: "True — Histograms segment continuous numerical data into discrete bins to display frequency distribution."
  },
  {
    id: 17,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "A heatmap can visualize correlation values.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "True",
    explanation: "True — Heatmaps are the primary graphical format for visualizing correlation matrices in Seaborn (sns.heatmap(df.corr()))."
  },
  {
    id: 18,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "A 3D scatter plot uses only two axes.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "False",
    explanation: "False — A 3D scatter plot uses three spatial dimensions (X, Y, and Z axes)."
  },
  {
    id: 19,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "A box plot can help identify outliers.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "True",
    explanation: "True — Points lying beyond 1.5 times the interquartile range (IQR) from the quartiles are explicitly plotted as outlier dots."
  },
  {
    id: 20,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "Seaborn is built on top of Matplotlib.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "True",
    explanation: "True — Seaborn builds directly on Matplotlib's graphics engine while offering high-level statistical plotting APIs."
  },
  {
    id: 21,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "A great-circle route represents a shortest path on a sphere.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "True",
    explanation: "True — The arc along a great circle is the shortest distance between any two coordinates on a spherical surface."
  },
  {
    id: 22,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "A KDE plot displays only raw individual data points.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "False",
    explanation: "False — Kernel Density Estimation computes and renders a continuous smoothed probability density estimate, rather than just isolated raw points."
  },
  {
    id: 23,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "Every map projection preserves all geographic properties perfectly.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "False",
    explanation: "False — Flattening a 3D sphere onto a 2D sheet inevitably introduces distortion in area, shape, distance, or angle."
  },
  {
    id: 24,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "A pairplot can show relationships between multiple numerical variables.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "True",
    explanation: "True — sns.pairplot creates an N × N grid displaying all pairwise bivariate joint relationships alongside univariate distributions."
  },
  {
    id: 25,
    category: "true_false",
    categoryLabel: "4. True or False",
    question: "The viewing angle of a 3D plot cannot be changed.",
    options: [
      "True",
      "False"
    ],
    correctAnswerText: "False",
    explanation: "False — Matplotlib provides ax.view_init(elevation, azimuth) to interactively or programmatically adjust the 3D camera viewing angle."
  },

  // ==========================================
  // SECTION 5: QUICK-FIRE QUESTIONS
  // ==========================================
  {
    id: 26,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "Which library is used for statistical visualization in Python?",
    options: [
      "Matplotlib",
      "NumPy",
      "Seaborn",
      "Pandas"
    ],
    correctAnswerText: "Seaborn",
    explanation: "Seaborn is Python's leading statistical graphics package."
  },
  {
    id: 27,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "Which plot is used for correlation matrix visualization?",
    options: [
      "Heatmap",
      "Scatter plot",
      "Box plot",
      "Line plot"
    ],
    correctAnswerText: "Heatmap",
    explanation: "Heatmaps cleanly visualize correlation coefficients using color-coded cells."
  },
  {
    id: 28,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "Which plot is used to show quartiles and outliers?",
    options: [
      "Pie chart",
      "KDE plot",
      "Count plot",
      "Box plot"
    ],
    correctAnswerText: "Box plot",
    explanation: "Box plots provide a standardized 5-point summary of data distribution."
  },
  {
    id: 29,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "Which geographic coordinate specifies north–south position?",
    options: [
      "Longitude",
      "Latitude",
      "Azimuth",
      "Elevation"
    ],
    correctAnswerText: "Latitude",
    explanation: "Latitude lines measure angular distance north or south of the Equator (0° to ±90°)."
  },
  {
    id: 30,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "Which geographic coordinate specifies east–west position?",
    options: [
      "Latitude",
      "Elevation",
      "Longitude",
      "Azimuth"
    ],
    correctAnswerText: "Longitude",
    explanation: "Longitude lines measure angular distance east or west of the Prime Meridian (0° to ±180°)."
  },
  {
    id: 31,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "Which plot shows a 3D point cloud of (X, Y, Z) coordinates?",
    options: [
      "Scatter3D",
      "Contour3D",
      "Heatmap",
      "Wireframe"
    ],
    correctAnswerText: "Scatter3D",
    explanation: "ax.scatter3D plots three-dimensional scatter point clouds."
  },
  {
    id: 32,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "What is the statistical technique used for estimating a smooth continuous distribution?",
    options: [
      "IQR",
      "PCA",
      "FFT",
      "KDE (Kernel Density Estimation)"
    ],
    correctAnswerText: "KDE (Kernel Density Estimation)",
    explanation: "KDE (Kernel Density Estimation) smooths discrete data samples into continuous probability densities."
  },
  {
    id: 33,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "What is the mathematical representation of Earth's surface on a flat map called?",
    options: [
      "Elevation",
      "Projection",
      "Azimuth",
      "Triangulation"
    ],
    correctAnswerText: "Projection",
    explanation: "Map projections transform 3D spherical coordinates to 2D planar map coordinates."
  },
  {
    id: 34,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "Which Seaborn plot displays several pairwise variable relationships simultaneously?",
    options: [
      "Jointplot",
      "Lmplot",
      "Pairplot",
      "FacetGrid"
    ],
    correctAnswerText: "Pairplot",
    explanation: "sns.pairplot plots a matrix of bivariate scatter plots and univariate distribution plots."
  },
  {
    id: 35,
    category: "quick_fire",
    categoryLabel: "5. Quick-Fire Questions",
    question: "Which Seaborn function is specifically used to plot linear regression relationships?",
    options: [
      "Heatmap",
      "Boxplot",
      "Countplot",
      "Lmplot"
    ],
    correctAnswerText: "Lmplot",
    explanation: "sns.lmplot plots linear regression models with scatter points across faceted dataset subsets."
  }
];

// Audio feedback synthesizers using Web Audio API (cross-platform, zero external assets)
class QuizAudio {
  constructor() {
    this.ctx = null;
  }

  init() {
    if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }
  }

  playCorrect() {
    try {
      this.init();
      if (!this.ctx) return;
      const now = this.ctx.currentTime;
      const osc1 = this.ctx.createOscillator();
      const osc2 = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc1.type = 'sine';
      osc2.type = 'triangle';
      osc1.frequency.setValueAtTime(523.25, now); // C5
      osc1.frequency.exponentialRampToValueAtTime(659.25, now + 0.1); // E5
      osc1.frequency.exponentialRampToValueAtTime(783.99, now + 0.22); // G5

      osc2.frequency.setValueAtTime(1046.50, now + 0.1); // C6

      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);

      osc1.connect(gain);
      osc2.connect(gain);
      gain.connect(this.ctx.destination);

      osc1.start(now);
      osc2.start(now + 0.1);
      osc1.stop(now + 0.45);
      osc2.stop(now + 0.45);
    } catch (e) {
      // Audio fallback
    }
  }

  playIncorrect() {
    try {
      this.init();
      if (!this.ctx) return;
      const now = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(220, now); // A3
      osc.frequency.linearRampToValueAtTime(170, now + 0.25);

      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.35);
    } catch (e) {
      // Audio fallback
    }
  }
}

const quizAudio = new QuizAudio();

// Main Interactive Quiz Controller Class
class QuizEngine {
  constructor(containerId, options = {}) {
    this.container = document.getElementById(containerId);
    if (!this.container) return;

    this.allQuestions = [...QUIZ_QUESTIONS];
    this.activeQuestions = [...this.allQuestions];
    this.currentCategory = 'all';
    this.currentIndex = 0;
    this.score = 0;
    this.hasAnswered = false;
    this.currentShuffledOptions = [];
    this.currentCorrectIndex = 0;
    this.userAnswers = [];
    this.isEmbedded = options.isEmbedded || false;

    this.init();
  }

  init() {
    this.renderLayout();
    this.attachEventListeners();
    this.loadQuestion();
  }

  setCategory(category) {
    this.currentCategory = category;
    if (category === 'all') {
      this.activeQuestions = [...this.allQuestions];
    } else {
      this.activeQuestions = this.allQuestions.filter(q => q.category === category);
    }
    this.currentIndex = 0;
    this.score = 0;
    this.hasAnswered = false;
    this.userAnswers = [];
    this.renderCategoryPills();
    this.loadQuestion();
  }

  renderLayout() {
    this.container.innerHTML = `
      <div class="quiz-app-card">
        <!-- Top Control Bar -->
        <div class="quiz-top-bar">
          <div class="quiz-category-pills" id="quizCategoryPills">
            <!-- Rendered dynamically -->
          </div>

          <div class="quiz-live-stats">
            <div class="quiz-stat-pill score-pill">
              <span class="stat-icon">⭐</span>
              <span class="stat-label">Score:</span>
              <span class="stat-value" id="quizLiveScore">0</span>
            </div>
            <div class="quiz-stat-pill progress-pill">
              <span class="stat-icon">🎯</span>
              <span class="stat-value" id="quizQuestionCounter">1 / ${this.activeQuestions.length}</span>
            </div>
          </div>
        </div>

        <!-- Progress Bar Indicator -->
        <div class="quiz-progress-track">
          <div class="quiz-progress-fill" id="quizProgressBar" style="width: 0%;"></div>
        </div>

        <!-- Question Body Section -->
        <div class="quiz-body-section" id="quizBodySection">
          <div class="quiz-category-tag" id="quizCategoryTag">Category</div>
          <h2 class="quiz-question-title" id="quizQuestionTitle">Question prompt goes here...</h2>

          <!-- Match Columns Container (Rendered dynamically if match question) -->
          <div class="match-columns-container" id="matchColumnsContainer" style="display: none;"></div>

          <!-- Options Grid (Collapsed 2x2 on desktop, clean stacked on mobile) -->
          <div class="quiz-options-grid" id="quizOptionsGrid"></div>

          <!-- Explanation Container (Revealed upon selection) -->
          <div class="quiz-explanation-box" id="quizExplanationBox" style="display: none;">
            <div class="explanation-badge" id="explanationBadge">Correct!</div>
            <p class="explanation-text" id="explanationText"></p>
          </div>

          <!-- Action Footer Dock -->
          <div class="quiz-footer-dock">
            <div class="quiz-lock-warning" id="quizLockWarning" style="display: none;">
              <span>⚠️ Please select an answer before proceeding. You cannot skip this question!</span>
            </div>
            <button class="quiz-next-btn" id="quizNextBtn" disabled>
              <span id="quizNextBtnText">Next Question ➔</span>
            </button>
          </div>
        </div>

        <!-- Result Screen (Hidden initially) -->
        <div class="quiz-result-dashboard" id="quizResultDashboard" style="display: none;"></div>
      </div>
    `;
    this.renderCategoryPills();
  }

  renderCategoryPills() {
    const pillsContainer = this.container.querySelector('#quizCategoryPills');
    if (!pillsContainer) return;

    const categories = [
      { id: 'all', label: 'All Questions', count: 35 },
      { id: 'mcq', label: '1. MCQs', count: 8 },
      { id: 'odd_one_out', label: '2. Odd One Out', count: 6 },
      { id: 'match', label: '3. Match', count: 1 },
      { id: 'true_false', label: '4. True/False', count: 10 },
      { id: 'quick_fire', label: '5. Quick-Fire', count: 10 }
    ];

    pillsContainer.innerHTML = categories.map(cat => `
      <button class="quiz-cat-pill ${this.currentCategory === cat.id ? 'active' : ''}" data-category="${cat.id}">
        ${cat.label} <span class="pill-count">(${cat.count})</span>
      </button>
    `).join('');

    pillsContainer.querySelectorAll('.quiz-cat-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        const cat = btn.getAttribute('data-category');
        this.setCategory(cat);
      });
    });
  }

  attachEventListeners() {
    const nextBtn = this.container.querySelector('#quizNextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (!this.hasAnswered) {
          this.triggerLockWarning();
          return;
        }
        this.goToNextQuestion();
      });
    }
  }

  triggerLockWarning() {
    const warning = this.container.querySelector('#quizLockWarning');
    const qSection = this.container.querySelector('.quiz-app-card');
    if (warning) {
      warning.style.display = 'flex';
      warning.classList.remove('shake-anim');
      void warning.offsetWidth;
      warning.classList.add('shake-anim');
    }
    if (qSection) {
      qSection.classList.remove('shake-anim');
      void qSection.offsetWidth;
      qSection.classList.add('shake-anim');
    }
  }

  /**
   * Scramble and shuffle options so answers are evenly distributed across A, B, C, D
   * and not clustered predictably in A or B!
   */
  shuffleOptions(optionsList, correctAnswerText, isTrueFalse = false) {
    if (isTrueFalse) {
      return {
        shuffledOptions: [...optionsList],
        correctIndex: optionsList.indexOf(correctAnswerText)
      };
    }

    // Clone array and perform randomized Fisher-Yates scramble
    const list = [...optionsList];
    for (let i = list.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [list[i], list[j]] = [list[j], list[i]];
    }

    const correctIndex = list.indexOf(correctAnswerText);
    return {
      shuffledOptions: list,
      correctIndex: correctIndex >= 0 ? correctIndex : 0
    };
  }

  loadQuestion() {
    const q = this.activeQuestions[this.currentIndex];
    if (!q) {
      this.showFinalScore();
      return;
    }

    this.hasAnswered = false;

    // Hide results & show question body
    const bodySection = this.container.querySelector('#quizBodySection');
    const resultDashboard = this.container.querySelector('#quizResultDashboard');
    bodySection.style.display = 'block';
    resultDashboard.style.display = 'none';

    // Update Category Tag & Title
    this.container.querySelector('#quizCategoryTag').textContent = q.categoryLabel;
    this.container.querySelector('#quizQuestionTitle').textContent = `${this.currentIndex + 1}. ${q.question}`;

    // Handle Match the Following Columns Display
    const matchColumnsContainer = this.container.querySelector('#matchColumnsContainer');
    if (q.matchColumns) {
      matchColumnsContainer.style.display = 'grid';
      matchColumnsContainer.innerHTML = `
        <div class="match-column col-a">
          <div class="match-col-header">Column A</div>
          <div class="match-col-items">
            ${q.matchColumns.colA.map(item => `
              <div class="match-col-item">
                <span class="match-badge num-badge">${item.num}</span>
                <span class="match-text">${item.text}</span>
              </div>
            `).join('')}
          </div>
        </div>
        <div class="match-column col-b">
          <div class="match-col-header">Column B</div>
          <div class="match-col-items">
            ${q.matchColumns.colB.map(item => `
              <div class="match-col-item">
                <span class="match-badge alpha-badge">${item.num}</span>
                <span class="match-text">${item.text}</span>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    } else {
      matchColumnsContainer.style.display = 'none';
      matchColumnsContainer.innerHTML = '';
    }

    // Update Counter & Progress
    const counterEl = this.container.querySelector('#quizQuestionCounter');
    counterEl.textContent = `${this.currentIndex + 1} / ${this.activeQuestions.length}`;
    
    const progressPercent = ((this.currentIndex) / this.activeQuestions.length) * 100;
    this.container.querySelector('#quizProgressBar').style.width = `${progressPercent}%`;

    // Live Score
    this.container.querySelector('#quizLiveScore').textContent = this.score;

    // Reset Explanation & Warnings
    const explanationBox = this.container.querySelector('#quizExplanationBox');
    explanationBox.style.display = 'none';
    const warning = this.container.querySelector('#quizLockWarning');
    warning.style.display = 'none';

    // Reset Next Button - STRICTLY LOCKED (DISABLED) UNTIL ANSWERED
    const nextBtn = this.container.querySelector('#quizNextBtn');
    nextBtn.disabled = true;
    nextBtn.classList.remove('unlocked');
    const nextBtnText = this.container.querySelector('#quizNextBtnText');
    if (this.currentIndex === this.activeQuestions.length - 1) {
      nextBtnText.textContent = "View Final Score 🏆";
    } else {
      nextBtnText.textContent = "Next Question ➔";
    }

    // Scramble / Collapse options dynamically so answers are distributed across A, B, C, D
    const isTrueFalse = q.category === 'true_false';
    const { shuffledOptions, correctIndex } = this.shuffleOptions(q.options, q.correctAnswerText, isTrueFalse);
    this.currentShuffledOptions = shuffledOptions;
    this.currentCorrectIndex = correctIndex;

    // Render Options in collapsed/compact grid
    const optionsGrid = this.container.querySelector('#quizOptionsGrid');
    optionsGrid.innerHTML = '';
    if (isTrueFalse) {
      optionsGrid.classList.add('two-col-compact');
    } else {
      optionsGrid.classList.remove('two-col-compact');
    }

    const optionLetters = ['A', 'B', 'C', 'D'];

    this.currentShuffledOptions.forEach((optText, optIdx) => {
      const btn = document.createElement('button');
      btn.className = 'quiz-option-btn';
      btn.dataset.index = optIdx;

      let letterBadge = optionLetters[optIdx] || (optIdx + 1);
      if (isTrueFalse) {
        letterBadge = optIdx === 0 ? '✓' : '✗';
      }

      btn.innerHTML = `
        <span class="option-letter">${letterBadge}</span>
        <span class="option-text">${optText}</span>
        <span class="option-status-icon"></span>
      `;

      btn.addEventListener('click', () => {
        this.selectOption(optIdx);
      });

      optionsGrid.appendChild(btn);
    });
  }

  selectOption(selectedIndex) {
    if (this.hasAnswered) return;
    this.hasAnswered = true;

    const q = this.activeQuestions[this.currentIndex];
    const isCorrect = selectedIndex === this.currentCorrectIndex;
    const optionLetters = ['A', 'B', 'C', 'D'];
    const correctLetter = q.category === 'true_false' 
      ? (this.currentCorrectIndex === 0 ? 'True' : 'False') 
      : `${optionLetters[this.currentCorrectIndex]}. ${this.currentShuffledOptions[this.currentCorrectIndex]}`;

    // Record user answer
    this.userAnswers.push({
      question: q.question,
      categoryLabel: q.categoryLabel,
      options: this.currentShuffledOptions,
      selectedIndex: selectedIndex,
      correctIndex: this.currentCorrectIndex,
      isCorrect: isCorrect,
      explanation: q.explanation
    });

    if (isCorrect) {
      this.score += 1;
      quizAudio.playCorrect();
    } else {
      quizAudio.playIncorrect();
    }

    // Update Live Score Counter
    this.container.querySelector('#quizLiveScore').textContent = this.score;

    // Style Option Buttons
    const optionBtns = this.container.querySelectorAll('.quiz-option-btn');
    optionBtns.forEach((btn, idx) => {
      btn.disabled = true;
      if (idx === this.currentCorrectIndex) {
        btn.classList.add('correct-answer');
        btn.querySelector('.option-status-icon').innerHTML = `
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
        `;
      }
      if (idx === selectedIndex && !isCorrect) {
        btn.classList.add('incorrect-answer');
        btn.querySelector('.option-status-icon').innerHTML = `
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg>
        `;
      }
    });

    // Show Explanation Banner
    const explanationBox = this.container.querySelector('#quizExplanationBox');
    const badge = this.container.querySelector('#explanationBadge');
    const text = this.container.querySelector('#explanationText');

    if (isCorrect) {
      explanationBox.className = 'quiz-explanation-box correct-box';
      badge.innerHTML = `🎉 Correct! (${correctLetter})`;
    } else {
      explanationBox.className = 'quiz-explanation-box incorrect-box';
      badge.innerHTML = `❌ Incorrect. Correct Answer: ${correctLetter}`;
    }

    text.innerHTML = q.explanation.replace(/\n/g, '<br>');
    explanationBox.style.display = 'block';

    const warning = this.container.querySelector('#quizLockWarning');
    if (warning) warning.style.display = 'none';

    // UNLOCK Next Button
    const nextBtn = this.container.querySelector('#quizNextBtn');
    nextBtn.disabled = false;
    nextBtn.classList.add('unlocked');
  }

  goToNextQuestion() {
    this.currentIndex++;
    if (this.currentIndex < this.activeQuestions.length) {
      this.loadQuestion();
    } else {
      this.showFinalScore();
    }
  }

  showFinalScore() {
    const total = this.activeQuestions.length;
    const percentage = Math.round((this.score / total) * 100);

    this.container.querySelector('#quizProgressBar').style.width = '100%';

    const bodySection = this.container.querySelector('#quizBodySection');
    const resultDashboard = this.container.querySelector('#quizResultDashboard');
    bodySection.style.display = 'none';
    resultDashboard.style.display = 'block';

    let badgeTitle = "";
    let badgeEmoji = "";
    let badgeColor = "";
    let message = "";

    if (percentage >= 90) {
      badgeEmoji = "🏆";
      badgeTitle = "Data Visualization Master";
      badgeColor = "#10b981";
      message = "Outstanding performance! You have mastered 3D Plotting, Basemap Cartography, and Seaborn Statistical Graphics!";
    } else if (percentage >= 75) {
      badgeEmoji = "🌟";
      badgeTitle = "Excellent Proficiency";
      badgeColor = "#2563eb";
      message = "Great job! You have demonstrated strong grasp of Python data visualization fundamentals and charts.";
    } else if (percentage >= 50) {
      badgeEmoji = "👍";
      badgeTitle = "Good Effort";
      badgeColor = "#d97706";
      message = "Good attempt! Review the questions and references to strengthen key data visualization concepts.";
    } else {
      badgeEmoji = "📚";
      badgeTitle = "Keep Learning";
      badgeColor = "#e11d48";
      message = "You can do better! Read the seminar slides and Jupyter notebook to master the concepts.";
    }

    if (percentage >= 70 && typeof launchFireworksConfetti === 'function') {
      setTimeout(launchFireworksConfetti, 120);
    }

    resultDashboard.innerHTML = `
      <div class="result-card-inner">
        <div class="result-badge-icon">${badgeEmoji}</div>
        <div class="result-badge-tag" style="background: ${badgeColor}22; color: ${badgeColor}; border: 1px solid ${badgeColor}55;">
          ${badgeTitle}
        </div>
        <h2 class="result-title">Quiz Completed!</h2>
        <p class="result-subtitle">${message}</p>

        <!-- Big Score Ring -->
        <div class="result-score-circle">
          <div class="result-percentage">${percentage}%</div>
          <div class="result-score-detail">${this.score} / ${total} Correct</div>
        </div>

        <!-- Metrics Grid -->
        <div class="result-metrics-grid">
          <div class="metric-box">
            <span class="metric-val" style="color: #10b981;">${this.score}</span>
            <span class="metric-lbl">Correct Answers</span>
          </div>
          <div class="metric-box">
            <span class="metric-val" style="color: #e11d48;">${total - this.score}</span>
            <span class="metric-lbl">Incorrect</span>
          </div>
          <div class="metric-box">
            <span class="metric-val" style="color: #2563eb;">${percentage}%</span>
            <span class="metric-lbl">Accuracy</span>
          </div>
          <div class="metric-box">
            <span class="metric-val" style="color: #7c3aed;">${total}</span>
            <span class="metric-lbl">Total Questions</span>
          </div>
        </div>

        <!-- Action Controls -->
        <div class="result-actions-dock">
          <button class="result-btn btn-retake" id="quizRetakeBtn">
            ↺ Retake Quiz
          </button>
          <button class="result-btn btn-review" id="quizToggleReviewBtn">
            📋 Review All Answers
          </button>
          <a href="reference.html" class="result-btn btn-ref">
            📚 Return to Slides
          </a>
        </div>

        <!-- Review Accordion Container -->
        <div class="quiz-answers-review" id="quizAnswersReview" style="display: none;">
          <h3 class="review-heading">Detailed Question Review (${total} Questions)</h3>
          <div class="review-items-list">
            ${this.userAnswers.map((item, idx) => `
              <div class="review-item-card ${item.isCorrect ? 'item-correct' : 'item-incorrect'}">
                <div class="review-item-header">
                  <span class="review-item-status">${item.isCorrect ? '✓ Correct' : '✗ Incorrect'}</span>
                  <span class="review-item-category">${item.categoryLabel}</span>
                </div>
                <div class="review-item-question">${idx + 1}. ${item.question}</div>
                <div class="review-item-options">
                  <div class="review-choice user-choice ${item.isCorrect ? 'choice-correct' : 'choice-incorrect'}">
                    <strong>Your Answer:</strong> ${item.options[item.selectedIndex] || 'Skipped'}
                  </div>
                  ${!item.isCorrect ? `
                    <div class="review-choice correct-choice">
                      <strong>Correct Answer:</strong> ${item.options[item.correctIndex]}
                    </div>
                  ` : ''}
                </div>
                <div class="review-item-explanation">
                  💡 <strong>Explanation:</strong> ${item.explanation.replace(/\n/g, '<br>')}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>
    `;

    // Retake handler
    this.container.querySelector('#quizRetakeBtn').addEventListener('click', () => {
      this.currentIndex = 0;
      this.score = 0;
      this.hasAnswered = false;
      this.userAnswers = [];
      this.loadQuestion();
    });

    // Toggle Review Handler
    const toggleBtn = this.container.querySelector('#quizToggleReviewBtn');
    const reviewContainer = this.container.querySelector('#quizAnswersReview');
    toggleBtn.addEventListener('click', () => {
      if (reviewContainer.style.display === 'none') {
        reviewContainer.style.display = 'block';
        toggleBtn.textContent = "▲ Hide Answers Review";
        reviewContainer.scrollIntoView({ behavior: 'smooth' });
      } else {
        reviewContainer.style.display = 'none';
        toggleBtn.textContent = "📋 Review All Answers";
      }
    });
  }
}

// Global initialization helper
window.QuizEngine = QuizEngine;
window.QUIZ_QUESTIONS = QUIZ_QUESTIONS;

document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('standaloneQuizContainer')) {
    window.mainQuizEngine = new QuizEngine('standaloneQuizContainer');
  }

  if (document.getElementById('slideEmbeddedQuizContainer')) {
    window.embeddedQuizEngine = new QuizEngine('slideEmbeddedQuizContainer', { isEmbedded: true });
  }
});
