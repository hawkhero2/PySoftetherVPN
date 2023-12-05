# PySoftetherVPN

<br/>

---

<br/>

## What is PySoftetherVPN?

- PySoftetherVPN is (_at the moment a work in progress_) project that attaches a UI to Softether VPN for Unix. Currently makes use of some bash scripts from  [intellexlab-files](https://github.com/mfaizanse/intellexlab-files) repo.


## How to compile to binary

- Install Nuitka 
```cmd
python3 -m pip install nuitka
```
- Then compile the vpn.py file
```
python3 -m nuitka vpn.py
```