# majestic.py
Parsing the top n websites (rank and domain) from the majestic.com project. See more here: https://majestic.com/reports/majestic-million
Installation: `pip -r requirements.txt`

**Usage**

```
majestic.py [-h] [-t TLD] max

positional arguments:
  max                upper-limit (in hundreds) < 1000000

optional arguments:
  -h, --help         show this help message and exit
  -t TLD, --tld TLD  limits results to a specifc TLD (e.g. de)
```

**Example**

`python majestic.py 200 -t de`

[[https://camo.githubusercontent.com/5e46145e7d7bb066400cdd3b39f7554ab196942f/68747470733a2f2f692e696d6775722e636f6d2f554379396c44712e706e67|alt=output]]

