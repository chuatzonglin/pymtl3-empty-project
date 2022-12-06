#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: conftest.py
# Project: sim
# Created Date: 2022-10-17 16:10:14
# Author: Kuroba
# Description: 
# -----
# Last Modified: 2022-10-17 17:07:15
# Modified By: Kuroba
# -----
# MIT License
# Copyright (c) 2022 Kuroba
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
# 2022-10-17	TL	Taken from ece-5745 tutorial
###

#=========================================================================
# conftest
#=========================================================================

import pytest
import random

#-------------------------------------------------------------------------
# pytest_addoption
#-------------------------------------------------------------------------

def pytest_addoption(parser):

  parser.addoption( "--prtl", action="store_true",
                    help="use PRTL implementations" )

  parser.addoption( "--vrtl", action="store_true",
                    help="use VRTL implementations" )

#-------------------------------------------------------------------------
# Handle other command line options
#-------------------------------------------------------------------------

def pytest_configure(config):
  import sys
  sys._called_from_test   = True
  sys._pymtl_rtl_override = False
  if config.option.prtl:
    sys._pymtl_rtl_override = 'pymtl'
  elif config.option.vrtl:
    sys._pymtl_rtl_override = 'verilog'

def pytest_unconfigure(config):
  import sys
  del sys._called_from_test
  del sys._pymtl_rtl_override

#-------------------------------------------------------------------------
# fix_randseed
#-------------------------------------------------------------------------

def pytest_report_header(config):
  if config.option.prtl:
    return "forcing RTL language to be pymtl"
  elif config.option.vrtl:
    return "forcing RTL language to be verilog"

#-------------------------------------------------------------------------
# fix_randseed
#-------------------------------------------------------------------------
# fix random seed to make tests reproducable

@pytest.fixture(autouse=True)
def fix_randseed():
  """Set the random seed prior to each test case."""
  random.seed(0xdeadbeef)

