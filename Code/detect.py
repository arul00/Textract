import boto3
import sys
import re
import json
import os

client  = boto3.client('textract')

# Use document converted to bytes
img_path = "invoice2.jpeg"


# Open img and convert it to bytes
def main (file_name):
    with open(file_name, 'rb') as file:
        img_test = file.read()
        bytes_test = bytearray(img_test)
        print('Image loaded', file_name)

    response = client.detect_document_text(Document={'Bytes': bytes_test})

    blocks = response ["Blocks"]
    all_lines = [l for l in blocks if l["BlockType"] == "LINE" and l["Confidence"] > 50]
    text_output_file = 'rawtext(' + file_name + ').txt'
    file = open(text_output_file,"w+") 
    file.readline()

    # Output response in JSON file (data of coordinates, relationships, type of block and stuff like that)
    json_output_file = 'data(' + file_name + ').json'
    with open(json_output_file, 'w', encoding='utf-8') as f:
        json.dump(blocks, f, ensure_ascii=False, indent=4)

    print ("Output stored in", json_output_file)


    for l in all_lines:
        print (l["Text"])
        file.write("%s\n" % (l["Text"]))
    print ("TXT OUTPUT FILE: ", text_output_file)
    print ("Number of blocks:", len(blocks))


if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)