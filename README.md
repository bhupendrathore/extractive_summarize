# extractive_summarize
extractive summarization with clustering and sentence embeddings


SETUP STEPS: 
```

1. cd extractive_summarize/
2. pip install -r req.txt
3. pip install "uvicorn[standard]" gunicorn
```
once installed run the following, make sure port open for the vm or port forward (for eg. with vscode)

```
uvicorn app.main:app --host 0.0.0.0 --port 8080

```
Go to the url and try out the summaraize url
```
http://<YOUR_HOST_IP>:8080/v1/docs
```


