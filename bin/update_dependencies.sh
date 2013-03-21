#!/bin/bash

cd ~
pip install -U --user git+git://github.com/Lokaltog/powerline
pip install -U --user paramiko
git submodule update --init --recursive
