import time
import random

def loading_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def fake_hacking_simulation():
    print("Welcome to SecureBank!")
    time.sleep(1)  
    print("Account Balance: $5,000.00")
    time.sleep(1)

    print("\n--- SYSTEM ERROR ---")
    time.sleep(1)
    
    loading_effect("WARNING: Unusual activity detected...")
    time.sleep(1)
    
    loading_effect("Attempting to secure your account...")
    time.sleep(2)
    
    print("\n!! ALERT: SECURITY BREACH DETECTED !!")
    time.sleep(1)
    
    loading_effect("SECURITY WARNING: Your bank has been hacked!")
    time.sleep(1)
    
    loading_effect("Retrieving compromised information...")
    time.sleep(1)
    
    for i in range(3):
        print("Bank Account Number:", random.randint(1000, 9999), "XXXX XXXX", random.randint(1000, 9999))
        time.sleep(1)

    # print("\nJust kidding! Your bank is safe. This was only a prank.")
    # time.sleep(2)
    # print("Thanks for being a good sport! 😊")
    # print("\033[92mThis text is green!\033[0m")

# Run the prank
fake_hacking_simulation()