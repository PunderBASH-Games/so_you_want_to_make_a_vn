label assets_return:
menu:
    "Where would you like to go next?"
    "Return to Assets Menu.":
        jump assets_menu
    "Return to Sections Menu":
        jump menu1
    "Exit to Main Menu":
        return


label assets_list:
    p "Assets are all the pieces that come together to make a VN. From the images to the sound to the writing, if it's going in your game then it's an \"asset\"."
    if persistent_overviewneeds:
        p "Looks like you already checked over the overview of what these things are, so we will stick to a quick list!"
    else:
        p "Hmm looks like you haven't looked at the overview yet, which talks about what each of these things are and which ones are optional. Would you like to go there now?"
        menu:
            "View overview?"
            "Yes":
                $ returntoassets = True
                jump vn_needs
            "No thanks":
                p "Alright then, we will carry on as if you already know the overview."
    pn """
    So we have our \"Essential\" assets:
    
    Writing, Sprites, Backgrounds, GUI and Code.

    And we have our \"Optional\" assets:

    CGs, Music, Sound Effects, Additional Menus, Galleries/Collectibles, Mini Games, and Other Features.

    But where do we get them all from? 
    """
    nvl clear 
    nvl hide
    p "The first option is to make everything yourself! That might be a lot more work than you think, though, so let's have a look at your other options."
    p "You could find a team to work with, often this could be friends, classmates, or teams formed for a game jam."
    p "Another option is to find existing assets you can use, although you will need to be careful with copyrights and licencing even for fan-games based on other existing works."
    p "The last option is to commission the work, where you will pay someone to do the listed work."
    p "Some of this is covered in the section about the cost of making a VN, and some will be covered in the section about teams."
    p "The main thing to remember with your assets is to make sure you have a clear idea of what you want and need, and keep a list somewhere when planning them out."
    p "You'll also want to keep them organised and have backups. A good rule of thumb is to have 2 backup saves of any work you have. The likelihood of your main files and one backup failing simultaneously is far from 0%, but 2 backups failing is much closer to 0%."
    p "You might change your mind on what you want to go in to your game, and that's fine. Sometimes we can cut down production time/costs by reducing assets, or we can use extra time to add a few more assets to spice things up."
    call assets_return
    
label assets_get:
    p "Which method would you like to view?"
    menu: "Which method would you like to view?"
        "Making my own assets.":
            jump make_assets
        "Finding free to use assets.":
            jump free_assets
        "Commissioning individual assets.":
            jump commission_assets
        "Return to assets menu.":
            jump assets_menu

label make_assets:
    p "So you want to make your own assets? That's great!"
    p "It's going to be a lot of work, but I believe in you! Try to have a clear idea of each thing you want to accomplish before you start and it'll help you get to the finish line."
    p "You can make your own concepts to develop designs, use references to find things similar to inspire your new original piece, or you can leap right in to creating from scratch."
    p "Whichever way you go, don't be afraid to make changes or even drop finished pieces if they no longer fit the theme of your game."
    p "Unused pieces can even be a part of the \"Extras\" in your game if you have that, or work as behind the scenes promotional materials!"
    p "It is worth noting that you might want to be careful where you share the assets you make. While you cannot guarantee they won't be used without permission, be clear when sharing progress that your work is not available for use."
    p "Protecting your intellectual property can be very hard, but using watermarks or other methods can help keep your work safer whilst you're developing it."
    p "Good luck with the process, we will cover a little more of the specifics in other topics!"
    label asset_menu_return:
    menu:
        "Where to next, boss?"
        "Go back to the previous menu.":
            jump assets_get

        "Go back to assets section menu.":
            jump assets_menu

        "Return to the main section menu.":
            jump menu1 

label free_assets:
    p "Finding ready to go free assets sounds like a cheap and easy way to go, but it isn't always so simple to find what you need!"
    p "The first thing to be aware of is legal licences. CC0 or Creative Commons is the easiest licence to use, assets with this licence can be used free of charge in any work even if it is commercial (sold for money, aka not a free game)."
    p "There are other licences like ones that require attribution meaning you would need to clearly credit the creator of that asset somewhere in your game and in the game details."
    p "There may be limits to attribution licences, like they are only available to use in games that will not earn any money (distributed for free only)."
    p "The lemmasoft forums have a section for assets that are available to use here (clicking this will open your default browser to the page): {b}{a=https://lemmasoft.renai.us/forums/viewforum.php?f=52&sid=67dfade9ee0d70405eebd167e459d3fa}Lemmasoft Creative Commons{/a}{/b}"
    p "For music and sound there are a lot of options like freesound.org, ZapSplat, or there are large libraries of free to use music out there. Again, always check your licences and permissions!"
    p "So, what's next?"
    call asset_menu_return

