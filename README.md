logmine - a log pattern analyzer CLI
==
[![PyPI version](https://badge.fury.io/py/logmine.svg)](https://badge.fury.io/py/logmine)

A command-line tool to help you quickly inspect your log files and identify
patterns.

Install
---

    pip install logmine

Usage
---

    cat sample/Apache_2k.log | logmine

`logmine` helps to cluster the logs into multiple clusters with common patterns
along with the number of messages in each cluster.

![image](https://user-images.githubusercontent.com/4214509/68392139-195cd500-01a4-11ea-907a-1a4391f23daa.png)

You can have more granular clusters by adjusting `-m` value, the lower the
value, the more details you will get.

    cat sample/Apache_2k.log | logmine -m0.2
    
![image](https://user-images.githubusercontent.com/4214509/68392281-6d67b980-01a4-11ea-96bc-92558a2a0e36.png)

The texts in red are the placeholder for multiple values that fit in the
pattern, you can replace those with your own placeholder.

    cat sample/Apache_2k.log | logmine -m0.2 -p'---'

![image](https://user-images.githubusercontent.com/4214509/68390718-d9e0b980-01a0-11ea-965c-38e44c32427f.png)

You can define variables to reduce the number unnecessary patterns and have
less clusters. For example, the command bellow replaces all time texts
with `<time>` variable.

    cat sample/Apache_2k.log | logmine -m0.2 -p'---' -v "<time>:/\\d{2}:\\d{2}:\\d{2}/"

![image](https://user-images.githubusercontent.com/4214509/68391053-a7838c00-01a1-11ea-992c-2e06bd4cfaa2.png)

[See all available options](#all-options)

How it works
---

LogMine is an implementation of the same name paper [LogMine: Fast Pattern
Recognition for Log Analytics](https://www.cs.unm.edu/~mueen/Papers/LogMine.pdf).
The idea is to use a distance function to calculate a distance between to log
line and group them into clusters.

![image](https://user-images.githubusercontent.com/4214509/68390818-08f72b00-01a1-11ea-8015-8d71ed100c0a.png)

The distance function is designed to work well on log dataset, where all log
messages from the same application are generated by a finite set of formats.

The Max Distance variable (`max_dist` or the `-m` option) represents the
maximum distance between any log message in a cluster. The smaller `max_dist`,
the more clusters will be generated. This can be useful to analyze a set of log
messages at multiple levels.

![image](https://user-images.githubusercontent.com/4214509/68390841-19a7a100-01a1-11ea-9a6e-38d2741a41c7.png)

More details on the clustering algorithm and pattern generation are available
in the paper.

Features
---

- Customizable `max_dist` and many other variables
- Parallel processing on multiple cores
- Colorful output
- Support pipe/redirect
- No dependencies
- Tail mode: watch the clusters on a continuous input stream (TODO)
- Sampling to reduce processing time on a large dataset (TODO)

Contribute / Development
---

- Welcome all contributions
- Create (if not yet exists) & activate virtual env:

        virtualenv -p $(which python3) .v
        source ./.v/bin/activate

- Run tests:

        ./test.sh

- Run the dev version:

        ./logmine sample/Apache_2k.log

- Publish:
    - Update the version value in `setup.py` following semver.
    - run `./publish.sh`

All options
---

```
usage: logmine [-h] [-m MAX_DIST] [-v [VARIABLES [VARIABLES ...]]]
               [-d DELIMETERS] [-i MIN_MEMBERS] [-k1 K1] [-k2 K2]
               [-s {desc,asc}] [-da] [-p PATTERN_PLACEHOLDER] [-dhp] [-dm]
               [-dhv] [-c]
               [-o OUTPUT_FILE]
               [file [file ...]]

LogMine: a log pattern analyzer

positional arguments:
  file                  Filenames or glob pattern to analyze. Default: stdin

optional arguments:
  -h, --help            show this help message and exit
  -m MAX_DIST, --max-dist MAX_DIST
                        This parameter control how the granularity of the
                        clustering algorithm. Lower the value will provide
                        more granular clusters (more clusters generated).
                        Default: 0.6
  -v [VARIABLES [VARIABLES ...]], --variables [VARIABLES [VARIABLES ...]]
                        List of variables to replace before process the log
                        file. A variable is a pair of name and a regex
                        pattern. Format: "name:/regex/". During processing
                        time, LogMine will consider all texts that match
                        varible regexes to be the same value. This is useful
                        to reduce the number of unnecessary cluster generated,
                        with trade off of processing time. Default: None
  -d DELIMETERS, --delimeters DELIMETERS
                        A regex pattern used to split a line into multiple
                        fields. Default: "\s+"
  -i MIN_MEMBERS, --min-members MIN_MEMBERS
                        Minimum number of members in a cluster to show in the
                        result. Default: 2
  -k1 K1, --fixed-value-weight K1
                        Internal weighting variable. This value will be used
                        as the weight value when two fields have the same
                        value. This is used in the score function to calculate
                        the distance between two lines. Default: 1
  -k2 K2, --variable-weight K2
                        Similar to k1 but for comparing variables. Two
                        variable is considering the same if they have same
                        name. Default: 1
  -s {desc,asc}, --sorted {desc,asc}
                        Sort the clusters by number of members. Default: desc
  -da, --disable-number-align
                        Disable number align in output. Default: True
  -p PATTERN_PLACEHOLDER, --pattern-placeholder PATTERN_PLACEHOLDER
                        Use a string as placeholder for patterns in output.
                        Default: None
  -dhp, --disable-highlight-patterns
                        Disable highlighting for patterns in output. Default:
                        True
  -dm, --disable-mask-variables
                        Disable masks for variables in output. When disabled
                        variables will be shown as the actual value. Default:
                        True
  -dhv, --disable-highlight-variables
                        Disable highlighting for variables in output. Default:
                        True
  -c, --single-core     Force LogMine to only run on 1 core. This will
                        increase the processing time. Note: the result output
                        can be different compare to when run with multicores,
                        this is expected. Default: False
  -o, --output-file     Name of the output JSON file. If not specified, 
                        nothing is saved. Default: None
```
