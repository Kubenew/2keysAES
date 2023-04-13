# 2keysAES
 AES encryption in Python using the cryptography library, using two keys.
 the encrypt function takes in a plaintext byte string, as well as two key byte strings, key1 and key2. 
 The plaintext is first padded to be a multiple of the AES block size (16 bytes). 
 Then, two AES cipher objects are created using the two keys, and they are concatenated into a single cipher object using the + operator. 
 The concatenated cipher object is then used to encrypt the padded plaintext, and the resulting ciphertext is returned.
  uses the ECB mode, which is not secure for general use. In practice, you should use a secure mode like CBC or GCM, and include an initialization vector (IV) in the encryption process.
