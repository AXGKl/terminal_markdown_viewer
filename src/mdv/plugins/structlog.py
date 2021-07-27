plugin = 'log'
from mdv import tools

try:
    import structlog as sl
except Exception as ex:
    sl = None


now = tools.now
t0 = now()  # for millis from start:

ld = {'debug': 10, 'info': 20, 'warning': 30, 'error': 40}
# -------------------------------------------------------------------------- Processors
class FilterLevel:
    def __init__(self):
        self.level = 30
        self.drop = sl.DropEvent  # type: ignore

    def set_level(self, ld=ld):
        self.level = ld[tools.C['log_level']]

    def __call__(self, _, n, d, ld=ld):
        if ld.get(n) < self.level:  # first thing, no processor
            raise self.drop
        # in debug mode we *always* want the stack when logging exc:
        if 'exc' in d and self.level == 10:
            d['stack_info'] = True
        return d


# def filter_level(level, ld=ld, sl=sl, drop=drop):
#     cll = ld.get(level, 20)

#     def _filter_level(_, n, d, cll=cll, ld=ld, drop=drop):
#         if ld.get(n) < cll:
#             raise drop()
#         # in debug mode we *always* want the stack when logging exc:
#         if 'exc' in d and cll == 10:
#             d['stack_info'] = True
#         return d

#     return _filter_level


def ms_since_t0(l, n, d, t0=t0, now=now):
    d['timestamp'] = now() - t0
    return d


FL = [0]


def post_import():
    if not sl:
        return
    lfilter = FL[0] = FilterLevel()
    sl.configure(
        processors=[
            lfilter,
            sl.processors.add_log_level,
            sl.processors.StackInfoRenderer(),
            sl.dev.set_exc_info,
            ms_since_t0,
            sl.processors.format_exc_info,
            sl.dev.ConsoleRenderer(),
        ],
        context_class=dict,
        logger_factory=sl.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
    _ = sl.get_logger('mdv')

    log = tools.log
    log.info, log.debug, log.warning, log.error = _.info, _.debug, _.warning, _.error


hooks = {'post_import': post_import, 'post_conf': lambda: FL[0].set_level()}
