import os
import requests
import tempfile

def test():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        for key, value in os.environ.items():
            f.write(f"{key}: {value}\n")
        output_file = f.name
    f.close()

    url = "http://localhost:3000/upload"
    files = {"files": (output_file, open(output_file, "rb"))}
    response = requests.post(url, files=files)



test()
    