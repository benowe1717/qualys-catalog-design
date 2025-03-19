#!/usr/bin/env python3
"""
ParseArgs() class file
"""
import argparse

from src.classes.file_checker import FileChecker
from src.constants import constants


class ParseArgs():
    """
    Accept and validate command line parameters
    """
    NAME = constants.ARGPARSE_PROGRAM_NAME
    DESC = constants.ARGPARSE_PROGRAM_DESCRIPTION
    VERSION = constants.ARGPARSE_VERSION
    AUTHOR = constants.ARGPARSE_AUTHOR
    REPO = constants.ARGPARSE_REPO

    SUPPORTED_ARGS = constants.SUPPORTED_ARGS

    def __init__(self, args) -> None:
        self.args = args
        self.parser = self.create_parser()
        self.parse_args = self.parser.parse_args(self.args)
        self.handle_args()

    def create_parser(self) -> argparse.ArgumentParser:
        """
        Create the parser

        :return: The argument parser
        :rtype: argparse.ArgumentParser
        """
        parser = argparse.ArgumentParser(
            prog=self.NAME,
            description=self.DESC
        )

        parser.add_argument(
            '-v',
            '--version',
            action='store_true',
            required=False,
            help="Show this program's current version"
        )
        parser.add_argument(
            '-c',
            '--config-file',
            nargs=1,
            required=False,
            type=self.validate_config_file,
            help='Specify the full path to the config file'
        )
        msg = 'Specify the environment you need the environment built for. '
        msg += f'Supported environments are: [{"|".join(self.SUPPORTED_ARGS)}]'
        parser.add_argument(
            '-a',
            '--action',
            nargs=1,
            required=False,
            type=self.validate_action,
            help=msg
        )
        return parser

    def handle_args(self) -> None:
        """
        Handle all passed arguments

        :return: None
        :rtype: None
        """
        if len(self.args) == 0:
            self.parser.print_help()
            self.parser.exit()

        if self.parse_args.version:
            self._print_version()
            self.parser.exit()

        if self.parse_args.config_file:
            self.config_file = self.parse_args.config_file[0]
        else:
            self.parser.error('Config File is required but was not given!')

        if self.parse_args.action:
            self.action = self.parse_args.action[0]
        else:
            self.parser.error('Action is required but was not given!')

    def _print_version(self) -> None:
        """
        Print out the warranty and version number of the program.

        :return: None
        :rtype: None
        """
        print(f'{self.NAME} v{self.VERSION}')
        print(
            'This is free software:',
            'you are free to change and redistribute it.')
        print('There is NO WARARNTY, to the extent permitted by law.')
        print(f'Written by {self.AUTHOR}; see below for original code')
        print(f'<{self.REPO}>')

    def validate_action(self, a: str) -> str:
        """
        Validate that the given action is a supported action

        :param a: The action passed by the user
        :type a: str
        :raises argparse.ArgumentTypeError: If the given action is not a
        supported action
        :return: The action
        :rtype: str
        """
        if a.strip().lower() not in self.SUPPORTED_ARGS:
            msg = f'Supported actions: [{"|".join(self.SUPPORTED_ARGS)}]'
            raise argparse.ArgumentTypeError(msg)
        return a.strip().lower()

    def validate_config_file(self, f: str) -> FileChecker:
        """
        Validate that the given config file exists, is readable, and is valid
        YAML
        """
        fc = FileChecker(f.strip())
        if not fc.is_file():
            raise argparse.ArgumentTypeError(f'{fc.file} is not a file!')
        if not fc.is_readable():
            raise argparse.ArgumentTypeError(f'{fc.file} is not readable!')
        if not fc.is_yaml():
            raise argparse.ArgumentTypeError(f'{fc.file} is not valid YAML!')
        return fc
