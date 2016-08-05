Steps for replication
---------------------

``` cmd
git clone https://github.com/colinbrownec/conan-problem
cd conan-problem
conan export colinbrownec
conan test
```

CMake will fail to find `conanbuildinfo.cmake`.

Uncomment line 28 in `conanfile.py` to implement my current fix
``` python
shutil.copy('conanbuildinfo.cmake', 'build')
```
