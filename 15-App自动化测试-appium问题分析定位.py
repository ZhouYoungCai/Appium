1、> 本文节选自霍格沃兹测试学院内部教材
使用 Appium 进行测试时，会产生大量日志，一旦运行过程中遇到报错，可以通过 Appium 服务端的日志以及客户端的日志分析排查问题。
Appium Server日志-开启服务  
通过命令行的方式启动 Appium Server，下面来分析一下启动日志，日志第一行显示了 Appium 版本信息和服务在本地的运行地址。
  *   *   *   *   * 
    $ appium -g appium.log[Appium] Welcome to Appium v1.8.0-beta3 (REV \  40e40975ebd3593d08c3f83de2546258f7ddf11d)[Appium] Appium REST http interface listener started \  on 0.0.0.0:4723
如果启动 Appium 服务时添加了参数，会在启动日志中展示，比如添加了 defaultCapabilities，启动日志也会显示出来。
  *   *   *   *   *   *   *   *   *   *   * 
    Hogwarts $ appium --log-timestamp --log-no-colors --no-reset     2021-04-29 10:11:58:545 - [Appium] Welcome to Appium v1.17.02021-04-29 10:11:58:547 - [Appium] Non-default server args:2021-04-29 10:11:58:547 - [Appium]   logTimestamp: true2021-04-29 10:11:58:547 - [Appium]   logNoColors: true2021-04-29 10:11:58:547 - [Appium]   noReset: true2021-04-29 10:11:58:548 - [Appium] Deprecated server args:2021-04-29 10:11:58:548 - [Appium]   --no-reset => --default-capabilities '{"noReset":true}'2021-04-29 10:11:58:548 - [Appium] Default capabilities, which will be added to each request unless overridden by desired capabilities:2021-04-29 10:11:58:548 - [Appium]   noReset: true2021-04-29 10:11:58:567 - [Appium] Appium REST http interface listener started on 0.0.0.0:4723
  * Appium 参数：http://appium.io/docs/en/writing-running-appium/server-args/
  * defaultCapabilities 详见：http://appium.io/docs/en/writing-running-appium/default-capabilities-arg/
