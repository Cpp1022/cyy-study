上下文规则:
项目规则 用户规则 团队规则 AGENTS.md

规则作用：
统一应用/指导所有模型

4种规则有什么区别 作用 影响范围 生效优先级

cursor如何识别规则文件
.curosr/rules下的md或mdc文件

/home/cuiyiyi/code/my-project/
├── .cursor/
│   └── rules/
│       ├── react-patterns.mdc      # 这是一个带有元数据的规则文件
│       ├── api-guidelines.md       # 这是一个简单的 Markdown 规则文件
│       └── frontend/               # 您可以在这里创建子文件夹来组织规则
│           └── components.md       # 针对前端组件的规则
├── src/
│   └── ...
└── package.json


.md/.mdc文件格式参考
> ---
> globs:
> alwaysApply: false
> ---
>
> - 定义服务时使用我们内部的 RPC 模式
> - 服务名称始终使用 snake_case 命名
>
> @service-template.ts

Frontmatter 元数据举例：
---
globs:
alwaysApply: false
---

---
description: "React组件开发规范，包括函数式组件、Hooks使用和样式约定。"
globs:
  - "src/components/**/*.tsx"  # 匹配 src/components 目录下的所有 TypeScript React 组件
  - "src/pages/**/*.tsx"      # 匹配 src/pages 目录下的所有 TypeScript React 页面组件
alwaysApply: false            # 不总是应用，让 Agent 智能判断
---

