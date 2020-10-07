# Data Engineering Code Test

1. Fork this repository in order to get started
1. Parse the english words in the entire works of Shakespeare provided in `data/shakespeare.txt`
1. Create a database table with information on each of the words including at a minimum:
    * Unique word ID
    * Number of times the word is used in the provided text
1. Create a second database table containing the part of speech for each word
    * Obtain the part of speech by scraping Dictionary.com, starter code is included in the `scrape_dictionary/` folder
1. Come to the interview with your completed code, ready to discuss your data pipeline, database structure, how you would deploy and potential follow-on improvements.

## Overview

The repo has the following structure:
```
data-eng-test
|   README.md
|---data
|       shakespeare.txt
|---scrape_dictionary
        scrape_dictionary.py
        requirements.txt
```
* `data/shakespeare.txt` contains a full text file of all of the works of shakespeare
* `scrape_dictionary/scrape_dictionary.py` contains starter code for scraping Dictionary.com
    * This script uses Beautiful Soup, if you are unfamiliar refer to the [Beautiful Soup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Answers

### Pre-requisites

#### Runtimes
Make sure you have the following runtimes available

* Python 3.8.x
* docker 19.03.x
* docker-compose 1.27.x

#### Environment variables

```shell script
export FILE_PATH=/code/shakespeare.txt
export DATABASE_HOST=postgresql
export DATABASE_PORT=5432
export DATABASE_USER=docker
export DATABASE_PASSWORD=docker
export DATABASE_NAME=valore
```

### Pipeline

#### Launch dependencies
In order to launch `postgres` and create the initial schema issue the following command:

```shell script
./bin/launch_dependecies.sh
```

#### Running the Pipeline
Execute the following command to run the pipeline:

```shell script
./bin/run_pipeline.sh
```

#### Running Integration Test
For such a small pipeline we can get more value by only writing integration tests. In order to do that issue the
following command (once the previous step is done):

```shell script
./bin/run_integration.sh
```

#### Future work
* Making production ready the deployment of the pipeline should not be difficult since we already have a runnable docker
image.
* Speeding up the pipeline (specially when scrapping `dictionary.com`) by making it multi-thread either using internal
standard libraries or frameworks such as `dask`, should be considered since right now everything is running
sequentially.

### Airflow Vs Prefect
Comparing two similar and excellent technologies without knowing the whole infrastructure and current architecture would
be irresponsible. Normally this type of decisions boils down to whether you should buy it or build it, happy to discuss
more tomorrow during our 1:1.
