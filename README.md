
<h1 align="center">XIV Dialogue Inspector - Python Version </h1> 
<p align="center"> 
  <img src="pythonimg.png" alt="alt text" width="900">
</p>

This is the Python version of the XIV Dialogue Inspector, a program that allows you to easily access the dialogue files of Final Fantasy 14. This version was created to make the program more accessible to users who are more comfortable with Python.

**Note:** If you encounter any errors with the Python version, it may be because it is not currently synced up with the Java version in terms of code content. If you experience any issues with syntax errors in dialogue files, trouble getting a name to show up in your files, or anything else, please open an issue and try out the Java version first. You can also contact me on Discord if you are having any troubles.

## Purpose

This program is designed for people who want to easily access the dialogue of Final Fantasy 14. It is especially useful for roleplayers, lore seekers, and anyone who wants to find information or quotes from the game.

## Features

- Reads the Dialogue CSV files of Final Fantasy 14
- Displays dialogue in chronological order
- Sorts through all dialogue in the game except for the `NpcYell.csv` file
- Allows users to search for all dialogue of a specific character or all instances of a word

## Installation & How to Use

1. Download the [latest release](https://github.com/8bllgrl/py-XIVAPI-DialogueScraper/releases) OR alternatively, clone the repository to your local machine using the command `git clone git@github.com:8bllgrl/py-XIVAPI-DialogueScraper.git`.
3. Run `runPython.bat` through the terminal, or by double clicking it in your file explorer.
4. Follow the prompts to search for dialogue, and read forward to further understand the different versions.

## Version 1 

example output:

```
Character is speaking:
TEXT_VOICEMAN_03003_000070_ESTINIEN -- If there is to be a meeting, I would accompany you.

TEXT_VOICEMAN_03003_000090_ESTINIEN -- Even with your intermediary, Nidhogg's bloodrage may render him deaf to reason. However, the mere attempt may afford our forces precious time to prepare. 

TEXT_VOICEMAN_03003_000100_ESTINIEN -- Of course...you might also consider a more direct approach to ending this conflict. With the power of the Eye at my disposal, and the vaunted strength of the Warrior of Light, we could conceivably slay the beast outright...

TEXT_VOICEMAN_03003_000120_ESTINIEN -- Perfectly. I shall assume that Iceheart enjoys similar diplomatic protection until instructed otherwise.

TEXT_VOICEMAN_03003_000130_ESTINIEN -- A word of advice: think carefully before divulging the particulars of this plan to Ser Aymeric. 'Twould not do to have the lord commander accused of consorting with heretics.

TEXT_VOICEMAN_03003_000150_ESTINIEN -- I am glad to be of service.

TEXT_VOICEMAN_03003_100070_ESTINIEN -- Know that I have offered my lance to aid in this endeavor. I cannot claim that its success is assured, but our actions should serve to delay Nidhogg's advance at the very least.

TEXT_VOICEMAN_03003_100080_ESTINIEN -- Which is more than can be said for the ill-conceived counterattack advocated by the See's more vocal crusaders. They offer glorious death, but little hope of victory.

TEXT_VOICEMAN_03003_500030_ESTINIEN -- You are wrong, Lady Iceheart.

TEXT_VOICEMAN_03003_500040_ESTINIEN -- Lest you misunderstand, I do not doubt your vision of the past─'tis true that Nidhogg greatly desired to reclaim the Eye.

TEXT_VOICEMAN_03003_500050_ESTINIEN -- Indeed, it was for that very reason that I kept it with me as I roamed the land, attempting to draw him away from the city.
```

Which also includes, later in the file, instances of the character being mentioned.

```
TEXT_AKTKMH110_04535_YSHTOLA_000_180 -- You surprise me, Estinien. For a lone wolf, you've shown an unusual degree of, shall we say, “involvement” in helping Vrtra reach this conclusion.

TEXT_AKTKMI104_04595_SEQ_00 -- Estinien looks at you with his piercing gaze.

TEXT_AKTKMI105_04596_TODO_08 -- Speak with Estinien.
```

## Version 2

example output:

```

 C>> If there is to be a meeting, I would accompany you.

 C>> Even with your intermediary, Nidhogg's bloodrage may render him deaf to reason. However, the mere attempt may afford our forces precious time to prepare. 

 C>> Of course...you might also consider a more direct approach to ending this conflict. With the power of the Eye at my disposal, and the vaunted strength of the Warrior of Light, we could conceivably slay the beast outright...

 C>> Perfectly. I shall assume that Iceheart enjoys similar diplomatic protection until instructed otherwise.

 C>> A word of advice: think carefully before divulging the particulars of this plan to Ser Aymeric. 'Twould not do to have the lord commander accused of consorting with heretics.

 C>> I am glad to be of service.

 C>> Know that I have offered my lance to aid in this endeavor. I cannot claim that its success is assured, but our actions should serve to delay Nidhogg's advance at the very least.

 C>> Which is more than can be said for the ill-conceived counterattack advocated by the See's more vocal crusaders. They offer glorious death, but little hope of victory.

 C>> You are wrong, Lady Iceheart.

 C>> Lest you misunderstand, I do not doubt your vision of the past--'tis true that Nidhogg greatly desired to reclaim the Eye.

 C>> Indeed, it was for that very reason that I kept it with me as I roamed the land, attempting to draw him away from the city.

```

Be careful, because this only shows the character talking, and does not work for looking up words and phrases, such as "Gridania" or "Tia". 
