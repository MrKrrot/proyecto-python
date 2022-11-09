# Proyecto Parcial 2
## Pre-requisitos
 - [Git](https://git-scm.com/download/win) (Obligatorio)
 - [Python](https://www.python.org/downloads/) (Obligatorio)
 - [Visual Studio Code](https://code.visualstudio.com/) (Recomendable)

Y tener una cuenta creada en [GitHub](https://github.com)

## Configurar Git

### 1. Configurar nombre y correo
**Si ya tienes configurado Git con tu nombre y correo puedes omitir este paso.**
En caso de que sea la primera vez que tienes instalado Git en tu computadora, tienes que configurarlo para que en el historial de los commits se vea tu nombre y correo. Para esto usaremos los siguientes comandos:

```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

Lo único que cambiará del comando será `John Doe` y `johndoe@example.com` ya que tendrás que poner tu nombre y correo respectivamente. Si quieres aprender más puedes hacer clic [aquí](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configurando-Git-por-primera-vez).

### 2. Descargar el repositorio de GitHub
Para descargar este repositorio utiliza el siguiente comando:
```bash
$ git clone https://github.com/MrKrrot/proyecto-python.git
```
Lo que hará es clonar el repositorio en tu computadora en la carpeta en donde estés situado al momento de ejecutar el comando, por lo que si abres una terminal situado en el escritorio, creará una carpeta con el nombre `proyecto-python` en el escritorio.

### 3. Agregar cambios al repositorio
Cuando hayamos descargado el repositorio en nuestra máquina ya seremos capaces de modificar los archivos para agregarle más contenido a estos. Para que se guarden los cambios en Git usaremos los siguientes dos comandos:
```bash
$ git add .
$ git commit -m "Mensaje explicando el cambio realizado"
```

El primer comando agregará todos los archivos del repositorio al `área de preparación` el cual le dirá a git que estos archivos serán los que queremos guardar sus cambios. El segundo comando realiza un nuevo commit agregando a todos los archivos que se encuentren en el `área de preparación`, por lo que ya tendremos guardado nuestros cambios realizados.

**NOTA**: Nótese el `.` en el comando `git add`, esto quiere decir que agregará todos los archivos del repositorio, si se quieren agregar solo ciertos archivos entonces utilizariamos el siguiente comando:
```bash
$ git add archivo.txt
```
Este comando agregaría solamente el archivo `archivo.txt` al `área de preparación`.

### 4. Subir los cambios a GitHub
Ya tenemos nuestros cambios, pero todavía no los agregamos al repositorio remoto para que todas las personas puedan tener nuestros archivos modificados. Para subir los cambios a GitHub usaremos el siguiente comando:

```bash
$ git push
```
Este comando subirá los cambios a GitHub de nuestra máquina local.

## **Integrantes**
 - Camacho Trejo Aurora Cristal
 - Curiel Román Mario Iván
 - Sánchez Olguín Rafael
 - Villareal De Leija Angela Elizabeth

