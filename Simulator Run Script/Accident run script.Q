[General]
SyntaxVersion=2
BeginHotkey=121
BeginHotkeyMod=0
PauseHotkey=0
PauseHotkeyMod=0
StopHotkey=123
StopHotkeyMod=0
RunOnce=1
EnableWindow=
MacroID=4a4a05c4-a486-4c77-8f79-4fbf89f511b7
Description=SGATR
Enable=0
AutoRun=0
[Repeat]
Type=0
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]

[Script]
//建立LOCA数据文件夹
KeyDown "Win", 1
KeyPress "R", 1
KeyUp "Win", 1
Delay 1000
MoveTo 105, 920
LeftClick 2
Delay 2000
KeyPress "BackSpace", 1
SayString "CMD"
KeyPress "Enter", 1
Delay 1000
KeyPress "D", 1
KeyDown "Shift", 1
KeyPress ";", 1
KeyUp "Shift", 1
Delay 1000
KeyPress "Enter", 1
Delay 1000
KeyPress "M", 1
KeyPress "D", 1
KeyPress "Space", 1
Private Declare Function GetKeyState Lib"user32"(ByVal nVirtKey As Long) As Integer
If GetKeyState(20) = 0 Then 
    KeyPress "CapsLock", 1
End If
KeyPress 83, 1
KeyPress 71, 1
KeyPress 65, 1
KeyPress 84, 1
KeyPress 82, 1 //需要改动
Delay 1000
KeyPress "Enter", 1
KeyDown "Alt", 1
KeyDown "Space", 1
KeyUp "Alt", 1
KeyUp "Space", 1
KeyPress "C", 1
Dim breaksize
breaksize = 43
For 58
Delay 2000
    RunApp "PCTran.exe"
    Delay 5000
    MoveTo 57, 18 //设置初始工况
    LeftClick 1
    Delay 1000
    MoveTo 65, 32
    LeftClick 1
    Delay 1000
    MoveTo 143, 235
    LeftClick 1
    Delay 1000
    MoveTo 385, 521
    LeftClick 1
    Delay 1000
    MoveTo 212, 20
    LeftClick 1
    Delay 1000
    MoveTo 190, 85
    LeftClick 1
    Delay 1000
    MoveTo 168, 353//设置故障类型 需要改动
    LeftClick 1
    Delay 1000
    MoveTo 577, 541
    LeftClick 1
    Delay 1000
    MoveTo 452, 352
    LeftClick 1
    KeyPress "BackSpace", 1
    SayString 100 //设置事故发生时间
    MoveTo 463, 384
    LeftClick 1
    KeyPress "BackSpace", 1
    SayString 10 //设置事故转变时间
    MoveTo 460, 420
    LeftClick 1
    KeyPress "BackSpace", 1 
    SayString breaksize  //设置破口尺寸
    MoveTo 552, 373
    LeftClick 1
    Delay 1000
    MoveTo 649, 358
    LeftClick 1
    MoveTo 442, 539
    LeftClick 1
    Delay 1000
    MoveTo 631, 732
    LeftClick 1
    Delay 500
    LeftClick 1
    Delay 500
    LeftClick 1
    Delay 500
    LeftClick 1
    MoveTo 604, 729
    LeftClick 1
    Delay 400000 //321000仿真时间
    MoveTo 143, 45
    LeftClick 1
    Delay 1000
    MoveTo 22, 20
    LeftClick 1
    Delay 1000
    MoveTo 55,85
    LeftClick 1
    Delay 1000
    MoveTo 55,85
    LeftClick 1
    Delay 2000
    MoveTo 922, 594
    LeftClick 1
    Delay 2000
    KeyPress "N", 1 //不保存初始工况
    Delay 2000
    KeyPress "Y", 1 
    Delay 2000
    KeyPress "Enter", 1
    Delay 4000
    If breaksize=1 Then
        KeyPress "F4", 1
        KeyDown "Ctrl", 1
        KeyPress "A", 1
        KeyUp "Ctrl", 1
        KeyPress "BackSpace", 1
        Delay 1000
        SayString "D:\SGATR"//需要改动
        Delay 1000
        KeyPress "Enter", 1
        KeyPress "Tab", 6
    End If
    Delay 4000
    SayString breaksize//输入文件名字
    Delay 4000
    KeyPress "Enter", 1
    Delay 2000
    KeyPress "Enter", 1//保存dose data
    Delay 2000
    KeyPress "Enter", 1
    Delay 5000
    SayString CStr(breaksize) + "dose"
    Delay 4000
    KeyPress "Enter", 1
    Delay 2000
    KeyPress "Enter", 1//保存Transient Report
    Delay 2000
    KeyPress "Enter", 1
    Delay 5000
    SayString CStr(breaksize) + "Transient Report"
    Delay 4000
    KeyPress "Enter", 1
    breaksize = breaksize + 1
    Delay 3000
Next
