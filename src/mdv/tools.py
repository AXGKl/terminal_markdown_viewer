import os
import shutil
import sys
import time

from .plugs import FileConfig, envget, here, plugins

# the global config dict, filled by conf plugin:
C = {}
cli_actions = []

now = lambda: int(time.time() * 1000)


def into(d, k, v):
    """
    adds k in d, with value v
    (walrus := not in all supported pyvers)
    """
    d[k] = v
    return d


PY3 = sys.version_info.major > 2


# https://github.com/axiros/terminal_markdown_viewer/issues/91
if sys.platform.startswith("win"):
    import colorama

    # will convert the 16 base colors but unfortunatelly not the 256 for the themes
    # -> provide -t d and it will work
    colorama.init()

# code analysis for hilite:
try:
    from pygments import lex, token
    from pygments.lexers import get_lexer_by_name
    from pygments.lexers import guess_lexer as pyg_guess_lexer

    have_pygments = True
except ImportError:  # pragma: no cover
    have_pygments = False


if PY3:
    unichr = chr
    from html import unescape

    bp = breakpoint

    get_element_children = lambda el: el

    string_type = str
else:
    from HTMLParser import HTMLParser

    unescape = HTMLParser().unescape
    get_element_children = lambda el: el.getchildren()

    string_type = basestring

    def bp():
        import pdb

        pdb.set_trace()


# try:
#     # in py3 not done automatically:
#     import xml.etree.cElementTree as etree
# except:
#     import xml.etree.ElementTree as etree


breakpoint = bp


def read_file(fn, kw={"encoding": "utf-8"} if PY3 else {}):
    fn = fn.replace("~", envget("HOME"))
    try:
        with open(fn, **kw) as fd:
            return fd.read()
    except:
        return ""


def_enc_set = [False]


def fix_py2_default_encoding():
    """ can be switched off when used as library"""
    if PY3:
        return
    if not def_enc_set[0]:
        import imp

        imp.reload(sys)
        sys.setdefaultencoding("utf-8")
        # no? see http://stackoverflow.com/a/29832646/4583360 ...
        def_enc_set[0] = True


S = {}
path = []


def ruler():
    j, k = 10, ""
    c = true_terminal_size(C)
    while j < c[0]:
        k += "----|--%s|" % j
        j += 10
    k += "-" * (c[0] - j + 10)
    return k[: c[0]]


def true_terminal_size(conf):
    """get terminal size for python3.3 or greater, using shutil.

    taken and modified from http://stackoverflow.com/a/14422538

    Returns:
        tuple: (column, rows) from terminal size, or (0, 0) if error.
    """
    fallback = conf["width_default"], conf["height_default"]
    try:
        ts = shutil.get_terminal_size(fallback=fallback)
        return ts.columns, ts.lines
    except:
        try:
            r, c = os.popen("stty size 2>/dev/null", "r").read().split()
        except:
            try:
                r, c = os.environ["LINES"], os.environ["COLUMNS"]
            except:
                return fallback
        if r:
            return int(c), int(r)


# ----------------------------------------------------------------------------- Logging
# this is just a simple fallback if not log plugin is loaded:


_pd = lambda kw: ", ".join(["%s: %s" % (k, v) for k, v in kw.items()])


class log:
    l = lambda msg, **kw: print(msg, "\t", _pd(kw), file=sys.stderr)
    info = debug = warning = error = l


die = lambda msg, **kw: (log.error(msg, **kw), sys.exit(1))


# ---------------------------------------------------------------------- Cached Property
# Our basic style mechanik is to use this after first calculation. Allows style.foo=23.

# this is basically stolen from 3.8's implementation , not available in 3.7
# we removed the rlock though, are single threaded and also some boilerplate not
# necessary for us
_NOT_FOUND = object()


class cached_property:
    def __init__(self, func):
        self.func = func
        self.attrname = None
        self.__doc__ = func.__doc__
        # self.lock = RLock()

    def __set_name__(self, owner, name):
        # the actual decorating action
        if self.attrname is None:
            self.attrname = name
        elif name != self.attrname:
            raise TypeError(
                "Cannot assign the same cached_property to two different names "
                f"({self.attrname!r} and {name!r})."
            )

    def __get__(self, instance, owner=None):
        n = self.attrname
        # if instance is None:
        #     return self
        # if self.attrname is None:
        #     raise TypeError(
        #         'Cannot use cached_property instance without calling __set_name__ on it.'
        #     )
        cache = instance.__dict__
        # except AttributeError:  # not all objects have __dict__ (e.g. class defines slots)
        #     msg = (
        #         f"No '__dict__' attribute on {type(instance).__name__!r} "
        #         f'instance to cache {self.attrname!r} property.'
        #     )
        #     raise TypeError(msg) from None
        val = cache.get(n, _NOT_FOUND)
        if val is _NOT_FOUND:
            # with self.lock:

            # check if another thread filled cache while we awaited lock
            val = cache.get(n, _NOT_FOUND)
            if val is _NOT_FOUND:
                val = self.func(instance)
                cache[n] = val
                # except TypeError:
                #     msg = (
                #         f"The '__dict__' attribute on {type(instance).__name__!r} instance "
                #         f'does not support item assignment for caching {self.attrname!r} property.'
                #     )
                #     raise TypeError(msg) from None
        return val
