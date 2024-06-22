#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_CHARS 256

void frequency_analysis(const char *ciphertext) {
    int freq[MAX_CHARS] = {0};
    
    // Calculate frequency of each character
    for (int i = 0; ciphertext[i] != '\0'; i++) {
        if (ciphertext[i] != ' ' && ciphertext[i] != '\n') {
            freq[(unsigned char)ciphertext[i]]++;
        }
    }
    
    // Display frequency of each character
    printf("Character frequencies:\n");
    for (int i = 0; i < MAX_CHARS; i++) {
        if (freq[i] > 0) {
            printf("'%c': %d\n", i, freq[i]);
        }
    }
}

int main() {
    const char *ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83\n(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*\n;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;";
    
    frequency_analysis(ciphertext);
    
    return 0;
}
