#coding:utf-8
"""
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）
への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.replace(".", "")
words = str.split(" ")
words_ans = {}

for i, word in enumerate(words): #i:0~19 word:Hi~Can
	n = i + 1
	if n in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
		words_ans[word[:1]] = n
	else:
		words_ans[word[:2]] = n

print words_ans