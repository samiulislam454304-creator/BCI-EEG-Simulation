# BCI-EEG Signal Processing System

A Python-based Brain-Computer Interface (BCI) system that streams real-time EEG brainwave microvolt signals ($\mu V$) from the **PhysioNet EEG Motor Movement/Imagery Dataset** and classifies them into distinct cognitive states using signal filtering.

## 🧠 Features & Mind States
* **PhysioNet Integration:** Fetches real human EEG brainwave data.
* **Signal Filtering:** Applies 1–40 Hz bandpass filtering using `mne` to remove noise.
* **RELAXED (< 15 $\mu V$):** Low activity / Resting state (IDLE).
* **FOCUS (15–35 $\mu V$):** Moderate activity / Standard task processing.
* **ALERT / HIGH STRESS (> 35 $\mu V$):** High activity / Turbo action trigger.

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3
* **Libraries:** `mne`, `numpy`

## 🚀 How to Run
1. Install the required libraries:
   ```bash
   pip install mne numpy matplotlib
