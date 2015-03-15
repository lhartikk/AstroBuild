#AstroBuild
Deploy  based on the planet alignments. 



##Example
Example usage when integrated to [capistrano](https://github.com/capistrano/capistrano)

    > cap production deploy
    
    INFO [dfe36319] Running /usr/bin/env python astro_build.py as lhartikk@188.166.5.240
    DEBUG [dfe36319] Command: python astro_build.py
    DEBUG [dfe36319]BUILD FAILED
    DEBUG [dfe36319]PLANETS ALIGNED: ['Mercury', 'Jupiter']
    DEBUG [dfe36319]ALIGNMENT: 149 degrees
    (Backtrace restricted to imported tasks)
    cap aborted!
    

##Technical specs

Calculates the geocentric apparent
longitude in degrees of each planet (+ sun) and rounds to the nearest integer. If any of the planets align, an error message is written to stderr.

Inspired by:
[How to compute planetary positions](http://www.stjarnhimlen.se/comp/ppcomp.html)


Visual: [Current Geocentric and Heliocentric
Planetary Positions](http://www.planetary-aspects.com/curr_asp/curr_posns.php)

##How to use?
Since AstroBuild is just a simple python script you can integrate it to your favourite deploy/CI workflow e.g. as a prebuild task!
