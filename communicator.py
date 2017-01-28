#!/usr/bin/env python3

#
# main.py
# Created by Stephen Brimhall on 1/24/17
# Copyright (c) SST CTF and Stephen Brimhall 2017. All Rights Reserved.
#
# Main for the SST CTF chat program
#

# Begin system imports
import curses;
import argparse
# End system imports

#######################
### Parse arguments ###
#######################
parser = argparse.ArgumentParser()

# Add hostname argument
parser.add_argument('server', help="Server hostname to connect to");
# Add username argument
parser.add_argument('username', help="Username to log in with. Can be specified in config file.");
# Add keyfile argument
parser.add_argument('--key', help="Private key to use, defaults to ~/.ssh/id_rsa. Cannot be encrypted. Can be specified in config file.", default="~/.ssh/id_rsa");

args = dict(parser.parse_args())
