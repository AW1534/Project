# this script was only tested on linux. if it doesnt work, just switch to linux bozo
if pip install -r requirements.txt; then
  echo "all good, running..."
  python3 src/main.py
else
  echo "There was an issue installing the requirements\nPerhaps you don't have python/pip installed, or you are at school and pip is blocked lmfao nerd"
fi