# Solution
Une fois qu'on a le username et le password, on peut les mettre dans le login form pour s'authentifier :) </br>
#### ``LEGO-us3rn4m3-5b1706:LEGO-p4ssw0rd-f72669`` </br>
<img src="https://github.com/user-attachments/assets/f009dc4b-b589-4c00-9994-b184b7ee85f6" alt="Alt Text" width="600" height="400">  </br></br>
Ewwwww, je dois m'authentifier en tant que iPhonescrub???? NOOOOOOOOOOOOOOOOO ok well lets use Burpy to see what I can do (BurpSuite). </br></br>
<img src="https://github.com/user-attachments/assets/39aaee72-c5cd-420e-a61d-0e625d4c97dd" alt="Alt Text" width="800" height="400">  </br></br>
Ok donc on a besoin du cookie auth= et user-agent. </br>
Modifions le user-agent pour qu'il soit "User-Agent: iPhone10 iOS/15.6" </br>
(En fait si on le fait de cette facon, on va voir que si on essaie d'envoyer par Burpsuite, Tailwind va comme reset le payload donc honnêtement, j'ai disable le domain de tailwing sur le Network tab pis voilà ahahaha) </br></br>
```
GET /ok HTTP/2
Host: auth10x.chals.ageei.org
Cookie: auth=5b1706f72669
Cache-Control: max-age=0
Sec-Ch-Ua: "iPhone";v="15.6"
Sec-Ch-Ua-Mobile: ?1
Sec-Ch-Ua-Platform: "iOS"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: iPhone10 iOS/15.6
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://auth10x.chals.ageei.org/
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
``` </br>
<img src="https://github.com/user-attachments/assets/f548b99c-f2ef-4d8c-9c71-e140486874aa" alt="Alt Text" width="300" height="300">  </br></br>

Flag: LEGO-us3R-4g3nt-e4d73c
