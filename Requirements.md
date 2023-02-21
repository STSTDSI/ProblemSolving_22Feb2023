## Prerequisites for the exercises of this workshop
1. Make sure a recent version of Python3 is installed on your machine.
2. Make sure [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) is installed on your machine.

### Install the [Pygame](https://www.pygame.org/docs/) library
`python3 -m pip install -U pygame`

Warning: If you are on Linux, please see the extra step below to finish the installation.

You are now set up! You can try the following command to verify that the library is installed:

`python3 -m pygame.examples.aliens`



### Linux users

#### If not using a specific conda virtual environment with Anaconda
Run this in bash:

```
$ cd /home/$USER/miniconda/lib  # Replace $ENV with the name of your conda environment.
$ mkdir backup  # Create a new folder to keep the original libstdc++
$ mv libstd* backup  # Put all libstdc++ files into the folder, including soft links
$ cp /usr/lib/x86_64-linux-gnu/libstdc++.so.6  ./ # Copy the c++ dynamic link library of the system here
$ ln -s libstdc++.so.6 libstdc++.so
$ ln -s libstdc++.so.6 libstdc++.so.6.0.19
```


#### If using a specific conda virtual environment with Anaconda
Run this in bash:

```
$ cd /home/$USER/miniconda/envs/$ENV/lib  # Replace $ENV with the name of your conda environment.
$ mkdir backup  # Create a new folder to keep the original libstdc++
$ mv libstd* backup  # Put all libstdc++ files into the folder, including soft links
$ cp /usr/lib/x86_64-linux-gnu/libstdc++.so.6  ./ # Copy the c++ dynamic link library of the system here
$ ln -s libstdc++.so.6 libstdc++.so
$ ln -s libstdc++.so.6 libstdc++.so.6.0.19
```

