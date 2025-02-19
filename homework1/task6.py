import pytest

filename = "task6_read_me.txt"
def word_counter(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return len(words)

text_files = [
    "task6_read_me.txt"
]

expected_counts = {
    "task6_read_me.txt": 104,
}

for filename in text_files:
    def make_test_function(filename):
        def test_word_count():
            assert word_counter(filename) == expected_counts[filename]
        return test_word_count

    test_name = f'test_word_count_{filename.replace(".", "_")}'
    globals()[test_name] = make_test_function(filename)

# I tried, I tried finding ways to implement this and am unable to find one that works fully based on the requirements

if __name__ == "__main__":
      pytest.main()