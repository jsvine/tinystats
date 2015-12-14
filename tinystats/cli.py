#!/usr/bin/env python
import tinyapi
import argparse
from getpass import getpass
import unicodecsv as csv
import json
import re
import sys

def dot_notate(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [ (key + '.' + str(k), v) 
                for k, v in dot_notate(value).items() ]
        elif isinstance(value, list):
            return [ (key + "[" + str(i) + "]", v) 
                for i, v in enumerate(value) ]
        else:
            return [ (key, value) ]

    items = [ item for k, v in d.items() 
        for item in expand(k, v) ]

    return dict(items)

reject_pat = re.compile(r"__|\.id$|\[")

def reject_key(key):
    return re.search(reject_pat, key) != None        

def csvify(rows, fields=None, sep=","):
    if hasattr(sys.stdout, "buffer"):
        buf = sys.stdout.buffer
    else:
        buf = sys.stdout
    if fields == None:
        fields = list(sorted(k for k in dot_notate(rows[0]).keys()
            if not reject_key(k)))
        fields = [ fields.pop(fields.index("id")) ] + fields
    writer = csv.DictWriter(buf, fields, delimiter=sep, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(map(dot_notate, rows))

def jsonify(data):
    json.dump(data, sys.stdout, indent=2)

commands = [
    "messages",
    "urls",
    "subscribers",
    "subscriber_count",
]

class TinyStats(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser("tinystats")
        self.parser.add_argument("command", choices=commands)
        self.args = self.parser.parse_args(sys.argv[1:2])
        self.subparser = argparse.ArgumentParser(" ".join([
            self.parser.prog,
            self.args.command
        ]))
        getattr(self, self.args.command)()

    def add_shared_params(self):
        sp = self.subparser

    def emit(self, results):
        if self.subargs.format == "json":
            jsonify(results)
        else:
            csvify(results, fields=self.subargs.fields, sep=self.subargs.sep)

    def subcmd_init(self, all_options=True):
        sp = self.subparser
        sp.add_argument("username")
        sp.add_argument("-p", "--password")

        if all_options:
            sp.add_argument("-n", help="Return only first X results.",
                type=int)
            sp.add_argument("--format", default="csv",
                choices=[ "csv", "json" ])
            sp.add_argument("--sep", help="Separator for CSV fields. Defaults to a comma.", default=",")
            sp.add_argument("--fields", nargs="+",
                help="Return only these fields")

        self.subargs = sp.parse_args(sys.argv[2:])
        s = tinyapi.Session(
            self.subargs.username,
            (self.subargs.password or getpass())
        )
        return s

    def messages(self):
        self.subparser.description = "All messages you've sent; most recent first."
        self.subparser.add_argument("--include-content",
            help="Include message content.", action="store_true")
        s = self.subcmd_init()
        results = s.get_messages(
            statuses=["sent"],
            content=self.subargs.include_content,
            count=self.subargs.n
        )
        self.emit(results)

    def urls(self):
        self.subparser.description = "All URLs you've linked to; most clicked first."
        s = self.subcmd_init()
        results = s.get_urls(count=self.subargs.n)
        self.emit(results)

    def subscribers(self):
        self.subparser.description = "All current subscribers to your newsletter; most recent first."
        s = self.subcmd_init()
        results = s.get_subscribers(count=self.subargs.n)
        self.emit(results)

    def subscriber_count(self):
        self.subparser.description = "Current number of subscribers to your newsletter."
        s = self.subcmd_init(all_options=False)
        count = s.count_subscribers()
        print(count)

def main():
    TinyStats()

if __name__ == "__main__":
    main()