label commission_assets:
    p "So if you don't have a team, don't want to make your own assets, and can't find what you need in existing assets available to use, what's left?"
    p "Find someone who you can pay to make it for you!"
    p "But when you're commissioning assets, there's a few things you should keep in mind - this will also apply to finding a team or working with a team."
    pn """
    Commissioning Essentials:

    - What are you offering? Few creators will work for free or for a profit share on release, so you need to work out what your budget is and what you're willing to pay. Many creators will have price lists available to look at too before you approach them.

    - What is your project about? Anyone you're hiring should know at least a little about your project. Is it NSFW? Are there topics that might be triggering for some people to work on? What is the genre and vague description of the game/story?

    - What are your deadlines? People will need to fit the work around their schedules, so if you have a specific deadline you need work done by you will need to be up front about that.

    - What exactly do you need? The number of images and expressions for sprites, number and length of music tracks, specific code jobs - whatever it is, people will need to know how much work they'd be doing, and what the nature of that work is.

    - Copyright and Licencing. Who will hold the final copyright of the work? Will it be limited to you and your project, or will the creator be free to share/sell the pieces themselves? Make sure you have a clear agreement before they complete any work for you.

    - Samples and Auditioning. Take a look at existing work by the potential person you're commissioning. Can they produce something in the style and standard that fits your project? Do they have proof of things they've done before? Do you need to consider paying them a small fee for a sample piece before committing to the main work?
    """
    nvl clear 
    nvl hide
    p "So you have found someone to commission and made an agreement with them, what next?"
    p "Well, you will need to communicate with them throughout the process, and keep them updated on any important changes."
    p "You should also give them as much detail as possible - let's look at some examples of what that might mean for different things!"
    pn """
    Commission Details - Things that will help the person doing the work you're paying for to match up to what you want from them. For all art, tell your artist what size, resolution, and image format you would like the final piece to be in (.png is the most common file type for images)

    - Background Art: Reference images, written description of the location, suggested colour pallette, level of detail, examples of similar styles, camera angle, image size and resolution, details of any areas to keep more clear (eg, an image shouldn't have too much detail under where the text box goes as this could make it hard to read). The more detail, the better.

    - Sprites: Description of each character and their outfits, colour pallette, description/list of expressions or expression parts, reference images for outfits/features, character height and build, description and/or reference for their main pose(s), and some detail on their personality can help. If you can give the artist a concept you have made, it will help even more.

    - CGs: If for any reason your CG artist is different to the background and/or sprite artist, give them the sprite and background image for the scene to use as their reference. Again as much detail as possible on camera angle, poses, clothing, expressions, etc will all help. You can use a website like MagicPoser to create an example of the pose and angle you want for the characters.

    - Music: As well as the number of tracks and mood for each track, consider also what kinds of instruments you would like used in the pieces. It can also help to give the composer a short playlist of tracks with a similar style/feeling to what you would like to hear for your game.

    - GUI: List all the images and image sizes you need to fit any GUI images you want to replace. I actually have a handy guide you can use {b}{a=https://docs.google.com/spreadsheets/d/1W-RvTQ-8Dhuo8KnwFB7e3a2RzNhhrBMjSRbiti4xiAo/edit?usp=sharing}here{/a}{/b} with the default GUI images, where to find them, and a rough size guide. Again, colours and an idea of the style will help them know what you want. 

    - Code: This is a trickier one as \"code\" covers a lot of jobs. So generally, be up front about all the features and functions you would like them to work on, with examples or references where possible. It may help to use something like Github to work with someone else on the code of your game, and even better if you're able to input the basics of dialogue, choices, jumps, and labels yourself. There's tutorials to help in the resources section!

    - Voice Acting: Voice actors may have different requirements, but firstly they will need to know about the character they would be voicing. An overview of the personality and storyline of the character as well as the number of lines that need to be spoken is essential, and if you need other vocalisations like loud shouts, screams, or similar vocal sound effects they will need to know in advance too. 
    """
    nvl clear 
    nvl hide
    p "That just about covers how to commission assets. What next?"
    call asset_menu_return

