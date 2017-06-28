from epevents import Event
from epevents.utils import ensure_fire, fire_me

class Fluid(Event):
    """
    The 'Fluid Event' will accept any number of arguments when being fired.
    It also accepts handlers with varying arguments without error. Excessive
    args are filled with `None`.
    """
    
    def fire(self, *args):
        with ensure_fire(self.handlers, args, wrap=fire_me) as results:
            pass
        # any exceptions will fire here
        return results
    
    __call__ = fire
    
    def __repr__(self): # pragma: no cover
        return "<FluidEvent object, {} handlers>".format(len(self.handlers))
    
    __unicode__ = __repr__
    __str__ = __repr__
