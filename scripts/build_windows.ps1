python -m pip install --upgrade pip
python -m pip install pyinstaller

pyinstaller `
  --name JobNchill `
  --noconfirm `
  --windowed `
  --add-data "templates;templates" `
  --add-data "static;static" `
  app\desktop.py
