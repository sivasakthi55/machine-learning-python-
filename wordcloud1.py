# WordCloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text="""Word Cloud is a data visualization technique used for representing text data in which the size of each word indicates its frequency or importance. Significant textual data points can be highlighted using a word cloud."""
print(text)

wordcloud=WordCloud(width=800,height=400,background_color="white").generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis('off')
plt