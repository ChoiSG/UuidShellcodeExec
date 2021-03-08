import uuid 

def convertToUUID(shellcode):
	# If shellcode is not in multiples of 16, then add some nullbytes at the end
	if len(shellcode) % 16 != 0:
		print("[-] Shellcode's length not multiplies of 16 bytes")
		print("[-] Adding nullbytes at the end of shellcode, this might break your shellcode.")
		print("\n[*] Modified shellcode length: ", len(shellcode)+(16-(len(shellcode)%16)))
		
		addNullbyte =  b"\x00" * (16-(len(shellcode)%16))
		shellcode += addNullbyte 

	uuids = []
	for i in range(0, len(shellcode), 16):
		uuidString = str(uuid.UUID(bytes_le=shellcode[i:i+16]))
		uuids.append('"'+uuidString+'"')

	return uuids

def main():
	# Copy/Paste the MessageBox payload here. buf = <shellcode> 

	uuids = convertToUUID(buf)
	print(*uuids, sep=",\n")

main()