# rename-translit-to-cyrillic
This simple script can rename files in specific folder from latin translited names to cyrillic
## Note: 
Put files you want to rename in separate directory, enter it and run the script. If there will be original english names script will skip it
## Example usage:
```
$ mkdir ~/tempdir
$ mv ~/Downloads/Teoria_avtomaticheskogo_upravlenia_E_I_Yurevich.pdf ~/tempdir
$ cd ~/tempdir
$ python3 ~/path/to/script/rename-translit.py -e pdf
```
otput will be
```
>>> Teoriya_avtomaticheskogo_upravleniya_E_I_Yurevich.pdf renamed to Теория_автоматического_управления_Е_И_Юревич.pdf
>>> 1 files succesfully renamed
```