label assets_music:
    p "Music can give your game atmosphere, mood, and depth! It isn't essential, but it can add to the overall experience."
    p "So what do you need to consider for using music assets in your game?"
    p "First, which I have said a few times through this little tutorial, is Licencing and Copyright."
    p "I may sound like a {i}broken record{/i}, but you must have permission to use the music you use in your game. That song you love might sound great and fit with your game, but if you use it without permission you'll likely end up in trouble!"
    p "You could contact the artist or licence holder for permission to use the music in your project, but be prepared for them to decline or to ask for payment."
    p "Otherwise, using music in your game isn't too difficult! I won't go into how to add it into the code of your game, but there are some things to consider with your tracks."
    pn """
    Music Essentials:

    - Volume. Check the volumes of your tracks in and out of the game, to make sure they're well balanced. You don't want to hurt your players' ears with a sudden loud track after a very quiet one!

    - File type. With Ren'py, I personally recommend using .ogg as your music file type. Whilst others may be compatible, this is the one I have found to be most reliable whilst also balancing file size and sound quality. 

    - Looping Backgrounds. I've mentioned this elsewhere, but it is best to have background music the loops smoothly. That means it will repeat easily without any obvious gap or change when the track ends and restarts. Ren'py will automatically loop the music for you, but the track will need to sound good when looped. If not it might break immersion for the player/reader!

    - Non-intrusive. A cool and epic track with killer vocals might be amazing as a theme tune or even main menu music, but when someone is trying to play a VN and read the story, it's better to have music that will blend into the background smoothly. It should add a mood, but not take away the focus entirely from the writing and images. It's a tough balance, but try listening to existing VN soundtracks to see how it has been done before.

    - Soundtrack Release. If you want to release your soundtrack outside of the game as an extra, you'll want to plan in advance where it will be and how you will protect the copyright if you're the copyright holder. If you're using CC0 music you won't be able to release the music outside of the game as your own, but if you have commissioned it you can work with the artist who made it on where and how to release it on other platforms.
    """
    nvl clear
    nvl hide
    p "That should cover the basics of what you need to know for the music, if you're adding it to your game."
    p "Music is optional, however, and plenty of games are released without music."
    p "You could even have a \"suggested playlist\" link to an external platform like Youtube or Spotify if you like, then people can listen to the music you feel fits your game without needing to licence it as it isn't a part of your game file and the artist is getting the views/clicks/listens." 
    p "This would use their own system to play the music externally, however, so it isn't always the ideal choice."
    p "What's next?"
    call asset_menu_return

label assets_sound:
    p "Time for sound effects, to spice things up!"
    p "Similar to music, you'll need the licences and permissions for any sounds that you include."
    p "You could record them yourself, but you'll need the right equipment to get the best quality."
    p "Similar to music, I personally prefer .ogg as the file type for sound effects, although there are others that are compatible."
    p "When you're choosing sound effects, it is worth thinking about if they're adding to the moment or if they might be distracting."
    p "You won't need to hear footsteps every time someone is walking, but if there's a key moment you want to highlight with sound then that's the place to put it in."
    p "If you're working on a horror project, or looking for violent sounds, it is worth noting that you won't necessarily find the sounds you're searching for by using the exact violent terms."
    p "Instead, you'll want to think of things that could sound similar to what you want and search for that instead, like someone snapping a carrot, or squashing a melon with a mallet."
    p "Foley artists can't really label their sound effects with violent or nsfw names, as it might call into question how the sound was recorded." 
    p "You'll find a lot of film/tv/game sound effects are recorded by doing very strange things to mix a particular sound to something that people feel is realistic for the action."
    p "For example, that classic \"punch\" sound isn't actually what it sounds like if someone punches someone else. It's mixed and emphasised to give a feeling of impact on the screen that people have come to expect."
    p "Too many sound effects in a VN can be distracting or feel strange to the player, but adding a few in the right places can add to your story and the sense of immersion."
    p "That roughly covers the things to keep in mind for sounds, onwards and upwards! Or downwards...I don't know directions, I'm just a dude made of cubes."
    call asset_menu_return

