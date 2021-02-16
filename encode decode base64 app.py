import base64

print("Welcom to breakers app")

ch = True
choose = input("\n\nwould you like to encode or decode a massage (en / de): ")
while ch is True:
    while choose == "en":
        massage = input("what is the phrase: ")
        text_byte = massage.encode('ascii')

        base64_byte = base64.b64encode(text_byte)

        base64_text = base64_byte.decode('ascii')
        print("\n\nthis encode massage: "+base64_text)
        break

    choose = input("\n\nwould you like to encode or decode a massage (en / de): ")

    while choose == "de":
        decode = input("what would you decode: ")

        decode_byte = decode.encode('ascii')

        base64_bytes2 = base64.b64decode(decode_byte)

        base64_decode_massage = base64_bytes2.decode('ascii')

        print(base64_decode_massage)
        break
    



