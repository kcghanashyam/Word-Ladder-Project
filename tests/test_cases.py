from src.word_ladder import word_ladder
from src.dictionary import dictionary


def run_test(start, end):
    path, message = word_ladder(start, end, dictionary)

    print(f"\nTesting: {start} -> {end}")
    print(message)

    if path:
        print(" -> ".join(path))


run_test("cat", "dog")
run_test("cat", "part")
run_test("cat", "cat")
run_test("cat", "zoo")
run_test("cold", "most")