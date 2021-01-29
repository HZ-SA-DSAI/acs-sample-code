#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
# <!-- MIT License
#
# Copyright (c) 2021 HZ-MS-CSA
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#  -->

# %%


import os


# %%


target_phone_numbers_dir = './target_phone_numbers/'
os.makedirs(target_phone_numbers_dir, exist_ok=True)
required_info_dir = './required_info/'
os.makedirs(required_info_dir, exist_ok=True)
output_dir = './output/'
os.makedirs(output_dir, exist_ok=True)
archive_dir = './archive/'
os.makedirs(archive_dir, exist_ok=True)
print(f"{target_phone_numbers_dir}, {required_info_dir}, {output_dir}, {archive_dir} are created")