label assets_gui:
    p "Your GUI is the interface your players will be seeing all the time as they interact with your game. It can add to the atmosphere and make your project feel unique."
    p "Ren'py has a basic GUI built in - when you start a new project you choose the colour scheme that your game will first appear with."
    p "You can choose to simply replace all of the GUI images with your own and keep the layout the same, or you could go into more detail on changing things around."
    p "I'll show you what I mean - this is an example of the main menu in a basic Ren'py project."
    p "Now let's have a look at something a little different - this is a completely different main menu screen that PunderBash Games made for their game \"Summer Horrordays\"."
    p "This involved changing a lot of the code and layout of the menu, as well as the images it used. In this one, each postcard starts a new story, and will change the image once the story has completed one or more times!"
    p "If you want to see what it looks like in game and how it works with the animated parts of the background, \"Summer Horrordays\" is available free {b}{a=https://punderbashgames.itch.io/summer-horrordays}here{/a}{/b}. (Shameless self promotion is allowed, we made this tutorial for you for free, too! Please be aware of age ratings and content warnings.)"
    p "But what about the preferences menu, what can we do there?"
    p "Here's the Ren'py default preference menu included with the basic build."
    p "And here is the menu we used for Summer Horrordays. Again it has an animated background in the game to fit the theme, and you'll notice we changed and removed some options."
    p "This is also what one of our dialogue text boxes looked like."
    p "And here's an example of the frame we used."
    p "My mini guide to the basic images you can replace is {b}{a=https://docs.google.com/spreadsheets/d/1W-RvTQ-8Dhuo8KnwFB7e3a2RzNhhrBMjSRbiti4xiAo/edit?usp=sharing}here{/a}{/b} and free for you to use as a reference guide."
    p "The sizes in that list are based on the defaults for a 1280 x 720 resolution game, as that was the default at the time we made it, so keep in mind you will want to scale up (or down) if you are using a different resolution."
    p "If you want to change the menus as well as just the images, you'll need to either learn what you're doing, or have someone working with you who knows how to accomplish what you want."
    p "Making mockups of the menus can be really helpful for this, to demonstrate what you want to accomplish and test out your images to make sure you've got them sized and positioned correctly."
    p "This is the concept for the menu layout we showed you above for Summer Horrordays. It was made by one of the team and passed on to another to work out the code for it to function, then the artwork was made to fit the final piece."
    p "Keeping things simple and sticking with the default layout can save you time and effort, but if you want to do something a bit more customised then you absolutely can!"
    p "If you want to learn more about how to make your own GUI, it's worth looking through some tutorials as well as the official Ren'py documentation."
    p "So, let's head on from here, shall we?"
    call asset_menu_return

label assets_writing:
    p "Writing is the core of your game, and I'm sorry to tell you I don't have any magic shortcuts to get your story out of your head and on to the page - if I did I'd be using them!"
    p "Well, not me, but the one at the keyboard writing my words for me right now. She wants you to know writing this tutorial is infinitely easier than writing the story, which is why she's doing it to procrastina- she means, to help you all out with your first projects!"
    p "There's lots of ways to approach writing, but one of the main things will be where and how you write the main dialogue scripts."
    p "Personally \"I\" prefer to write directly into the script file, using the defined characters and including the menus, conditions, jumps, and labels as I go."
    p "Other people might prefer to write in another program like Notepad++, Word, or Google Docs, then transfer the writing into the script files later. This is fine, although you might find you need to change the indents or the type of \" symbol that your other program used."
    p "Here's some things to think about before you start tapping away on your keyboard!"
    pn """
    Writing Tips

    - Planning. It helps to have at least a basic outline plan for your story before you start, then you know what you need to do to get to the ending(s).

    - Choices and Branches. If your story has choices and a story that branches to different endings, it is a good idea to plan these out. You can still change them later if you like, but if you know where things are going to split and what plot points or conditions people need to reach the different endings it will make it much easier to continue.

    - Twine and Flowcharts. A lot of people like to use Twine or a flowchart program to envision their choices and routes before they start. Twine is actually an online VN engine, it works a little differently to Ren'py but you can test out the choices and see how the branches and flow will look. Similarly a flowchart can help you to see a visual layout of your overall plan.

    - Story Structure. There's lots of ways to structure your story, but generally you'll want a beginning middle and end, with some kind of plot twists and character development along the way. I'm personally fond of the 27 Chapter Method as outlined in {b}{a=https://livingwriter.com/blog/27-chapter-method-made-easy}this article{/a}{/b}, and for a branching story you can write different versions of the plot points for different branches.

    - Character Profiles. It is handy to know what your characters' personalities and motivations are before you write them, and there's lots of ways to do this. I have a free to use character profile template {b}{a=https://docs.google.com/document/d/11zaR-uqgLHOVDyDUHjglUuX9zJ0LfVYoRvDCptkZolA/edit?usp=sharing} here{/a}{/b} that you're welcome to use for your own planning, and adjust to fit your needs.

    - Just. Write. No, I mean it. You can't edit a blank page - your words don't need to be the very best words for every single sentence of your first draft. Get your story down first, and edit it after to improve it. Lots of authors will tell you their first draft can be very different from the final sometimes, so don't panic if it's not perfect right away. 

    - Character and Place Names. Honestly, this is something I personally find tough, but I have a lovely little link for you all. {b}{a=https://www.fantasynamegenerators.com/}Fantasy Name Generators{/a}{/b} website doesn't just have fantasy, it has tons of genres, including names based in real world locations. It also has generators for location, town, country, and even business names. If you're stuck on what to call something, try this for inspiration.

    - Hiring and Collaborating. If you're not writing yourself and instead have a writer on your team, or you're working with a team of writers, make sure you keep clear communication and feedback. Check everything for potential spelling errors (typos happen, even to the most literate amongst us) and work together on editing notes and continuity where needed.

    - Continuity Tips. If your story has branches and choices, keep a list of them! That way it is easier to reference them later. So for example you give players a choice of their favourite colour early in the game, you can reference this later in dialogue like maybe they are given a gift of a hat in that colour. The more variation you have in choices, the closer watch you'll need to keep on continuity later.

    - Scope and Writing. Word counts are handy to look at, and it might be tempting to reach lofty numbers, but remember everything you write will need the rest to go with it. If you want to keep things more simple, stick to fewer branches and endings. If you're willing to have more routes and branches, keep in mind this is also more work on every part of the game and will take longer to complete it.

    - Chapters and Pacing. If you're making a longer story, it will help with your pacing and for player experience to have chapters. You can use title screens for the chapters, or some other method to show the player they've hit a point to advance. This helps them know when it is a good place to stop, just like when reading a book you may want to get to the end of a chapter before putting it down. 

    - Translations and Multiple Languages. It is possible to translate your game and have different language options if you want to. Unless you are multi-lingual, however, this might cost you more to have properly translated. If you're interested in having multiple languages, take a look at the documents on translations before you start writing and ask around for tips if you need to.
    """
    nvl clear
    nvl hide
    p "Phew, that's a lot of words! But writing is the core of your game, so you will likely be reading your own words many, many times in the process of making your game and testing it before release."
    p "There's no real right or wrong way to approach it, so good luck and have fun with it! Remember to write the story you'd want to read, make the game you'd want to play. That's why we're here, isn't it?"
    p "Shall we head on?"
    call asset_menu_return

