<<<<<<< HEAD
przesłać 3 pliki:
service.py (Twój kod serwera z zadania 2)

bentofile.yaml (Plik konfiguracyjny, który robiliśmy przed chwilą)

moj_model.bentomodel



# 1. Instalujemy Pythona i narzędzie pip
sudo apt update
sudo apt install python3-pip -y

# 2. Instalujemy BentoML na serwerze
pip3 install bentoml

pip3 install torch torchvision pillow

export PATH=$PATH:~/.local/bin


# budowanie dockera
# 1. Ładujemy Twój model do pamięci serwera
bentoml models import /home/maciek_szukalo/moj_model.bentomodel
# musi byc pelną ścieżką bo cos ten bentoml nie lubil samej nazwy pliku

# 2. Budujemy paczkę Bento (łączy kod z modelem)
bentoml build

# 3. Zmieniamy paczkę w gotowy kontener DOCKER!
# (Uwaga: upewnij się, że nazwa pasuje do tego, co wypluje komenda wyżej)
bentoml containerize st_l10_classifier: "wez poprawny tutaj id ze wszcesniejszej komendy"

4.
wlaczanie servera z jakims widokiem ze zyje
sudo docker run -it --rm -p 3000:3000 st_l10_classifier:kkg7eysn5g2ihmky serve
=======
przesłać 3 pliki:
service.py (Twój kod serwera z zadania 2)

bentofile.yaml (Plik konfiguracyjny, który robiliśmy przed chwilą)

moj_model.bentomodel



# 1. Instalujemy Pythona i narzędzie pip
sudo apt update
sudo apt install python3-pip -y

# 2. Instalujemy BentoML na serwerze
pip3 install bentoml

pip3 install torch torchvision pillow

export PATH=$PATH:~/.local/bin


# budowanie dockera
# 1. Ładujemy Twój model do pamięci serwera
bentoml models import /home/maciek_szukalo/moj_model.bentomodel
# musi byc pelną ścieżką bo cos ten bentoml nie lubil samej nazwy pliku

# 2. Budujemy paczkę Bento (łączy kod z modelem)
bentoml build

# 3. Zmieniamy paczkę w gotowy kontener DOCKER!
# (Uwaga: upewnij się, że nazwa pasuje do tego, co wypluje komenda wyżej)
bentoml containerize st_l10_classifier: "wez poprawny tutaj id ze wszcesniejszej komendy"

4.
wlaczanie servera z jakims widokiem ze zyje
sudo docker run -it --rm -p 3000:3000 st_l10_classifier:kkg7eysn5g2ihmky serve
>>>>>>> 67c31a867bc2eaf808bf2b9070126c5c0b99d120
