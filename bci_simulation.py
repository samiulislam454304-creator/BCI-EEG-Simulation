import mne
import numpy as np

def load_real_eeg_data():
    print("📥 PhysioNet থেকে আসল EEG ডেটাসেট লোড করা হচ্ছে...")
    
    # PhysioNet EEG Motor Movement/Imagery Dataset (Subject 1, Run 1)
    raw_files = mne.datasets.eegbci.load_data(subject=1, runs=[1])
    raw = mne.io.read_raw_edf(raw_files[0], preload=True, verbose=False)
    
    # নোয়েজ ফিল্টার করা (1-40 Hz)
    raw.filter(l_freq=1.0, h_freq=40.0)
    
    # সিগন্যাল মাইক্রোভোল্টে কনভার্ট করা
    data, times = raw.get_data(return_times=True)
    eeg_channel_1 = data[0] * 1e6
    
    print("\n✅ সফলভাবে আসল ব্রেন সিগন্যাল লোড হয়েছে!\n" + "-" * 50)
    
    # বাস্তব ব্রেন সিগন্যাল লুপ
    for i in range(0, min(100, len(eeg_channel_1)), 5):
        signal = abs(eeg_channel_1[i])
        
        if signal < 15:
            state = "RELAXED (Low Activity)"
            action = "IDLE"
        elif 15 <= signal <= 35:
            state = "FOCUS (Moderate Activity)"
            action = "NORMAL PROCESS"
        else:
            state = "ALERT / HIGH STRESS"
            action = "TURBO ACTION TRIGGERED"
            
        print(f"Time: {times[i]:.2f}s | Real Signal: {signal:.2f} uV | State: {state} | Action: {action}")

if __name__ == "__main__":
    load_real_eeg_data()
