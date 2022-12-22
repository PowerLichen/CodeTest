#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* checknum(char* s){
    int i;
    char cur_c;
    int top = -1;
    int count = 0;
    int s_size = strlen(s);
    char* stack = (char*)malloc(sizeof(char)*s_size);

    for(i=0; i<s_size; i++){
        cur_c = s[i];
        if(top>0){
            if(stack[top]=='1' && stack[top-1]=='1' && cur_c == '0'){
                top -= 2;
                count++;
                continue;
            }
        }
        
        stack[++top] = cur_c;

    }

    for(; top>=0 && stack[top]=='1'; top--){
        s[--i] = stack[top];
    }
    for(int j=0; j<count; j++){
        s[--i] = '0';
        s[--i] = '1';
        s[--i] = '1';
    }
    for(; top>=0; top--){
        s[--i] = stack[top];
    }

    free(stack);

    return s;
}

char** solution(const char* s[], size_t s_len) {
    char** answer = (char**)malloc(sizeof(char*)*s_len);
    for(int i=0; i < s_len;i++){
        answer[i] = checknum(s[i]);        
    }
    
    return answer;
}