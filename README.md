# GoodReads Kindle Ed   
  
i wanted to have my goodreads recommendations in my kindle but the only way that was technically 'possible' was to use the kindle browser which is VERY slow and klunky on my K4 and isnt much better on newer kindles either  
  
So my solution is this :  
  
A proxy server that sits in the middle of the kindle and goodreads and requests the bulky page , strips it down and turn its contents into json then turn that json back to plain and simple html to send to the kindle  
  
  ok now the setup part  
  setting this up is easy  
  first install the browser extension "cookies.txt" and install it   
  go to "goodreads.com" login if you havent already and click on 'cookies.txt' and copy and save everything into a cookies.txt file  
  clone the repo by running ```git clone https://github.com/idreesmuhammadqazi-create/goodreadskindle```
  go in the directory by running ```cd goodreadskindle```
  put cookies.txt file in repo root  
  then run this from repo root  

  ```pip install -r requirements.txt```  
  then this also from repo root    
  ```python3 main.py```  
to run the flask server
visit that url on your kindle if ur on the same network OR you can host it on hackclub nest


Acknowledgements 
https://github.com/havanagrawal/
for the scraper

