# PERCEPTRON
  **AUTHOR:** Ridham Singhal  
  **Student ID:** 26SCSE1010788  
  **TASK NAME:** TJ AI MEDIUM TASK  

---

## Overview
  This ***Perceptron*** takes study hours and attendance percentage to predict if the student will pass or fail  

---

## How it Works
  1. Takes in raw inputs (*i.e. study hours and attendance percentage*)  
  2. Normalizes them to be in the range [0,1]  
  3. Multiplies them with weights `study hours weight = W1 , attendance weight= W1`  
  4. Adds a bias to them `bias= -3`
  5. Passes Decision ```if weighted_sum >= 0: PASS, If weighted sum <=0: FAIL```

---

## Example Screenshot

Study hours = 12hrs  
Attendance = 75%  
Output= PASS  
   
<img width="575" height="230" alt="image" src="https://github.com/user-attachments/assets/5d58fe33-9720-49e9-97b9-db88d1f0dbf3" />

