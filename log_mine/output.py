from .pattern_generator import PatternPlaceholder
from .variable import Variable
from .debug import log
import functools


CRED = '\33[31m'
CYELLOW = '\33[33m'
CEND = '\033[0m'


class Output():
    def __init__(self, sorted='desc', number_align=True, pattern_placeholder=None, mask_variables=True, highlight_patterns=True, highlight_variables=True):
        self.sorted = sorted
        self.number_align = number_align
        self.pattern_placeholder = pattern_placeholder
        self.mask_variables = mask_variables
        self.highlight_patterns = highlight_patterns
        self.highlight_variables = highlight_variables

    def out(self, clusters):
        log("Output: out", clusters)
        if len(clusters) == 0:
            return

        if self.sorted == 'desc':
            sort_func = functools.cmp_to_key(lambda x, y: y[1] - x[1])
            clusters = sorted(clusters, key=sort_func)
        if self.sorted == 'asc':
            sort_func = functools.cmp_to_key(lambda x, y: x[1] - y[1])
            clusters = sorted(clusters, key=sort_func)

        if self.number_align is True:
            width = max([len(str(c[1])) for c in clusters])
        else:
            width = 0

        for [fields, count, pattern, _] in clusters:
            output = []

            # Note: the length of "fields" can be different with the length of
            # "pattern", this is because with a large max_dist config, many
            # different lines are put into the same cluster, thus the pattern
            # is not accurate. For cases like this, just print the patterns to
            # be safe and avoid confusions.
            if len(fields) != len(pattern):
                log('subject = pattern')
                subject = pattern
            else:
                log('subject = fields')
                subject = fields

            for i in range(len(subject)):
                field = subject[i]
                if isinstance(pattern[i], PatternPlaceholder):
                    placeholder = self.pattern_placeholder
                    if placeholder is None:
                        value = field
                    else:
                        value = placeholder
                    if self.highlight_patterns is True:
                        value = CRED + value + CEND
                    output.append(value)
                elif isinstance(pattern[i], Variable):
                    if self.mask_variables is True:
                        value = str(field)
                    else:
                        value = field.name
                    if self.highlight_variables is True:
                        value = CYELLOW + value + CEND
                    output.append(value)
                else:
                    output.append(field)

            log("Output: start print -----------------------------------")
            print('%s %s' % (str(count).rjust(width), ' '.join(output)))