label assets_code:
    p "Games run on code. There's no getting around that! You'll need to know at least the basics, or work with someone else who knows enough to do what you want to do."
    p "Don't worry though! Ren'py is built with beginners in mind and made to be as easy as possible to make a working Visual Novel with minimal experience and knowledge."
    p "My benevolent overlord who is writing this started off knowing absolutely nothing about code, and now she knows \"enough to be dangerous\" as she puts it."
    p "Luckily she has a team-mate who can do the more complicated parts, and fix her mistakes, but she wants you to know that lots of people with no experience at all have made full and complete Ren'py Visual Novels by learning from square one!"
    p "She may even recommend a fun little game made by someone who started off from nothing, \"After School Murder Club!!\", which is free on {b}{a=https://store.steampowered.com/app/1639890/After_School_Murder_Club/}Steam{/a}{/b} or {b}{a=https://rabbitdeeryou.itch.io/asmc}itch.io {/a}{/b}. Please be aware of age ratings and content warnings before downloading or playing." 
    p "She wasn't paid to say this, she just enjoyed seeing it being made and playing it when it was done, and it is a good proof of what someone can make in Ren'py with a fair amount of hard work and dedication and no starting experience."
    p "I'm not going to go into detail on how to code here - there are lots of people with much more expertise who have made some fantastic tutorials aimed at beginners as well as more experienced programmers. They'll be in the resources menu too."
    p "If you want to skip ahead to the links though, I highly recommend {b}{a=https://www.lezcave.com/renpy-tutorials/}Lezcave{/a}{/b} for beginner tutorials as well as {b}{a=https://feniksdev.com/navigation/}Feniks Dev{/a}{/b} for a more Python-oriented approach to learning. Both are made by real experts in the field and come highly recommended, by me, because I think they're both lovely creators as well as very handy resources."
    p "It might be tempting to skip looking at tutorials and dive right in, but it's better to take a look at the basics first and be fully familiar with them before you begin."
    p "Even with the documentation, it is easy to make beginnner mistakes, or to do 10 times more work than you need to achieve what you want to in your game."
    p "Remember if you're starting new that you're a Level 1 programmer, so make sure you can walk before you try sprinting! Even if you know Python well, it is a good idea to familiarise yourself with Ren'py as it has some different functions and features."
    p "As for extra features, they can be great to add to your game, but will mean more work and time added to your project."
    p "It's always worth thinking carefully about what will add value to your game, and what features might actually detract from the experience."
    p "Mini games are an example of this - some people love them, but others feel that in some projects they get in the way of the story."
    p "There's also the thought of pushing the game engine to its limits."
    p "The original \"Doki Doki Literature Club\" (if you want to play this please check age rating and content warnings) was made in Ren'py before it was remade in the DDLC+ version for multi-platform release. It went outside of the box with what Ren'py can do, and did some really clever things, but this isn't necessarily right for your first game."
    p "It can be tempting to see how far you can push the engine, to make an RPG with it, or a point and click adventure, or a complex simulation game, but Ren'py was largely built for Visual Novels to make it easier for people to develop VN games."
    p "Unless you're really certain in what you're doing and exactly how to achieve it, I really recommend keeping your first project closer to a traditional VN format. There are other engines out there designed for RPGs or Point and Click games which are more suited to them."
    p "I also have a hot tip from the code expert!"
    pn """    
    Feniks says: \"Rarely do people think about save compatibility, but if you're releasing a demo you want people to carry progress from, or releasing in episodes, or even have to release a bug fix, you really need to consider compatibility before the first release. For most projects this can be as simple as just keeping around the original rpyc files and making sure you use default for variables\".
    
    To know more about this, check out their tutorials or have a look for discussions on this topic on the Lemmasoft Forums or in the Ren'py Discord server.

    Generally this is something to consider when you're close to release, and particularly to note down if you want to release your game in smaller parts or episodes, or want to add DLC later down the line. 

    My non-expert top tip is simple: \"Get used to error screens and learn what they mean, because you'll likely see them a lot.\" This might sound bad, but honestly it is so easy to mis-type something, or leave out an essential colon or comma.

    Don't panic if you find an error or bug, it can likely be fixed, and as time goes on you'll likely make less and less mistakes and know how to fix them when they do pop up.
    """
    nvl clear
    nvl hide
    p "So as a recap, code isn't something you can avoid in making a game, but Ren'py can make it a lot simpler for making your first Visual Novels."
    p "There's a lot of support for Ren'py, as well as a welcoming community of developers and experts who can help you when you get stuck."
    p "Which leaves us looking for our next destination, where will it be?"
    call asset_menu_return

