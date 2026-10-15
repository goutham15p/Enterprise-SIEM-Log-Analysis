
import time
import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - SECURITY_ALERT - %(levelname)s - %(message)s'
)

TARGET_IP = "192.168.1.45"
TARGET_PORT = 22
SUSPICIOUS_USERNAMES = ["admin", "root", "user1", "database_admin", "guest"]

def run_brute_force_simulation():
    logging.info(f"Initializing simulation tracking on target {TARGET_IP}:{TARGET_PORT}...")
    time.sleep(1)
    
   
    for attempt in range(1, 6):
        username = random.choice(SUSPICIOUS_USERNAMES)
        logging.warning(
            f"AUTH_FAILURE: SSH connection rejected for user '{username}' from source 203.0.113.5. "
            f"Reason: Invalid credentials. Attempt {attempt}/5."
        )
       patterns rather than human typing speeds
        time.sleep(0.5)
        
    
    logging.error(f"THRESHOLD_BREACHED: Multiple failed authentication patterns tracked on interface {TARGET_IP}.")

if __name__ == "__main__":
    try:
        run_brute_force_simulation()
    except KeyboardInterrupt:
        print("\nSimulation terminated by operator.")
