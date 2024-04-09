# Arica
Use AI with the ever powerfull Linux terminal

>The Model uses a simple PyTorch chatbot. You can use natural language to give commands but they are laid out in a specific pattern, better consult `model_ml/dataset.json` for best usage!
## Requirements
```
- Pytorch 
- NLTK
```
## Features
```
File Creation
Directory Creation
File Deletion
Directory Deletion
Copy File
Install Packages
Remove Packages
Send File - NetCat
Recive File - NetCat
IP Address
ARP Scan
Check Internet Connection
List PCI Devices
List USB Devices
Display Contents - File
List Block Devices
List Running Services
Compress File
Change MAC Address
```

## Usage
```
python main.py -q="<YOUR_QUERY>"
```

Example
```
python main.py -q="list all the pci devices"
python main.py -q="check if internet is working"
python main.py -q="install the package htop"
```
