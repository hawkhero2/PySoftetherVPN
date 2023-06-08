from cryptography.fernet import Fernet
import json

# Generates fernet key for encryption ans saves it to settings file ?maybe
def generateFernKey(settings_file : dict):
        key = Fernet.generate_key()
        settings_file.__setitem__("key", key.decode())

# Encrypt password, creates key if there isnt one yet. WIP
def encrypt_pass(password_to_encrrypt : bytes):
        settings_file:dict = json.load(open("/libs/settings.json"))
        if settings_file.get("key")=="" :
                key = Fernet.generate_key()
                fern = Fernet(key)
                settings_file.__setitem__("key", key.decode())

                encrypted_password = fern.encrypt(password_to_encrrypt)
                settings_file.__setitem__("pw",encrypted_password.decode())

        else:
                key = bytes(settings_file.get("key"))
                fern = Fernet(key)

                encrypted_password = fern.encrypt(password_to_encrrypt)
                settings_file.__setitem__("pw",encrypted_password.decode())

                # encrypted_pw = fern.encrypt(bytes(settings_file.get("pw"),"utf-8"))
                
                # print("-------------below is fern key into str format in order to save it to settings file")
                # settings_file.__setitem__("key", key.decode())
                # print(settings_file.get("key"))
                # print("-----------")
                # print("this is the encrypted password decoded to str  = "+  encrypted_pw.decode())
                
                # settings_file.__setitem__("pw",encrypted_pw.decode())

                # decrypted_pw  = fern.decrypt(settings_file.get("pw"))
                # print("decrypted pw after saving it to a dict "+ decrypted_pw.decode())

                # print(settings_file)