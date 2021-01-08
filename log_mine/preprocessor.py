import re


class Preprocessor():
    def __init__(self, variables=None):
        if variables is None:
            variables = []
        parsed_variables = []
        for variable in variables:
            parts = variable.split(':')
            if len(parts) <= 1:
                raise Exception('Invalid variable fortmat')
            name = parts[0]
            wrapped_regex = ':'.join(parts[1:])
            regex = wrapped_regex[1:-1]
            parsed_variables.append((name, regex))
        self.variables = [
            (tuple[0], re.compile(tuple[1])) for tuple in parsed_variables
        ]

    def process(self, line):
        for (name, regex) in self.variables:
            line = re.sub(regex, name, line)
        return line
