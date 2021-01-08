import re
from .preprocessor import Preprocessor
from .line_scorer import LineScorer
from .pattern_generator import PatternGenerator


class Clusterer():
    def __init__(
            self,
            k1=1,
            k2=1,
            max_dist=0.6,
            variables=[],
            delimeters='\\s+',
            min_members=2):
        self.pattern_generator = PatternGenerator()
        self.delimeters = delimeters
        self.preprocessor = Preprocessor(variables)
        self.scorer = LineScorer(k1, k2)
        self.max_dist = max_dist
        self.min_members = min_members
        # Each cluster is an array of
        # [representative line as list of fields, count, pattern, list of original logs]
        self.clusters = []

    def reset(self):
        self.clusters = []

    def process_line(self, line):
        processed_line = self.preprocessor.process(line)
        processed_tokens = re.split(self.delimeters, processed_line.strip())

        found = False
        for i in range(len(self.clusters)):
            [representative, _, pattern, _] = self.clusters[i]
            score = self.scorer.distance(
                # representative, processed_tokens, self.max_dist
                representative, processed_tokens, self.max_dist
            )
            if score <= self.max_dist:
                found = True
                self.clusters[i][1] += 1
                merged_pattern = self.pattern_generator.create_pattern(
                    pattern, processed_tokens)
                self.clusters[i][2] = merged_pattern
                self.clusters[i][3].append(line)
                break
        if not found:
            self.clusters.append(
                [processed_tokens, 1, processed_tokens, [line]])

    def result(self):
        if self.min_members > 1:
            return [c for c in self.clusters if c[1] >= self.min_members]
        else:
            return self.clusters

    def find(self, iterable_logs):
        self.reset()
        for line in iterable_logs:
            self.process_line(line)
        return self.result()
