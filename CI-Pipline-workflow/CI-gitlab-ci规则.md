好 👍 我从零开始帮你梳理 **GitLab CI/CD 的 `.gitlab-ci.yml`** 文件配置规则。
你可以把它理解成 **流水线说明书**，告诉 GitLab 在代码 push/merge 时要跑哪些任务。

---

# 🔹 `.gitlab-ci.yml` 入门

## 1. 文件层次结构

通常有三层：

1. **全局配置**（对所有 Job 生效）
2. **模板 Job**（以 `.` 开头，只用来复用）
3. **实际 Job**（真正执行的任务）

---

## 2. 常用关键字

### （1）流水线阶段（stages）

定义执行顺序：先 `build` → 再 `test` → 最后 `deploy`。

```yaml
stages:
  - build
  - test
  - deploy
```

---

### （2）全局变量（variables）

所有 Job 都能用，可以覆盖。

```yaml
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"  # 缓存 pip 依赖
  APP_ENV: "dev"                               # 应用环境变量
```

在脚本中就能用：

```bash
echo $APP_ENV
```

---

### （3）镜像（image）

CI 运行在 **Docker 容器**里，这里指定默认镜像：

```yaml
image: python:3.11
```

也可以每个 Job 单独指定：

```yaml
test-job:
  stage: test
  image: node:20
  script:
    - node --version
```

---

### （4）before\_script / after\_script

在 **所有 Job** 之前/之后执行。

```yaml
before_script:
  - echo "Global setup"

after_script:
  - echo "Global cleanup"
```

---

### （5）模板 Job（隐藏 job）

名字以 `.` 开头，不会直接执行，只能被继承。

```yaml
.build_template:
  stage: build
  script:
    - echo "Default build steps"
```

---

### （6）实际 Job

流水线真正执行的任务。

```yaml
build-job:
  stage: build
  script:
    - echo "Compiling source..."
    - make all
```

---

### （7）artifacts（产物）

保存执行结果，比如日志、报告、编译结果。

```yaml
test-job:
  stage: test
  script:
    - pytest -v --junitxml=report.xml
  artifacts:
    paths:
      - report.xml
    expire_in: 1 week   # 保留时间
    when: always        # always / success / failure
```

---

## 3. `.gitlab-ci.yml` 完整示例

```yaml
stages:              # 定义流水线顺序
  - build
  - test
  - deploy

variables:           # 全局变量
  GLOBAL_ENV: "all-jobs"

image: python:3.11   # 默认运行环境

before_script:       # 所有 job 前执行
  - echo "Setup done"

.build_template:     # 模板 job
  stage: build
  script:
    - echo "Building by default"

build-job:           # 实际 job
  extends: .build_template
  script:
    - echo "Custom build"
    - make all

test-job:
  stage: test
  script:
    - pytest -v
  artifacts:
    paths:
      - reports/
    expire_in: 1 week
    when: always

deploy-job:
  stage: deploy
  script:
    - echo "Deploying..."
```

---

## 4. 常用内置变量（GitLab 提供）

* `$CI_PROJECT_DIR`：项目目录
* `$CI_COMMIT_BRANCH`：当前分支名
* `$CI_COMMIT_SHA`：当前 commit 的哈希
* `$CI_JOB_STAGE`：当前 Job 所属阶段
* `$CI_JOB_NAME`：当前 Job 名字
* `$CI_PIPELINE_ID`：流水线 ID

---

有的 👍 `.gitlab-ci.yml` 除了我前面介绍的 **核心结构**（stages、variables、jobs、artifacts 等），在实际项目里还有很多常用功能。下面我帮你整理一个更完整的清单，按场景分类：

---

# 🔹 `.gitlab-ci.yml` 常用结构扩展

## 1. 流水线控制

### （1）only / except（旧写法）

指定某些分支或 tag 才运行。

```yaml
deploy-job:
  stage: deploy
  script: echo "Deploying..."
  only:
    - main
    - tags
```

---

### （2）rules（推荐写法）

更灵活，可以用条件表达式。

```yaml
deploy-job:
  stage: deploy
  script: echo "Deploying..."
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: always
    - if: '$CI_COMMIT_TAG'
      when: always
    - when: never
```

---

### （3）needs（并行依赖）

控制 job 之间的依赖关系，加快流水线。

```yaml
test-job:
  stage: test
  needs: ["build-job"]
  script: pytest
```

---

### （4）workflow

控制整个 pipeline 是否触发。

```yaml
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - when: never
```

---

## 2. 缓存与优化

### （1）cache（依赖缓存）

保存依赖，跨 job 重用。

```yaml
cache:
  key: pip-cache
  paths:
    - .cache/pip
```

---

### （2）artifacts 与 reports

除了保存产物，还可以让 GitLab UI 展示结果。

```yaml
test-job:
  stage: test
  script: pytest --junitxml=report.xml
  artifacts:
    reports:
      junit: report.xml
```

GitLab UI 会自动解析 JUnit 测试报告。

---

## 3. Job 执行环境

### （1）services（依赖服务）

让 job 里起一个数据库、Redis 等。

```yaml
test-job:
  stage: test
  image: python:3.11
  services:
    - postgres:14
  script:
    - pip install psycopg2
    - pytest
```

---

### （2）tags（Runner 标签）

如果有多个 Runner，用 `tags` 指定要在哪个 Runner 执行。

```yaml
build-job:
  stage: build
  tags:
    - docker-runner
```

---

### （3）retry（失败重试）

自动重试失败的 job。

```yaml
test-job:
  stage: test
  script: pytest
  retry: 2
```

---

### （4）timeout（超时时间）

设置单个 job 超时。

```yaml
deploy-job:
  stage: deploy
  script: ./deploy.sh
  timeout: 30m
```

---

## 4. 复用与模块化

### （1）extends

继承模板 job，覆盖部分字段。

```yaml
.default-job:
  image: python:3.11
  before_script:
    - pip install -r requirements.txt

lint-job:
  extends: .default-job
  stage: test
  script: flake8 .
```

---

### （2）include（拆分配置）

把多个 CI 文件组合在一起。

```yaml
include:
  - local: 'ci/common.yml'          # 当前仓库里的文件
  - project: 'sv_admin/ci_files'    # 跨项目文件
    file: '/templates/base.yml'
    ref: main
  - remote: 'https://example.com/template.yml'  # 远程 URL
```

---

## 5. 高级控制

### （1）environment（部署环境）

用于 GitLab 的 **Environments + Deploy Board** 功能。

```yaml
deploy-job:
  stage: deploy
  script: ./deploy.sh
  environment:
    name: production
    url: https://example.com
```

---

### （2）when（执行时机）

决定 job 在 pipeline 中是否执行。

```yaml
job1:
  stage: test
  script: pytest
  when: on_success   # 默认
```

可选值：

* `on_success`（成功才跑）
* `on_failure`（失败时跑）
* `always`（总是跑）
* `manual`（手动触发）

---

### （3）parallel（并行）

同一个 job 多份并行执行。

```yaml
test-job:
  stage: test
  script: pytest
  parallel: 4   # 同时起 4 个 job
```

---

# ✅ 总结

`.gitlab-ci.yml` 功能非常丰富，可以分为：

1. **基本结构**：stages, variables, jobs, artifacts
2. **控制执行**：rules, workflow, needs, when
3. **优化加速**：cache, retry, parallel
4. **运行环境**：image, services, tags
5. **复用拆分**：extends, include
6. **部署支持**：environment, reports

---

要不要我帮你画一张 **.gitlab-ci.yml 常用结构速查图（树状图）**，这样你能一眼看全局？

