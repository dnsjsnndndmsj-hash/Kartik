import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's add the NCERT Line-by-Line MCQs section to the HTML
mcq_section = """
        <section id="view-ncert-mcq" class="view-section">
            <h1 class="page-title"><i class="fa-solid fa-list-check" style="color:var(--primary)"></i> NCERT Line-by-Line MCQs</h1>
            <p class="page-subtitle">Master every sentence of the NCERT textbooks with pinpoint precision.</p>

            <div class="filter-bar">
                <button class="filter-btn active" data-subject="bio" onclick="filterMcqs('bio')">Biology</button>
                <button class="filter-btn" data-subject="chem" onclick="filterMcqs('chem')">Chemistry</button>
                <button class="filter-btn" data-subject="phys" onclick="filterMcqs('phys')">Physics</button>
            </div>

            <div class="grid" id="mcqSubjectsGrid">
                <!-- Biology Chapters -->
                <div class="card mcq-card subject-bio" onclick="startMcqSession('bio-ch1')">
                    <div class="card-icon"><i class="fa-solid fa-leaf"></i></div>
                    <h3>The Living World</h3>
                    <p>120 Questions extracted line-by-line</p>
                </div>
                <div class="card mcq-card subject-bio" onclick="startMcqSession('bio-ch2')">
                    <div class="card-icon"><i class="fa-solid fa-microbe"></i></div>
                    <h3>Biological Classification</h3>
                    <p>150 Questions extracted line-by-line</p>
                </div>
                <div class="card mcq-card subject-bio" onclick="startMcqSession('bio-ch8')">
                    <div class="card-icon"><i class="fa-solid fa-cube"></i></div>
                    <h3>Cell: The Unit of Life</h3>
                    <p>210 Questions extracted line-by-line</p>
                </div>

                <!-- Chemistry Chapters -->
                <div class="card mcq-card subject-chem" onclick="startMcqSession('chem-ch1')" style="display:none;">
                    <div class="card-icon"><i class="fa-solid fa-weight-scale"></i></div>
                    <h3>Some Basic Concepts</h3>
                    <p>90 Questions extracted line-by-line</p>
                </div>
                <div class="card mcq-card subject-chem" onclick="startMcqSession('chem-ch2')" style="display:none;">
                    <div class="card-icon"><i class="fa-solid fa-atom"></i></div>
                    <h3>Structure of Atom</h3>
                    <p>110 Questions extracted line-by-line</p>
                </div>

                <!-- Physics Chapters -->
                <div class="card mcq-card subject-phys" onclick="startMcqSession('phys-ch1')" style="display:none;">
                    <div class="card-icon"><i class="fa-solid fa-ruler"></i></div>
                    <h3>Units and Measurements</h3>
                    <p>85 Questions extracted line-by-line</p>
                </div>
                <div class="card mcq-card subject-phys" onclick="startMcqSession('phys-ch2')" style="display:none;">
                    <div class="card-icon"><i class="fa-solid fa-arrows-up-down-left-right"></i></div>
                    <h3>Vectors & Motion in 2D</h3>
                    <p>100 Questions extracted line-by-line</p>
                </div>
            </div>

            <div id="mcqSessionContainer" style="display:none; margin-top:2rem;">
                <div class="card">
                    <h3 id="mcqSessionTitle">Session Active</h3>
                    <div id="mcqQuestionBox" style="margin:2rem 0; font-size:1.2rem; font-weight:600;"></div>
                    <div id="mcqOptionsBox" style="display:flex; flex-direction:column; gap:1rem;"></div>
                    <button class="btn btn-primary" id="mcqNextBtn" onclick="nextMcq()" style="margin-top:2rem; display:none;">Next Question</button>
                </div>
            </div>
        </section>
"""

# Find where to inject it (after #view-ncert)
insert_point = content.find('</section>\n\n        <section id="view-settings"')
if insert_point != -1:
    content = content[:insert_point] + '</section>\n\n' + mcq_section + content[insert_point+11:]

