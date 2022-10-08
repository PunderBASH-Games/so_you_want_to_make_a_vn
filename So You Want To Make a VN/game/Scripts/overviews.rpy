label overviews_return:
menu:
    "Where would you like to go next?"
    "Return to Overviews Menu.":
        jump overviews_menu
    "Return to Sections Menu":
        jump menu1
    "Exit to Main Menu":
        return



label vn_needs:
    p "Visual Novels might seem like very simple games, and they are - but there's still a lot to think about including."
    p "VN games by their definition have a focus on the story through the writing, with or without choices, and images that support the story. The following is a list of the things that most visual novel games will include, they'll all be discussed in more detail in other sections."
    pn """
    - Writing. The story will need to be written. It might branch out into different parts of the story by having the player make decisions that impact the narrative, but you can also write a Kinetic Novel which does not have choices and follows a linear story. This still needs to be written, though!
    - Artwork. Most visual novel games will have sprites to show the characters, backgrounds to show the locations, and some might have special images known as CGs to emphasise a special or important moment in the story. Like a climactic battle, a romantic scene, or the big plot twist reveal.
    - User Interface. The GUI is the set of images that give the game style, like text boxes, icons, and stylised menus.
    - Code. Code is the skeleton of the Visual Novel, it won't do anything without it! Ren'py has a lot already built in to make this easier for you, but even the dialogue and narration will need to be put into script files. You could write this directly into the script as you go, or copy it over later, depending on your personal preference.
    """
    nvl clear
    nvl hide 
    p "Now let's take a look at some optional features, which you may or may not want to include in your game. Remember, any items you include will be more work to complete, and it is best to think about them in balance."
    p "When considering a new feature, think about what it adds to the game, and if the game would be incomplete or suffer if the feature wasn't in there. Sometimes a feature might be cool to add, but should be left to the end of your pipeline in case you want or need to cut it."
    pn """
    - Sound and Music. Sound effects and background music can add a lot of atmosphere to a game, but some games choose not to include them and work just fine without them.
    - Additional Options Menus. Adding new options to your menus, like an on/off switch for showing the main character's image, will be adding another job for the coding. You may also want to be careful your options menus aren't too crowded for a player to easily navigate.
    - Galleries and Collectibles. It can be nice for players to have a place to view the CG images they've unlocked by playing the game, or to view other things like character profiles or extra scenes.
    - Mini Games. These are one of the more controversial options, some people love mini games that add to the gameplay, but some people prefer a visual novel to focus on reading and making choices as the core gameplay. Mini games are often some of the harder things to add in as the code is more complex, so this is something to take into consideration.
    - Disabling Built-in Features. Even more controversial is choosing to disable rollback, or to change or remove other general features that are built in to Ren'py. Generally this is not advisable, even if it is possible to do, because players may become frustrated when they're not able to enjoy the game in the way they wish to.
    - Other. This might seem pretty self-explanatory, but any feature you're adding to your game is adding more work to it, and often requires more skill. If you already know your way around code, or have someone on your team who does, that's great! But you might still want to put any extra features in a priority list, so you work on the most important first.
    """   
    nvl clear
    nvl hide
    p "So, that covers the basics of what makes a Visual Novel game, but there's a lot more to each part, and more background work that isn't mentioned here."
    call overviews_return

