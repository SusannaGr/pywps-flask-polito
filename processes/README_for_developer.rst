Per importare le variabili configurate nel file pywps.cfg nei processi è possibile utilizzare:

**METODO 1 (Il più idoneo)**
-----------------------------
::

  import pywps.configuration as config
  
  
  currentworkdir=self.workdir                                     #Cartella temporanea corrente. Es: /var/www/pywps_flask_env/pywps-flask/workdir/pywps_process_l8q9kb06
  workdir=config.get_config_value('server', 'workdir')            #/var/www/pywps_flask_env/pywps-flask/workdir
  outputpath=config.get_config_value('server', 'outputpath')      #/var/www/pywps_flask_env/pywps-flask/outputs
  file_url = config.get_config_value('server', 'outputurl')       # http://localhost/outputs/
  GISBASE = config.get_config_value('grass', 'gisbase')           #/usr/local/src/grass7/grass-7.8.1/dist.x86_64-pc-linux-gnu


**METODO 2**
------------

Example for import GISBASE from pywps.cfg::

  from configparser import ConfigParser
  config = ConfigParser()
  proc_dir = os.path.dirname(os.path.abspath(__file__))
  #For accessing the file in the parent folder of the current folder
  **file= os.path.join(proc_dir, '../pywps.cfg')**
  **config.read(file)**
  
  GISBASE=config.get("grass", "gisbase")
