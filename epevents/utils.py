import types

def fire_me(handler, *args):
    """
    Behaves like javascript functions. Unspecified args are `None`, extra args
    are ignored.
    
    @param handler: callable function/method type
    @params ...: anything to pass to handler
    """
    
    argc = handler.__code__.co_argcount
    if isinstance(handler, types.MethodType):
        argc -= 1
    
    if len(args) >= argc:
        return handler(*args[:argc])
    
    if len(args) < argc:
        argc -= len(args)
        args = args + tuple(None for _ in range(argc))
        return handler(*args)


def ensure_fire(handlers, args, wrap=None):
    "This holds any errors raised until all handlers have been fired"
    errors = []
    
    for h in handlers:
        try:
            if wrap:
                yield wrap(h, *args)
            else:
                yield h(*args)
        
        except Exception as e: # pylint: disable=broad-except
            errors.append(e)
    
    for e in errors:
        raise e


def check_missing(args, verify):
    "Determine which args in verify are missing or excessive"
    alen, vlen = len(args), len(verify)
    
    if alen > vlen:
        missing = args[vlen:]
        raise ArgsError("missing args: [{}]".format(", ".join(missing)))
    
    elif alen < vlen:
        extra = (str(i) for i in verify[alen:])
        raise ArgsError("too many args: [{}]".format(", ".join(extra)))


class ArgsError(AttributeError):
    pass
