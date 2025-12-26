==================== ESP32 CORE DUMP START ====================

Crashed task handle: 0x40835648, name: 'BTC_TASK', GDB name: 'process 1082349128'

================== CURRENT THREAD REGISTERS ===================
ra             0x4200a05a	0x4200a05a <uart_write+116>
sp             0x40835210	0x40835210
gp             0x40812370	0x40812370 <char_description_value+180>
tp             0x40801fe4	0x40801fe4 <esp_coex_common_timer_arm_us_wrapper+12>
t0             0x40028140	1073905984
t1             0x20000000	536870912
t2             0x0	0
fp             0x12	0x12
s1             0x0	0
a0             0x0	0
a1             0x66	102
a2             0x0	0
a3             0x80	128
a4             0x60000000	1610612736
a5             0xe07f8000	-528515072
a6             0x420087fc	1107331068
a7             0xa	10
s2             0x66	102
s3             0x2e	46
s4             0x40822a6c	1082272364
s5             0x0	0
s6             0x0	0
s7             0x0	0
s8             0x0	0
s9             0x0	0
s10            0x0	0
s11            0x0	0
t3             0x0	0
t4             0x0	0
t5             0x0	0
t6             0x0	0
pc             0x42008fb6	0x42008fb6 <uart_tx_char+40>

==================== CURRENT THREAD STACK =====================
#0  0x42008fb6 in uart_ll_get_txfifo_len (hw=0x60000000) at /home/cuiyiyi/esp/esp-idf/components/hal/esp32c6/include/hal/uart_ll.h:506
#1  uart_tx_char (fd=<optimized out>, c=102) at /home/cuiyiyi/esp/esp-idf/components/vfs/vfs_uart.c:163
#2  0x4200a05a in uart_write (fd=0, data=0x40822a6c, size=46) at /home/cuiyiyi/esp/esp-idf/components/vfs/vfs_uart.c:216
#3  0x42008828 in console_write (fd=<optimized out>, data=0x40822a6c, size=46) at /home/cuiyiyi/esp/esp-idf/components/vfs/vfs_console.c:73
#4  0x420082c8 in esp_vfs_write (r=0x408356a4, fd=1, data=0x40822a6c, size=46) at /home/cuiyiyi/esp/esp-idf/components/vfs/vfs.c:445
#5  0x4003071e in __sflush_r ()
#6  0x4003079a in _fflush_r ()
#7  0x4003e4c2 in __swbuf_r ()
#8  0x420c8604 in __sputc_r (_p=0x40821470, _c=10, _ptr=0x408356a4) at /builds/idf/crosstool-NG/.build/src/newlib-git-ff0b7d93/newlib/libc/include/stdio.h:693
#9  _putc_r (ptr=0x408356a4, c=c@entry=10, fp=0x40821470) at /builds/idf/crosstool-NG/.build/riscv32-esp-elf/src/newlib/newlib/libc/stdio/putc.c:88
#10 0x420c867a in putchar (c=c@entry=10) at /builds/idf/crosstool-NG/.build/riscv32-esp-elf/src/newlib/newlib/libc/stdio/putchar.c:85
#11 0x42012ef8 in ssc_ble_gap_cb (event=<optimized out>, param=0x408230c0) at /home/cuiyiyi/esp/SSC/components/bt_cmd/bluedroid/ssc_ble_gap.c:710
#12 0x4202abf2 in btc_gap_ble_cb_to_app (event=ESP_GAP_BLE_EXT_ADV_REPORT_EVT, param=param@entry=0x408230c0) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/btc/profile/std/gap/btc_gap_ble.c:70
#13 0x4202c392 in btc_gap_ble_cb_handler (msg=0x408230bc) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/btc/profile/std/gap/btc_gap_ble.c:1283
#14 0x420635ac in btc_thread_handler (arg=0x408230bc) at /home/cuiyiyi/esp/esp-idf/components/bt/common/btc/core/btc_task.c:277
#15 0x42066cb0 in osi_thread_run (arg=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:165
#16 0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

======================== THREADS INFO =========================
  Id   Target Id          Frame 
