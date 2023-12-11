# linkedin-crawler

Crawler for LinkedIn Company profiles.   
This automation scrapes company URLs and number of employees.  

## Setup
Requires Python 3.8 or higher.
Is is recommended to use a virtualenv for managing/scoping python packages.   


1. Install `pip packages`:

```sh
    pip install -r requirements.txt
```

2. Install playwright browsers:


```sh
    playwright install
```

## Run the crawler

The crawler receives two optional arguments: 
- input `-i`: defaults to `input.csv`
- output `-o`: defaults to `output.csv`

```sh
    python main.py [-i INPUT] [-o OUTPUT]
```

In order to crawl some LinkedIn features such as search you must provide credentials.   
When you run the crawler a browser window will promp you to login to LinkedIn.   
After you enter your credentials and possibly 2FA, the crawler will start.   
DO NOT CLOSE THE BROWSER WINDOW.   

### Example

```sh
    python main.py -i companies.csv
```

### Help

```sh
    python main.py --help
```
