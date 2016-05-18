# 从键盘读入

沈哲言 2013011371 叶子鹏 2013011404

详细见`driver/console.c`以及`trap.c`

```
trap_dispatch()::case IRQ_OFFSET + IRQ_KBD
-->cons_getc()-->kbd_intr()-->cons_intr(kbd_proc_data)

kbd_proc_data()是一个处理键盘读入数据的函数
```