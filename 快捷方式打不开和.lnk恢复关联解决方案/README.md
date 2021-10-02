请尝试以下步骤：
1、首先 win+r    
2、打开运行程序   
3、输入: regedit   
4、找到: 计算机\HKEY_CURRENT_USER\SOFTWARE\MICROSOFT\WINDOWS\currentversion\Explorer\FileExts\.lnk
会发现有openwithlist 和 openwithprogids 两项，如果有其他的选项将其删除。 
5、再将openwithlist 内的除默认以外的所有键值都删除。 
6、将openwithprogids内的除默认和lnkfile以外的所有键值都删除。
7、保存退出即可。