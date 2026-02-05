触发n8n条件
场景1.执行完某脚本，触发n8n
1.脚本中调用n8n相关URL
    webhook URL（webhook trigger）
    RESET API
2.消息队列、文件监听
    - 监听某个指定文件
    - Kafka/MQTT
3.执行脚本时加"收尾动作"
    linux/Mac: 
        ./myscript.sh && curl -X POST https://your-n8n/webhook/test
    windows:
        .\myscript.ps1; if ($LASTEXITCODE -eq 0) { Invoke-RestMethod -Uri https://your-n8n/webhook/test -Method Post }

成功案例
webhook -> response_webhook
webhook配置:
    HTTP Method: POST
    Authentication: None
    Respond: Using 'Respond to Webhook' node
response_webhook配置:
    Respond With: Text
    Response Body: 收到啦！
    Response Code: 200
命令行指令:
PS C:\codes> python .\cyy-study\test-n8n.py; curl.exe -X POST "https://cpppp.app.n8n.cloud/webhook-test/6699d0ce-246f-4bc0-ae5e-dcff550ac130"
打印:
test n8n execute
finsh execute
收到啦！