from scicam.constants import CAMERA_CONFIG_FILE
from collections import OrderedDict
import yaml


def load_setup_cameras(setup=None):
    with open(CAMERA_CONFIG_FILE, "r") as filehandle:
        config = yaml.load(filehandle, yaml.SafeLoader)
    
    # if setup is not None:
    #     config = config[setup]
        
        
    config_ordered = OrderedDict()
    if "FlirCamera" in config:
        config_ordered["FlirCamera"] = config["FlirCamera"]
    
    for k, v in config.items():
        if k != "FlirCamera":
            config_ordered[k] = v
        
    return config_ordered



def save_setup_cameras(config):
    config=dict(config)
    with open(CAMERA_CONFIG_FILE, "w") as filehandle:
        config = yaml.dump(config, filehandle, yaml.SafeDumper)
    
    return True