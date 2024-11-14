def sherch(key, sentences):
    index = -1
    flag = False
    sherch_word = key
    for sentence in sentences:
        if sherch_word in sentence.lower():
            index = sentences.index(sentence)
            flag = True
            break
    if flag:
        sentence = sentences[index]
        sentences.pop(index)
        sentences.insert(0, sentence)
        print(key)

    return flag, sentences

def chek_hostage(email):
    sentences = email["sentences"]
    flag, sentences = sherch("hostage", sentences)
    return flag, sentences

def chek_explosive(email):
    sentences = email["sentences"]
    flag, sentences = sherch("explos", sentences)
    return flag, sentences