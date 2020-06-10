__author__ = 'Susanna Grasso'

from pywps import Process, LiteralInput, LiteralOutput, Format, ComplexOutput
import os, sys
import pywps.configuration as config

class Test_syspath(Process):

    def __init__(self):
        outputs = [LiteralOutput('text_output0', 'alcune variabili definite in pywps.cfg', data_type='string'),
                   LiteralOutput('text_output1', 'sys.path', data_type='string'),
                   LiteralOutput('text_output2', 'environ', data_type='string')
                  ]
        super(Test_syspath, self).__init__(
            self._handler,
            identifier='test_syspath',
            version='0.1',
            title='Processo per testare alcune variabili',
            abstract='Il processo restituisce alcune variabili inserite nel file pywps.cfg e alcune variabili di sistema',
            outputs=outputs,
            store_supported=True,
            status_supported=True,
        )

    def _handler(self, request, response):
        #test import conf
        currentworkdir=self.workdir
        workdir=config.get_config_value('server', 'workdir')
        outputpath=config.get_config_value('server', 'outputpath')
        file_url = config.get_config_value('server', 'outputurl')
        gisbase = config.get_config_value('grass', 'gisbase')

        res='currentworkdir:'+str(currentworkdir)+'   workdir: '+str(workdir)+'    outputpath: '+ str(outputpath)+'    outputurl: '+str(file_url)+'     gisbase:'+str(g$
        response.outputs['text_output0'].data = res

        #sys.path
        res=''
        for p in sys.path:
            res+=str(p) + '\n'
        response.outputs['text_output1'].data = res

        #environ
        response.outputs['text_output2'].data=str(os.environ["PATH"])+'------------------------------------------------'+ str(os.environ["PYTHONPATH"])
        return response
