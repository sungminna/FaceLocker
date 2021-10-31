import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Encrypt:
    def __init__(self):
        #self.salt = os.urandom(16)
        self.salt = b']\xd5*-\n\xcdN>h\x8b\xbc\xfe9\xc5\x03\x17'
        self.encrypt('123', 'tests')
        self.decrypt('123', 'gAAAAABhfovUT2c968AJsVXRrnrEQKbDdGtWaeA_5DHmkvC3ll2BTwgv1HoBXCn48NaE8mD8GHIfyvwqo-DCYfTO3mjQOLmg8w==')


    def encrypt(self, uid, text):
        password = uid.encode('utf-8')
        text_encoded = text.encode('utf-8')
        print(password)
        salt = self.salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)

        token = f.encrypt(text_encoded)
        token_str = token.decode('utf-8')
        print(token_str)

    def decrypt(self, uid, token_str):
        password = uid.encode('utf-8')
        token = token_str.encode('utf-8')
        salt = self.salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        text_encoded = f.decrypt(token)
        text = text_encoded.decode('utf-8')
        print(text)



if __name__ == '__main__':
    enc = Encrypt()