import streamlit as st
import random
import string


st.header("Aplikasi Encript dan Decript")

# algoritam xor
def xor_encrypt_decrypt(data, key):
    from itertools import cycle
    # Mengubah string data dan key menjadi bytes jika belum dalam format tersebut
    if not isinstance(data, bytes):
        data = data.encode()
    if not isinstance(key, bytes):
        key = key.encode()
    
    # Melakukan operasi XOR antara data dan key
    xored_data = bytes([a ^ b for a, b in zip(data, cycle(key))])
    
    return xored_data

#untuk menambahkan salt
def tambah_salt(kata, salt):
    return ''.join([char + salt for char in kata])

#untuk men-generate salt random
def salt_random ():
    return ''.join(random.choice(string.ascii_letters) for _ in range(4))

#untuk men-generate angka random
def generate_angka_random():
    return random.randrange(1000,9999)

def pisahkan_salt(kata_dan_salt, salt):
    return kata_dan_salt.replace(salt, '')

tab1, tab2 = st.tabs(["Enkripsi","Dekripsi"])
with tab1:
    kata = st.text_input(label="Masukan tulisan")
    salt = st.text_input(label="Masukan Salt (optional)")
    kunci = st.text_input(label="Masukan kunci (optional)")

    if salt == "" :
        salt = str(salt_random())
    else:
        salt = salt

    kata_dan_salt = tambah_salt(kata, salt)

    angka_random = generate_angka_random()
    # Enkripsi
    if kunci == "":
        encrypted = xor_encrypt_decrypt(kata_dan_salt, str(angka_random))
        st.write("## Data terenkripsi:", encrypted)
        if kata == "":
            st.write("## Kunci : ")
            st.write("## Salt : ")
        else:
            st.write("## Kunci : ", angka_random)
            st.write("## Salt : ", salt)
    else:
        encrypted = xor_encrypt_decrypt(kata_dan_salt, kunci)
        st.write("## Data terenkripsi:", encrypted)
        st.write("## Kunci : ", kunci)
        st.write("## Salt : ", salt)
        

    # Dekripsi
    if kunci == "":
        decrypted = xor_encrypt_decrypt(encrypted, str(angka_random))
        st.write("## Data + salt yang diekripsi:", decrypted.decode())
    else:
        decrypted = xor_encrypt_decrypt(encrypted, kunci)
        st.write("## Data + salt yang diekripsi:", decrypted.decode())

    kata_asli = pisahkan_salt (kata_dan_salt, salt)
    st.write("## Data asli yang dienkripsi : ", kata_asli)

with tab2:
    kata_decr = st.text_input(label="Masukan tulisan untuk didecript")
    salt_decr = st.text_input(label="Masukan Salt untuk didecript")
    kunci_decr = st.text_input(label="Masukan kunci untuk didecript")

    # Dekripsi
    decrypted_func = xor_encrypt_decrypt(kata_decr, kunci_decr)
    hasil = decrypted_func.decode('utf-8')
    st.write("## Data + salt yang diekripsi:", decrypted_func.decode())

    kata_asli = pisahkan_salt(hasil, salt_decr)
    st.write("## Kata asli tanpa salt : ", kata_asli)