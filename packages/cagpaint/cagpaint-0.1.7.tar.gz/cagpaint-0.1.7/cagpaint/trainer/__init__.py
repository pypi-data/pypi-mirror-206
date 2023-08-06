from .trainer import Trainer
from .loss import *
from .data_utils import *
from .datasets import *
from .file_utils import *
from .instructions import *
from .metrics import *
from .model_utils import *
from .patch_seg import *
from .scp_utils import *
from .startup import *
from .unet3d import *
import importlib
import pkgutil

# Get the current package name
package_name = __name__

# Iterate through all the modules in the package
for _, module_name, _ in pkgutil.iter_modules(__path__):
    # Import the module
    module = importlib.import_module(f"{package_name}.{module_name}")

    # Iterate through all the attributes in the module
    for attr_name in dir(module):
        # Get the attribute
        attr = getattr(module, attr_name)

        # Check if the attribute is a class or a function
        if callable(attr) and not attr_name.startswith("__"):
            # Import the attribute into the package's namespace
            globals()[attr_name] = attr
