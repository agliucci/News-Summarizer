import tkinter as tk
import nltk #type: ignore
from newspaper import Article #type: ignore
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context



nltk.download('punkt')

# url = "https://www.cnn.com/business/live-news/doj-apple-antitrust-lawsuit-03-21-24/index.html"

# article = Article(url)

# article.download()
# article.parse()

# article.nlp()

#print(f"Title: {article.title}")
# print(f"Author: {article.authors}")
# print(f"Publication date: {article.publish_date}")
# print(f"Summary: {article.summary}") 





def summarize():
    user_input = url_textbox.get()
    article = Article(user_input)
    article.download()
    article.parse()
    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    publish.config(state="normal")
    summary_text.config(state="normal")

    title.delete("1.0", "end")
    title.insert("1.0", article.title)


    
    author.delete("1.0", "end")
    author.insert("1.0", article.authors)

    publish.delete("1.0", "end")
    publish.insert("1.0", article.publish_date)

    summary_text.delete("1.0", "end")
    summary_text.insert("1.0", article.summary)

    title.config(state="disabled")
    author.config(state="disabled")
    publish.config(state="disabled")
    summary_text.config(state="disabled")




window = tk.Tk()
window.title("News Article Summarizer")
window.geometry("900x1200")
window_label = tk.Label(text="Welcome to the news article summarizer!", font = ("Times New Roman", 20), pady=20)
window_label.pack()
'''URL Label'''
url_label = tk.Label(text="Enter the URL: ", font = ("Times New Roman", 20))
url_label.pack()

'''URL textbox'''
url_textbox = tk.Entry(font = ("Times New Roman", 20), width=140)
url_textbox.pack()

'''URL Button'''
url_button = tk.Button(text="Summarize", font = ("Times New Roman", 20), command=summarize)
url_button.pack()

'''Title'''
title_label = tk.Label(text="Title: ", font = ("Times New Roman", 20))
title_label.pack()
title = tk.Text(height = 1.8, width=140)
title.config(state="disabled", font=("Times New Roman", 16))
title.pack()

'''Author'''
author_label = tk.Label(text="Author: ", font = ("Times New Roman", 20))
author_label.pack()
author = tk.Text(height = 1.8, width=140)
author.config(state="disabled", font=("Times New Roman", 16))
author.pack()

'''Publish Date'''
publish_label = tk.Label(text="Publication Date: ", font = ("Times New Roman", 20))
publish_label.pack()
publish = tk.Text(height = 1.8, width=140)
publish.config(state="disabled", font=("Times New Roman", 16))
publish.pack()


'''Summary'''
summary_label = tk.Label(text="Summary: ", font = ("Times New Roman", 20))
summary_label.pack()
summary_text = tk.Text(height = 80, width=140)
summary_text.config(state="disabled", font=("Times New Roman", 16))
summary_text.pack()




window.mainloop()