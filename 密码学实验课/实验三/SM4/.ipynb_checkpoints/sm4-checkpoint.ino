#include "sm4.h"

uint8_t key[16] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                   0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10};/*补充密钥*/;
uint8_t plaintext[16] = {0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
                         0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10
                        };
uint8_t out[16] = {};

void setup() {
  sm4_key_expansion(key);/*补充函数进行密钥扩展*/;
  Serial.begin(115200);
  pinMode(8, OUTPUT);
  digitalWrite(8, LOW);
}

void loop() {
  if (Serial.available()== 16){
    Serial.readBytes(plaintext, 16);
    digitalWrite(8, HIGH);
    sm4_cipher(plaintext, out);/*补充函数进行SM4加密*/;
    digitalWrite(8, LOW);
    Serial.write(out, 16);
  }
}
