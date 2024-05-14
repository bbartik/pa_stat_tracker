Clone the Repo:

```
git clone https://github.com/bbartik/pa_stat_tracker.git
```

Run in a virtual environment:

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python pa_stat_tracker
```

Example output:

```
(.venv) $ python pa_stat_tracker.py 
Enter firewall IP: 2.2.2.2
Enter username: admin
Enter password: 
Time     Throughput (kbps)
2024-05-14 06:45:18      252
2024-05-14 06:45:48      586
2024-05-14 06:46:12      202
2024-05-14 06:46:36      222
```


