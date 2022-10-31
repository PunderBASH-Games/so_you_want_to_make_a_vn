
label start:

    p "Hello there!"
menu:
    "General Kenobi...":
        p "Haha, 10 points to you for the reference, friend! My name is Mr Placeholder, because the writer of this mini project is very bad at names. And art. And lots of things."
        jump start2
    "Hi?...":
        p "Nice to meet you, friend! My name is Mr Placeholder, because the writer of this mini project is very bad at names. And art. And lots of things."
    "Skip to the menus, please." if persistent_firstcomplete:
        jump menu1

label start2:
    p "Anyway, you want to make your very own Visual Novel Game, right? Well here's the basics of what you might want to include, as well as some frequently asked about topics in the Indie Dev community."
    p "This tutorial game won't cover anything in detail, like how to learn Ren'py code, because other tutorials have that covered in far better detail than I could ever hope to. You'll find links later or in the About section of the main menu."
    p "Lots of projects get started, but some never make it to the finish line. This could be for many reasons, but sometimes it's because we don't realise all of the little parts that are needed for a finished game - even a small one has more to it than you might think!"
    p "And that's where we come in here! This guide will give you an idea of the amount of work needed to produce and publish a finished Visual Novel Game. We want to see lots of people succeed, and the way to success is knowing what's ahead."
    p "It might look intimidating, but please don't be discouraged! With a bit of work and preparation, almost anyone can make a Visual Novel game, and that includes, you, friend!"
    p "So the best place to start is planning. You don't need to plan every detail right away, but it is good to know."
    p "Most games have some kind of plan to making them, this is usually called a Pipeline or Production Pipeline."
menu:
    "Do you want an overview of Pipelines?"
    "I know what a Pipeline is.":
        p "Great, we'll move on then! You might want to make notes as this project will cover the main topics you'll want to think about including in your own pipeline."
        p "Remember to work out your Alpha, Beta, Silver and Gold targets, and be prepared to alter your goals as you go along if you need to."
        jump after_pipelines
    
    "I don't know what a Pipeline is, can you tell me?":
        p "Of course!"
        p "A pipeline is like a big \"to do list\" of all the parts that make a finished game, except it is also often broken down into production stages."
        p "The first stage is Alpha, this is the roughest draft stage of the VN. This is like a proof of concept, and likely won't have all of the features you'll want in the finished product."
        p "The Alpha stage may also use placeholders for some of the assets (like art and music), just like me! I was drawn to be a test for sprite sizes, I'm just lucky I turned out so handsome!"
        p "Beta is the second stage, where you'll have a lot of your game in place but you may not have all of the features or final polish." 
        p "Think about Beta testing for mainstream games - things can still change from Beta but a lot of the main concept and design is there."
        p "The last 2 stages are Silver and Gold. Silver will need almost everything in place, with only final testing and checks before you reach Gold. Think Gold Standard as the final target to release your complete game."
        p "Don't worry if you don't stick to your initial outline plan - it's there to help you, so change it and adapt it as needed."
        jump after_pipelines

label after_pipelines:
    p "So we might want to make a pipeline of the jobs we need to do, but what exactly does a Visual Novel need?"
    p "That can vary a lot from person to person and what you prefer, so I'm going to break this down into a bunch of menus so you're able to pick and choose the topics you want to read about and what order you'd like to read them."
    p "If this is your first time making a VN, it's probably best to look over every topic and what you need to do to make it."
    $ persistent_firstcomplete = True

label menu1:

menu:
    "Which section would you like to view next?"
    "Overviews and General":
        jump overviews_menu
    "Assets - Writing, Music, Sound, Art, etc":
        jump assets_menu
    "Job Roles, Solo Devs, Teams, and Hiring":
        jump jobs_menu
    "Legal Considerations and Age Ratings":
        jump legal_menu
    "Finishing Touches, Marketing, and Releasing":
        jump finishing_menu
    "Everything About Code":
        jump code_menu
    "Accessibility and Translations":
        jump access_menu
    "Tutorials, Links, and Other Helpful Resources":
        jump resources_menu
    "Exit to Main Menu":
        return

