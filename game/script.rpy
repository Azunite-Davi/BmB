
define e = Character(("Erin"), color="#5f00a8",)
define m = Character(("Miq"), color="#ff6200", image="miq")
define n = Character(("Nemmi"), color="#08a800", image="nemmi")
define o = Character(("Obelisk"), color="#9a0000",)
define l = Character(("Mul"), color="#000000",)

layeredimage miq:
    zoom 0.35


    group body:
        attribute body default:
            "sprites/miq/b_miq.webp"
    group face:
        attribute face default:
            "sprites/miq/face.webp"

    group shirts:
        attribute WhiteDress:
            "sprites/miq/WhiteDress.webp"
        attribute YellowCasual:
            "sprites/miq/YellowCasual.webp"


    group pants:
        attribute BlackSlacks:
            "sprites/miq/BlackSlacks.webp"
    group undie:
        attribute undie:
            "sprites/miq/Red.webp"

    group e_expressions:
        attribute normal default:
            "sprites/miq/e_normal.webp"
        attribute angry:
            "sprites/miq/e_angry.webp"
        attribute sad:
            "sprites/miq/e_sad.webp"
        attribute happy:
            "sprites/miq/e_happy.webp"
        attribute surprised:
            "sprites/miq/e_surprise.webp"
        attribute thinking:
            "sprites/miq/e_thinking.webp"

    group m_expressions:
        attribute t:
            "sprites/miq/Open.webp"
        attribute Closed default:
            "sprites/miq/Closed.webp"

    group shoe:
        attribute boots default:
            "sprites/miq/Boots.webp"

layeredimage nemmi:
    zoom 0.35

    group body:
        attribute backhair default:
            "sprites/nemmi/backhair.png"
        attribute body default:
            "sprites/nemmi/nemmibody.png"
        attribute fronthair default:
            "sprites/nemmi/frontHair.png"


    group shirts:
        attribute BlackHoodie:
            "sprites/nemmi/BlackHoodie.webp"
        attribute Tanktop:
            "sprites/nemmi/Tanktop.webp"


    group pants:
        attribute short:
            "sprites/nemmi/GreenShorts.webp"
    group undie:
        attribute undie:
            "sprites/nemmi/WhiteBrief.webp"
    group footwear:
        attribute shoe default:
            "sprites/nemmi/DarkSneakers.webp"
        attribute sock default:
            "sprites/nemmi/DarkSneakers.webp"


    group e_expressions:
        attribute eye_normal default:
            "sprites/nemmi/9 eyes/eyeNormal.png"
        attribute angry:
            "sprites/nemmi/9 eyes/Angry.png"
        attribute sad:
            "sprites/nemmi/9 eyes/eyeSad.png"
        attribute happy:
            "sprites/nemmi/9 eyes/Happy.webp"
        attribute surprised:
            "sprites/nemmi/9 eyes/eyeSurprise.png"
        attribute confused:
            "sprites/nemmi/9 Eyes/eyeConfused.png"

    group m_expressions:
        attribute normal:
            "sprites/nemmi/8 muzzle/Normal.png"
        attribute angry:
            "sprites/nemmi/8 muzzle/Angry.png"
        attribute sad:
            "sprites/nemmi/8 muzzle/Sad.png"
        attribute happy:
            "sprites/nemmi/8 muzzle/Happy.png"
        attribute t:
            "sprites/nemmi/8 muzzle/Talk.png"
        attribute pout:
            "sprites/nemmi/8 muzzle/Pout.png"
        attribute scared:
            "sprites/nemmi/8 muzzle/Scared.png"
        attribute surprised:
            "sprites/nemmi/8 muzzle/Surprise.png"
        attribute grit:
            "sprites/nemmi/8 muzzle/Grit.png"
image Crayon_village = "bg/Crayon Village Slope.png" 
image library = "bg/library.jpg" 
image living_room = "bg/Living Room.png" 
image moutain = "bg/Mountain Day.png" 
image landscape = "bg/Abstract landscape.png" 
image bedroom = "bg/Bedroom.png"
image dream = "bg/mountain_dream.png"
image castle = "bg/castle.jpg"
image castle_inside = "bg/castle-interior.jpg"
image trainstation = "bg/trainstation.jpg"
image park = "bg/CityPark.jpg"
image bath = "bg/bathroom.jpg"
image kitchen = "bg/kitchen.jpg"
