
#ifndef SM4_SM4_H
#define SM4_SM4_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stdlib.h>

void sm4_key_expansion(uint8_t *key);

void sm4_cipher(uint8_t *in, uint8_t *out);

#ifdef __cplusplus
}
#endif //extern "C"

#endif //SM4_SM4_H
