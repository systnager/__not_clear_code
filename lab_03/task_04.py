import re

class SmartTextReader:
    def read_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            lines = [list(line.rstrip("\n")) for line in f]
        return lines

class SmartTextChecker:
    def __init__(self, reader):
        self.reader = reader

    def read_file(self, filename):
        print(f"File '{filename}' opened successfully")
        result = self.reader.read_file(filename)
        print(f"File '{filename}' read successfully")
        print(f"File '{filename}' closed successfully")
        total_lines = len(result)
        total_chars = sum(len(line) for line in result)
        print(f"Total lines: {total_lines}, Total characters: {total_chars}")
        return result

class SmartTextReaderLocker:
    def __init__(self, reader, pattern):
        self.reader = reader
        self.pattern = pattern

    def read_file(self, filename):
        if re.search(self.pattern, filename):
            print("Access denied!")
            return None
        return self.reader.read_file(filename)



if __name__ == "__main__":
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("Hello World\nThis is a test file")
    with open("allowed.txt", "w", encoding="utf-8") as f:
        f.write("Allowed file\nSecond line")
    with open("restricted.txt", "w", encoding="utf-8") as f:
        f.write("Restricted file\nSecret data")
    reader = SmartTextReader()
    checker = SmartTextChecker(reader)
    locker = SmartTextReaderLocker(reader, r"restricted.*")
    print("SmartTextChecker output:")
    checker.read_file("sample.txt")
    print("\nSmartTextReaderLocker output for allowed file:")
    result_allowed = locker.read_file("allowed.txt")
    if result_allowed is not None:
        for row in result_allowed:
            print("".join(row))
    print("\nSmartTextReaderLocker output for restricted file:")
    locker.read_file("restricted.txt")
