import logging
from logging import INFO
from rich.logging import RichHandler


class CustomFormatter(logging.Formatter):

    # Formatting Configuration
    MODULE_FMT = "[yellow]\[%(module)-10s][/]"

    INFO_FMT = "%(levelname)-8s▶"
    DEBUG_FMT = "[black on white]%(levelname)-8s[/]▶"
    WARNING_FMT = "[black on yellow]%(levelname)-8s[/][yellow]▶[/yellow]"
    ERROR_FMT = "[black on red]%(levelname)-8s[/][red]▶[/red]"
    CRITICAL_FMT = "[black on purple]%(levelname)-8s[/][purple]▶[/purple]"

    DATEFORMAT = "[%X]"

    FORMATS = {
        logging.DEBUG: f"{MODULE_FMT}{DEBUG_FMT} %(message)s",
        logging.INFO: f"{MODULE_FMT}{INFO_FMT} %(message)s",
        logging.WARNING: f"{MODULE_FMT}{WARNING_FMT} %(message)s",
        logging.ERROR: f"{MODULE_FMT}{ERROR_FMT} %(message)s",
        logging.CRITICAL: f"{MODULE_FMT}{CRITICAL_FMT} %(message)s"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


DEBUGGER = 0
# Color
if DEBUGGER:
    color_handler = RichHandler(
            log_time_format="[%X]",
            show_level=False,
            rich_tracebacks=True,
            tracebacks_extra_lines=1,
            markup=True
            )
else:
    color_handler = RichHandler(
            log_time_format="[%X]",
            show_level=False,
            markup=True
            )

color_handler.setFormatter(CustomFormatter())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

log = logging.getLogger('rich')
log.setLevel(logging.DEBUG)
log.addHandler(color_handler)