运行时的Session日志  
###  
###  
自动化测试运行起来之后，Appium Server 的日志提供了一些基本的 Session 信息，特别是 desired capabilities
的配置信息。应该时刻注意 Appium 服务是否正确接收了请求内容。
###  
  *   *   *   *   *   *   *   *   *   *   *   * 
    ...[debug] [BaseDriver] Creating session with W3C capabilities: {[debug] [BaseDriver]   "alwaysMatch": {[debug] [BaseDriver]     "platformName": "android",[debug] [BaseDriver]     "appium:appActivity": ".view.WelcomeActivityAlias",[debug] [BaseDriver]     "appium:appPackage": "com.xueqiu.android",[debug] [BaseDriver]     "appium:automationName": "UiAutomator2",[debug] [BaseDriver]     "appium:deviceName": "emulator-5554",[debug] [BaseDriver]     "appium:noReset": "true",[debug] [BaseDriver]     "appium:udid": "emulator-5554"[debug] [BaseDriver]   },... 
上面的日志创建了一个 Session，设置了 Capabilities 参数，以 JSON 格式告诉 AppiumServer 被测试设备的一些重要信息。
Appium GET 请求的日志  
###  
###  
Appium 是一个 REST 服务，接收 HTTP 请求，返回结果。Appium 服务端日志用 `[HTTP] -->` 和 `[HTTP]
<--`展示了请求和返回的信息。
  *   *   *   *   * 
    [HTTP] --> GET /wd/hub/status {}[debug] [MJSONWP] Calling AppiumDriver.getStatus() with args: [][debug] [MJSONWP] Responding to client with driver.getStatus()\ result: {"build":{"version":"1.8.0-beta3","revision":"30e7b45bdc5668124af33c41492aa5195fcdf64d"}}[HTTP] <-- GET /wd/hub/status 200 121 ms - 126
“-->”代表发出 HTTP 请求，“<\--”代表响应，中间是指令细节。`[MJSONWP]` 指使用 MJSONWP(Mobile JSON Wire
Protocol 协议)，调用 AppiumDriver.getStatus( )这个方法（无参），返回给客户端 `result` 信息，整个过程耗时
121 毫秒，传输了 126 个字节。
通过日志进行错误排查  
###  
###  
利用日志可以非常容易的排查和定位问题，问题通常发生在 automation Session 之后，如果 Session 持续存在，错误也可能发生。
  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   * 
    [HTTP] --> POST /wd/hub/session...[debug] [ADB] 1 device(s) connected[debug] [ADB] Running '/home/user/Android/Sdk/platform-tools//adb' \with args: ["-P",5037,"-s","ec8c4df","shell","am","force-stop",\"io.appium.unlock"][debug] [AndroidDriver] Not cleaning generated files. Add \`clearSystemFiles` capability if wanted.[MJSONWP] Encountered internal error running command: Error: \Cannot stop and clear com.company.app. Original error: Error \executing adbExec. Original error: 'Command '/home/user/Android\/Sdk/platform-tools//adb -P 5037 -s ec8c4df shell pm clear com.\company.app' exited with code 1'; Stderr: 'Error: java.lang.SecurityException:\ PID 22126 does not have permission android.permission.CLEAR_APP_USER_DATA to \ clear data of package com.company.app'; Code: '1'at Object.wrappedLogger.errorAndThrow (../../lib/logging.js:63:13)at ADB.callee$0$0$ (../../../lib/tools/adb-commands.js:334:9)at tryCatch (/home/linuxbrew/.linuxbrew/lib/node_modules/appium/node_modules\/babel-runtime/regenerator/runtime.js:67:40)at GeneratorFunctionPrototype.invoke [as _invoke] (/home/linuxbrew/.\linuxbrew/lib/node_modules/appium/node_modules/babel-runtime/regenerator\/runtime.js:315:22)....[HTTP] <-- POST /wd/hub/session 500 40811 ms - 557
Appium Driver 启动 Session ，清理 `com.company.app` 时发生错误。这个错误让我们知道两件事：“Appium
正在尝试做什么”，“哪里出错了”。
在这个例子中，Appium 尝试运行 adb 命令（adb shell am force-stop），adb 参数在错误信息中也有显示。发生了
Android 系统权限错误。此时，可以手动运行这个 adb 命令，查看错误是否可以重现。如果错误重现，可以通过错误类型定位问题。
这个例子只是众多错误中的一个，但它说明至关重要的一点，当错误发生时，日志可以提供更多的信息，如果没有完整的日志信息，对 Appium 排错难上加难。
改变日志输出的参数  
###  
###  
下面的参数可以改变 Appium 服务端的日志行为：
\--log-level：改变 Appium 日志显示级别。Appium 默认展示所有日志  
，它有以下一些选项：'info', 'info:debug', 'info:info', 'info:warn', 'info:error', ...
\--log-no-colors：关闭颜色，如果日志是彩色的，可能会出现奇怪的字符，比如"TODO: find the
color"，你可以用这个参数关闭颜色。
\--log-timestamp：在日志前添加时间戳
展示如下：
  *   *   *   * 
    2018-03-15 13:17:58:663 - [Appium] Welcome to Appium v1.8.0-beta3 (REV 30e7b45bdc5668124af33c41492aa5195fcdf64d)2018-03-15 13:17:58:664 - [Appium] Non-default server args:2018-03-15 13:17:58:665 - [Appium] logTimestamp: true2018-03-15 13:17:58:732 - [Appium] Appium REST http interface listener started on 0.0.0.0:4723
### Appium 执行测试时会遇到各种问题，如果大家有其他的问题需要定位的话，可以在下方留言给我哦！
 ** _ 

来霍格沃兹测试开发学社，学习更多软件测试与测试开发的进阶技术，知识点涵盖web自动化测试 app自动化测试、接口自动化测试、测试框架、性能测试、安全测试、持续集成/持续交付/DevOps，测试左移、测试右移、精准测试、测试平台开发、测试管理等内容，课程技术涵盖bash、pytest、junit、selenium、appium、postman、requests、httprunner、jmeter、jenkins、docker、k8s、elk、sonarqube、jacoco、jvm-sandbox等相关技术，全面提升测试开发工程师的技术实力

视频资料领取：https://qrcode.testing-studio.com/f?from=jianshu&url=https://ceshiren.com/t/topic/15844

干货|app自动化测试之Appium问题分析及定位：https://ceshiren.com/t/topic/16833

使用 Appium 进行测试时，会产生大量日志，一旦运行过程中遇到报错，可以通过 Appium 服务端的日志以及客户端的日志分析排查问题。

Appium Server日志-开启服务
通过命令行的方式启动 Appium Server，下面来分析一下启动日志，日志第一行显示了 Appium 版本信息和服务在本地的运行地址。

$ appium -g appium.log
[Appium] Welcome to Appium v1.8.0-beta3 (REV \
  40e40975ebd3593d08c3f83de2546258f7ddf11d)
[Appium] Appium REST http interface listener started \
  on 0.0.0.0:4723

如果启动 Appium 服务时添加了参数，会在启动日志中展示，比如添加了 defaultCapabilities，启动日志也会显示出来。

Hogwarts $ appium --log-timestamp --log-no-colors --no-reset     
2021-04-29 10:11:58:545 - [Appium] Welcome to Appium v1.17.0
2021-04-29 10:11:58:547 - [Appium] Non-default server args:
2021-04-29 10:11:58:547 - [Appium]   logTimestamp: true
2021-04-29 10:11:58:547 - [Appium]   logNoColors: true
2021-04-29 10:11:58:547 - [Appium]   noReset: true
2021-04-29 10:11:58:548 - [Appium] Deprecated server args:
2021-04-29 10:11:58:548 - [Appium]   --no-reset => --default-capabilities '{"noReset":true}'
2021-04-29 10:11:58:548 - [Appium] Default capabilities, which will be added to each request unless overridden by desired capabilities:
2021-04-29 10:11:58:548 - [Appium]   noReset: true
2021-04-29 10:11:58:567 - [Appium] Appium REST http interface listener started on 0.0.0.0:4723

Appium 参数：CLI Arguments - Appium 1
defaultCapabilities 详见：The --default-capabilities flag - Appium 1
运行时的Session日志
自动化测试运行起来之后，Appium Server 的日志提供了一些基本的 Session 信息，特别是 desired capabilities 的配置信息。应该时刻注意 Appium 服务是否正确接收了请求内容。

...
[debug] [BaseDriver] Creating session with W3C capabilities: {
[debug] [BaseDriver]   "alwaysMatch": {
[debug] [BaseDriver]     "platformName": "android",
[debug] [BaseDriver]     "appium:appActivity": ".view.WelcomeActivityAlias",
[debug] [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
[debug] [BaseDriver]     "appium:automationName": "UiAutomator2",
[debug] [BaseDriver]     "appium:deviceName": "emulator-5554",
[debug] [BaseDriver]     "appium:noReset": "true",
[debug] [BaseDriver]     "appium:udid": "emulator-5554"
[debug] [BaseDriver]   },
... 

上面的日志创建了一个 Session，设置了 Capabilities 参数，以 JSON 格式告诉 AppiumServer 被测试设备的一些重要信息。

Appium GET 请求的日志
Appium 是一个 REST 服务，接收 HTTP 请求，返回结果。Appium 服务端日志用 [HTTP] → 和 [HTTP] <–展示了请求和返回的信息。

[HTTP] --> GET /wd/hub/status {}
[debug] [MJSONWP] Calling AppiumDriver.getStatus() with args: []
[debug] [MJSONWP] Responding to client with driver.getStatus()\
 result: {"build":{"version":"1.8.0-beta3","revision":"30e7b45bdc5668124af33c41492aa5195fcdf64d"}}
[HTTP] <-- GET /wd/hub/status 200 121 ms - 126

“–>”代表发出 HTTP 请求，“<–”代表响应，中间是指令细节。[MJSONWP] 指使用 MJSONWP(Mobile JSON Wire Protocol 协议)，调用 AppiumDriver.getStatus( )这个方法（无参），返回给客户端 result 信息，整个过程耗时 121 毫秒，传输了 126 个字节。

通过日志进行错误排查
利用日志可以非常容易的排查和定位问题，问题通常发生在 automation Session 之后，如果 Session 持续存在，错误也可能发生。

[HTTP] --> POST /wd/hub/session
...
[debug] [ADB] 1 device(s) connected
[debug] [ADB] Running '/home/user/Android/Sdk/platform-tools//adb' \
with args: ["-P",5037,"-s","ec8c4df","shell","am","force-stop",\
"io.appium.unlock"]
[debug] [AndroidDriver] Not cleaning generated files. Add \
`clearSystemFiles` capability if wanted.
[MJSONWP] Encountered internal error running command: Error: \
Cannot stop and clear com.company.app. Original error: Error \
executing adbExec. Original error: 'Command '/home/user/Android\
/Sdk/platform-tools//adb -P 5037 -s ec8c4df shell pm clear com.\
company.app' exited with code 1'; Stderr: 'Error: java.lang.SecurityException:\
 PID 22126 does not have permission android.permission.CLEAR_APP_USER_DATA to \
 clear data of package com.company.app'; Code: '1'
at Object.wrappedLogger.errorAndThrow (../../lib/logging.js:63:13)
at ADB.callee$0$0$ (../../../lib/tools/adb-commands.js:334:9)
at tryCatch (/home/linuxbrew/.linuxbrew/lib/node_modules/appium/node_modules\
/babel-runtime/regenerator/runtime.js:67:40)
at GeneratorFunctionPrototype.invoke [as _invoke] (/home/linuxbrew/.\
linuxbrew/lib/node_modules/appium/node_modules/babel-runtime/regenerator\
/runtime.js:315:22)
....
[HTTP] <-- POST /wd/hub/session 500 40811 ms - 557

Appium Driver 启动 Session ，清理 com.company.app 时发生错误。这个错误让我们知道两件事：“Appium 正在尝试做什么”，“哪里出错了”。
在这个例子中，Appium 尝试运行 adb 命令（adb shell am force-stop），adb 参数在错误信息中也有显示。发生了 Android 系统权限错误。此时，可以手动运行这个 adb 命令，查看错误是否可以重现。如果错误重现，可以通过错误类型定位问题。
这个例子只是众多错误中的一个，但它说明至关重要的一点，当错误发生时，日志可以提供更多的信息，如果没有完整的日志信息，对 Appium 排错难上加难。

改变日志输出的参数
下面的参数可以改变 Appium 服务端的日志行为：
–log-level：改变 Appium 日志显示级别。Appium 默认展示所有日志
，它有以下一些选项：‘info’, ‘info:debug’, ‘info:info’, ‘info:warn’, ‘info:error’, …
–log-no-colors：关闭颜色，如果日志是彩色的，可能会出现奇怪的字符，比如"TODO: find the color"，你可以用这个参数关闭颜色。
–log-timestamp：在日志前添加时间戳
展示如下：

2018-03-15 13:17:58:663 - [Appium] Welcome to Appium v1.8.0-beta3 (REV 30e7b45bdc5668124af33c41492aa5195fcdf64d)
2018-03-15 13:17:58:664 - [Appium] Non-default server args:
2018-03-15 13:17:58:665 - [Appium] logTimestamp: true
2018-03-15 13:17:58:732 - [Appium] Appium REST http interface listener started on 0.0.0.0:4723

