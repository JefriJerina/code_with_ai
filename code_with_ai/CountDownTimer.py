#!/usr/bin/env python3
"""
SimpleCountdownTimer.py - A simple countdown timer without LangChain dependencies
"""

import time
import sys

def countdown_timer(start_number=10, delay=1.0):
    """Run countdown from start_number to 0"""
    print("🚀 Starting countdown timer!")
    print("-" * 40)
    
    for i in range(start_number, -1, -1):
        if i == 0:
            print("🎉 Time's up! Countdown complete! 🎉")
        else:
            print(f"⏰ Countdown: {i}")
        
        if i > 0:
            time.sleep(delay)
    
    print("-" * 40)
    print("✅ Countdown timer completed!")

def main():
    """Main function"""
    try:
        start_num = 10
        delay = 1.0
        
        if len(sys.argv) > 1:
            start_num = int(sys.argv[1])
        if len(sys.argv) > 2:
            delay = float(sys.argv[2])
        
        countdown_timer(start_num, delay)
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Countdown timer stopped by user!")
    except ValueError as e:
        print(f"❌ Error: Invalid number format - {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()