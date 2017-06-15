EmptyPage Events
================
From http://emptypage.jp/notes/pyevent.en.html

![build status](https://git.mk2es.com.au/mk2/epevents/badges/master/build.svg)
![coverage report](https://git.mk2es.com.au/mk2/epevents/badges/master/coverage.svg)


This library builds on the events API described by Masaaki Shibata.


## Fluid Events
This is a slight modification of the `Event` class to allow any number of args
for handlers and the `fire()` function without errors.

```py
from epevents import Fluid as Event

ev = Event()
ev += lambda a, b, c: print(a,b,c)
ev += lambda a: print(a)

ev.fire(1, 2)
# handler 1 => "1, 2, None"
# handler 2 => "1"
```


## Strict Events
This is the polar opposite of a 'Fluid' event. Permissible arguments are specific
on init and handlers and events will throw `ArgsError` whenever the rules are
broken.

```py
from epevents import Strict as Event

ev = Event('a', 'b')

ev += lambda a,b,c: print(a,b,c) # => throws ArgsError
ev += lambda a: print(a)         # => throws ArgsError

ev.fire(1)       # => throws ArgsError
ev.fire(1, 2, 3) # => throws ArgsError

# acceptable
ev += lambda a,b: print(a,b)
ev.fire(1,2)
```


Authors
-------
- [Gwilyn Saunders](https://git.gwillz.com.au/u/gwillz)
- [MK2 Engineering Solutions](https://mk2engineeringsolutions.com.au)
- [Masaaki Shibata](http://emptypage.jp)


Legal
-----
[Creative Commons CC BY License](https://creativecommons.org/licenses/by/2.1/jp/deed.en)
