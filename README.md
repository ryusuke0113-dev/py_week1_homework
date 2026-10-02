$ python tests/test_a_python_basic.py 
A-1 OK
A-2 OK
A-3 OK
A-4 OK
A-5 OK
A-6 OK
A-7 OK
A-8 OK
Bob
Dylan
79
A-9 OK
Traceback (most recent call last):
  File "C:\Users\user\camp\python\week1_homework\tests\test_a_python_basic.py", line 108, in <module>     
    main()
    ~~~~^^
  File "C:\Users\user\camp\python\week1_homework\tests\test_a_python_basic.py", line 105, in main
    test_a_10()
    ~~~~~~~~~^^
  File "C:\Users\user\camp\python\week1_homework\tests\test_a_python_basic.py", line 85, in test_a_10     
    from python_basic.a_10 import dice
ModuleNotFoundError: No module named 'python_basic'  

user@DESKTOP-FK0VUEK MINGW64 C:/Users/user/camp/python/week1_homework (main)
$ python tests/test_b_python_basic.py
Traceback (most recent call last):
  File "C:\Users\user\camp\python\week1_homework\tests\test_b_python_basic.py", line 24, in <module>      
    main()
    ~~~~^^
  File "C:\Users\user\camp\python\week1_homework\tests\test_b_python_basic.py", line 12, in test_b_1
    table = create_kuku_table()
TypeError: create_kuku_table() missing 2 required positional arguments: 'rows' and 'columns'
