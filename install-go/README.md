# Installation de golang et configuration pour la production

La procédure officielle d'installation de golang est disponible :
* [window](https://golang.org/doc/install?download=go1.14.6.windows-amd64.msi)
* [Linux](https://golang.org/doc/install?download=go1.14.6.linux-amd64.tar.gz)
* [mac](https://golang.org/doc/install?download=go1.14.6.darwin-amd64.pkg)

# Go environnement

Pour pouvoir utiliser golang en console vous devez l'ajouter à variable d'environnements;
* Linux & mac : 
```shell
    export GOPATH=$HOME/go
    export PATH=$PATH:$GOPATH/bin
```
* *Window* :
    - Taper dans les recherches *"modifier les variables d'environnements"*
    - Cliquer sur ouvir
    - Puis cliquer une fois de plus sur variables d'environnement
    - Puis nouvelle variable;
    - Ajouter la ligne suivante au path:
```
    %USERPROFILE%\go\bin
```

# Go modules

Si vous voulez gérez les dépendances de vos fichiers où pouvoir publier un module vous utiliserez la commande ``` go mod init <mon_dossier> ```
Cette commande créera un fichier ```go mod``` qui peut se présenter de la façon suivante : 
```
module cmd

go 1.14

require (
        github.com/google/pprof v0.0.0-20190515194954-54271f7e092f
        golang.org/x/arch v0.0.0-20190815191158-8a70ba74b3a1
        golang.org/x/tools v0.0.0-20190611154301-25a4f137592f
)
```

Avec tous les dépendances dont votre modules a besoin pour fonctionner.

Pour en savoir un peu plus sur la commande `go mod`

```
go help mod
go help mod init
```

# Configuration de l'éditeur de code

Comme éditeur de code je vous recommande [visual studio code](https://code.visualstudio.com/)

Une fois que vous avez installé cet éditeur de texte, taper la commande suivante :


```
code .
```

qui permet d'ouvrir l'editeur de code dans le répertoire courant dans lequel vous vous êtes.

Pour une meilleur prise en main de golang il suffit d'installer l'extension suivante par le biais de la commande suivante : 

```
code --install-extension golang.go
```

Cette extension permet de faire de l'auto-complétion avec notre editeur de code en ce qui concerne le langage golang mais aussi de faire des analyses sur notre code pendant que nous codons.

# Premier programme en golang

créer un fichier portant le nom que vous souhaitez avec pour extension *.go*

```go
package main

import "fmt"

func main() {
	fmt.Printf("hello, world\n")
}
```

une fois ce code écrit, en console tapez

```shell
go build <hello.go>
```

*N.B :* Vous devez être dans le même repertoire courant que votre fichier que vous venez de créer.

L'execution de ce code produira le resultat suivant : 

```
hello, world
```
