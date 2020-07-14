# How To
clone first and change the directory then

```
python3 -m pip install -r requirements.txt
uvicorn main:app --port=5555
```
Buat file cosim.service di /etc/systemd/system/ isinya :
```
[Unit]
Description=Cosine Similarity for AES

[Service]
WorkingDirectory=/path/to/the/app
ExecStart=/path/to/uvicorn main:app --port=5555
```
Melihat tempat uvicorn :
```
which uvicorn
```
Cara Start :
```
service cosim start
```
