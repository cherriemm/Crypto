#include "aes.h"
// 设置AES加密密钥
uint8_t key[] = {
    0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00,
};
uint8_t in[16];

uint8_t out[16]; // 128
uint8_t *w;
void setup() {
  // put your setup code here, to run once:
  int i;
  w = aes_init(sizeof(key));
  aes_key_expansion(key, w);
  Serial.begin(115200);
  pinMode(8, OUTPUT); 
  digitalWrite(8, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.print("start\n");
  if (Serial.available()== 16){
    Serial.readBytes(in, 16);
    // 设置触发信号
    digitalWrite(8, HIGH);
    aes_cipher(in, out , w);
    digitalWrite(8, LOW);
    Serial.write(out, 16);
  }
}
