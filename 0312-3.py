import requests
response = requests.get("http://www.novelscape.net/wxxs/j/ jingyong/ffwz/001.htm")
response.encoding = "big5"
book1 = response.text
print(book1)
print("length: "+str(len(book1))+"\n")
print("\n第300個字元: "+book1[300])
print("\n從300開始: "+book1[300:])
print("\n從頭到300: "+book1[:300])
print("\n從10開始到300, 間隔10: "+book1[10:300:10])
book1list=book1.split()
print("\nsplit space to list: ")
print(book1list)
joinlist=""
joinlist=", ".join(book1list)
print("\njoin list with , : "+joinlist)
print("\nif it starts with A")
print(book1.startswith("A"))
print("\nif it ends with .")
print(book1.endswith("."))
print("\nfind html: "+str(book1.find("html")))
print("\nfind last html: "+str(book1.rfind("html")))
print("\ncount html: "+str(book1.count("html")))