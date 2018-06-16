# majestic.py
Parsing the top n websites (rank and domain) from the majestic.com project.  
See more here: https://majestic.com/reports/majestic-million

**Installation**

`pip -r requirements.txt`

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

Executing `python majestic.py 200 -t de` will output:

![output](https://user-images.githubusercontent.com/38978231/41494194-4b167252-7110-11e8-8a7a-453b07f71b6a.png)
