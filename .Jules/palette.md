## 2024-03-24 - Add accessible labels to Gemini FAB
**Learning:** Found that the Gemini AI floating action button and its internal controls (close, microphone) lacked `aria-label`s, rendering them inaccessible to screen reader users as they are icon-only buttons.
**Action:** Adding explicit `aria-label` attributes to these buttons ensures they have an accessible name, making this critical chat/tutor feature usable for assistive technologies.
