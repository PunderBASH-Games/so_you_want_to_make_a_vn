label access_what:
    p "Accessibility refers to the ways a game can be made available for various disabled people or those with other impairments to be able to enjoy games."
    p "It might be easy to dismiss these options as surplus to requirements, but if we can make games more accessible not only do we gain a wider audience for our own games but we also provide enjoyment and entertainment to people who might otherwise be missing out or struggle to find games they're able to play and enjoy."
    p "If you're particularly interested in how accessibility can impact the lives of disabled gamers, I recommend looking into the UK based charity {b}{a=https://www.specialeffect.org.uk/}Special Effect{/a}{/b}."
    p "Let's have a quick look at what accessibility might refer to in the context of Visual Novels."
    pn """
    Accessibility and Disabled Players

    The following are potential barriers people might have to enjoying games, and the ways you can help remove those barriers so they can enjoy your game.

    Deaf and Hard of Hearing. People who are deaf and hard of hearing might not have many access needs with a visual novel, but if your game uses a lot of sound effects you may want to include an option to show closed captions for any important sounds.

    Blind, Partially Sighted, and Visually Impaired. This is one of the bigger demographics that is missed by many games. Whilst you may feel that a \"visual\" novel might not be something that would interest this kind of player, that can simply be because very few have been made accessible. Things like image descriptions and features to help screen readers or the built-in self-voicing can be very helpful in opening up your game to a wider audience.

    Colour Blindness. This is more difficult, but you may wish to have people with different types of colour blindness look at a sample of your game screens and menus to make sure the colours you're using aren't making the text impossible to read. You can also check out different colour schemes developed for different types and find ways to apply these to your game so people can enable them if needed.

    Dyslexia and Reading Difficulties. Visual Novel games tend to mean a lot of reading, which might be offputting to players who have difficulties in this area, but there are still ways you can improve this and bring in more players. This could also be vital if you're making a project with an educational focus, so that no student is at a disadvantage or less able to learn from the material you're presenting.

    Physical and Motor Difficulties. This is unlikely to affect your game making, as Visual Novels have very simple gameplay and controls by default, but if you're making mini games or extra features then you may wish to include a way to make them easier or skippable for people who may struggle to hit certain timings so they can still enjoy the story you've created.

    Photosensitive Epilepsy, Migraines, and Seizures. This is a big one - if you use strobing or flashing lights in your game, or any kind of flickering image, you must at minimum give a warning for this. You could also look at ways to disable these effects too. The last thing you want to do is have your game trigger severe health conditions in your players!

    Jump Scares and Fear. If your game includes jump scares, sudden loud noises, or other content/features that might be a shock to a player, then it might not be accessible to them. This doesn't mean you shouldn't use these tools in storytelling, but you should be warning players in the game information so those who may be at risk of health issues with this kind of shock can either avoid the game or be prepared when they play.

    Mental Health and PTSD. Just as we look out for physical health, we should not ignore the potential of our games to have an impact on mental health too. A lot of this will come down to the content warnings discussed in that section, but there may also be other common triggers that some players may need to avoid for their mental health like certain sound effects or images. 
    """

    p "There might be some topics that I've missed here - please do let me know and I will add them in for potential updates to this project! I'll go in to more detail of how we can reduce and remove these barriers in the other parts of this section."
    p "Shall we take a look now?"
    jump access_menu

