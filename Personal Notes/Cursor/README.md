### Cursor的使用

### 软件背景：基于VScode进行开发的AI编程工具

#### 使用前提

1、cursor使用前，需要配置MCP服务，具体可以查看[该文档](https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/MCPServersConfig.md)将需要的配置导入到`mcp.json`中。

2、cursor在自动操作中可能会删除你需要的文件，注意通过一些网络建议来进行修改它们。如：在cursor setting的features中，你需要在command denylist中排除掉`rm -f`的使用，确保它不会删除你重要的文件。

3、cursor在操作中，会频繁的提问您是否要运行某些命令，通过勾选cursor setting的features中`Enable auto-run mode`时，可以自动进行终端命令。

### `Cursor`入门

1、配置`cursor setting`

![Cursor1](https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/assets/Cursor1.png)

2、配置**任务操作自动运行**和**禁止删除**

![Cursor2](https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/assets/Cursor2.png)

3、配置MCP服务（重要）

![Cursor3](https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/assets/Cursor3.png)

### 软件说明

**1、最左边的内容**

<img src="https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/assets/image-20250425185829767.png" alt="image-20250425185829767" style="zoom: 67%;" />

2、中间部分

![image-20250425185931199](https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/assets/image-20250425185931199.png)

3、右侧内容

![image-20250425190005312](https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/assets/image-20250425190005312.png)

#### 运行配置

当你运行自动操作时，它可能会出现某些报错，这是它会停下让你去处理问题，这时可以通过导入[这个文档](https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/CursorBaseSetting.md)来说明如何进行操作，来引导它进行自动处理。

#### 我的其他记录

1、尝试导入角色设定，进行更好的文件操作

2、生成或者编写一个操作流程，引导cursor完成我的需求


### 运行架构图

基于`Cursor`[运行规则2.0](https://github.com/Yotoha0303/AI_RoleTemplate/blob/main/Personal%20Notes/Cursor/SettingCursor2_plus.md)

```
┌──────────────┐
│   用户输入   │──┐
└──────────────┘  │
                  ▼
       ┌────────────────────┐
       │ 环境与依赖检查阶段 │
       └────────────────────┘
        │         │        │
        ▼         ▼        ▼
  [系统信息] [开发环境] [终端类型]
        │         │        │
        └────┬────┘        │
             ▼             │
     是否符合任务需求？    │
        │否              │是
        ▼                 ▼
[提示修复方法/终止]     继续执行
        │
        ▼
  [生成 logs/error_log.txt]

─────────────────────────────────────
         ▼
┌──────────────────────────────┐
│   任务准备与流程文档生成阶段   │
└──────────────────────────────┘
        │
        ▼
 在 ./tasks/ 目录生成：
 📄 `任务名称.md`：
 - 任务目标
 - 环境要求
 - 执行步骤
 - 错误处理规则

─────────────────────────────────────
         ▼
┌────────────────────────┐
│   任务执行阶段（自动化） │
└────────────────────────┘
        │
        ▼
  执行每一步任务命令（MCP调度）
        │
        ▼
 出现错误？───是────┐
        │ 否         │
        ▼            ▼
  结果校验阶段     启动错误处理模块
（输出是否符合预期）   （查错、修复、重试）
        │            │
        ▼            ▼
  ✅ 正确输出      ❌ 错误报告 & 记录
        │
        ▼
┌────────────────────────────┐
│ 写入 logs/ 和 tasks/ 完成记录 │
└────────────────────────────┘


```
