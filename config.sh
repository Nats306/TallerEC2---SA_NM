
mkdir fastapi
cd fastapi
curl 

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp fastapi.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start fastapi
sudo systemctl enable fastapi




