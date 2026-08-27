import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

safe = """
        function startMcqSession(chapterId) {
            if (mcqData[chapterId]) {
                currentMcqSession = [...mcqData[chapterId]];
                currentMcqIndex = 0;
                currentMcqScore = 0;
                document.getElementById('mcqSubjectsGrid').style.display = 'none';
                const fb = document.querySelector('#view-ncert-mcq .filter-bar');
                if (fb) fb.style.display = 'none';
                document.getElementById('mcqSessionContainer').style.display = 'block';
                renderMcq();
            } else {
                alert('Questions for this chapter are currently being added.');
            }
        }
"""
start = content.find("function startMcqSession(chapterId) {")
if start != -1:
    end = content.find("function renderMcq() {", start)
    if end != -1:
        content = content[:start] + safe + content[end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
