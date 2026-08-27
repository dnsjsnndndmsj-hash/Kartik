import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

safe = """
        function renderMcq() {
            if (currentMcqIndex >= currentMcqSession.length) {
                const qBox = document.getElementById('mcqQuestionBox');
                if(qBox) qBox.innerHTML = `Session Complete! You scored ${currentMcqScore} out of ${currentMcqSession.length}.`;

                const optBox = document.getElementById('mcqOptionsBox');
                if(optBox) optBox.innerHTML = '';

                const nBtn = document.getElementById('mcqNextBtn');
                if(nBtn) nBtn.style.display = 'none';

                const btn = document.createElement('button');
                btn.className = 'btn btn-outline';
                btn.textContent = 'Back to Chapters';
                btn.onclick = () => {
                    const sCont = document.getElementById('mcqSessionContainer');
                    if (sCont) sCont.style.display = 'none';
                    const grid = document.getElementById('mcqSubjectsGrid');
                    if (grid) grid.style.display = 'grid';
                    const fb = document.querySelector('#view-ncert-mcq .filter-bar');
                    if (fb) fb.style.display = 'flex';
                };
                if(optBox) optBox.appendChild(btn);
                return;
            }

            const q = currentMcqSession[currentMcqIndex];
            const qBox2 = document.getElementById('mcqQuestionBox');
            if(qBox2) qBox2.textContent = `Q${currentMcqIndex + 1}. ${q.q}`;

            const optionsBox = document.getElementById('mcqOptionsBox');
            if(optionsBox) {
                optionsBox.innerHTML = '';
                q.o.forEach((opt, idx) => {
                    const btn = document.createElement('button');
                    btn.className = 'quiz-opt';
                    btn.textContent = opt;
                    btn.onclick = () => selectMcqOption(idx, q.a, btn);
                    optionsBox.appendChild(btn);
                });
            }
            const next2 = document.getElementById('mcqNextBtn');
            if (next2) next2.style.display = 'none';
        }
"""

start = content.find("function renderMcq() {")
if start != -1:
    end = content.find("function selectMcqOption(", start)
    if end != -1:
        content = content[:start] + safe + content[end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
