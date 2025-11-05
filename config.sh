
mkdir fastapi
cd fastapi
git clone https://github.com/Nats306/TallerEC2---SA_NM.git .

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo cp fastapi.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start fastapi
sudo systemctl enable fastapi




