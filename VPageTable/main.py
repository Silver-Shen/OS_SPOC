# coding:utf-8
from preprocess import getMem
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Please enter a Virtual address in Hex format!"
        sys.exit(0)
    v_address = int(sys.argv[1], 16)
    print "Virtual Address " + hex(v_address) + ":"
    offset = v_address & 31
    pte_index = (v_address >> 5) & 31
    pde_index = (v_address >> 10) & 31
    Mem, Disk = getMem()
    PDT = 0x6c;
    #Look Up Page Directory Table
    PT = Mem[PDT][pde_index]
    if(PT < 128):
        print "  --> pde index:" + hex(pde_index) + "  pde contents:(valid 0, pfn " + hex(PT) + ")"
        print "      --> Fault (page directory table entry not valid)"
        sys.exit(0)
    else:
        PT = PT - 128
        print "  --> pde index:" + hex(pde_index) + "  pde contents:(valid 1, pfn " + hex(PT) + ")"
    #Look up Page Table
    pfn = Mem[PT][pte_index]
    if (pfn == 127):
        print "    --> pte index:" + hex(pte_index) + "  pte contents:(valid 0, pfn " + hex(pfn) + ")"
        print "      --> Fault (page table entry not valid)"
        sys.exit(0)
    elif (pfn < 128):
        print "    --> pte index:" + hex(pte_index) + "  pte contents:(valid 0, pfn " + hex(pfn) + ")"
        data = Disk[pfn][offset]
        p_address = pfn * 32 + offset
        print "      -->To Disk Sector Address " + hex(p_address) +" --> Value: " + hex(data)
    else:
        pfn = pfn - 128
        print "    --> pte index:" + hex(pte_index) + "  pte contents:(valid 1, pfn " + hex(pfn) + ")"
        data = Mem[pfn][offset]
        p_address = pfn * 32 + offset
        print "      -->To Physical Address " + hex(p_address) +" --> Value: " + hex(data)
