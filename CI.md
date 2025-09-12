
---

# 📚 学习路线（基础 → 实战）

### 1️⃣ 基础概念

* **持续集成 CI**：代码提交后，自动化执行构建、测试、报告。
* **持续交付 CD**：产物（固件/包/镜像）能自动部署到测试环境或产线。
* **核心要素**：

  * *触发*（代码提交/定时任务/手动触发）
  * *执行环境*（Runner/Agent/Docker）
  * *阶段*（lint → build → test → deploy）
  * *产物*（artifacts，如报告、日志、固件）
  * *反馈*（状态、报告、通知）

---

### 2️⃣ 工具选型

* **CI 平台**（三选一，取决于你项目托管位置）：

  * GitHub Actions（推荐，适合开源/私有仓库）
  * GitLab CI（适合企业内网部署）
  * Jenkins（灵活，但配置繁琐）
* **测试工具**：pytest + allure + logging
* **制品存储**：artifact 存储（GitHub 内置 / minio / S3）
* **通知**：Slack / 飞书 / 邮件

---

### 3️⃣ 必备知识点

* **YAML 文件配置**：CI pipeline 的描述语言。
* **Docker 基础**：把测试框架环境打包成镜像，保证一致性。
* **pytest / allure 报告输出**：

  * `pytest --alluredir=results`
  * `allure generate results -o report`

---

### 4️⃣ 高阶主题（后面慢慢学）

* 并行执行测试（pytest-xdist + CI matrix）
* DUT farm / 硬件测试调度
* 自动发布（固件烧录、pip 包、docker 镜像）
* CI/CD 最佳实践（artifact 生命周期管理、缓存依赖、回归测试）

---

# 🛠 实践路线（逐步落地）

## 阶段一：最小可行 CI（MVP）

目标：让测试框架在 CI 里能跑起来，并生成报告。

1. 在 GitHub/GitLab 创建仓库。
2. 新建 `.github/workflows/ci.yml`（或 `.gitlab-ci.yml`）：

   * 安装 Python、依赖
   * 运行 pytest
   * 保存 allure 报告作为 artifact
3. 验证：代码 push 后，CI 自动跑 pytest，并在页面下载报告。

---

## 阶段二：产物管理 + 报告可视化

目标：自动化产物（报告/日志）归档。

1. 配置 CI 把 `allure-report`、NativeLog HTML 作为 artifact。
2. 上传 artifact 到 CI 的存储（GitHub Actions → Artifacts，GitLab → Job Artifacts）。
3. 在 CI 界面挂链接，方便下载或在线查看。

---

## 阶段三：硬件集成（DUT 测试）

目标：把串口 DUT 测试跑进 CI。

1. 配置 CI runner 运行在接 DUT 的物理机上。
2. 串口映射到 runner（如 `/dev/ttyUSBx`）。
3. CI 流水线调用 pytest + DUT 脚本，自动收发日志。
4. 把 DUT 日志 + 报告一并上传。

---

## 阶段四：优化与扩展

* **并行化**：不同 DUT / 不同用例集并行跑。
* **缓存依赖**：pip 包 / 编译产物缓存，减少重复安装时间。
* **自动部署**：

  * Python 包 → 内部 PyPI
  * 固件 → DUT 烧录 farm
  * Docker → registry

---

# 🚦 推荐学习顺序（时间线）

### 第 1 周

* 学习 GitHub Actions / GitLab CI 基础（workflow、job、step）。
* 写一个最简单的 CI：跑 `pytest -v`，保存测试日志。

### 第 2 周

* 学习 allure 报告生成，集成到 CI artifact。
* 学习 Docker，把 pytest 环境封装成镜像，CI 直接用 docker 跑。

### 第 3-4 周

* 在物理机 runner 上集成 DUT 测试（串口操作、日志收集）。
* CI 流水线能调用 DUT 执行完整用例，上传报告。

### 第 2 个月

* 学习高级主题：并行测试、回归测试、artifact 生命周期管理。
* 引入 Release 流程：CI 自动生成产物 + 报告，CD 发布到测试环境。

---
# 💡 GitLab CI 配置文件

### 1️⃣ 强制 CI/CD 文件路径的机制

* **设置位置**：每个项目（子项目）都可以在

  ```
  Project → Settings → CI/CD → General pipelines → CI/CD configuration file
  ```

  指定路径。
* **GitLab push 检查**：

  1. 只检查 **子项目仓库**里是否存在这个路径对应的文件
  2. **如果不存在** → push 失败
* **关键点**：GitLab 并不会自动去 Group 仓库或模板仓库查找文件，**强制路径必须在子项目仓库里存在**

---

### 2️⃣ 为什么报错里会显示 `project 'sv_admin/ci_files' file 'ble-auto-test-gitlab-ci.yml' does not exist`

* 这是 GitLab 内部显示的 **仓库映射信息**，并不代表它真的去 Group 仓库找过
* GitLab push 时：

  * 找不到路径 `ci_files/ble-auto-test-gitlab-ci.yml`
  * 为了让报错信息明确，它会显示项目所属 Group（`sv_admin`）+ 路径
  * 结果就是报错显示：

    ```
    project 'sv_admin/ci_files' file 'ble-auto-test-gitlab-ci.yml' does not exist
    ```
* **本质**：GitLab 仍然只检查 **子项目仓库**，外部仓库并没有被访问

---

### 3️⃣ 核心结论

| 误区                                        | 真相                          |
| ----------------------------------------- | --------------------------- |
| 强制 CI/CD 文件路径不存在 → GitLab 会去 Group 仓库找    | ❌ 不会，它只检查子项目仓库              |
| 报错里显示 `sv_admin/ci_files` → 文件在 Group 仓库里 | ❌ 只是内部显示信息，实际 push 只检查子项目仓库 |
| 要通过 push                                  | 必须在 **子项目仓库**里创建路径匹配的文件     |

---

💡 总结：

* **强制路径必须存在于子项目仓库**
* **报错显示外部仓库只是 GitLab 内部信息**，并不意味着它真的访问了 Group 仓库

---

