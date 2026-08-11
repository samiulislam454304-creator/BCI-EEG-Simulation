import random
import time

def fake_bci_signal():
    """ একাধিক ব্রেনওয়েভ সিগন্যাল তৈরির জন্য সিমুলেটর """
    return random.randint(10, 50)

print("--- ADVANCED BCI MULTI-STATE SYSTEM STARTED ---")

# ১০ রাউন্ডের অ্যাডভান্সড সিগন্যাল টেস্টিং
for i in range(1, 11):
    bci_signal = fake_bci_signal()
    
    # ৩টি মাইন্ড স্টেট লজিক
    if bci_signal <= 25:
        state = "RELAXED  [ 🧘 ]"
        action = "গাড়ি ধীর গতিতে চলছে"
    elif 26 <= bci_signal <= 40:
        state = "FOCUS    [ 🚗 ]"
        action = "গাড়ি স্বাভাবিক গতিতে চলছে"
    else:
        state = "ALERT!!  [ ⚡ ]"
        action = "গাড়ি টার্বো স্পিডে ছুটছে!"
        
    print(f"Step {i:02d} | Signal: {bci_signal}uV | State: {state} | Action: {action}")
    time.sleep(0.5)

print("--- SIMULATION COMPLETE ---")
