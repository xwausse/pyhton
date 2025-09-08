import threading
from collections import Counter

def process_lines(lines, counter, lock):
    """Process a list of lines and update word counts"""
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    with lock:
        counter.update(local_counter)

if __name__ == "__main__":
    filename = "large_text.txt"
    num_threads = 4

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    step = len(lines) // num_threads
    threads = []
    counter = Counter()
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i != num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], counter, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Word occurrences:")
    for word, count in counter.most_common(10):  
        print(word, ":", count)
