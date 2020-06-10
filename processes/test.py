import sys, os
import subprocess
from pywps import Process, ComplexInput, ComplexOutput, LiteralOutput, Format, FORMATS

#from pywps.inout.formats import FORMATS
# Input - output pywps FORMATS:
# https://pywps.readthedocs.io/en/latest/api.html#pywps.inout.formats.FORMATS
# https://pywps.readthedocs.io/en/master/_modules/pywps/inout/formats.html

__author__ = 'Susanna Grasso'

class Test(Process):
    def __init__(self):
        vector_input = [ComplexInput('vector_input', 'vector_input',[Format('application/gml+xml')])]
        vector_output = [ComplexOutput('vector_output', 'vector_output',[Format('application/gml+xml')])]
        super(Test, self).__init__(
            self._handler,
            identifier='test',
            title='Test esempio 3',
            abstract="""Processo che prevede l'inserimento di un file vettoriale GML o XML e restituzione dello stesso """,
            inputs=vector_input,
            outputs=vector_output,
            store_supported=True,
            status_supported=True
        )
    def _handler(self, request, response):
        input_gml = request.inputs['vector_input'][0].file
        file_name, file_extension = os.path.splitext(input_gml)
        print(file_name)
        print(file_extension)     

        ##In alternativa per prendere il nome del layer
        #from osgeo import ogr
        #inSource = ogr.Open(input_gml)
        #inLayer = inSource.GetLayer()
        #output_gml= inLayer.GetName() + '_buffer'

        output_gml= file_name + '_copia'+file_extension
        import shutil
        shutil.copyfile(input_gml,output_gml)
        response.outputs['vector_output'].file = output_gml
        return response
