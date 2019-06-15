# Vanilla-Normals-Renewed-1.13
A shaders compatible minecraft texture pack, based on vanilla but with normals and proper glossiness information.
This version (renewed) is made for PBR, but still a WORK IN PROGRESS, so you may encounter some textures with strange behavior.

⚠️ THIS VERSION IS NOT COMPATIBLE FOR MINECRAFT 1.12 OR BELOW ⚠️

## Description

I didn't want any of those fancy high-resolution texture packs in order to enjoy normal mapping and specular highlights.
So I decided to make my own, but based on vanilla textures.

This texture pack is free for everyone to use! However if you wish to support me, you can join my Patreon : https://www.patreon.com/Poudingue

## Copyright


You can do whatever you want with my texture pack, screenshots, videos, modifications for personal use or redistribution, as long as you don't sell it and provide a link to this page or my Patreon page.

## Screenshots

⚠️ The screenshots provided here were made with SEUS renewed, an an old version of minecraft, the results will differ with other shaders ⚠️

Textures have bump mapping information, allowing parallax occlusion mapping and normal mapping.
Smoothness information is very important for the credibility of materials too, especially when the sun lights it at grazing angles.

![Normals and smoothness](https://user-images.githubusercontent.com/18035775/34640565-eb2fc134-f2f4-11e7-9d06-c615fb50aed1.png)

Metals and smooth materials now have the correct information to compute reflections.
SEUS renewed heavily relies on Screen Space Reflections for this and don't take correctly roughness surfaces for it, so the reflections may be too shiny and imperfect. However using SEUS PTGI will provide Path-Traced reflections and indirect lighting, and correctly take into account roughness.

![Metal and smooth materials](https://user-images.githubusercontent.com/18035775/34640564-eb1388de-f2f4-11e7-8597-e132e9cde2db.png)

## Installation

- Install a shader supporting normal and specular mapping. If you don't know which one, give this one a shot : https://sonicether.com/seus/ and if you want raytracing, it should also work properly with SEUS PTGI E7 : https://www.patreon.com/sonicether

- Joining the discord server is recommended for update notifications, support, and giving feedback.
  [Join Here](https://discord.gg/bn8S5Z3)

### Old zip Based Method

1. On this page, click on «Clone or download», then «Download as ZIP»
2. Go to the minecraft folder
    - For windows, go to "%appdata%/.minecraft" on your start menu.
    - For Linux, go to "~/.minecraft" in your file explorer.
    - For Mac OS, go to "~/Library/Application Support/minecraft" in your file explorer
3. Go into the resourcepacks folder. Create it if it doesn't exist
4. Extract the file you downloaded here
5. Select the right shader and resourcepack in minecraft options
6. Enjoy !

### NEW GIT powered Install Method

Git is a version control software that github uses to manage all the code that they host, which can be used to make installation really easy.
Version Control software allows multiple authors to collaborate, and track all the changes made, and who made what changes

#### Linux Git Install
    1. To do this, you will first need to open a terminal window
    2. Then verify that git is installed by running `git --version` This will make sure that it is installed, and additionally, show what version is installed
        - If you get an output that looks like `git version 2.21.0` then it is installed.
        - If you get an output like this `bash: git: command not found` (Different shells will appear different, but most will basically state that the command wasn't found.) Different Distros have different approaches to installing software, if you're having trouble look up "<insert Linux Distro Here> Install git"
    3. Once you have certified git is installed, move your terminal to the folder `~/.minecraft/resourcepacks` by running `cd ~/.minecraft/resourcepacks`
    4. After you're in the right folder, run 'git clone https://github.com/Poudingue/Vanilla-Normals-Renewed.git` to clone the entire repository to your computer.
        - You will not need to zip the repo to have it work, Minecraft can handle unzipped texture packs.

##### Linux Git Update
    1. Please have installed the texture pack using the above guide. This won't work if you went on github, downloaded the Zip, and extracted it.
    2. Open up a terminal
    3. Change to the TEXTURE PACK'S folder by running `cd ~/.minecraft/resourcepacks/Vanilla-Normals-Renewed`
    4. Run `git pull origin' to download the latest version.
        - You might want to relaunch Minecraft after this to make sure it uses the latest textures.


#### Windows Git Install
    1. Install Git and add to the path (don't' worry there is a guide below)
        1. Open a web browser and [download](https://git-scm.com/download/win) the latest version of git
        2. Run the installer
            - When it comes to the "Adjusting your PATH environment" the middle option is recommended, as it allow for more flexibility, but doesn't cause problems.
            - When it comes to the "Configuring the line ending conventions", set it to "Checkout Windows-style, commit Unix-style line endings"
                - Linux and Windows use different line ending in text files, and this will prevent any problems.
            - When it comes to the " Configuring the Terminal Emulator to use with Git Bash" the Windows one is sufficient for most work
        3. Once it is installed, launch command prompt
            - Press the Windows key + "R", to open a run box, then type in cmd.exe, and press enter
        4. Change to the resourcepack folder using the command  `cd %AppData%/.minecraft/resourcepacks`
        5. Clone the repository to your computer by running git clone https://github.com/Poudingue/Vanilla-Normals-Renewed-1.12.git
            - You will not need to zip the repo to have it work, Minecraft can handle unzipped texture packs.

##### Windows Git Update
    1. Please have installed the texture pack using the above guide. This won't work if you went on github, downloaded the Zip, and extracted it.
    2. Open up command prompt
        - Press the Windows key + "R", to open a run box, then type in cmd.exe, and press enter
    3. Change to the TEXTURE PACK'S folder by running `cd %appdata%/.minecraft/resourcepacks/Vanilla-Normals-Renewed`
    4. Then run `git pull origin' to download the latest version.
        - You might want to relaunch Minecraft after this to make sure it uses the latest textures.            

## Knowg Bugs on BSL 7.1
- Some reflections on edges are sometimes directly reflecting the sky, looking incorrectly bright.

## Known Bugs on SEUS Renewed
- All reflections are smooth reflections. This strongly affects the materials appearances and can look wrong.

## Known Bugs on SEUS PTGI E7.1
- Insufficiently smooth metals do not look like metals if “full raytrace reflections” is not active. (This is what causes stripes on iron blocks)
- Underwhelming normals cause surfaces to look more flat
- Parallax Occlusion Mapping not supported yet