* 1    process 1082349128 0x42008fb6 in uart_ll_get_txfifo_len (hw=0x60000000) at /home/cuiyiyi/esp/esp-idf/components/hal/esp32c6/include/hal/uart_ll.h:506
  2    process 1082651492 0x4080e55a in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
  3    process 1082278840 0x40809154 in esp_cpu_wait_for_intr () at /home/cuiyiyi/esp/esp-idf/components/esp_hw_support/cpu.c:145
  4    process 1082271624 vPortClearInterruptMaskFromISR (prev_int_level=1) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:416
  5    process 1082649512 0x4080e558 in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
  6    process 1082644884 0x4080e55a in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
  7    process 1082353972 0x4080e55a in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
  8    process 1082361748 0x4080e558 in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
  9    process 1082342768 0x4080e55a in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549

==================== THREAD 1 (TCB: 0x40835648, name: 'BTC_TASK') =====================
#0  0x42008fb6 in uart_ll_get_txfifo_len (hw=0x60000000) at /home/cuiyiyi/esp/esp-idf/components/hal/esp32c6/include/hal/uart_ll.h:506
#1  uart_tx_char (fd=<optimized out>, c=102) at /home/cuiyiyi/esp/esp-idf/components/vfs/vfs_uart.c:163
#2  0x4200a05a in uart_write (fd=0, data=0x40822a6c, size=46) at /home/cuiyiyi/esp/esp-idf/components/vfs/vfs_uart.c:216
#3  0x42008828 in console_write (fd=<optimized out>, data=0x40822a6c, size=46) at /home/cuiyiyi/esp/esp-idf/components/vfs/vfs_console.c:73
#4  0x420082c8 in esp_vfs_write (r=0x408356a4, fd=1, data=0x40822a6c, size=46) at /home/cuiyiyi/esp/esp-idf/components/vfs/vfs.c:445
#5  0x4003071e in __sflush_r ()
#6  0x4003079a in _fflush_r ()
#7  0x4003e4c2 in __swbuf_r ()
#8  0x420c8604 in __sputc_r (_p=0x40821470, _c=10, _ptr=0x408356a4) at /builds/idf/crosstool-NG/.build/src/newlib-git-ff0b7d93/newlib/libc/include/stdio.h:693
#9  _putc_r (ptr=0x408356a4, c=c@entry=10, fp=0x40821470) at /builds/idf/crosstool-NG/.build/riscv32-esp-elf/src/newlib/newlib/libc/stdio/putc.c:88
#10 0x420c867a in putchar (c=c@entry=10) at /builds/idf/crosstool-NG/.build/riscv32-esp-elf/src/newlib/newlib/libc/stdio/putchar.c:85
#11 0x42012ef8 in ssc_ble_gap_cb (event=<optimized out>, param=0x408230c0) at /home/cuiyiyi/esp/SSC/components/bt_cmd/bluedroid/ssc_ble_gap.c:710
#12 0x4202abf2 in btc_gap_ble_cb_to_app (event=ESP_GAP_BLE_EXT_ADV_REPORT_EVT, param=param@entry=0x408230c0) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/btc/profile/std/gap/btc_gap_ble.c:70
#13 0x4202c392 in btc_gap_ble_cb_handler (msg=0x408230bc) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/btc/profile/std/gap/btc_gap_ble.c:1283
#14 0x420635ac in btc_thread_handler (arg=0x408230bc) at /home/cuiyiyi/esp/esp-idf/components/bt/common/btc/core/btc_task.c:277
#15 0x42066cb0 in osi_thread_run (arg=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:165
#16 0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

==================== THREAD 2 (TCB: 0x4087f364, name: 'uTask') =====================
#0  0x4080e55a in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
#1  0x4080c766 in xQueueReceive (xQueue=0x4087efa4 <l_taskCB+376>, pvBuffer=pvBuffer@entry=0x40826584, xTicksToWait=<optimized out>, xTicksToWait@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/queue.c:1605
#2  0x42022954 in uart_task (pvParameters=0x0, pvParameters@entry=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/SSC/components/libssc/libssc_uart.c:83
#3  0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

==================== THREAD 3 (TCB: 0x408243b8, name: 'IDLE') =====================
#0  0x40809154 in esp_cpu_wait_for_intr () at /home/cuiyiyi/esp/esp-idf/components/esp_hw_support/cpu.c:145
#1  0x420af050 in esp_vApplicationIdleHook () at /home/cuiyiyi/esp/esp-idf/components/esp_system/freertos_hooks.c:59
#2  0x4080cd6c in prvIdleTask (pvParameters=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/tasks.c:4058
#3  0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

