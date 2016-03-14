#include <stdio.h>

int main(){
    int va, pa, i;
    FILE *fp = fopen("input.txt","r");
    for (i=0; i<10; i++){
        fscanf(fp,"va %x, pa %x\n", &va, &pa);
        int pde_idx, pde_ctx, pte_idx, pte_ctx;
        pde_idx = (va >> 22) & 0x3FF;
        pde_ctx = (pde_idx - 0x300 + 1) << 12 | 0x3;
        pte_idx = (va >> 12) & 0x3FF;
        pte_ctx = pa & ~0x3FF | 0x3;
        printf("va %08x, pa %08x, pde_idx %08x, pde_ctx %08x, pte_idx %08x, pte_ctx %08x\n", 
            va, pa, pde_idx, pde_ctx, pte_idx, pte_ctx);
    }
    return 0;
}