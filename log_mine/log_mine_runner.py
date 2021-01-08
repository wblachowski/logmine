from .processor import Processor, StringProcessor
from .output import Output
from .debug import log


class LogMineRunner():
    def __init__(self, processor, output=None):
        self.processor = processor
        self.output = output

    def run(self, data):
        log("LogMine: run with data:", data)
        clusters = self.processor.process(data)
        log("LogMine: output cluster:", data)
        if self.output:
            self.output.out(clusters)
        return clusters

    def run_with_string(self, string):
        log("LogMine: run with string:", string)
        clusters = self.processor.process(string)
        log("LogMine: output cluster:", clusters)
        return clusters