==================== THREAD 4 (TCB: 0x40822788, name: 'esp_timer') =====================
#0  vPortClearInterruptMaskFromISR (prev_int_level=1) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:416
#1  0x4080e518 in vPortExitCritical () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:517
#2  0x4080dd70 in ulTaskGenericNotifyTake (uxIndexToWait=uxIndexToWait@entry=0, xClearCountOnExit=xClearCountOnExit@entry=1, xTicksToWait=xTicksToWait@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/tasks.c:5453
#3  0x42007a26 in timer_task (arg=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/esp-idf/components/esp_timer/src/esp_timer.c:477
#4  0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

==================== THREAD 5 (TCB: 0x4087eba8, name: 'SSCAppTask') =====================
#0  0x4080e558 in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
#1  0x4080c766 in xQueueReceive (xQueue=0x4087daec, pvBuffer=pvBuffer@entry=0x4087eb54 <uart_rx_buff+1336>, xTicksToWait=<optimized out>, xTicksToWait@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/queue.c:1605
#2  0x4202277e in ssc_app_task (pvParameters=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/SSC/components/libssc/ets_console.c:503
#3  0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

==================== THREAD 6 (TCB: 0x4087d994, name: 'sscTask') =====================
#0  0x4080e55a in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
#1  0x4080c766 in xQueueReceive (xQueue=0x4087cd38, pvBuffer=pvBuffer@entry=0x4087d938, xTicksToWait=<optimized out>, xTicksToWait@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/queue.c:1605
#2  0x420226c2 in vSsc_task (pvParameters=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/SSC/components/libssc/ets_console.c:104
#3  0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

==================== THREAD 7 (TCB: 0x40836934, name: 'hciT') =====================
#0  0x4080e55a in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
#1  0x4080c272 in xQueueGenericSend (xQueue=0x40837110, pvItemToQueue=0x40836828, xTicksToWait=<optimized out>, xTicksToWait@entry=4294967295, xCopyPosition=xCopyPosition@entry=0) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/queue.c:1090
#2  0x42066dfe in osi_thead_work_queue_put (wq=<optimized out>, item=item@entry=0x40836828, timeout=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:118
#3  0x420670c6 in osi_thread_post (thread=0x408370d4, func=func@entry=0x42048190 <btu_hci_msg_process>, context=context@entry=0x40842b84, queue_idx=queue_idx@entry=0, timeout=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:344
#4  0x42048362 in btu_task_post (sig=sig@entry=1, param=param@entry=0x40842b84, timeout=timeout@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/stack/btu/btu_task.c:228
#5  0x42031aba in dispatch_reassembled (packet=packet@entry=0x40842b84) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/hci/hci_layer.c:521
#6  0x42032400 in hal_says_packet_ready (packet=0x40842b84) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/hci/hci_layer.c:418
#7  0x420312f4 in hci_hal_h4_hdl_rx_packet (packet=0x40842b84) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/hci/hci_hal_h4.c:470
#8  0x420317aa in hci_upstream_data_handler (arg=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/hci/hci_hal_h4.c:230
#9  0x42066e3c in osi_thread_generic_event_handler (context=0x40836d58) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:425
#10 0x42066cb0 in osi_thread_run (arg=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:165
#11 0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

