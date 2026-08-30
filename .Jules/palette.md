## 2024-05-18 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** Many icon-only buttons (like Gemini chat, sidebar toggles, bookmarks) lack descriptive text, making them inaccessible to screen readers. This is a common pattern in SPAs built quickly.
**Action:** Always verify that buttons containing only icons (e.g., FontAwesome `<i>` tags) have a descriptive `aria-label` attribute explaining their function.
