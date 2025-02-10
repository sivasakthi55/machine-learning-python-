import pandas as pd
from wordcloud import WordCloud 
import matplotlib.pyplot as plt

data=pd.read_excel('sales.xlsx')
text=" ".join(data['Description'].astype(str))
print(text)

wordcloud=WordCloud(width=800,height=400,background_color="white").generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt