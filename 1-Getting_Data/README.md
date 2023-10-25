# How to install PATRIC Command Line (Windows)

1. First of all, type

```console
wsl
```

on Windows CMD to enter on Windows Subenvironment for Linux.

2. Follow the steps of installation on Linux here: https://www.bv-brc.org/docs/cli_tutorial/cli_installation.html

The following commands were used:

```console
curl -O -L https://github.com/BV-BRC/BV-BRC-CLI/releases/download/1.040/bvbrc-cli-1.040.deb
sudo dpkg -i bvbrc-cli-1.040.deb
sudo sudo apt-get -f install
```

3. Create an account on https://www.bv-brc.org/

Before starting to work with PATRIC Command Line, login:

```console
p3-login username
```

After that, it will ask for your password.

Now you are able to looking for any type of data from PATRIC database.

All available strains for a species can be obtained typing (using Salmonella enterica as an example):

```console
p3-all-genomes --eq "species,Salmonella enterica"
```

To save this information in a file (for example, genomes.tsv), type:

```console
p3-all-genomes --eq "species,Salmonella enterica" > genomes.tsv
```

The file will be saved on your current directory.