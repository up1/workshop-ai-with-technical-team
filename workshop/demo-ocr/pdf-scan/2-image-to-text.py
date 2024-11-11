import easyocr
reader = easyocr.Reader(['en', 'th'])
result = reader.readtext("image_2.png", detail=0)
# type
print(type(result))
# print all index in list
for i in range(len(result)):
    print(result[i])

# Write result to text file
with open('page_1.txt', 'w') as f:
    for i in range(len(result)):
        f.write(result[i] + '\n')


