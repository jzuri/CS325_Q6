
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def debug(self, message):
        print('Debugging data")

    @abstractmethod
    def info(self, message):
        print("User info")

    @abstractmethod
    def warning(self, message):
        print("Warning message!")

    @abstractmethod
    def error(self, message):
        print("Error")

class LoggingLogger(Logger):
    def debug(self, message):
        print("Debugging data")

    def info(self, message):
        print("User info")

    def warning(self, message):
        print("Warning message!")

    def error(self, message):
        print("Error")
      
class LoguruLogger(Logger):
    def debug(self, message):
        print("Debugging data")

    def info(self, message):
        print("User info")

    def warning(self, message):
        print("Warning message!")

    def error(self, message):
        print("Error")

class ExampleClass:
    def __init__(self, logger: Logger):
        self.logger = logger

    def do_something(self):
        try:
            # Some logic here
            self.logger.debug("Doing something...")
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")

def main():
    logger1 = LoggingLogger()
    obj1 = ExampleClass(logger1)
    obj1.do_something()

    logger2 = LoguruLogger()
    obj2 = ExampleClass(logger2)
    obj2.do_something()

if __name__ == "__main__":
    main()
