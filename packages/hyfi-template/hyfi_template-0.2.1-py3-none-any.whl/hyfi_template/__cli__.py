"""Command line interface for hyfi_template"""

# Importing the libraries
import sys

from hyfi import hydra_main, about


def main() -> None:
    """Main function for the CLI"""
    sys.argv.append(f"--config-path={about.config_path}")
    hydra_main()


if __name__ == "__main__":
    main()
