---
created: 2022-11-19 13:35:00
modified:
title: Computer Graphics
---

# Computer Graphics:

## SDL2

- SDL documentation: http://wiki.libsdl.org/CategoryInit
- SDL tutorial (with setup): https://www.youtube.com/watch?v=yFLa3ln16w0&ab_channel=CS50

## Immediate Mode GUI

- Sol on Immediate Mode GUIs (IMGUI): http://iki.fi/sol/imgui/

## Java 3D

- https://docs.oracle.com/cd/E17802_01/j2se/javase/technologies/desktop/java3d/forDevelopers/j3dguide/j3dTOC.doc.html

# BASIC language

- QBasic 1.1 online: https://archive.org/details/msdos_qbasic_megapack

## Use QuickBasic with dosbox

Install dosbox with the following command:

```shell
    $ sudo apt-get install dosbox
```

Create a directory for the dos mount

```shell
    $ mkdir /home/<user>/.olddos
```

> Note: replace <user> with your own user on the command above

Download QuickBasic 7.1 on https://www.qbasic.net/en/top-ten-downloads/ unzip it and move it to the mount directory

```shell
    $ mv /<path-to-unzipped-folder>/qbx /home/user/.olddos
```

Startup dosbox and QuickBasic

```shell
    $ dosbox
    Z:\>mount c /home/<user>/.olddos
    Drive C is mounted as local directory /home/<user>/.olddos
    Z:\>C:
    C:\>
    C:\> cd QBX
    C:\> BIN\QBX.EXE
```
