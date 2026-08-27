with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find("function bumpDailyQuest(type, amount) {")
end = content.find("function showQuestToast(quest)", start)

safe_bump = """function bumpDailyQuest(type, amount) {
            amount = amount || 1;
            let data = loadData();
            if (typeof ensureDailyQuestsFresh !== 'undefined') {
                data = ensureDailyQuestsFresh(data);
            }
            const dq = data.dailyQuests || { progress: {}, claimed: [] };
            dq.progress[type] = (dq.progress[type] || 0) + amount;
            let newlyClaimed = null;
            if (typeof QUEST_DEFS !== 'undefined' && QUEST_DEFS && Array.isArray(QUEST_DEFS)) {
                QUEST_DEFS.forEach(q => {
                    if (q.id === type && !dq.claimed.includes(q.id) && dq.progress[type] >= q.target) {
                        dq.claimed.push(q.id);
                        data.bonusXp = (data.bonusXp || 0) + q.xp;
                        newlyClaimed = q;
                    }
                });
            }
            saveData(data);
            if (document.getElementById('view-dashboard') && document.getElementById('view-dashboard').classList.contains('active')) {
                if (typeof renderDailyQuests !== 'undefined') renderDailyQuests(data);
                if (typeof renderXpCard !== 'undefined') renderXpCard(data);
                if (typeof renderAchievements !== 'undefined') renderAchievements(data);
                if (typeof renderDashboard !== 'undefined') renderDashboard();
            }
            if (newlyClaimed) {
                if (typeof showQuestToast !== 'undefined') showQuestToast(newlyClaimed);
            }
            return data;
        }
        """

if start != -1 and end != -1:
    content = content[:start] + safe_bump + content[end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success")
else:
    print("Failed to find", start, end)
