import pandas as pd
DF = pd.read_csv(r'/Users/christinemagnotta/Web-Design-Challenge/WebVisualizations/cities.csv')
html = DF.to_html()
print(html)

