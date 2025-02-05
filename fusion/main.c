#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

void secret() {
    printf("Bienvenue au QG LEGO!\n");
    printf("Félicitations! Vous avez construit la structure la plus solide!\n");

    errno = 0;
    FILE *file = fopen("flag", "r");
    if (file == NULL) {
        printf("Le flag est manquant? %d\n", errno);
        exit(0);
    }
    char flag[100];
    fgets(flag, sizeof(flag), file);
    printf("%s\n", flag);
    fclose(file);
}

int fusion() {
    char buffer[50];
    int check = 0;

    printf("Entrez les sets LEGO à assembler : (max 100 caractères) \n");
    scanf("%100s", buffer);

    printf("1969: Assemblage des briques en cours...\n");

    if (check == 0xdeadbeef) {
        secret();
    }

    printf("Assemblage des briques LEGO complété avec succès!\n");
    return 0;
}

int main(void) {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    printf("Construction 0.1969\n");
    printf("L'année du lancement d'un set LEGO emblématique.\n");
    printf("Un assemblage historique de briques pour bâtir un nouveau modèle LEGO!\n");
    printf("Initialisation du système en cours... OK\n");
    printf("Chargement des plans de construction... OK\n");
    system("/bin/cat /fusion.txt");

    fusion();

    printf("1969: Assemblage en cours avec les briques des sets Château, Espace, "
           "et de la gamme City... ERR\n");

    return 0;
}
