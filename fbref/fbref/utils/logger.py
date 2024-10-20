import logging
from functools import lru_cache
from typing import Optional

from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme

# Custom theme for Rich
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "critical": "bold white on red",
})

console = Console(color_system="256", width=150, theme=custom_theme)

@lru_cache
def get_logger(
    module_name: str,
    level: int = logging.INFO,
    log_file: Optional[str] = "logs/app.log",
    format_string: Optional[str] = None
) -> logging.Logger:
    """Get a customized logger for the module.

    Args:
        module_name (str): Name of the module.
        level (int): Logging level. Defaults to logging.DEBUG.
        log_file (Optional[str]): If provided, also log to this file.
        format_string (Optional[str]): Custom format string for log messages.

    Returns:
        logging.Logger: Customized logger for the module.
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(level)

    # Remove any existing handlers to avoid duplication
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Rich console handler
    rich_handler = RichHandler(
        rich_tracebacks=True,
        console=console,
        tracebacks_show_locals=True,
        tracebacks_extra_lines=2,
        tracebacks_theme="monokai",
        show_time=True,
        show_path=True,
    )

    # Use custom format string if provided, else use default
    if not format_string:
        format_string = "%(asctime)s - %(name)s - [%(threadName)s:%(funcName)s:%(lineno)d] - %(levelname)s - %(message)s"

    rich_handler.setFormatter(logging.Formatter(format_string))
    logger.addHandler(rich_handler)

    # Add file handler if log_file is specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(format_string))
        logger.addHandler(file_handler)

    return logger

# # Example usage
# if __name__ == "__main__":
#     logger = get_logger("example_module", level=logging.INFO, log_file="logs/app.log")
#     logger.info("This is an info message")
#     logger.warning("This is a warning message")
#     logger.error("This is an error message")
#     try:
#         1 / 0
#     except Exception as e:
#         logger.exception("An exception occurred")
