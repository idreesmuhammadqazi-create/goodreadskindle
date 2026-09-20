# GoodReads Kindle Ed   
  
i wanted to have my goodreads recommendations in my kindle but the only way that was technically 'possible' was to use the kindle browser which is VERY slow and klunky on my K4 and isnt much better on newer kindles either  
  
So my solution is this :  
  
A proxy server that sits in the middle of the kindle and goodreads and requests the bulky page , strips it down and turn its contents into json then turn that json back to plain and simple html to send to the kindle  

  
  you can demo it at http://k.pseudorun.tech by opening it in your kindle browser
  
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
the steps for that are here :  
1 ssh in to your hackclub nest machine and clone the repo  
2 cd in to the repo  
3 run ```nano cookies.txt``` and then copy and paste all cookies from cookies.txt and then press ctrl + s and then ctrl + x to save and quit  
4 run ```pip install -r requirements.txt --break-system-packages ##sorry i dont know how to avoid using this flag```  
5 run ```python3 main.py &``` to run it detached or run(use for actual persistent hosting) ```python3 main.py``` to run normally
6 get a cloudflare tunnel with https off if you have an older non jailbroken kindle   
7 vist the tunnel address from your kindle

7 if you DO have a newer kindle then just use any normal hosting service that supports flask ,which is basically all of them tho you have to first enocde ur cookies in base64 and make an env var with the name 'COOKIES' and the base64 as value
  
  
NOTES :
    this is a WIP so expect lots of improvements and changes (rn my priority is to add a book search and book page view option)  

TODOS :
    1 : Add a book search option that allows a user to search a book on goodreads and veiw its title description etc  
    2 : add a book page feature that allows you to see a book's rating and reviews (might add a post review functionality too)

Acknowledgements 
https://github.com/havanagrawal/
for the scraper logic i picked up quite a few things from this guy  


HACKCLUB NEST for hosting  

  
