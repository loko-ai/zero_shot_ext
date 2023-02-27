zeroshot_doc = '''### Description
**Zero Shot Classifier** component performs multilingual text classification.

### Configuration

- **classes** allows to set the output labels.

### Input
The component accepts text.

**Example**:

```
Il vostro prodotto è meraviglioso
```

### Output
The output is the predicted probability to belong to the required **classes**:

**Example**:

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

'''