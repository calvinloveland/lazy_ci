"""Main entry point for lazy-ci."""

import configargparse

from loguru import logger

from lazy_ci.code_quality import run_code_quality
from lazy_ci.ship import ship


def main():
    """Main entry point for lazy-ci."""
    parser = configargparse.ArgParser(default_config_files=["config.yml"])
    parser.add("-c", "--config", is_config_file=True, help="config file path")
    parser.add("--code-quality", help="Run code quality checks", action="store_true")
    parser.add("--ship", help="Ship code", action="store_true")

    options = parser.parse_args()

    if options.code_quality:
        logger.info("Running code quality checks")
        if not run_code_quality():
            sys.exit(1)
    elif options.ship:
        logger.info("Shipping code!")
        if not run_code_quality():
            logger.critical("Code quality checks failed, not shipping code!!!")
            sys.exit(1)
        else:
            if not ship():
                sys.exit(1)
    else:
        logger.warning("No command provided, running code quality checks as default")
        if not run_code_quality():
            sys.exit(1)


if __name__ == "__main__":
    main()
