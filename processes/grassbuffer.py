__author__ = 'Susanna Grasso'

from pywps import Process, LiteralInput, ComplexInput, ComplexOutput, LiteralOutput, Format, FORMATS
from pywps.validator.mode import MODE
import os,sys

class GrassBuffer(Process):

    def __init__(self):
        inputs = [ComplexInput('poly_in', 'Vettoriale GML in WGS84-UTM32N',
                  supported_formats=[Format('application/gml+xml')],
                  mode=MODE.SIMPLE),
                  LiteralInput('buffer', 'Buffer', data_type='float',
                  allowed_values=(0, 1, 10, (10, 10, 100), (100, 100, 1000)))]
        outputs = [ComplexOutput('buff_out', 'Buffered', 
                  supported_formats=[Format('application/gml+xml')
                  ])]
        super(GrassBuffer, self).__init__(
            self._handler,
            identifier='grassbuffer',
            version='0.1',
            title='GRASS g.gisenv -n',
            abstract='Il processo utilizzando la funzione v.buffer di GRASS restituisce un buffer del file vettoriale in formato GML caricato in EPSG 32632. Output temporaneo',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True,
            grass_location="epsg:32632"
        )

    def _handler(self, request, response):

        import grass.script as grass
        import grass.script.setup as gsetup
        import subprocess
        import logging
        import os, sys

        LOGGER = logging.getLogger('PYWPS')
        LOGGER.info(" ---- Start grassbufer process ---- ")
        print(" ---- Start grassbufer process ---- ")

        fun_config()
        #print (sys.path)

        distanza=float(request.inputs['buffer'][0].data)
        input_gml=request.inputs['poly_in'][0].file
        workdir = self.workdir
        output_gml=os.path.join(workdir,'buffer.gml')

        p1 = grass.start_command('v.in.ogr', input=input_gml, output='poly', overwrite = True, stderr=subprocess.PIPE)
        stdoutdata, stderrdata = p1.communicate()
        print("Error occured: %s" % stderrdata)

        #from grass.pygrass.modules import Module
        #Module('v.buffer',input='poly', distance=distanza, output='buffer', type="area")

        p2 = grass.start_command('v.buffer', input='poly', output='buffer', distance=distanza)
        stdoutdata, stderrdata = p2.communicate()
        print("Error occured: %s" % stderrdata)

        p3 = grass.start_command('v.out.ogr', input='buffer', output_layer='bufferlayer', output=output_gml, format='GML')
        stdoutdata, stderrdata = p3.communicate()
        print("Error occured: %s" % stderrdata)

        #response.outputs['buff_out'].output_format = FORMATS.GML
        response.outputs['buff_out'].file = output_gml
        return response
