// Tải dữ liệu câu hỏi từ file JSON
let questionsData = [];

// Load questions từ file JSON
async function loadQuestions() {
    try {
        const response = await fetch('questions.json');
        questionsData = await response.json();
        console.log(`Đã tải ${questionsData.length} câu hỏi`);
        return true;
    } catch (error) {
        console.error('Lỗi khi tải câu hỏi:', error);
        // Fallback: sử dụng dữ liệu mẫu nếu không load được
        questionsData = [
            {
                id: 1,
                question: "Lỗi: Không thể tải câu hỏi từ file. Vui lòng kiểm tra file questions.json",
                answers: ["A", "B", "C", "D"],
                correctAnswer: 0
            }
        ];
        return false;
    }
}

// State management
let currentQuestionId = null;
let answeredQuestions = {}; // {questionId: {answered: true/false, correct: true/false, selectedAnswer: index}}
let questionOrder = []; // Danh sách ID câu hỏi theo thứ tự random
let currentFilter = 'all';

// Initialize app
async function init() {
    // Load questions first
    const loaded = await loadQuestions();
    if (!loaded) {
        alert('Không thể tải câu hỏi. Vui lòng kiểm tra file questions.json');
    }
    
    loadProgress();
    generateQuestionList();
    if (questionOrder.length === 0) {
        shuffleQuestions();
    }
    showQuestion(questionOrder[0]);
    updateStats();
    attachEventListeners();
}

// Shuffle questions for random order
function shuffleQuestions() {
    questionOrder = questionsData.map(q => q.id);
    for (let i = questionOrder.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [questionOrder[i], questionOrder[j]] = [questionOrder[j], questionOrder[i]];
    }
    saveProgress();
}

// Generate question list in sidebar
function generateQuestionList() {
    const questionList = document.getElementById('questionList');
    questionList.innerHTML = '';
    
    questionsData.forEach(q => {
        const item = document.createElement('div');
        item.className = 'question-item';
        item.textContent = q.id;
        item.dataset.questionId = q.id;
        
        if (answeredQuestions[q.id]) {
            if (answeredQuestions[q.id].correct) {
                item.classList.add('correct');
            } else {
                item.classList.add('incorrect');
            }
        }
        
        if (currentQuestionId === q.id) {
            item.classList.add('current');
        }
        
        item.addEventListener('click', () => {
            showQuestion(q.id);
        });
        
        questionList.appendChild(item);
    });
    
    applyFilter();
}

