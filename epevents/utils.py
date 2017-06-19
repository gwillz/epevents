import types
from contextlib import contextmanager

def fire_me(handler, *args):
    """
    Behaves like javascript functions. Unspecified args are `None`, extra args
    are ignored.
    
    @param handler: callable function/method type
    @params ...: anything to pass to handler
    """
    try: # decorator support
        wrapped = handler.__wrapped__
    except AttributeError:
        wrapped = handler
    
    # method support
    argc = wrapped.__code__.co_argcount
    if isinstance(wrapped, types.MethodType):
        argc -= 1
    
    # too many args
    if len(args) >= argc:
        return handler(*args[:argc])
    
    # too little args
    else: # len(args) < argc
        args = args + tuple(None for _ in range(argc - len(args)))
        return handler(*args)


@contextmanager
def ensure_fire(handlers, args, wrap=None):
    "This holds any errors raised until all handlers have been fired"
    results, errors = [], []
    
    for h in handlers:
        try:
            results.append(wrap(h, *args) if wrap else h(*args))
        except Exception as e: # pylint: disable=broad-except
            errors.append(e)
    
    # this goes into the 'as' variable
    yield results
    
    # this throws any errors after exiting the context manager
    for e in errors: raise e


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
