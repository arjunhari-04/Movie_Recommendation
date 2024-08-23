import streamlit as st
import os , requests, re , json
apiKey = "aaf111a5-9ae5-452d-b38e-a4b0c7dcaf25"
def apiFunction(usersInputObj):
    inputsArray = [{"id": "{input_1}", "label": "Enter your movie preference", "type": "text"}]
    prompt = "Recommend movies based on the user's preference {input_1}"
    filesData, textData = {}, {}
    for inputObj in inputsArray:
        inputId = inputObj['id']
        if inputObj['type'] == 'text':
            prompt = prompt.replace(inputId, usersInputObj[inputId])
        elif inputObj['type'] == 'file':
            path = usersInputObj[inputId]
            file_name = os.path.basename(path)
            f = open(path, 'rb')
            filesData[inputId] = f

    textData['details'] = json.dumps({'appname': 'movie recommender 101','prompt': prompt,'documentId': 'no-embd-type','appId' : '66c899c964d827b744a29fdf' , 'memoryId' : '','apiKey': apiKey})
    response = requests.post('https://apiappstore.guvi.ai/api/output', data=textData, files=filesData)
    output = response.json()
    return output['output']
usersInputObj = {'{input_1}' : input("Enter your movie preference "),}
output = apiFunction(usersInputObj)
url_regex = r'http://localhost:7000/'
replaced_string = re.sub(url_regex,'https://apiappstore.guvi.ai/' , output)
print(replaced_string)