label pipeline:
    p "Writing out your pipeline is a good way to make sure you have a priority list of jobs that need to be done, when you want to complete them by, and if you're working with other people it's a useful way to assign tasks."
    p "There are lots of ways to accomplish this, so it really is up to you how you prefer to work."
    p "You could draw up a table or spreadsheet, or you could use a task management website like Trello to organise your tasks."
    p "I personally like Trello, because I can have different boards for different job groups. So all of the art tasks are in one place, and all of the music tasks are in another, but you should stick to whichever method you feel makes sense to you (and your team if you have one)."
    p "It can be helpful to separate into your production stages, so you have a list for each stage. This way you can focus on completing one stage before moving on to tasks on the next stage, which is especially useful if you're planning to have pre-release demos at the end of certain stages to test and get feedback."
    p "Each task in your project should have: a priority, a person assigned to the task, a deadline (if you are working to specific release dates), a description and/or checklist of what needs to be done, and a box to check when it is ready for testing and another to check when it is fully tested and working."
    p "Pipelines might not seem very important when you're making a game on your own, but they can be helpful for you to see your own progress and work out which tasks you still have left to do. Switching between tasks can help to prevent burnout, too, and keep your motivation up to continue."
    p "As an example, the art section of your pipeline might look like this."
    pn """
    Alpha
    
    1. Make a list of backgrounds, characters, and CGs.

    2. Decide on the game's resolution, and the size of the images.

    3. Find placeholder images, and/or draw concept art.

    4. Put the placeholders/concepts into the game and test.

    """
    nvl clear
    pn """
    Beta

    1. Decide on the final designs of the images.

    2. Add flat colour to the images.

    3. Add in the expressions for the sprites. 

    4. Replace the placeholders with the new images.
    """
    nvl clear
    pn """
    Silver

    1. Add shading and final effects to all of the images.

    2. Replace the images in the game with the finals.

    3. Check the expressions in the game.

    4. Review with testers if any last minute changes are needed.
    """
    nvl clear
    pn """
    Gold

    1. Check the quality of all images and how they look in the game.

    2. Make any edits if necessary.

    3. Add in any optional visual effects or special transitions.

    4. Review and fully test all images for the final time before building.
    """
    nvl clear
    nvl hide
    p "This might not look like a huge list on the surface, and Gold is very similar to Silver, but by the time you hit Silver you should be getting close to release levels."
    p "When you have your full pipeline, it might also look a bit intimidating, but that's also why it is helpful to break it down into these smaller tasks and stages. Ticking off a job done can help to keep up motivation and a feeling of accomplishment."
    p "That said, it can easy to fall into a planning trap and take a long time to get started! Work out what kind of list works for you, whether you need something more detailed or if you work better with a simpler short overview."
    call overviews_return

label costs:
    p "It might seem like making a game shouldn't cost you much, but that really depends on how you are working!"
    p "Ren'py is a great VN engine because it is free to use, and streamlines the VN making process particularly for those of us who have never touched coding before. For those familiar with Python, it can also be an easy switch to make as you can use some Python inside Ren'py."
    p "The programs needed alongside Ren'py are also often free to download and use too. Many people choose to use Visual Studio Code to write their games, as Atom has a couple of faults in it that haven't been fixed."
    p "So getting the code into your project is essentially free (unless you are commissioning someone to work on the code for you - we'll get to that later), but what about the other assets?"
    p "Art making programs might be free, but others are paid versions. If you're making your own art and don't currently have the hardware and/or software to do it, that's something you'll want to take into account as a cost."
    p "The same goes for the other assets, like music and sound effects. If you're making them yourself, that means equipment and software."
    p "If you're going to look for art, music, or sounds effects that have already been created by someone else, you will need to make sure you have the licence and permission to do this (we will cover this later), and/or pay for the assets that you're using."
    p "You might also commission new assets, where you pay someone to make a new piece to fit your project. Commissioning usually means paying in advance, as most creators will not generally work for free or for a share of the profits."
    p "We'll cover commissioning in the Job Roles section later."
    p "You may also want to think about where you want to release your game. Steam has one of the biggest user bases, but it does have a fee to put your project on the site. It does allow this fee to be refunded after a certain number of sales/downloads, so it is a cost that can potentially be recouped." 
    p "The same is true for mobile phone app stores, so if you want to release on iOS or Android you will want to look at your options here and work out what is worth it for you to do."
    p "The other popular option is itch.io, which is free to publish your games to, but may not have the same audience reach as other platforms."
    p "So there are ways to make a game and publish it without spending a single shiny coin, but you'll want to think about what is best for your project and what is affordable if you do pay for assets/work."
    call overviews_return 

