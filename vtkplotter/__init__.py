"""
A python class to easily draw, analyse and animate 3D objects.

![tea1](https://user-images.githubusercontent.com/32848391/46815773-dc919500-cd7b-11e8-8e80-8b83f760a303.png)

## [**Git website**](https://github.com/marcomusy/vtkplotter) 
"""

__author__     = "Marco Musy"
__license__    = "MIT" 
__maintainer__ = "M. Musy, G. Dalmasso"
__email__      = "marco.musy@embl.es"
__status__     = "dev"
__website__    = "https://github.com/marcomusy/vtkplotter"

__version__    = "8.7.4" ### defined also in setup.py


# frequently used stuff
from vtkplotter.plotter import Plotter, show
from vtkplotter.colors import colorMap, printc
from vtkplotter.vtkio import ProgressBar, load
from vtkplotter.utils import vector, mag, mag2, norm, to_precision
from vtkplotter.actors import Actor, Assembly, ImageActor

from numpy import sin, cos, sqrt, exp, log, dot, cross, array, arange

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


