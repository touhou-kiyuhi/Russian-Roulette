from cx_Freeze import setup, Executable


py = "tkRussian_Roulette.py"

build_exe_options = {
    # 默認可不填，會自動尋找，如果運行時有缺少 package ，可以在這裡添加
    "packages": [], 
    "excludes": [], 
    # 可添加會用到的其他文件
    "include_files": []
}

setup(
    name = "Russian Roulette", 
    version = "0.0", 
    description = "Russian Roulette", 
    author = "ljjmk94", 
    options = {
        "build_exe": build_exe_options
    }, 
    executables = [
        Executable(
            script = py, 
            base = "win32gui", 
        )
    ]
)