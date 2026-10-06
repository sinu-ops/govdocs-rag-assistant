// Main application logic

document.addEventListener('DOMContentLoaded', () => {
    const askButton = document.getElementById('askButton');
    const questionInput = document.getElementById('question');

    askButton.addEventListener('click', () => {
        askQuestion(questionInput.value);
    });

    questionInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            askQuestion(questionInput.value);
        }
    });
});

async function askQuestion(questionText) {
    if (!questionText.trim()) return;

    const askButton = document.getElementById('askButton');
    const questionInput = document.getElementById('question');
    
    // Disable input
    askButton.disabled = true;
    askButton.innerText = 'Searching...';
    questionInput.disabled = true;

    // Display user question
    appendMessage(questionText, 'user');
    questionInput.value = '';

    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: questionText })
        });

        if (!response.ok) {
            throw new Error('API request failed');
        }

        const data = await response.json();
        
        // Display AI answer
        displayAnswer(data.answer);
        
        // Display sources
        if (data.sources && data.sources.length > 0) {
            displaySources(data.sources);
        }

    } catch (error) {
        console.error('Error:', error);
        appendMessage('Unable to connect to GovDocs API.', 'ai');
    } finally {
        // Enable input
        askButton.disabled = false;
        askButton.innerText = 'Ask';
        questionInput.disabled = false;
        questionInput.focus();
    }
}

function appendMessage(text, sender) {
    const messagesContainer = document.getElementById('chat-messages');
    const msgElement = document.createElement('div');
    msgElement.className = `message ${sender}`;
    
    if (sender === 'ai') {
        // Basic markdown formatting: **bold** -> <strong>bold</strong>, line breaks
        let formattedText = text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');
        msgElement.innerHTML = formattedText;
    } else {
        msgElement.innerText = text;
    }
    
    messagesContainer.appendChild(msgElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function displayAnswer(answer) {
    appendMessage(answer, 'ai');
}

function displaySources(sources) {
    const sourcesContainer = document.getElementById('sources');
    sourcesContainer.innerHTML = ''; // Clear previous sources
    
    sources.forEach((source, index) => {
        const card = document.createElement('div');
        card.className = 'source-card';
        
        const contentPreview = document.createElement('div');
        contentPreview.className = 'evidence-content';
        contentPreview.innerText = source.content;

        card.innerHTML = `
            <div class="source-header">
                <span>Source ${index + 1}</span>
                <span style="color: var(--success-green);">${source.status || 'Current'}</span>
            </div>
            <div class="source-title" title="${source.document_title}">${source.document_title}</div>
            <div class="source-meta">
                <span>Page: ${source.page || 'N/A'}</span>
                <span>Version: ${source.version || 'N/A'}</span>
            </div>
            <div class="evidence-toggle">View Evidence ▾</div>
        `;
        
        card.appendChild(contentPreview);
        
        // Toggle evidence
        card.addEventListener('click', () => {
            card.classList.toggle('active');
            card.classList.toggle('expanded');
        });
        
        sourcesContainer.appendChild(card);
    });
}