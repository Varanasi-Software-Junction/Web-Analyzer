import downloader as dd
import analyzer as an
import tokenizer as tk
import Training as t

from flask import Flask,render_template
app = Flask(__name__)

url="https://en.wikipedia.org/wiki/Main_Page"
# url="https://www.youtube.com"
# url="https://www.facebbok.com"

# url="http://varanasikshetra.com"
data=dd.downloadUrl(url)
divs=an.GetDivs(data)
pics=an.GetImages(data,url)
headings=an.GetHeadings(data)
paragraphs=an.GetParagraphs(data)
words=tk.words(data)
sentences=tk.Sentence(data)
frequency=tk.wordswithfrequencies(data)
stopwords=tk.stopwords(data)
removestopwords=tk.Removestopword(data)
frerstopword=tk.frerstopword(data)
plot=tk.plot(data)
rswplot=tk.RSWplot(data)
getset=tk.getset(data)
intersectionset=tk.intersectionset(data)
freinterset=tk.freinterset(data)
interfreGraph=tk.interfreGraph(data)
trainingset=t.training2()
getFullData=tk.getFullData(data,trainingset)
getsaveFullplot=tk.getsaveFullplot(data,trainingset)
@app.route("/")
 
def index():
    return render_template('display.html',pictures=pics,divs=divs,headings=headings,paragraphs=paragraphs,sentences=sentences,words=words,frequency=frequency,plot=plot,stopwords=stopwords,removestopwords=removestopwords,frerstopword=frerstopword,rswplot=rswplot,getset=getset,trainingset=trainingset,intersectionset=intersectionset,freinterset=freinterset,interfreGraph=interfreGraph,getFullData=getFullData,getsaveFullplot=getsaveFullplot)
if __name__ == "__main__":
 app.run(host="localhost", port=int("777"))