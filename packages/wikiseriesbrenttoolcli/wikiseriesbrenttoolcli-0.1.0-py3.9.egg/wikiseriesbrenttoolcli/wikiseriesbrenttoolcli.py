#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: wikiseriesbrenttoolcli.py
#
# Copyright 2023 brent de cubber
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
Main code for wikiseriesbrenttoolcli.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

"""

import logging
import logging.config
import json
import argparse
import coloredlogs
from wikiseriesbrentlib.wikiseriesbrentlib import search_series
from pathlib import Path


__author__ = '''brent de cubber <blah@hotmail.com>'''
__docformat__ = '''google'''
__date__ = '''01-05-2023'''
__copyright__ = '''Copyright 2023, brent de cubber'''
__credits__ = ["brent de cubber"]
__license__ = '''MIT'''
__maintainer__ = '''brent de cubber'''
__email__ = '''<blah@hotmail.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".


# This is the main prefix used for logging
LOGGER_BASENAME = '''wikiseriesbrenttoolcli'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


def get_arguments():
    """
    Gets us the cli arguments.

    Returns the args as parsed from the argsparser.
    """
    # https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='''a cli tool to use wikipedia to retrieve tv series information''')
    parser.add_argument('--log-config',
                        '-l',
                        action='store',
                        dest='logger_config',
                        help='The location of the logging config json file',
                        default='')
    parser.add_argument('--log-level',
                        '-L',
                        help='Provide the log level. Defaults to info.',
                        dest='log_level',
                        action='store',
                        default='info',
                        choices=['debug',
                                 'info',
                                 'warning',
                                 'error',
                                 'critical'])

    # examples:
    parser.add_argument('--name', '-n',
                        action='store',
                        help='Describe the parameter here',
                        type=str,
                        required=True)
    parser.add_argument('--path', '-p',
                        action='store',
                        required=False,
                        type=str,
                        )
    # parser.add_argument('--no-feature',
    #                     dest='feature',
    #                     action='store_false')
    args = parser.parse_args()
    return args


def setup_logging(level, config_file=None):
    """
    Sets up the logging.

    Needs the args to get the log level supplied

    Args:
        level: At which level do we log
        config_file: Configuration to use

    """
    # This will configure the logging, if the user has set a config file.
    # If there's no config file, logging will default to stdout.
    if config_file:
        # Get the config for the logger. Of course this needs exception
        # catching in case the file is not there and everything. Proper IO
        # handling is not shown here.
        # pylint: disable=unspecified-encoding
        # pylint: disable=raise-missing-from
        try:
            with open(config_file) as conf_file:
                configuration = json.loads(conf_file.read())
                # Configure the logger
                logging.config.dictConfig(configuration)
        except ValueError:
            print(f'File "{config_file}" is not valid json, cannot continue.')
            raise SystemExit(1)
    else:
        coloredlogs.install(level=level.upper())


def main():
    """
    Main method.

    This method holds what you want to execute when
    the script is run on command line.
    """
    args = get_arguments()
    setup_logging(args.log_level, args.logger_config)
    # filepathseries = Path('temp')
    returned_series = search_series(args.name)
    # if args.path == None:
    #     filepath = Path().absolute()
    #     create_tmp_directories(filepath, args.name, returned_series)
    # else:
    #     create_tmp_directories(args.path, args.name, returned_series)

    filepath = args.path if args.path else Path().absolute()
    create_tmp_directories(filepath, args.name, returned_series)
    # for k, v in returned_series.items():
    #     print(k, v)
    # print('####################')
    # create_tmp_directories(args.path)
    # Main code goes here

    # if the path is given we need to make the season directories in that path, including the episode.txt
    # dir with season name
    # in that dir a txt file with episode-1.txt
    # in episode-1.txt put the summary there.


def create_tmp_directories(argpath, series_name, returned_series):
    """Creates tmp dirs.."""
    filepath = Path(argpath)
    filepath = filepath.joinpath('temp')
    # now it's included in the --path arg, don't do that, comma seperate or string together
    filepath = filepath.joinpath(series_name)
    filepath.mkdir(parents=True, exist_ok=True)
    seasons_path = filepath
    for k, v in returned_series.items():
        create_series_structure(k, seasons_path, v)


def create_series_structure(k, seasons_path, v):
    # make the args clearer in name, you won't know what k/v is after a while
    seasons_path = seasons_path.joinpath(k)
    seasons_path.mkdir(parents=True, exist_ok=True)
    for number, episode in enumerate(v):
        text_file = 'episode' + str(number) + ".txt"
        text_file = text_file  # pylint: disable=self-assigning-variable
        episode = episode  # pylint: disable=self-assigning-variable
        # rewrite in fstring
        # print(text_file)
        # print(episode)


if __name__ == '__main__':
    main()


# change the parser.add_argument to fit what we need
# Build our main business logic  in def main():
# pathlib for the dir/path's
# if path exists, what then? What if there's already files?
