from .processor import Processor, StringProcessor
from .output import Output
from .debug import log


class LogMine():
    def __init__(self, **options):
        log("LogMine: init with config:", options)
        processor_config = {k: options.get(k, None) for k in (
            'single_core',
            'output_file'
        )}
        print(processor_config)
        print("---")
        cluster_config = {k: options.get(k, None) for k in (
            'max_dist',
            'variables',
            'delimeters',
            'min_members',
            'k1',
            'k2',
        )}
        output_options = {k: options.get(k, None) for k in (
            'sorted',
            'number_align',
            'pattern_placeholder',
            'mask_variables',
            'highlight_patterns',
            'highlight_variables',
        )}
        self.processor = Processor(processor_config, cluster_config)
        self.string_processor = StringProcessor(cluster_config)
        self.output = Output(output_options)

    def run(self, files):
        log("LogMine: run with files:", files)
        clusters = self.processor.process(files)
        log("LogMine: output cluster:", clusters)
        self.output.out(clusters)

    def run_with_string(self, string):
        log("LogMine: run with string:", string)
        clusters = self.string_processor.process(string)
        log("LogMine: output cluster:", clusters)
        return clusters
