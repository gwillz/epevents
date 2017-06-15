class Event(object):
    "C# style events for Python"
    
    def __init__(self):
        self.handlers = []
    
    def add(self, handler):
        self.handlers.append(handler)
        return self
    
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    
    def clear(self):
        "Remove all handlers"
        self.handlers = []
    
    def fire(self, sender, eargs=None):
        "Immediately execute each of the handlers with sender and eargs and parameters."
        return tuple(h(sender, eargs) for h in self.handlers)
    
    def __contains__(self, handler):
        return handler in self.handlers
    
    __iadd__ = add
    __isub__ = remove
    __call__ = fire