// Show a specific question
function showQuestion(questionId) {
    currentQuestionId = questionId;
    const question = questionsData.find(q => q.id === questionId);
    
    if (!question) return;
    
    document.getElementById('currentQuestionNumber').textContent = questionId;
    document.getElementById('questionText').textContent = question.question;
    
    const answersContainer = document.getElementById('answersContainer');
    answersContainer.innerHTML = '';
    
    question.answers.forEach((answer, index) => {
        const answerDiv = document.createElement('div');
        answerDiv.className = 'answer-option';
        answerDiv.dataset.answerIndex = index;
        
        const label = document.createElement('span');
        label.className = 'answer-label';
        label.textContent = String.fromCharCode(65 + index); // A, B, C, D
        
        const text = document.createElement('span');
        text.className = 'answer-text';
        text.textContent = answer;
        
        answerDiv.appendChild(label);
        answerDiv.appendChild(text);
        
        // If question was already answered, show the result
        if (answeredQuestions[questionId]) {
            answerDiv.classList.add('disabled');
            
            if (index === question.correctAnswer) {
                answerDiv.classList.add('correct');
            }
            
            if (index === answeredQuestions[questionId].selectedAnswer && index !== question.correctAnswer) {
                answerDiv.classList.add('incorrect');
            }
        } else {
            answerDiv.addEventListener('click', () => selectAnswer(questionId, index));
        }
        
        answersContainer.appendChild(answerDiv);
    });
    
    // Update result message
    const resultMessage = document.getElementById('resultMessage');
    resultMessage.classList.remove('show', 'correct', 'incorrect');
    
    if (answeredQuestions[questionId]) {
        resultMessage.classList.add('show');
        if (answeredQuestions[questionId].correct) {
            resultMessage.classList.add('correct');
            resultMessage.textContent = '✓ Chính xác! Bạn đã trả lời đúng.';
        } else {
            resultMessage.classList.add('incorrect');
            const correctAnswerLetter = String.fromCharCode(65 + question.correctAnswer);
            resultMessage.textContent = `✗ Sai rồi! Đáp án đúng là ${correctAnswerLetter}. ${question.answers[question.correctAnswer]}`;
        }
    }
    
    generateQuestionList();
    updateNavigationButtons();
    
    // Scroll to current question in sidebar
    const currentItem = document.querySelector(`.question-item[data-question-id="${questionId}"]`);
    if (currentItem) {
        currentItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

// Select an answer
function selectAnswer(questionId, answerIndex) {
    const question = questionsData.find(q => q.id === questionId);
    if (!question) return;
    
    const isCorrect = answerIndex === question.correctAnswer;
    
    answeredQuestions[questionId] = {
        answered: true,
        correct: isCorrect,
        selectedAnswer: answerIndex
    };
    
    saveProgress();
    showQuestion(questionId);
    updateStats();
}

// Update statistics
function updateStats() {
    const answered = Object.keys(answeredQuestions).length;
    const correct = Object.values(answeredQuestions).filter(a => a.correct).length;
    const incorrect = answered - correct;
    const accuracy = answered > 0 ? Math.round((correct / answered) * 100) : 0;
    
    document.getElementById('answered').textContent = answered;
    document.getElementById('total').textContent = questionsData.length;
    document.getElementById('correct').textContent = correct;
    document.getElementById('incorrect').textContent = incorrect;
    document.getElementById('accuracy').textContent = accuracy + '%';
}

// Navigation
function showNextQuestion() {
    const currentIndex = questionOrder.indexOf(currentQuestionId);
    if (currentIndex < questionOrder.length - 1) {
        showQuestion(questionOrder[currentIndex + 1]);
    }
}

function showPrevQuestion() {
    const currentIndex = questionOrder.indexOf(currentQuestionId);
    if (currentIndex > 0) {
        showQuestion(questionOrder[currentIndex - 1]);
    }
}

function showRandomQuestion() {
    // Get unanswered questions
    const unanswered = questionOrder.filter(id => !answeredQuestions[id]);
    
    if (unanswered.length > 0) {
        const randomId = unanswered[Math.floor(Math.random() * unanswered.length)];
        showQuestion(randomId);
    } else {
        // If all answered, show any random question
        const randomId = questionOrder[Math.floor(Math.random() * questionOrder.length)];
        showQuestion(randomId);
    }
}

function updateNavigationButtons() {
    const currentIndex = questionOrder.indexOf(currentQuestionId);
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    
    prevBtn.disabled = currentIndex === 0;
    nextBtn.disabled = currentIndex === questionOrder.length - 1;
}

// Reset progress
function resetProgress() {
    if (confirm('Bạn có chắc chắn muốn làm lại từ đầu? Tất cả tiến trình sẽ bị xóa.')) {
        answeredQuestions = {};
        shuffleQuestions();
        saveProgress();
        showQuestion(questionOrder[0]);
        updateStats();
        generateQuestionList();
    }
}

// Filter questions
function applyFilter() {
    const items = document.querySelectorAll('.question-item');
    
    items.forEach(item => {
        const questionId = parseInt(item.dataset.questionId);
        let show = true;
        
        if (currentFilter === 'correct') {
            show = answeredQuestions[questionId] && answeredQuestions[questionId].correct;
        } else if (currentFilter === 'incorrect') {
            show = answeredQuestions[questionId] && !answeredQuestions[questionId].correct;
        } else if (currentFilter === 'unanswered') {
            show = !answeredQuestions[questionId];
        }
        
        item.classList.toggle('hidden', !show);
    });
}

// Search questions
function searchQuestions(searchTerm) {
    const items = document.querySelectorAll('.question-item');
    
    if (!searchTerm) {
        applyFilter();
        return;
    }
    
    items.forEach(item => {
        const questionId = parseInt(item.dataset.questionId);
        const show = questionId.toString().includes(searchTerm);
        item.classList.toggle('hidden', !show);
    });
}

// Save progress to localStorage
function saveProgress() {
    localStorage.setItem('answeredQuestions', JSON.stringify(answeredQuestions));
    localStorage.setItem('questionOrder', JSON.stringify(questionOrder));
}

// Load progress from localStorage
function loadProgress() {
    const savedAnswers = localStorage.getItem('answeredQuestions');
    const savedOrder = localStorage.getItem('questionOrder');
    
    if (savedAnswers) {
        answeredQuestions = JSON.parse(savedAnswers);
    }
    
    if (savedOrder) {
        questionOrder = JSON.parse(savedOrder);
    }
}

// Event listeners
function attachEventListeners() {
    document.getElementById('nextBtn').addEventListener('click', showNextQuestion);
    document.getElementById('prevBtn').addEventListener('click', showPrevQuestion);
    document.getElementById('randomBtn').addEventListener('click', showRandomQuestion);
    document.getElementById('resetBtn').addEventListener('click', resetProgress);
    
    // Filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            currentFilter = e.target.dataset.filter;
            applyFilter();
        });
    });
    
    // Search input
    document.getElementById('searchInput').addEventListener('input', (e) => {
        searchQuestions(e.target.value);
    });
    
    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
            showPrevQuestion();
        } else if (e.key === 'ArrowRight') {
            showNextQuestion();
        } else if (e.key === 'r' || e.key === 'R') {
            showRandomQuestion();
        }
    });
}

// Start the app
init();
