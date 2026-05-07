from src.word_ladder import word_ladder
from src.dictionary import dictionary

if __name__ == "__main__":
    start = "cat"
    end = "dog"

    path, message = word_ladder(start, end, dictionary)

    print(message)

    if path:
        print(" -> ".join(path))