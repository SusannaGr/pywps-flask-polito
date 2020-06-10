from pywps import Process, LiteralInput, ComplexInput, ComplexOutput, FORMATS, Format
from pywps.inout.outputs import MetaLink, MetaLink4, MetaFile

from pywps.inout.literaltypes import AllowedValue
from pywps.app.Common import Metadata

import os
import logging
LOGGER = logging.getLogger("PYWPS")


class Return_pdf_metalink(Process):
    def __init__(self):
        inputs = [
		    LiteralInput('namebacino', 'Nome del bacino',
                         data_type='string',
                         abstract="Inserire il nome del bacino",
                         min_occurs=1),
            ComplexInput('vectorbacino', 'Vettoriale del bacino',
                          abstract="Vettoriale del bacino delimitato in formato GML-XML",
                          supported_formats=[Format('application/gml+xml')]
                          )
        ]
        outputs = [
            ComplexOutput('output', 'METALINK v3 output',
                          abstract='Testing metalink v3 output',
                          as_reference=False,
                          supported_formats=[FORMATS.METALINK]),
            ComplexOutput('output_meta4', 'METALINK v4 output',
                          abstract='Testing metalink v4 output',
                          as_reference=False,
                          supported_formats=[FORMATS.META4])
        ]

        super(Return_pdf_metalink, self).__init__(
            self._handler,
            identifier='return_pdf_metalink',
            title='return_pdf_metalink',
            abstract='Inserimento di uno shapefile in formato GML e ritorno di un link per visualizzazione di un pdf scelto come esempio',
            version='0.1',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        response.update_status('PyWPS Process started.', 0)

        LOGGER.info("starting ...")
        max_outputs = 1

	#Genera un file di testo di prova
        #path=self.workdir
        filein="/var/www/pywps_env/pywps-flask/static/data/dummy.pdf"
        file="/var/www/pywps_env/pywps-flask/outputs/dummy.pdf"
        import shutil
        shutil.copy(filein, file)

        url="http://localhost/outputs/dummy.pdf"

        # generate MetaLink v3 output
        ml3 = MetaLink('Test PDF', 'Testing MetaLink with text files.', workdir=self.workdir)
        for i in range(max_outputs):
            mf = MetaFile('output_{}'.format(i), 'Test output', fmt=FORMATS.TEXT)
            #mf.data = 'output: {}'.format(i)
            mf.url=url
            ml3.append(mf)
        response.outputs['output'].data = ml3.xml

        # ... OR generate MetaLink v4 output (recommended)
        ml4 = MetaLink4('test-ml-1', 'Testing MetaLink with text files.', workdir=self.workdir)
        for i in range(max_outputs):
            mf = MetaFile('output_{}'.format(i), 'Test output', fmt=FORMATS.TEXT)
            #mf.data = 'output: {}'.format(i)
            mf.file=file
            ml4.append(mf)
        response.outputs['output_meta4'].data = ml4.xml

        response.update_status('PyWPS Process completed.', 100)
        return response
