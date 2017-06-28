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
        
        with ensure_fire(self.handlers, args) as results:
            pass
        # any exceptions will fire here
        return results
    
    def add(self, handler):
        argcount = handler.__code__.co_argcount
        argnames = handler.__code__.co_varnames[:argcount]
        
        # remove 'self'
        if isinstance(handler, types.MethodType):
            argnames = argnames[1:]
        
        check_missing(self.args, argnames)
        return Event.add(self, handler)
    
    __call__ = fire
    __iadd__ = add
    
    def __repr__(self):
        return "<StrictEvent object, accepts: [{}]>".format(", ".join(self.args))
    
    __unicode__ = __repr__
    __str__ = __repr__
    
