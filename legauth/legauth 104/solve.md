# Solution
Une fois qu'on a le username et le password, on peut les mettre dans le login form pour s'authentifier :) </br>
#### ``LEGO-us3rn4m3-5b1706:LEGO-p4ssw0rd-f72669`` </br>
<img src="https://github.com/user-attachments/assets/f009dc4b-b589-4c00-9994-b184b7ee85f6" alt="Alt Text" width="300" height="300">  </br>
Ewwwww, je dois m'authentifier en tant que iPhonescrub???? NOOOOOOOOOOOOOOOOO ok well lets use Burpy to see what I can do (BurpSuite). </br>
<img src="https://github.com/user-attachments/assets/39aaee72-c5cd-420e-a61d-0e625d4c97dd" alt="Alt Text" width="300" height="300">  </br>
Ok donc on a besoin du cookie auth= et user-agent. </br>
Modifions le user-agent pour qu'il soit "User-Agent: iPhone10 iOS/15.6" </br>
(En fait si on le fait de cette facon, on va voir que si on essaie d'envoyer par Burpsuite, Tailwind va comme reset le payload donc honnêtement, j'ai disable le domain de tailwing sur le Network tab pis voilà ahahaha) </br>
