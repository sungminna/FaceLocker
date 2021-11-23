# FaceLocker
password manager with face recognition

## Setup
1.  download latest anaconda
2.  run this command with the provided requirements.yaml 
```
conda env create -f requriements.yaml
```
3. update dependency
```
conda env update --file requirements.yaml --prune
```

## How to use 
1. run main.py
2.  add user and save confidential information 
3.  unlock and get access to your confidential

## Video tutorial
![aa_Trim](https://user-images.githubusercontent.com/26839173/143031312-3ab1f257-8244-40f8-9662-1b0af9db792f.gif)

----------

## Program structure
![st](https://user-images.githubusercontent.com/26839173/143029928-cb52bd65-f850-4ba4-aecb-93c4044bc701.png)

## UI
![ui](https://user-images.githubusercontent.com/26839173/143032454-48e3ed3d-0cb6-4d06-ae16-e7c0059ee576.png)

## UI event
![uie](https://user-images.githubusercontent.com/26839173/143032600-b33108cf-a967-4aa4-86da-0eef4a8855ae.png)

## Used stack
- PyQt6
- OpenCV
- Mediapipe
- Sqlite
- Pandas
- Numpy

## Future Task
- [ ] add encryption
- [ ] build release exe
- [ ] adopt other face comparison method (current version has slightly false negative tendency)
