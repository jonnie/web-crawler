OUTPUT_FILEPATH = './output.txt'
DOWNLOAD_DELAY  = 0.5 # number of seconds to wait between each url crawled

ITEM_PIPELINES = {
    'app.pipelines.ListOutputPipeline': 300,
}