label overviews_menu:
menu:
    "Which topic would you like to view next?"

    "What does a VN need?":
        jump vn_needs
    "What might a pipeline look like and how do I make one?":
        jump pipeline
    "What are the costs and hidden costs involved in making a VN?":
        jump costs 
    "How do I keep myself and/or my team motivated to finish?":
        jump motivation
    "How long does a VN take to make?":
        jump how_long
    "How big should my game be?":
        jump game_scope
    "What else do I need to think about when planning my first VN?":
        jump what_else

    "Go back to Section Selection":
        jump menu1

label assets_menu:
menu:
    "Which topic would you like to view next?"

    "What are assets, and what do I need in my VN?":
        jump assets_list
    "How do I find, buy, commission, or make assets?":
        jump assets_get
    "Music":
        jump assets_music
    "Art":
        jump assets_art
    "Sound Effects":
        jump assets_sound
    "GUI":
        jump assets_gui
    "Writing":
        jump assets_writing
    "Code and Extra Features":
        jump assets_code
    "Voice Acting":
        jump assets_voice
    
    "Go back to Section Selection":
        jump menu1

label jobs_menu:
menu:
    "Which topic would you like to view next?"
    "What jobs and roles are involved in making a VN?":
        jump roles
    "How do I find a team to work with, and what do I need to know for working in teams?":
        jump teams
    "What do I need to know if I'm working solo?":
        jump solo 

    "Go back to Section Selection":
        jump menu1
        
label legal_menu:
    "{i}{b}As a disclaimer, none of this is official legal advice. Always check the laws for individual regions where appropriate.{/b}{/i}"
menu:
    "Which topic would you like to view next?"
    "What do I do if I want to make a fan game?":
        jump fangames
    "What about modding (modifying) an existing game?":
        jump modding
    "How do I stop piracy?":
        jump piracy
    "Age Ratings and Content Warnings":
        jump content_age
    "General Legal Concerns":
        jump general_legal
    "Go back to Section Selection":
        jump menu1
label finishing_menu:
menu:
    "Which topic would you like to view next?"
    "What is marketing, and how do I approach marketing with an Indie VN?":
        jump marketing
    "How about Beta Testing? How do I find testers and work with them for usable feedback?":
        jump using_feedback
    "How do I build and release my game when it is complete?":
        jump building_releasing
    "What are the last things I should be doing to finish my game before releasing it?":
        jump finishing_touches    
    "Go back to Section Selection":
        jump menu1
label code_menu:
menu:
    "Which topic would you like to view next?"
    "How much do I need to know about code to make a basic Ren'py game? What are the basic tips to start?":
        jump code_know
    "What code do I need to know to use more of Ren'py and add extra features?":
        jump code_extra
    "Where can I go to learn about Ren'py code?":
        jump code_learn
    "Go back to Section Selection":
        jump menu1
label access_menu:
menu:
    "Which topic would you like to view next?"
    "What is accessibility and why do we need it?":
        jump access_what
    "What is the built-in self-voicing feature and how can I use it?":
        jump access_selfvoice
    "What are the other ways I can make my game more accessible?":
        jump access_other
    "How can I include multiple languages and translate my game?":
        jump access_language
    "Go back to Section Selection":
        jump menu1
label resources_menu:
menu:
    "Which topic would you like to view next?"
    #links to other websites - go through every topic and pull out a few links
    "Tutorials and Guides":
        jump resources_tut
    "Assets":
        jump resources_assets
    "Communities":
        jump resources_communities
    "Useful Tools and Software":
        jump assets_tools
    
    #""
    "Go back to Section Selection":
        jump menu1



#### false story, gerald and the haunted moon?