label assets_voice:
    p "Voice acting is one of the things that our team hasn't used, and isn't planning to use as yet. But it can be a popular choice for others, so we're including it here!"
    p "Finding voice actors will mean not only finding someone in your budget and who likes your story and character enough to agree to it, but also auditioning those actors and directing their performances."
    p "There are lots of places to look for voice actors, so you may find they have varying pay rates and quality of performance too."
    p "Voice lines will need to be recorded, so if you're doing any of this yourself then you'll want to make sure you have the right equipment and environment to capture good quality sound."
    p "You will also need each individual line to be in its own sound file, so plan accordingly!"
    p "Make sure you have file names for every line that make sense to you. It may be best to make a spreadsheet with the line numbers in the code and a reference number for the voice."
    p "So if you were to have someone voice my lines, you could leave a blank line in the code above each of my written lines and have the file name for the voice file as \"mp rpyfile linenumber\", so it could be \"mp guidetoassets 289\" for this line."
    p "It is important that your performers agree to the expectations and that you're happy with their audition and samples before you start the main work."
    p "There are different ways to incorporate voice acting into your game, too, which depends on your personal preferences."
    p "Some people like to have every line voiced, whereas others might only have some important scenes with voice acting like CG scenes and character introductions."
    p "Others might only choose to use vocalisations for emotional emphasis, like a gasp, laugh, or crying, rather than having many or even any full lines read out."
    p "How you approach it is up to you, but as with all things it will give you more work to do."
    p "You may want to consider looking at market research before you decide on having voice acting. For example, surveys have shown that Otome genre players actually prefer not to have voice acting and only enjoy voice acting in Japanese, particularly from their favourite voice actors."
    p "It's something to think about, certainly. But where would you like to go now?"
    call asset_menu_return

label assets_art:
    p "Art is the big one here! It's the main Visual part of a Visual Novel, after all!"
    p "Whether you're making your own art or working with someone else, there's a lot to consider."
    p "Which topic would you like to know more about?"
label art_menu:
menu:
    "Which topic would you like to view?"
    "Background Art":
        jump bg_art
    "Sprites and Characters":
        jump sprite_art
    "CGs and Special Images":
        jump cg_art
    "Return to Asset Menu":
        call asset_menu_return

