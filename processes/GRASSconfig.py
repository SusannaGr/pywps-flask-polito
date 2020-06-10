import os,sys
from configparser import ConfigParser
config = ConfigParser()
file='/var/www/pywps_env/pywps-flask/pywps.cfg'
#file='../pywps.cfg'
config.read(file)

def fun_config():
    GISBASE=config.get("grass", "gisbase")
    #GISBASE="/usr/local/src/grass7/grass-7.8.1/dist.x86_64-pc-linux-gnu"
    GRASS_PATH=[os.path.join(GISBASE, "bin"),os.path.join(GISBASE, "scripts")]
    GRASS_LD_LIBRARY_PATH=os.path.join(GISBASE, "lib")
    GRASS_PYTHONPATH=[os.path.join(GISBASE, "etc/python"), os.path.join(GISBASE, "etc/python/grass/script/")]

    os.environ['PATH']+= os.pathsep + os.pathsep.join(GRASS_PATH)
    os.environ['LD_LIBRARY_PATH']= os.pathsep + os.pathsep.join(GRASS_LD_LIBRARY_PATH)
    os.environ['PYTHONPATH']=os.pathsep + os.pathsep.join(GRASS_PYTHONPATH)
    os.environ['GRASS_SKIP_MAPSET_OWNER_CHECK'] = '1'

    sys.path.append(GRASS_PYTHONPATH[0])
    sys.path.append(GRASS_PYTHONPATH[1])
    print (GISBASE)
