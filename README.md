<html><p><a href="https://loko-ai.com/" target="_blank" rel="noopener"> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/30443495/196493267-c328669c-10af-4670-bbfa-e3029e7fb874.png" width="8%" align="left" /> </a></p>
<h1>Zero Shot Classifier</h1><br></html>

**Zero Shot Classifier** extension performs multilingual text classification without any previous training.
It allows to set the output labels directly from the block configuration:

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/233393933-92920ff8-9368-4db4-9a0a-48edc4f5a80f.png" width="80%" /></p>

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

In the file *config.json* you can set the **Hugging Face model**
(you can find the available models <a href="https://huggingface.co/models?pipeline_tag=zero-shot-classification&sort=downloads">here</a>), your **Hugging Face token** and where to mount your 
**Hugging Face volume** (all the downloaded models will be saved in this directory):

```
{
  "main": {
    "environment": {
      "HF_TOKEN": "<insert your HF token here>",
      "HF_MODEL": "joeddav/xlm-roberta-large-xnli"
    },
      "volumes": [
        "/var/opt/huggingface:/root/.cache/huggingface"
      ]
    }
}
```
**Note:** you can drop the **HF_TOKEN** variable if your model does not require authentication, otherwise you have to 
<a href="https://huggingface.co/models?pipeline_tag=zero-shot-classification&sort=downloads">sign up</a> and create your 
Access Token.  