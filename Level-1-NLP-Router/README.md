# NLP Intent Router 🚀

**Author:** Ridham Singhal  
**Student ID:** 26SCSE1010788  
**Organization:** TechnoJam AI Task  

---

## 📌 Overview

This project is a lightweight, rule-based **NLP Intent Router** written in Python. It processes user text queries by tokenizing input, removing common English stopwords, and routing the request to the appropriate support department based on keyword matching.

---

## 🛠️ How It Works

1. **Tokenization (`tokenizing_text`)**: Converts the input query to lowercase and splits it into individual words.
2. **Stopword Filtering (`removing_words`)**: Filters out common non-essential words (e.g., `"is"`, `"the"`, `"to"`) to extract core keywords.
3. **Intent Routing (`routing`)**: Evaluates the remaining keywords against target category lists and routes the query.

---
