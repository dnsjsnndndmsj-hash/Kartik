## 2024-09-06 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** Found several icon-only interactive elements (like the chat FAB and microphone button) that were missing `aria-label` attributes. Screen readers would only announce these as "button", rendering them inaccessible to visually impaired users who rely on screen readers.
**Action:** Always ensure that icon-only buttons include descriptive `aria-label`s. This is particularly important for floating action buttons or core interactive tools like the voice chat microphone.
