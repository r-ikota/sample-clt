# Sample project to illustrate how to make a Python command line tool

## Install
  python setup.py Install

## Uninstall
For unix

    python setup.py install --record files.txt
    cat files.txt | xargs rm -rf

For Windows

    python setup.py install --record files.txt
    Get-Content files.txt | ForEach-Object {Remove-Item $_ -Recurse -Force}

How to use

    $ pdata
    $ salut

Key words in setup.py

  * files
    * [(dir1, files1), (dir2, files2), ...]
    * dir1: a directory where each element of files1 will be placed
    * files1: a list of data files
  * packages
    * a list of packages
  * package_dir
    * a dictionary whose keys and values are packages and its directories respectively