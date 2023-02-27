<html><p><a href="https://loko-ai.com/" target="_blank" rel="noopener"> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/30443495/196493267-c328669c-10af-4670-bbfa-e3029e7fb874.png" width="8%" align="left" /> </a></p>
<h1>Zero Shot Classifier</h1><br></html>

**Zero Shot Classifier** extension performs multilingual text classification without any previous training.
It's built on top of the <a href="https://huggingface.co/joeddav/xlm-roberta-large-xnli">xlm-roberta-large-xnli</a> model 
and allows to set the output labels directly from the block configuration:

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/220967321-959526ea-8a46-4bd2-83b6-d8117adadf8d.png" width="80%" /></p>

The first time you run your flow, the extension automatically downloads the requested model. Once the model is loaded in
memory, output results will be faster. 

**Example**:

Input: 
```
Il vostro prodotto è meraviglioso
```

Output:
```
{
    "labels": [
        "positive",
        "neutral",
        "negative"
        ],
    "scores": [
        0.9860814213752747,
        0.007435222622007132,
        0.0064834230579435825
        ],
    "sequence": "Il vostro prodotto è meraviglioso"
}
```


## Configuration

In the file *config.json* you can choose where to mount your huggingface volume.
All the downloaded models will be saved in this directory:

```
{
  "main": {
    "volumes": [
      "/var/opt/loko/huggingface:/root/.cache/huggingface"
    ]
  }
}
```