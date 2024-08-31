# testing-ollama


### Set up Ollama on an Ubuntu machine

```bash
sudo apt-get update

curl -fsSL https://ollama.com/install.sh | sh

ollama ps
ollama list

ollama run llama3.1:8b


python3 -m venv myenv
source myenv/bin/activate

pip install jupyter

jupyter notebook --generate-config
# /home/vgdadmin/.jupyter/jupyter_notebook_config.py --> update c.ServerApp.allow_remote_access = True

jupyter lab --ip=10.0.0.4 --port=8888

````


