# Automatic-Bridger
Selenium script to bridge TP-LINK (Model No. TL-WR740N / TL-WR740ND) router.

Installation of selenium using pip:
```ssh
pip install selenium
```

Usage :
```python
python router.py --v 1
```
OR
```python
python router --v 0
```
The v flag will determine the type of IP address. ( 0 for 192.168.0.1 and 1 for 192.168.1.1 )

Run the following to restart router
```python
python3 restart_router.py --v 1
```
