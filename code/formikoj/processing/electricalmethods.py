from . import MethodManager
from formikoj.utils import *

class ElectricalDataManager(MethodManager):
    
    'Class for managing the processing of electrical data'
    
    def __init__(self, workdir):
        """Create an instance of the ElectricalDataManager class.
        
        Parameters
        ----------
        workdir: str
            Path of the project directory.
        """
        
        return 0

    def _plot_pseudosection(self, **kwargs):
        """Plot the apparent resistivity values as pseudosection.
        
        Parameters
        ----------
        **kwargs: arbitrary keyword arguments
            Keyword arguments forwarded to the underlying plotting methods of
            the matplotlib, e.g., 'fontsize', 'color'    
        """
        
        return 0
        
    def plot(self, type='', **kwargs):
        """Plot different visualizations of the data.
        
        Parameters
        ----------
        type: str
            Parameters defining which visualization to plot. Valid keywords
            are 'pseudosection', 'nra' (what else can we plot?).
            
        **kwargs: arbitrary keyword arguments
            Keyword arguments forwarded to the underlying plotting methods of
            the matplotlib, e.g., 'fontsize', 'color' etc.
        """
        
        return 0
