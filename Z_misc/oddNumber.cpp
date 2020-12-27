#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int* oddNumbers(int l, int r, int* result_size) {
    int i = 0;
    int number;
    for(number = l;number <= r; number++)
        std::cout << number << std::endl;
        if(number % 2 !=0)
            std::cout<<"Actual Number " << number <<std::endl;
            result_size[i]=number;
            i++;
    return result_size;
}

int main() {
    char *output_path = getenv("OUTPUT_PATH");
    FILE *f;
    if (output_path != NULL) {
    	f = fopen(output_path, "w");
    }
    else {
    	f = stdout;
    }
    
    int res_size;
    int* res;
    int _l;
    scanf("%d", &_l);
    
    int _r;
    scanf("%d", &_r);
    
    res = oddNumbers(_l, _r, &res_size);
    int res_i;
    for(res_i=0; res_i < res_size; res_i++) {
    
        fprintf(f, "%d\n", res[res_i]);
        
    }
    
    
    fclose(f);
    return 0;
}