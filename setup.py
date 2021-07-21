import cx_Freeze

executables = [cx_Freeze.Executable("FlappyBird.py", base="Win32GUI")]

cx_Freeze.setup(
    name="Flappy",
    options={"build_exe": {"packages": ["pygame", "sys", "random"],
                           "include_files": ["04b_19.ttf", "assets/suck.png", 'assets/background-day.png',
                                             'assets/base.png', 'assets/pipe-green.png',
                                             'assets/bluebird-downflap.png', 'assets/bluebird-midflap.png',
                                             'assets/bluebird-upflap.png'
                                             ]}},
    executables=executables

)
