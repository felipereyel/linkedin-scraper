# linkedin-scraper

Scraper for LinkedIn Company profiles.   
This automation scrapes company URLs and number of employees.  

## Setup
Requires Python 3.8 or higher.   
Is is recommended to use a `virtualenv` for managing python packages.   


1. Install `pip packages`:

```sh
    pip install -r requirements.txt
```

2. Install playwright browsers:


```sh
    playwright install
```

## Run the scraper

### Credentials Notice

In order to scrap some LinkedIn features such as search you must provide credentials.   
When you run the scraper a browser window will prompt you to login to LinkedIn.   
After you enter your credentials and possibly 2FA, the scraper will start.   
DO NOT CLOSE THE BROWSER WINDOW.   


### Command

The scraper receives two optional arguments: 
- input `-i`: defaults to `input.csv`; The expected format can be found at [input example](./examples/input.csv)
- output `-o`: defaults to `output.csv`; The result format can be found at [output example](./examples/output.csv)

```sh
    python main.py [-i INPUT] [-o OUTPUT]
```


### Example

```sh
    python main.py -i examples/input.csv -o examples/output.csv
```

### Help

```sh
    python main.py --help
```

## Notes on the system design

Here are some notes about the decisions made in this project and possibly future works.   

### About credentials

The scraping process in LinkedIn needs credentials and for this problem some options are available:

- Save credentials in a file
- Iterative session for the user to log in

For this MVP, the interactive session was chosen because although it requires user iteration, in the situation where LinkedIn or their CDN suspect network activity, they can ask for confirmation of a human being or token via email (which happened during development) and this makes the static credentials approach impossible.   

A future hybrid implementation is probably ideal, where the system starts with static credentials and in case of failure requests user interaction. 

### About CSS Selectors

In the [driver file](./scraper/driver.py) the scraping was done with css selectors.   
There is always the possibility of LinkedIn updating their website and changing the classes used, which would break the current implementation.

This is a serious problem but easily remedied if it happens.


### About parallelism

This process takes about a few seconds per enterprise thread, so a good next step would be to parallelize the procedure across worker threads.   

The necessary requirement for this improvement is the issue of credentials.
