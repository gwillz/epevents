import types
from epevents import Event
from epevents.utils import ensure_fire, check_missing, ArgsError

class Strict(Event):
    """
    The 'Strict Event' requires definition of the args on init. It will then
    raise an `ArgsError` whenever these requirements are not adhered to. This
    includes checking of `fire()` parameters and handler function args.
    """
    
    def __init__(self, *arg_names):
        if len(set(arg_names)) != len(arg_names):
            raise ArgsError("Cannot accept args of same name")
        
        self.args = arg_names
        Event.__init__(self)
    
    def fire(self, *args):
        check_missing(self.args, args)
        yield from ensure_fire(self.handlers, args)
    
    def add(self, handler):
        varnames = handler.__code__.co_varnames
        if isinstance(handler, types.MethodType):
            varnames = varnames[1:]
        
        check_missing(self.args, varnames)
        return Event.add(self, handler)
    
    __iadd__ = add
    __call__ = fire
    