==================== THREAD 8 (TCB: 0x40838794, name: 'BTU_TASK') =====================
#0  0x4080e558 in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
#1  0x4080c272 in xQueueGenericSend (xQueue=0x40833f34, pvItemToQueue=0x40838508, xTicksToWait=<optimized out>, xTicksToWait@entry=4294967295, xCopyPosition=xCopyPosition@entry=0) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/queue.c:1090
#2  0x42066dfe in osi_thead_work_queue_put (wq=<optimized out>, item=item@entry=0x40838508, timeout=timeout@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:118
#3  0x420670c6 in osi_thread_post (thread=0x40833ef8, func=func@entry=0x4206355c <btc_thread_handler>, context=context@entry=0x40823648, queue_idx=queue_idx@entry=0, timeout=timeout@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:344
#4  0x420635cc in btc_task_post (msg=msg@entry=0x40823648, timeout=timeout@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/bt/common/btc/core/btc_task.c:288
#5  0x420636b0 in btc_transfer_context (msg=msg@entry=0x40838558, arg=arg@entry=0x4083855c, arg_len=arg_len@entry=276, copy_func=copy_func@entry=0x0, free_func=free_func@entry=0x0) at /home/cuiyiyi/esp/esp-idf/components/bt/common/btc/core/btc_task.c:333
#6  0x4202affa in btc_ble_5_gap_callback (event=<optimized out>, params=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/btc/profile/std/gap/btc_gap_ble.c:1140
#7  0x4203ab84 in BTM_ExtBleCallbackTrigger (event=event@entry=27 '\\033', params=params@entry=0x40838690) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/stack/btm/btm_ble_5_gap.c:213
#8  0x4203c71a in btm_ble_ext_adv_report_evt (params=params@entry=0x408386d0) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/stack/btm/btm_ble_5_gap.c:1199
#9  0x42046c08 in btu_ble_ext_adv_report_evt (p=0x4084185d <error: Cannot access memory at address 0x4084185d>, evt_len=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/stack/btu/btu_hcif.c:2210
#10 0x42047b04 in btu_hcif_process_event (controller_id=<optimized out>, p_msg=p_msg@entry=0x40841838) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/stack/btu/btu_hcif.c:393
#11 0x420481da in btu_hci_msg_process (param=0x40841838) at /home/cuiyiyi/esp/esp-idf/components/bt/host/bluedroid/stack/btu/btu_task.c:159
#12 0x42066cb0 in osi_thread_run (arg=<error reading variable: value has been optimized out>) at /home/cuiyiyi/esp/esp-idf/components/bt/common/osi/thread.c:165
#13 0x4080e2d4 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:234

==================== THREAD 9 (TCB: 0x40833d70, name: 'll') =====================
#0  0x4080e55a in vPortYield () at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:549
#1  0x4080c766 in xQueueReceive (xQueue=0x40830070, pvBuffer=pvBuffer@entry=0x40833cfc, xTicksToWait=<optimized out>, xTicksToWait@entry=4294967295) at /home/cuiyiyi/esp/esp-idf/components/freertos/FreeRTOS-Kernel/queue.c:1605
#2  0x40802502 in npl_freertos_eventq_get (evq=<optimized out>, tmo=4294967295) at /home/cuiyiyi/esp/esp-idf/components/bt/porting/npl/freertos/src/npl_os_freertos.c:197
#3  0x42082516 in ?? ()


======================= ALL MEMORY REGIONS ========================
Name   Address   Size   Attrs
.rtc.text 0x50000000 0x0 RW  
.rtc.force_fast 0x50000000 0x0 RW  
.rtc_noinit 0x50000000 0x0 RW  
.rtc.force_slow 0x50000000 0x0 RW  
.iram0.text 0x40800000 0x11b6e R XA
.iram0.text_end 0x40811b6e 0x0 RW  
.iram0.bss 0x40811b70 0x0 RW  
.dram0.data 0x40811b70 0x3d94 RW A
.flash.text 0x42000020 0xcb0b8 R XA
.flash.appdesc 0x420d0020 0x100 R  A
.flash.rodata 0x420d0120 0x33660 RW A
.eh_frame 0x42103780 0x28fe8 R  A
.eh_frame_hdr 0x4212c768 0x8e14 R  A
.flash.rodata_noload 0x4213557c 0x0 RW  
.dram0.heap_start 0x40820a30 0x0 RW  
.coredump.tasks.data 0x40835648 0x154 RW 
.coredump.tasks.data 0x40835190 0x4b0 RW 
.coredump.tasks.data 0x4087f364 0x154 RW 
.coredump.tasks.data 0x40826480 0x150 RW 
.coredump.tasks.data 0x408243b8 0x154 RW 
.coredump.tasks.data 0x408242e0 0xd0 RW 
.coredump.tasks.data 0x40822788 0x154 RW 
.coredump.tasks.data 0x408226a0 0xe0 RW 
.coredump.tasks.data 0x4087eba8 0x154 RW 
.coredump.tasks.data 0x4087ea80 0x120 RW 
.coredump.tasks.data 0x4087d994 0x154 RW 
.coredump.tasks.data 0x4087d860 0x120 RW 
.coredump.tasks.data 0x40836934 0x154 RW 
.coredump.tasks.data 0x40836740 0x1e0 RW 
.coredump.tasks.data 0x40838794 0x154 RW 
.coredump.tasks.data 0x40838420 0x360 RW 
.coredump.tasks.data 0x40833d70 0x154 RW 
.coredump.tasks.data 0x40833c20 0x140 RW 

===================== ESP32 CORE DUMP END =====================
===============================================================
Done!
