def n_gram(str, n):
    return [str[i:i+n] for i in range (len(str) - n + 1)]

if __name__ == "__main__":
    str = "I am an NLPer"
    print("単語bi-gram＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿")
    print(n_gram(str.split(), 2))
    print("文字bi-gram＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿")
    print(n_gram(str, 2))