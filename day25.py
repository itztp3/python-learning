import time

sentence = "Python helps us solve real problems"

print("=== Typing Speed Tester ===")
print("Type this sentence:")
print(sentence)

input("\nPress Enter when you are ready...")

start_time = time.time()
typed_text = input("\nStart typing: ")
end_time = time.time()

elapsed_time = end_time - start_time
words = len(typed_text.split())

if elapsed_time > 0:
    speed = words / (elapsed_time / 60)

    print("\n--- Your Results ---")
    print("Time:", round(elapsed_time, 2), "seconds")
    print("Words typed:", words)
    print("Typing speed:", round(speed, 2), "WPM")

    if typed_text == sentence:
        print("Accuracy: Exact match!")
    else:
        print("Accuracy: Sentence does not match.")

