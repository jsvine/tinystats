# tinystats

`tinystats` is a command-line tool for fetching message, URL, and subscriber data for the TinyLetter newsletters you own. Built and maintained by the author of [Data Is Plural](https://tinyletter.com/data-is-plural), a weekly newsletter of interesting/curious datasets.

Looking for more customized reports? Try [`tinyapi`](https://github.com/jsvine/tinyapi), the Python library that powers `tinystats`.

## Warning

It's probably unwise to depend on `tinystats` for anything important. The library's functionality depends on TinyLetter's undocumented API. If that API changes, `tinystats` will likely break.

## Installation

Run the following command from [your computer's command line](http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything):

```
pip install tinystats
```

## Usage

`tinystats` can run four types of reports:

- `messages`: All messages you've sent; most recent first.
- `urls`: All URLs you've linked to; most clicked first.
- `subscribers`: All current subscribers to your newsletter; most recent first.
- `subcriber_count`: Simply prints the current number of subscribers to your newsletter.

To run a report, execute the command `tinystats [report-type] [your-newsletter-username]`. You'll be prompted for your password. (Your password is not stored *anywhere* or sent anywhere other than to TinyLetter's servers.)

By default, each command outputs the data as a CSV spreadsheet to the terminal's standard output. So, to save a spreadsheet of every URL I've included in [Data Is Plural](https://tinyletter.com/data-is-plural) as `dip-urls.csv`, I'd run this command:

```
tinystats urls data-is-plural > dip-urls.csv
```

## Details And Options

### `tinystats messages`

usage: tinystats messages [-h] [--include-content] [-p PASSWORD] [-n N]
                          [--format {csv,json}] [--sep SEP]
                          [--fields FIELDS [FIELDS ...]]
                          username

All messages you've sent; most recent first.

positional arguments:
  username

optional arguments:
  -h, --help            show this help message and exit
  --include-content     Include message content.
  -p PASSWORD, --password PASSWORD
  -n N                  Return only first X results.
  --format {csv,json}
  --sep SEP             Separator for CSV fields. Defaults to a comma.
  --fields FIELDS [FIELDS ...]
                        Return only these fields


### `tinystats urls`

usage: tinystats urls [-h] [-p PASSWORD] [-n N] [--format {csv,json}]
                      [--sep SEP] [--fields FIELDS [FIELDS ...]]
                      username

All URLs you've linked to; most clicked first.

positional arguments:
  username

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
  -n N                  Return only first X results.
  --format {csv,json}
  --sep SEP             Separator for CSV fields. Defaults to a comma.
  --fields FIELDS [FIELDS ...]
                        Return only these fields

### `tinystats subscribers`

usage: tinystats subscribers [-h] [-p PASSWORD] [-n N] [--format {csv,json}]
                             [--sep SEP] [--fields FIELDS [FIELDS ...]]
                             username

All current subscribers to your newsletter; most recent first.

positional arguments:
  username

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
  -n N                  Return only first X results.
  --format {csv,json}
  --sep SEP             Separator for CSV fields. Defaults to a comma.
  --fields FIELDS [FIELDS ...]
                        Return only these fields

### `tinystats subscriber_count`

usage: tinystats subscriber_count [-h] [-p PASSWORD] username

Current number of subscribers to your newsletter.

positional arguments:
  username

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD

## Feedback / Improvements?

[I'm all ears](https://github.com/jsvine/tinyapi/issues/).
