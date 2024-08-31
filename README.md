# testing-ollama


### Set up Ollama on an Ubuntu machine

```bash
sudo apt-get update

curl -fsSL https://ollama.com/install.sh | sh
````


```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

```


