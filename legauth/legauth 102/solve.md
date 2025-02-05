# Solution
Bon, lorsqu'on rentre dans le site, on se retrouve avec le login form des challenges précédents. Cependant on nous dit "On a décider d'enlever la validation client. On utilise maintenant une BD."... Intéressant. Ca veut dire qu'on va devoir faire du SQLi. Youpiiiii
Alors, on commence par un petit boolean-based query...    
<img src="https://github.com/user-attachments/assets/5f8d6c81-9d73-4a9e-98b1-90663f47a401" alt="Alt Text" width="400" height="400">  
What? Ok lol... après quelques petits tests, on se rend compte que le caractère interdit est le point-virgule (;) donc si on l'enlève  
<img src="https://github.com/user-attachments/assets/eae3c530-b317-4d42-869f-df6f44b82cb9" alt="Alt Text" width="400" height="400">   
Interéssant. On ne nous affiche rien à l'écran sauf que des messages d'erreur. Ca tombe donc dans ce qui serait du Error-based Blind SQLi. Notre 1e intuition devrait être de chercher à savoir quel type de BD qu'on travaille avec...bah pas pour moi qui était convaincu que c'était du Postgresql for some reason lololol (SQLite). Donc, prochaine étape est de savoir combien de colonnes qu'il y a  
<img src="https://github.com/user-attachments/assets/14add371-c953-4a32-8d31-9dd391323f47" alt="Alt Text" width="400" height="400">   
Trouvé!! Il y a 3 colonnes et vu qu'on est dans un login form la table doit forcément s'appeler "users" donc essayons ceci  
``1' UNION SELECT username,null,null from users where username LIKE '%'-- ``  
<img src="https://github.com/user-attachments/assets/69ceeea4-ded6-4cb8-934d-52b571dc4e30" alt="Alt Text" width="400" height="400">  
Ok donc on va devoir fort probablement faire un script pour brute force le username qui est probablement le 1er flag     
<img src="https://github.com/user-attachments/assets/9d1021a0-8e22-47ec-83aa-ce8653bf45a4" alt="Alt Text" width="400" height="400">    
SUCCESS!!!!    
Flag: LEGO-us3rn4m3-5b1706

