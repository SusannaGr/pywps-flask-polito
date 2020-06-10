__author__ = 'Susanna Grasso'

from pywps import Process, LiteralInput, LiteralOutput, Format
import os, sys

class Test_Grass(Process):

    def __init__(self):
        outputs = [LiteralOutput('text_output', 'Output text', data_type='string')]
        super(Test_Grass, self).__init__(
            self._handler,
            identifier='test_grass',
            version='0.1',
            title='GRASS g.gisenv -n',
            abstract='Il processo crea una location TEMPORANEA di GRASS utilizzando il codice EPSG fornito (32632) e utilizzando la funzione di GRASS "g.gisenv -n" restitusice il gis environment in uso',
            outputs=outputs,
            store_supported=True,
            status_supported=True,
            # grass_location="/home/osboxes/grassdata/ESPG32632"
            grass_location="epsg:32632"
        )

    def _handler(self, request, response):

        import grass.script as grass
        from grass.pygrass.modules import Module
        print("grass script importati")

        res=grass.parse_command('g.gisenv', flags='n')
        response.outputs['text_output'].data = res
        #response.outputs['text_output'].data = sys.path
        return response
