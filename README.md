# Web Spider
This web spider will accept a start URL and will crawl internally within the site for all internal links. Then these are outputted into a file.

## Setting up the environment
This guide assumes that Python 3 is already installed. To setup this project follow these instructions:

    python3 -m venv env
    . env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

Note: if you get an error stating `python3` cannot be found simply replace this with `python`

## Running the web spider app
Run the following command to begin the crawl:

    scrapy runspider app/spider.py -a domain=example.com -a start_url=http://example.com

changing the `domain` to be the only domain you want to crawl within and `start_url` where to start the crawl from.

When the crawl has finished, the output by default will appear in the root of the project as `output.txt`.

Note: the crawl framework automatically respects the `robots.txt` file.

## Configuration
The filepath of the output file can be changed in `app/settings.py`:

    OUTPUT_FILEPATH = './output.txt'

In addition, the `DOWNLOAD_DELAY` can be changed in the same file:

    DOWNLOAD_DELAY = 0.5

As a default the system will process 2 URLs per second (2 x 0.5 = 1)