# Add logic
script_logic = """
        // NCERT Line-by-Line MCQs Logic
        const mcqData = {
            'bio-ch1': [
                {q: "The term 'Biology' is derived from Greek words. What does 'bios' mean?", o: ["Life", "Study", "Earth", "Animals"], a: 0},
                {q: "Which of the following is NOT a defining property of living organisms?", o: ["Growth", "Reproduction", "Metabolism", "Cellular organization"], a: 1}
            ],
            'bio-ch2': [
                {q: "Who proposed the five-kingdom classification?", o: ["Linnaeus", "Whittaker", "Aristotle", "Pasteur"], a: 1}
            ],
            'bio-ch8': [
                {q: "Who first saw and described a live cell?", o: ["Robert Hooke", "Anton von Leeuwenhoek", "Matthias Schleiden", "Theodore Schwann"], a: 1}
            ]
        };

        let currentMcqSession = [];
        let currentMcqIndex = 0;
        let currentMcqScore = 0;

        function filterMcqs(subject) {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            document.querySelector(`.filter-btn[data-subject="${subject}"]`).classList.add('active');

            document.querySelectorAll('.mcq-card').forEach(c => {
                if (c.classList.contains(`subject-${subject}`)) c.style.display = 'flex';
                else c.style.display = 'none';
            });
            document.getElementById('mcqSessionContainer').style.display = 'none';
        }

        function startMcqSession(chapterId) {
            if (mcqData[chapterId]) {
                currentMcqSession = [...mcqData[chapterId]];
                currentMcqIndex = 0;
                currentMcqScore = 0;
                document.getElementById('mcqSubjectsGrid').style.display = 'none';
                document.querySelector('.filter-bar').style.display = 'none';
                document.getElementById('mcqSessionContainer').style.display = 'block';
                renderMcq();
            } else {
                alert('Questions for this chapter are currently being added.');
            }
        }

        function renderMcq() {
            if (currentMcqIndex >= currentMcqSession.length) {
                document.getElementById('mcqQuestionBox').innerHTML = `Session Complete! You scored ${currentMcqScore} out of ${currentMcqSession.length}.`;
                document.getElementById('mcqOptionsBox').innerHTML = '';
                document.getElementById('mcqNextBtn').style.display = 'none';

                const btn = document.createElement('button');
                btn.className = 'btn btn-outline';
                btn.textContent = 'Back to Chapters';
                btn.onclick = () => {
                    document.getElementById('mcqSessionContainer').style.display = 'none';
                    document.getElementById('mcqSubjectsGrid').style.display = 'grid';
                    document.querySelector('.filter-bar').style.display = 'flex';
                };
                document.getElementById('mcqOptionsBox').appendChild(btn);
                return;
            }

            const q = currentMcqSession[currentMcqIndex];
            document.getElementById('mcqQuestionBox').textContent = `Q${currentMcqIndex + 1}. ${q.q}`;

            const optionsBox = document.getElementById('mcqOptionsBox');
            optionsBox.innerHTML = '';

            q.o.forEach((opt, idx) => {
                const btn = document.createElement('button');
                btn.className = 'quiz-opt';
                btn.textContent = opt;
                btn.onclick = () => selectMcqOption(idx, q.a, btn);
                optionsBox.appendChild(btn);
            });

            document.getElementById('mcqNextBtn').style.display = 'none';
        }

        function selectMcqOption(selectedIdx, correctIdx, btnEl) {
            const btns = document.getElementById('mcqOptionsBox').querySelectorAll('.quiz-opt');
            btns.forEach(b => b.disabled = true);

            if (selectedIdx === correctIdx) {
                btnEl.style.background = 'var(--success)';
                btnEl.style.color = '#fff';
                currentMcqScore++;
            } else {
                btnEl.style.background = 'var(--danger)';
                btnEl.style.color = '#fff';
                btns[correctIdx].style.background = 'var(--success)';
                btns[correctIdx].style.color = '#fff';
            }

            document.getElementById('mcqNextBtn').style.display = 'inline-block';
        }

        function nextMcq() {
            currentMcqIndex++;
            renderMcq();
        }
"""
# inject script logic right before <script> ends
script_insert = content.rfind('</script>')
if script_insert != -1:
    content = content[:script_insert] + script_logic + content[script_insert:]

# add sidebar link
sidebar_insert = content.find('<div class="sidebar-item" onclick="switchView(\'ncert\')" data-view="ncert">')
if sidebar_insert != -1:
    content = content[:sidebar_insert] + '<div class="sidebar-item" onclick="switchView(\'ncert-mcq\')" data-view="ncert-mcq"><i class="fa-solid fa-list-check"></i> NCERT Line-by-Line</div>\n                        ' + content[sidebar_insert:]

# register view
# we don't strictly need to do much for switchView as it unhides automatically for view-* but let's make sure it's in the menu
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