label motivation:
    p "So you've started making your game, but it's getting harder to keep going. Should you give up?..."
    p "Hold it right there, friend!"
    p "Keeping up motivation can be really tough, making a game is a lot of work, but that doesn't mean it's time to throw in the towel just yet!"
    p "Before you begin, it's worth thinking about the things that help keep you going with projects." 
    p "Different things work for different people, so while some people might get more done by setting specific times or goals to work on every day/week, other people may find it better to do more work in less structured bursts of inspiration."
    p "What matters is finding what works for {i}you{/i}. Try a few different methods if you aren't sure, and stick to what works or even switch around if you need to."
    p "But what do you do when you're losing that inspiration and motivation? Well, here's some ideas! Again, different things work for different people, so try a few and pick what works for you."
    pn """
    Ideas to help you get motivated:
    
    - Listen to music. Headphones can also help to tune out distractions and get you focusing in on the work at hand. Pick some playlists, make some new ones, or just put something on that makes you feel inspired.

    - Play some games. No, really! Either replay that VN that inspired you to make your own, or play some new VN games that you haven't played before. The secret part here is you can class it as research by making a few notes on tropes/features that you like/dislike and want to include/avoid in your game!

    - Switch tasks. If you're working on more than one part of your game (for example, writing and background art) then if you're hitting a creative wall on one task switch to a different task. Go back to the other one when you feel ready to. Variety can help the work feel fresh and interesting.

    - Talk to people. Dev communities, like the Ren'py discord server, can be really good places to find motivation and inspiration. Talk to your team if you have one too, but if you're a solo dev you can really increase your chances of finishing your project by talking to fellow developers about the process.

    - Take a break. Walk away, put it down, and do something completely different. Unless you're working on a jam or a tight deadline, taking time off from development is not always a bad idea. Tell yourself you're going back to it later, but for the here and now you're going to have a little holiday. Then when you go back, you'll be more refreshed and ready to go.

    - Do something related to development, but not on your project. Keep the creative gears turning on something close to your project but not your actual project. Maybe this is writing a brief few paragraphs of "what if"s scenes for your characters, or maybe it's drawing some fanart for something else you love. Whatever you feel like!

    - Go back to the drawing board. This doesn't mean starting again, it just means going back to your planning and looking over things again. See if there's anything you want to change, or just check over the things you've done.

    - Play your own game. Hit the launch button and play through what you already have, even if it isn't anywhere near done. Seeing the parts in place and looking at how it is coming together can be great motivation to keep going to make it better, and it's also handy to keep testing for bugs and keep an eye out for errors.
    """
    nvl clear 
    nvl hide
    p "Feeling motivated yet? I hope so! Shall we move on to the next part?"
    call overviews_return

label how_long:
    p "How long does it take to make a VN game?"
    p "Well, that's the golden question! How long is a piece of string?"
    p "How long it takes to make your game depends on how much you want to do, how much time you can spend working on it (without letting higher priorities like education, employment, or other needs fall behind), and what deadlines you want to set for yourself."
    p "As a shameless self plug, the PunderBash Games kinetic novel \"Summer Horrordays\" was made within 28 days. It was a game jam project worked on by 4 people, with about 1 week of intermittent planning (pipeline and ideas) before starting work on the game itself."
    p "The jam only allowed for the game to be worked on from the 1st of September that year, and had to be released by the end of the month, so we had to plan to make sure we would be able to finish everything on time."
    p "There are even shorter game jams out there, where you only have 1 week to make the game from start to finish! But those are usually very small games."
    p "The more time you spend on a game, the faster it will get made. But it is very important to keep in mind a few facts of the dev business."
    pn """
    - Big and established label games are made by huge teams, and they still take 1-3 years to make them. 

    - The more complicated the game, the longer it will take to make. Think about how long you would be willing to keep going on your game to get it completed. 

    - Teams can complete games faster, because there's more people doing the work. {i}BUT{/i} teams may also have personal delays with members, because life happens.

    - And there's a point too: Life Happens. Emergencies come up, situations change, amounts of free time you have available will vary. There are things in life that will, and should, take priority over making your VN, and that can make it take longer to complete. 
    """
    nvl clear 
    nvl hide
    p "So, in conclusion, you could make a game in a single day if you really wanted to. Or you could spend 2 years on the same project before it is ready to release. How long it takes is up to you, and your team if you have one."
    p "Be prepared for things to take a bit of time to get to where you want them to be, and don't get too discouraged if it's taking a bit longer than you initially hoped. You can get there."
    p "Shall we continue?"
    call overviews_return

