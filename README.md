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

With the proposed approach:

``` cmd
git clone https://github.com/colinbrownec/conan-problem
cd conan-problem
// No export is necessary, it is automatic now with 0.11
conan test_package
```

And it also allows to build, work, debug in your IDE, locally:

``` cmd
git clone https://github.com/colinbrownec/conan-problem
mkdir conan-problem-build && cd conan-problem-build
conan install ../conan-problem
conan build ../conan-problem
// I can now open VS, if I am in Windows and have that default compiler, to build, etc.
```


