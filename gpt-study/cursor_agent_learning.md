如何指定模型使用哪些规则文件。
**alwaysApply-agent通过description只能判断是否使用**
**globs-用到globs中匹配的文件，就会应用该规则**
**chat中手动@规则(不带md或mdc后缀)**

### 1. 通过规则的 `frontmatter` 配置（最常用）

这是最核心的方式，通过在规则文件的 `frontmatter`（即 Markdown 文件开头用 `---` 包裹的 YAML 数据）中设置 `alwaysApply` 和 `globs`。

*   **`alwaysApply: true` （始终应用）**
    *   **如何指定**: 将您希望 Agent 始终使用的规则文件的 `frontmatter` 中的 `alwaysApply` 字段设置为 `true`。
    *   **效果**: 无论当前的聊天上下文或您正在编辑的文件是什么，只要这个规则被 Agent 识别到（因为它存在于 `.cursor/rules/` 目录中），它就会被添加到 Agent 的上下文中。
    *   **示例**:
        ```markdown
        ---
        description: "Agent 通用行为规则，如回复语言和代码呈现形式。"
        globs:
          - "**/*"
        alwaysApply: true # 确保这条规则始终被 Agent 应用
        ---
        # Agent 通用行为规则
        # ...
        ```
    *   **您的 `general_agent_rules.md` 和 `conn_rule.mdc` 都是这样配置的，这意味着它们会始终被应用。**

*   **`alwaysApply: false` + `description` （智能应用）**
    *   **如何指定**: 如果您不希望规则总是被应用，而是希望 Agent 根据当前任务智能判断，那么将 `alwaysApply` 设置为 `false`，并提供一个清晰的 `description`。
    *   **效果**: Agent 会在处理您的请求时，读取所有 `alwaysApply: false` 的规则的 `description`，并根据当前的聊天上下文和您正在处理的代码，智能地选择它认为最相关的规则来应用。
    *   **示例**:
        ```markdown
        ---
        description: "关于图像处理算法的优化建议。"
        globs:
          - "src/image_processor/**/*.py"
        alwaysApply: false # 让 Agent 智能判断何时需要图像处理规则
        ---
        # 图像处理优化指南
        # ...
        ```

*   **`globs` （应用于特定文件）**
    *   **如何指定**: 在 `frontmatter` 中添加 `globs` 字段，并指定文件匹配模式。
    *   **效果**: Agent 会检查您当前正在编辑或 Agent 正在分析的文件路径是否匹配 `globs` 中定义的模式。如果匹配，这条规则就会被考虑应用。这可以与 `alwaysApply: false` 结合使用，使得 Agent 只在处理特定类型文件时才智能判断是否应用规则。
    *   **示例**:
        ```markdown
        ---
        description: "React组件开发规范，只适用于 TypeScript React 文件。"
        globs:
          - "src/components/**/*.tsx"
          - "src/pages/**/*.tsx"
        alwaysApply: false # 仅在处理 .tsx 文件时智能应用
        ---
        # React 组件开发模式
        # ...
        ```

### 2. 在聊天中手动 `@` 提及规则（手动应用）

文档中提到：

> `Apply Manually`：在对话中被 @ 提及时应用（例如：`@my-rule`）
>
> 来源: [https://cursor.com/cn/docs/context/rules](https://cursor.com/cn/docs/context/rules)

*   **如何指定**: 在您的聊天消息中，直接使用 `@` 符号，然后键入您规则文件的文件名（不带 `.md` 或 `.mdc` 后缀，或包含文件夹路径）。
*   **效果**: 无论规则的 `alwaysApply` 设置如何，当您在聊天中 `@` 提及一个规则时，Agent 会强制性地将其内容添加到当前上下文，从而应用该规则。这对于临时性地、明确地激活某个规则非常有用。
*   **示例**:
    *   如果您有一个规则文件名为 `coding_standards.mdc`，您可以在聊天中输入：`@coding_standards 请帮我重构这段代码。`
    *   如果您有一个规则文件在子目录中，例如 `.cursor/rules/frontend/components.md`，您可能需要输入：`@frontend/components 请 review 这个组件。`