label game_scope:
    p "Scope. Scope is a term you may here a lot for Indie Game development."
    p "This is referring to the amount of work it'll take to complete what you have planned."
    p "For your first VN project, it is best to keep this goal smaller. Once you've made a small completed game, you will have proven to yourself that you {i}can{/i} finish and make a game, even if it isn't the big project of your dreams right away."
    p "Making a small game first also gives you some good practice and experience in the full process, start to finish. It can be good to look for a game jam for your first time, but we will talk about that in the job role section later."
    p "Keeping your scope in check is a balance between what you want to achieve, how much work you're willing to do to achieve it, and how long you are willing to keep going on it until it is finished."
    p "If your scope is too large, you risk burning out before you're done and never reaching the end. But if it is too small, you also risk feeling unsatisfied or like you haven't done everything you wanted to."
    p "One way to control scope is to prioritise sections. So you can have elements of your game, like an epilogue story, that isn't vital to complete the game but that you can have as an idea to add if you want when the rest is done."
    p "This way, you can drop low priority sections if it's getting too big or you feel it's taking too long, without losing the notes for those ideas if you do want to use them."
    p "Here's a few other tips on handling the scope of your game."
    pn """
    - Keep your cast small. Less characters means less work, you can tell a lot of story with only a handful of people.

    - Not every character needs a sprite. Need a side character who is only there for one scene or a few lines? They don't need a sprite. You can also use a simplified sprite for a background character that you can reuse for other similar characters, with or without changing the colour pallette. Some games simplify these designs further by hiding the eyes and having no expression changes.

    - Limit your locations. It might be great to have an adventure story, travelling across vast landscapes with lots of fun new locations, but keep in mind every new location is likely going to need a new background. It won't really work to have open fields for a scene in the middle of a forest, or the Eiffel Tower in a scene set in the centre of Denmark.

    - Reuse your assets. If you have 3 shops across your story, you can likely use the same shop background. Or you can change it slightly by swapping around a few items on the same counters, changing the colour scheme, and/or flipping the image horizontally. Have characters show up in different storylines, reuse sound effects for similar situations, if you can reuse something without it being intrusive or nonsensical then you probably should.

    - Keep the expressions simple. There can be a lot of nuance in facial expressions and body language of sprites, but you don't necessarily need to show every tiny change. You likely don't need to show the player the difference between shocked and scared, or shy and embarrassed, if the expression is close enough to both to work.

    - Use layered images for sprites. This one is a little bit more work for the art and coding, but it can give you a greater range of expressions with a smaller pool of resources. You can mix and match eyes, eyebrows, and mouth shapes to give different expressions. 
    """
    nvl clear
    nvl hide
    p "There are lots of ways to keep the size of your game manageable, but the main part is planning. It is always ok to go back and change your initial plans if you need to, though having a plan from the start will help you to keep things from growing out of control in excitement."
    p "So, adventurer, where next?"
    call overviews_return

