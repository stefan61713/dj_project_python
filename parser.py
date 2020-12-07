import re


def split(text):
    text = text.replace("\n\n", "<nl>")
    text = text.replace("\n", " ")
    text = text.replace("U.S.", "<abbrev>")
    quotations = re.findall(r'\"(.+?)\"', text)
    for i in range(len(quotations)):
        text = text.replace(quotations[i], f"<quo{i}>")
    text = text.replace(".", ".<nl>")
    text = text.replace("!", "!<nl>")
    text = text.replace("?", "?<nl>")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("<abbrev>", "U.S.")
    text = " ".join(text.split())
    text = text.replace("<nl> ", "<nl>")
    for i in range(len(quotations)):
        text = text.replace(f"<quo{i}>", quotations[i])
    char = sum(ch.isalpha() for ch in text)
    sentences = text.split("<nl>")
    sentences = list(filter(None, sentences))
    return sentences, len(sentences), char
