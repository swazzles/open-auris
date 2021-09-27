from sonotext import *
import nacl.secret
import nacl.utils
import base64

def generate_secret_key():
    return nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

def play_encrypted_symmetric(key, message):
    box = nacl.secret.SecretBox(key)
    encrypted = base64.b64encode(box.encrypt(message)).decode()
    message_to_sound(encrypted, base64.b64encode(key).decode())

k = generate_secret_key()
play_encrypted_symmetric(k, b'Hello, world.')