label what_else:
    p "So you've almost got your starter plan going, you have your ideas, and a plan of action. Is there anything else to consider before you start?"
    p "Well, one thing can be to think about doing some market research."
    pn """
    Market research can mean a lot of different things, but some of the main ideas are as follows:
    
    - What kind of game do you want to make? What games are already out there that are similar? Have a look at what you can learn from them before you start, the things you like and dislike, and how this might relate to what you want to do when making your own game.

    - Who is your target audience, and what do they want from a game? I'll preface this one with \"your first target audience needs to be YOU, make the game you want to play.\" But I know you want to make the game for other people to play, too. Look for their opinions and use them as a guideline, but not a hard rule, for what you want to make.
    
    - Existing research. For some genres, like Otome, there's already some great market research articles analysing the opinions of people who play those games. But you may also want to do your own questionnaire to pass out to potential players and see what things they might want to see, or not see, in a game like yours. Again, these should be guidelines - sometimes people find themselves loving something they don't normally enjoy so it can be worth the risk for variety!

    - Think ahead. Look at where you want to publish and what rules they have. So if you want to publish a game with NSFW content, you need to ensure the platform will accept your submission. Places like Steam will have their rules available for you to read ahead of time, and you can also ask others in the dev community about the best places to put your game and what rules they have about content.
    """
    nvl clear
    nvl hide
    p "So we've covered market research, what else is there?"

    pn """
    - Advertising. This is a tricky one. You don't want to advertise too long before release, or you risk losing people's attention and hype dying down. But if you advertise at about the right point in advance you can help generate hype, get on wishlists, and secure a better release day sale/download rate.

    - Funding. You might want to try using platforms like Kickstarter, Patreon, Ko-fi, or others to get funding towards making your dream game a reality. But you should handle this with care, make sure you can actually achieve the goals you promise to people who subscribe/pay, keep them updated, and above all be careful to adhere to the rules of the funding site. 

    - Building the skills you need. If you've never touched code, or Ren'py, before now, then it's time to get some practice in and look at some tutorials. You'll find some handy links in the Resources section. The same goes for art, gui design, website design, and more.

    - Social Media. This can be a powerful tool for advertising, and it can be better to have separate accounts for your game dev pursuits. That way you can keep your personal things personal, and have the game's social media nice and focused to reach your target audience. Be wary of signing up to too much though, it helps to be consistent if you want to maintain presence and interest.

    - Names, logos, and design. You don't have to give your game its final name right away, but when you do, {i}google it{/i}. The last thing you want is for your game, or team/studio, name to be the same or very close to something already in use. The same applies to your logo(s), do some searches on your ideas. You should want your brand to be at the top of any searches for your work, and avoid any unpleasant copyright or trademark issues.

    - Testing. I cannot stress this enough, test your project. Make sure you know inside and out that it works exactly how you want it to, and where possible have one or more people outside of your team test it too. They may notice errors that you didn't, and give you a chance to fix them before release.

    - Designing your product page. Game pages can benefit from being well designed. That means not only a good blurb telling people about the features and story premise, but also having screenshots and trailers, and making your game page look both professional and eyecatching. This isn't always easy, but look at similar game releases and take note of what looks good and how that could be applied to your own (without just copying, plagiarising isn't a good look!)

    - Money and Teams. If you're selling your game, or making any profit at all from it, you'll need to manage this money. Be aware of any income tax laws where you are, and keep records of the things you have spent money on to make your game as you can subtract this from the profits. You'll also want to ensure you agree revenue share long in advance if you are working with other people and sharing the profts. Everyone needs to be happy the money is safe and will be split fairly before you earn anything at all.
    """
    nvl clear
    nvl hide
    p "That should be everything, but it's always possible that I missed something in here!"
    p "Still, there's lots to think about and be aware of. It might seem like a huge list, but break it down into little pieces at a time and it isn't too bad. Don't be put off by these things, just keep them in mind for things to take into account."
    p "It's entirely up to you how you handle your project. As long as you have a clear idea of your goal and how you want to reach it, you'll be able to get there."
    p "Where to next, friend?"
    call overviews_return 