label access_selfvoice:
    p "Self-voicing is a feature built in to Ren'py as a default. It can be activated, or deactivated, at any time by pressing V on your keyboard. You can try it now if you like!"
    p "If you have it enabled, you'll notice how it is using the system voice to read out my name as well as the text in this text box."
    p "Some of you might already know about Screen Readers and similar software designed for blind and visually impaired people to read all on screen text, but this can be too much for a Visual Novel."
    p "A screen reader might end up reading out the quick menu with every line, or reading the full name of a character. It might also have difficulty pronouncing certain names and words in your script, particularly if you're using unusual words."
    p "However, the self-voicing can be adjusted for pronunciations or even skipping words and symbols that would not be read out correctly. I'll show you, turn on Self Voicing now with V if you don't already have it active."
    p "That's wonderful {alt}heart symbol{/alt}{noalt} <3{/noalt}"
    p "Let's take a look at that line in the code! The parts within the alt tag were read out by self voicing and shown on screen if you have self voicing enabled, and the symbols themselves were not read out."
    p "You can use this for symbols or unusual punctuation, as well as for pronunciations. Let's look at how the latter might work now."
    p "We have a character with the nickname \"Tyr\" in a game we're still making. You might notice the name there is read as if each letter is spoken like an acronym, but really it should sound more like \"Teer\"."
    p "If we use the alt/noalt we can show the word as intended and have the pronunciation match, like this: {alt}Teer{/alt}{noalt} Tyr{/noalt}. This can also be used in the character definitions if you don't want their full name read aloud every line and use a shorter name instead."
    p "There's also something else you can do with the self voicing that a screen reader won't pick up, and that is adding in image descriptions. How and where you use image descriptions is entirely up to you, but it can be a useful addition for players who use self-voicing."
    #include a picture of something
    alt "Desription of the picture."
    p "So there if you had the self-voicing enabled, you would've heard (and potentially seen) the image description before this line of dialogue. If you go back a few lines and turn self-voicing off, you will norice that the description is not shown."
    #screenshot the line
    p "This is achieved by using a special character, alt, as you can see here. Again this can open up your game to people who use this software as you can describe the appearance of characters, the scenery they're in, or any other important visual details that are important to your story."
    p "Using all of this is entirely up to you, and it will be more work to add in alt/no alt but it could be worth the extra time and effort to make your game accessible."
    p "The other thing to mention with this is that it will help you with in game menus and buttons, as the self-voicing will only read menu options when they are hovered, and you can also use the alt text with image buttons and other selectable elements on screen."
    p "I recommend testing the self voicing, and if you're using a lot of unusual names or words that you're not certain will be pronounced correctly it can be a good idea to test them all out in a separate empty game project. Then you'll know if you need to adjust pronunciation with alt/no alt."
    p "It is also worth keeping in mind that it is not only blind or visually impaired players who will make use of this feature, it can also be popular with dyslexic players and others with reading difficulties."
    p "If you have full voice acting it might be less important for you to use it, too, but it's still worth considering for the other elements like image descriptions."
    p "With your game trailer, too, it may be helpful to include a transcript of the images and words shown during the trailer video as this may not be captured by a screen reader." 
    p "You can write this up on your game page to let players know they will be able to enjoy your game using the accessibility you've put your time and effort into."
    p "That roughly covers it for self-voicing here, let's hop skip and jump to the next topic!"
    jump access_menu

label access_other:
    p "There are a couple of other options included with Ren'py that may help make your game more accessible."
    p "We've gone through self-voicing in the other section, but did you know there's an accessibility menu that players can use at any time?"
    p "By pressing \"shift + A\" you will see a menu of several options that will help players out. It may be worth letting them know this is an option in the tutorial or even on your game page."
    p "Alongside easier to read fonts that may be helpful for different forms of dyslexia and/or reading difficulties, there's also the slider to adjust the volume of the self-voicing which can be very helpful for players who use this."
    p "Aside from this, there are other things that you can implement to help players enjoy your game."
    p "With flashing lights and images, it is a good idea to give players the option to disable or skip this element. You can also add in a separate warning notification before they appear, so people are aware when there might be a point to look away or be prepared for it."
    p "The same can be done for disturbing images or content, to allow the player to hide the image or even skip a section of the scene that is not heavily plot relevant."
    p "As an example, this could be for explicit romance scenes in a game where the explicit nature is not the focus - you can give the player an option to skip those scenes and replace them with a \"fade to black\" with a brief line or 2 if there's any plot relevant information in the scene."
    p "Some games may also have things like a choice to enable or disable swearing in the game, or to censor any violence or blood in the game images, or even silencing certain sound effects."
    p "Optional censoring is again down to personal choice, but there are a significant portion of players who would really appreciate some of these options being present so they can enjoy the game without worrying about triggering content."
    p "It's all about considering your audience and working out what their needs might be. This can be some thing testers can give you feedback on, and sensitivity readers for difficult topics can be a valuable resource."
    p "It might be tough to make the One Perfectly Accessible Game, but every time we take steps to level the playing field we are opening up the hobby to more people to enjoy."
    p "We can also serve as good examples to encourage more and more games to consider accessibility in the future, too."
    p "There are likely other things I haven't mentioned, or more things you can think of, that could help your game be accessible to a whole variety of players. Give things a try, and if possible aim to find some testers from those groups before release to check your game for any issues or improvements."
    p "So, onwards and upwards? Or downwards? I'm not sure, I'm made of boxes and poorly scribbled lines..."
    jump access_menu
