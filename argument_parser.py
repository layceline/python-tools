import argparse


class ArgumentParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.required = self.parser.add_argument_group("required arguments")

    def add_required_argument(self, option_short, option_long, option_help):
        self.required.add_argument(option_short, option_long, help=option_help)

    def add_optional_argument(self, option_short, option_long, option_help):
        self.required.add_argument(option_short, option_long, help=option_help)

    def add_optional_flag(self, option_short, option_long, option_help):
        self.parser.add_argument(option_short, option_long, option_help,  action="store_true")

    def print_help(self):
        self.parser.print_help()

    def get_arguments(self):
        return self.parser.parse_args()


if __name__ == '__main__':

    args_parser = ArgumentParser()
    args_parser.add_optional_argument("-v", "--verbose", "Turn on verbose")
    args_parser.add_required_argument("-c", "--config", "Path to config file")
    args_parser.add_required_argument("-l", "--log-level", "Log level")
    args_parser.print_help()

    args = args_parser.get_arguments()

