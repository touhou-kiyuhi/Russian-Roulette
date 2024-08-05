# Russian-Roulette
## Prepare：
### tkinter
```console
pip install tk
```
### cx_Freeze
```console
pip install cx-Freeze
```
**在 terminal 打下面指令打包 exe，打包後的文件方在 build 目錄下**
```concole
python setup.py build
```
**生成 .msi 格式的 windows 安裝包**
```concole
python setup.py bdist_msi
```
* #### 兩種區別
    * **build 會在當前目錄下生成目錄，存放可執行的文件以及依賴，目錄結構如下：**
    ```concole
    lib\
    python3.dll
    python38.dll
    main.exe
    ```
    * **bdist_msi 想當漁把這些壓縮打包成一個文件，並且可以安裝。
    分發時，單個文件比較方便。**
---
## 參考資料
* [cx_Freeze 打包 Python 高级用法详解](https://blog.csdn.net/oLawrencedon/article/details/140169165)
* [Python脚本到Windows可执行程序——Cxfreeze的安装与使用](https://cloud.tencent.com/developer/article/2147403)