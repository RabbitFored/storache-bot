from Crypto.Cipher import AES
import os

key = "7F30F2253DEC8C1E88D3C0C91416AE1B".encode('utf-8')  
iv = "C085CCCB55A247AC".encode('utf-8')  
chat = int(os.environ.get("chat"))