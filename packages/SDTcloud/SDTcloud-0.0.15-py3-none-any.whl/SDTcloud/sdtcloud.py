import requests
import getpass
import json
import pandas as pd 

from datetime import datetime

class SDTcloud():
    def __init__(self):
        self.url = "http://10.110.31.15:31779"
        self.userId = input("ID: ")
        self.userPassword = getpass.getpass("PW: ")
        self.userToken = f"Bearer {self.login(self.userId, self.userPassword)}"

    # 로그인
    def login(self, 
            id: str, 
            pw: str
        ):
        "oauth/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        param = {
            "grantType": "password",
            "email": id,
            "password": pw
        }
        
        response = requests.request('post',f"{self.url}/oauth/token", headers=headers, params=param)
        
        if int(response.status_code/200) != 1:
            raise Exception(f"[ERROR] {response.text}")
        
        result = json.loads(response.content)

        return result["accessToken"]

    # 스토리지 등록
    def create_storage(self, name, tag):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.userToken
        }

        bodys = json.dumps({
            "name": name,
            "tag": tag
        })

        response = requests.request('post',f"{self.url}/stackbase/v1/storages", headers=headers, data=bodys)
        
        if int(response.status_code/200) != 1:
            raise Exception(f"[ERROR] {response.txt}")

        result = json.loads(response.content)
        result['createdAt'] = str(datetime.fromtimestamp(int(result['createdAt']/1000)))
        result['updatedAt'] = str(datetime.fromtimestamp(int(result['updatedAt']/1000)))

        return result
    
    # 스토리지 단건 정보 조회
    def get_storage(self):
        print("single get")
    
    # 유저의 스토리지 리스트 조회
    def list_storage(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.userToken
        }

        response = requests.request('get',f"{self.url}/stackbase/v1/storages", headers=headers)
       
        if int(response.status_code/200) != 1:
            raise Exception(f"[ERROR] {response.text}")
        
        result = json.loads(response.content)
        df = pd.DataFrame(result)
        for n in range(len(df)):
            df.loc[n, 'createdAt'] = datetime.fromtimestamp(int(df.loc[n, 'createdAt']/1000))
            df.loc[n, 'updatedAt'] = datetime.fromtimestamp(int(df.loc[n, 'updatedAt']/1000))
    
        return df

    # 스토리지 정보 수정
    def update_storage(self):
        print("update")
    
    # 스토리지 삭제
    def delete_storage(self):
        print("delete")

    # 폴더 등록
    def create_folder(self, storageId, parentId, dirName):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.userToken
        }

        bodys = json.dumps({
            "parentId": parentId,
            "name": dirName,
            "storageId": storageId
        })

        response = requests.request('post',f"{self.url}/stackbase/v1/folder", headers=headers, data=bodys)
        
        if int(response.status_code/200) != 1:
            raise Exception(f"[ERROR] {response.text}")

        result = json.loads(response.content)
        result['createdAt'] = str(datetime.fromtimestamp(int(result['createdAt']/1000)))
        
        return result
    
    # 트리 검색
    def get_tree(self, storageId, parentId):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.userToken
        }

        param = {
            "storageId": storageId,
            "parentId": parentId
        }

        response = requests.request('get',f"{self.url}/stackbase/v1/trees", headers=headers, params=param)
        
        if int(response.status_code/200) != 1:
            raise Exception(f"[ERROR] {response.text}")
        
        result = json.loads(response.content)
        df1 = pd.DataFrame(result)
        df2 = pd.DataFrame(result['trees'])
        
        df = pd.concat([df1.drop(['trees'], axis=1), df2], axis=1)
        
        return df

    # 폴더 수정
    def update_folder(self):
        print("update")

    # 폴더 삭제
    def delete_folder(self):
        print("delete")

    # 컨텐츠 조회
    def get_content(self):
        print("get")

    # 컨텐츠 수정
    def update_content(self):
        print("test")
    
    # 컨텐츠 삭제
    def delete_content(self):
        print("test")

    # 컨텐츠 다운로드
    def fget_content(self, fileId, getPath):
        
        headers = {
            "Authorization": self.userToken
        }

        response = requests.request('get',f"{self.url}/stackbase/v1/contents/download/{fileId}", headers=headers)

        if int(response.status_code/200) != 1:
            raise Exception(f"[ERROR] {response.text}")

        open(getPath, "wb").write(response.content)
        print("Success upload...")
    
    # 컨텐츠 등록
    def fput_content(self, storageId, folderId, filePath, fileVersion, fileFormat, fileTag):
        headers = {
            "Authorization": self.userToken
        }

        bodys = json.dumps({
            "storageId": storageId,
            "folderId": folderId,
            "version": fileVersion,
            "format": fileFormat,
            "tag": fileTag
        })

        file_open = open(filePath, 'rb')

        files={
            'request': (None, bodys, 'application/json'),
            "content": (filePath.split("/")[-1], file_open, 'application/octet-stream')
        }

        response = requests.request("POST", f"{self.url}/stackbase/v1/contents", headers=headers, files=files)

        if int(response.status_code/200) != 1:
            raise Exception(f"[ERROR] {response.text}")

        result = json.loads(response.content)
        result['createdAt'] = str(datetime.fromtimestamp(int(result['createdAt']/1000)))
        result['modifiedAt'] = str(datetime.fromtimestamp(int(result['modifiedAt']/1000)))
        
        return result