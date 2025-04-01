class Logger:
    def Log(self, msg):
        print(f"\033[32m {msg} \033[0m")

    def Error(self, msg):
        print(f"\033[31m {msg} \033[0m")

    def Warn(self, msg):
        print(f"\033[38;5;208m {msg} \033[0m")


class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def Write(self, text):
        with open(self.filename, "a") as f:
            f.write(text)

    def WriteLine(self, text):
        with open(self.filename, "a") as f:
            f.write(text + "\n")


class FileLogger:
    def __init__(self, filename):
        self.writer = FileWriter(filename)

    def Log(self, msg):
        self.writer.WriteLine(msg)

    def Error(self, msg):
        self.writer.WriteLine(f"ERROR: {msg}")

    def Warn(self, msg):
        self.writer.WriteLine(f"WARN: {msg}")


if __name__ == "__main__":
    logger = Logger()
    logger.Log("Lorem ipsum")
    logger.Error("Error message")
    logger.Warn("Warning message")
    file_logger = FileLogger("log.txt")
    file_logger.Log("Lorem ipsum")
    file_logger.Error("Error message")
    file_logger.Warn("Warming message")