label art_menu_return:
    menu:
        "Where would you like to go next?"
        "Return to previous topic menu for art assets.":
            jump art_menu
        "Leave the art assets section.":
            jump asset_menu_return

label bg_art:
    p "Backgrounds make up your scenery, the locations in which your story is set. They will give context and a theme, so they're pretty important pieces!"
    p "Most backgrounds will be static images, like this one."
    p "But you can also use ATL code in Ren'py to have a layered image with moving parts."
    p "Here we have a road with cloudy weather, a part of a project being made by PunderBash Games."
    p "And here we have the same image with some layers of rain coming in to the image, the layers of rain are shifting in and out to give it more depth and a feel of moving rain."
    p "!!Warning!! The following demonstration contains flashing light images to show lightning effects. Use the following choice to skip this if you are sensitive to flashing lights."
    menu:
        "The following image contains flashing lights. Do you wish to continue or skip?"
        "Continue and show the image, please.":
            #show the image
            p "And now we have added a new layers to the image to include lightning effects."
            p "You may notice the lightning is at random intervals, which is something Ren'py is able to do with composite images and some extra work in the code. It could be used for a variety of random visual effects to highlight special moments in your games!"
            p "The lightning effect will now stop as we move on to the next part for those who skipped the flashing light effect."

        "Skip the flashing image and move on to the next lines.":
            p "Alright, no problem! Moving right along."    

    p "So as you see you can have some interesting effects, although it will take a fair amount more work to create and code moving images and images with changing parts."
    p "There are lots of things you can do with backgrounds like this, but keep in mind whether it is something that the project would benefit from or if it isn't worth the extra workload."
    p "There are some other things to think about with backgrounds, too!"
    pn """
    Background Tips:

    - Keep in mind where your dialogue box will be. It usually takes up the bottom section of the screen, so it can be a good idea to ensure that this part of the image is not too packed with details. Details here will either be hidden by the dialogue window, or they could even make the writing harder to read.

    - Your backgrounds will likely want to be in a similar style to the character images to keep things in theme.

    - Backgrounds may also want to be less striking than your character images too. Strong colours and thickly inked lines may distract from your character sprites on centre stage.

    - Take a look at backgrounds in existing games, think about what makes them good and what about them doesn't work so well.

    - Reference images can help a lot with working out your perspectives and layout, but be very careful with copyrighted material! You could use a game like Sims to work out a layout for a room, and even trace the position of items, but you shouldn't fully trace every detail of items and textures without changing them. 
    
    - Some art programs like Clip Studio Paint have pre-made backgrounds that you can use, or even 3D assets that you can move and place to create your scene and trace as a basis, but check the licence on each asset you use.

    - The same can be true of photos. CC0 photos could be used as backgrounds, and some people even use clever photoshop techniques to turn their own photographs into something that looks more like a drawn background. Be careful that there's no restrictions on photographs of the locations you use if they're public places.

    - Backgrounds are an asset that can be easily re-used for multiple locations. Even big name games will do this, and you may not even have noticed or at least not particularly minded when this was done because the focus is more towards the sprites and writing rather than the scenery. 
    
    - You can flip images, recolour them, or even crop them differently and change minor details to save yourself some time and work if you want more variety in your backgrounds.

    - There are ways to apply shaders in Ren'py to give your backgrounds the lighting of a different time of day, and/or to tint your sprites to match the lighting in a background so they blend in more naturally.

    - You might find some available background sets on {b}{a=https://lemmasoft.renai.us/forums/viewforum.php?f=52&sid=67dfade9ee0d70405eebd167e459d3fa}Lemmasoft Creative Commons{/a}{/b}, check the individual licences on each before using them as with any assets. 

    - The size of image will be the same as the screen size/resolution you are making the game. So a 1920 x 1080 game would need backgrounds that are 1920 pixels wide and 1080 pixels high to fill the screen. 
    """
    nvl clear
    nvl hide
    p "Lots of things to think about in your background art, so what would you like to check out next?"
    jump art_menu_return

