# Deactivate
deactivate
# Delete the folder
Remove-Item -Recurse -Force venv

# Create a Fresh Environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Upgrade pip first (to avoid that notices)
python -m pip install --upgrade pip

# reinstall
pip install -r requirements.txt





(venv) PS D:\Documents\github\djangogirls> pip install --upgrade --force-reinstall --no-cache-dir django
Collecting django
  Downloading django-6.0.2-py3-none-any.whl.metadata (3.9 kB)
Collecting asgiref>=3.9.1 (from django)
  Downloading asgiref-3.11.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.5.0 (from django)
  Downloading sqlparse-0.5.5-py3-none-any.whl.metadata (4.7 kB)
Collecting tzdata (from django)
  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading django-6.0.2-py3-none-any.whl (8.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 47.2 MB/s  0:00:00 
Downloading asgiref-3.11.1-py3-none-any.whl (24 kB)
Downloading sqlparse-0.5.5-py3-none-any.whl (46 kB)
Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
  Attempting uninstall: tzdata
    Found existing installation: tzdata 2025.3
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0/4 [tzdata]
[notice] A new release of pip is available: 25.3 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0/4 [tzdata]ERROR: Exception:
Traceback (most recent call last):
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\cli\base_command.py", line 107, in _run_wrapper
    status = _inner_run()
             ^^^^^^^^^^^^
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\cli\base_command.py", line 98, in _inner_run
    return self.run(options, args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\cli\req_command.py", line 85, in wrapper
    return func(self, options, args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\commands\install.py", line 458, in run
    installed = install_given_reqs(
                ^^^^^^^^^^^^^^^^^^^
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\req\__init__.py", line 79, in install_given_reqs
    uninstalled_pathset = requirement.uninstall(auto_confirm=True)        
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\req\req_install.py", line 674, in uninstall
    uninstalled_pathset = UninstallPathSet.from_dist(dist)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\req\req_uninstall.py", line 523, in from_dist
    for path in uninstallation_paths(dist):
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\req\req_uninstall.py", line 49, in unique
    for item in fn(*args, **kw):
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\req\req_uninstall.py", line 75, in uninstallation_paths
    entries = dist.iter_declared_entries()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\metadata\base.py", line 502, in iter_declared_entries
    self._iter_declared_entries_from_record()
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\metadata\base.py", line 463, in _iter_declared_entries_from_record     
    text = self.read_text("RECORD")
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Documents\github\djangogirls\venv\Lib\site-packages\pip\_internal\metadata\importlib\_dists.py", line 195, in read_text
    content = self._dist.read_text(str(path))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\drake\AppData\Local\Programs\Python\Python312\Lib\importlib\metadata\__init__.py", line 818, in read_text
    return self._path.joinpath(filename).read_text(encoding='utf-8')      
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      
  File "C:\Users\drake\AppData\Local\Programs\Python\Python312\Lib\pathlib.py", line 1029, in read_text
    return f.read()
           ^^^^^^^^
  File "<frozen codecs>", line 322, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9c in position 2: invalid start byte
