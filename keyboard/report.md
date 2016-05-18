# 从键盘读入

沈哲言 2013011371 叶子鹏 2013011404

详细见`driver/console.c`以及`trap.c`

## 初始化

```
cons_init-->kbd_init-->kbd_intr
                    -->pic_enable(IRQ_KBD)
```

当我们初始化之后，我们就可以响应中断，来处理键盘的输入。

## 中断处理

```
trap_dispatch()::case IRQ_OFFSET + IRQ_KBD
-->cons_getc()-->kbd_intr()-->cons_intr(kbd_proc_data)

kbd_proc_data()是一个处理键盘读入数据的函数
```

在cons_getc中我们判断了2个，串口和键盘。