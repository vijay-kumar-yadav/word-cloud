import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    punctuation = []
    for e in punctuations:
      punctuation.append(e)
    
    text = ""
    for letter in file_contents:
      if(letter not in punctuation):
        text+=letter
      else:
        text+=" "    
    text_list = text.split(" ")
    text_list_new = []
    for word in text_list:
      if word not in uninteresting_words and word.lower() not in uninteresting_words:
        text_list_new.append(word)
    while("" in text_list_new) :
      text_list_new.remove("")
    count_dict = {}
    for word in text_list_new:
      if(not word.isnumeric()):
        if word not in count_dict:
          count_dict[word] = 1
        else:
          count_dict[word] += 1
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(count_dict)
    return cloud.to_array()



file_contents = "He that goeth about to persuade a multitude that they are not so well Governed[21] as they ought to be, shall never want attentive and favorable hearers; because they know the manifold defects whereunto every kind of regimen is subject, but the secret lets and difficulties, which in public proceedings are innumerable and inevitable, they have not ordinarily the judgment to consider."
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()