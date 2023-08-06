from .trainer import Trainer
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
