import pyttsx3

def main():
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say("First time i'm using a package in next.py course")
    engine.runAndWait()

if __name__ == "__main__":
    main()