label sprite_art:
    p "Sprites are your character images, like me!"
    p "As you can see, I am 2D, which is mostly what we will be talking about here."
    p "Sprites will often have a mixture of different facial expressions to show the player the mood of the character who is speaking."
    p "They might have different poses too, like this! Although remember this adds more work for the art of your game."
    p "You could even have more than one outfit, though again this will add more to do for you."
    p "My hat does look pretty cool though, right?"
    p "You can also have your sprites move on and off the screen with different effects - be right back!"
    p "Phew, that hat was just too cool, I don't think I can really pull off the look."
    p "But I could fall down..."
    p "Or pounce from the ceiling!"
    p "Or I could come closer..."
    p "And closer..."
    p "To tell you some secrets...like how you can save time and energy in making sprites like me! Well, maybe not quite like me, I am one of a kind, you know."
    p "There's a few different ways you can make sprites. I won't be telling you how to do this in your code, but I can tell you the options that are available!"
    pn """
    Making and Displaying Sprites

    - Individual images. One of the simplest options is to have every sprite expression as its own full image. This will be easier to code, however it might also add a lot to the size of your game files.

    - Layered images. The space-saving option is to make use of layers. For those of you who haven't made a lot of art, images can be drawn on separate layers - like putting different pieces on top so you can swap and change them. For sprites, this can mean having arm positions, outfit items, and facial features on their own layer images then mixing and matching these to create each pose and expression. A frown with a shouting mouth looks angry, but a frown with a grin has a different mood entirely.

    - Software to make sprites. {b}{a=https://store.steampowered.com/app/1280420/Mannequin/}Mannequin{/a}{/b} is a relatively cheap 2D sprite making software you can use to make simple 2d characters with different expressions that are able to be used in your own game. You may also be able to input your own sprite parts (or ones from your artist) and use this to build the expressions from those parts.

    - Image Formats. The most common image type for a sprite is to use .png with a transparent background. This will work for layered images or for standalone complete sprites. 

    - Image Sizes. The size of your sprite images will depend on the resolution and size of your game. If your game is the default 1920 x 1080, that means you have that much space on the screen. So a sprite that is 1000 pixels tall will take up most of the height of the screen.

    - Mr Placeholder. Oh yes it is indeed time to mention our own little sprite fellow here! Curious why he exists? I made him to test my sprite sizes and placements. His head box is the size from the top of the tallest character's head to the chin of the smallest character at the bottom, and his body is close to the width of the widest sprites. I put him in this game because he deserved the spotlight {i}somewhere{/i}. 

    - How many sprites? That depends how many characters you have. However, some side characters who only have a few lines may not need sprites. You can also use \"generic\" sprites with uniforms, helmets, and/or hidden eyes to take the place of basic side characters like soldiers, classmates, work colleagues, or other random citizens in your world.

    - Does my MC need a sprite? That's up to you! Some games have the MC on screen with the other sprites, but others will never show the MC to allow a more \"self insert\" approach for the player. Another common option is to only show the MC sprite in the \"Side Image\", and sometimes this includes allowing the player to choose not to see this side image in your options/preferences menu.

    - Other things to consider. Your sprites should be clear against your background so they can be seen easily. You may also want to give important character sprites a main colour to tell them apart from each other - in some games the colour scheme of a character can be a hint to their personality type too, so you could lean into the common stereotype colours or even do the opposite to play with players expectations.
    """
    p "Sprites are not actually necessary for a Visual Novel game, but it is very unusual particularly for a 2D art style to not use them."
    p "3D art styles might lean more towards having the characters and backgrounds in the same fully rendered images, but how you approach it is entirely up to you."
    p "Remember that the images you use are there to enhance your story and show people the world and characters they are interacting with throughout your VN."
    p "So, what's on the menu next?"
    jump art_menu_return

label cg_art:
    p "CGs are very similar to your backgrounds, except they will include characters and may have more detail than your simple background."
    p "Here's an example of a background from a project in development by PunderBash Games. I'll just slip out of the way for a moment to show you the next part!"
    p "And here is an example of a CG from the same project, where the characters are now included in the area."
    p "You can see the image has changed with some extra detail and added the characters, this is to show the moment that these characters first meet each other and a key point in their story."
    p "Hi again! So this is one way to use a CG. It takes the characters and places them in the scene directly rather than as sprites on top."
    p "CG scenes are optional, but they may well enhance the game experience for the player, especially when used for important, memorable, or emotional moments."
    p "Keep in mind, they tend to take more time to make than a background and sprites, and will add to your costs if you are commissioning them. So you may want to save CGs for particularly special moments!"
    p "CGs can also have layers and animation added to them, just like we saw in the backgrounds section with the rainy road."
    p "Some people will have the same artist doing the BGs, Sprites, and CGs, but others might have separate people working on them. It is up to you how you want to approach this, and what level of detail and styles you want to use for your assets."
    p "There's not a lot more to say about CGs beyond what we have already covered, except to say that when someone else is making them for you that you should give them as much detail on what you want as possible."
    p "So, shall we move on?"
    jump art_menu_return

