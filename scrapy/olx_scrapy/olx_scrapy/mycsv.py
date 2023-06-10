from scrapy.exporters import CsvItemExporter

class MyCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['delimiter'] = ";"
        super(MyCsvItemExporter, self).__init__(*args, **kwargs)