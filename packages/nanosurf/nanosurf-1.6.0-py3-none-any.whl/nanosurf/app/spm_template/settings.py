""" Defines the configuration values of the module.
    Values in the ProStore are saved and loaded during application startup/shutdown automatically
Copyright Nanosurf AG 2021
License - MIT
"""

import enum
import pathlib
import os
from dataclasses import dataclass
import nanosurf as nsf

""" Available monitoring channels defined by the worker task"""
class MonitorChannelID(enum.IntEnum):
    User1Input = 0,
    Deflection = 1,

@dataclass
class Settings(nsf.PropStore):
    """ settings defined here as PropVal are stored persistently in a ini-file 
        Could be connected also to GUI elements (e.g.: look into bind_gui_elements() in gui.py)
    """
    repetitions = nsf.PropVal(int(300))
    time_per_repetition = nsf.PropVal(nsf.SciVal(0.1, "s"))
    channel_id = nsf.PropVal(int(MonitorChannelID.Deflection))
    save_path = nsf.PropVal(pathlib.Path(os.getenv(r"UserProfile")) / "Desktop")

@dataclass
class ModuleResults:
    """ This class saves the worker module result (e.g.: be read by gui elements like NSFChart or saved to file) """
    data_stream = nsf.SciStream()
    mean_value = nsf.SciVal()
    last_value = nsf.SciVal()
    last_index : int = -1

