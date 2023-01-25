label captain_billiard_room_speech_part_1:
    
    captain """
    It was in June of 1900, so some of you might remember.

    A group of rebels, called the \"Boxers\", had taken up arms against foreign presence in their country.

    They were a group of mostly peasants, poorly armed. 
    
    We called them Boxers because of their use of martial art in their fights.
    """

    return

label captain_billiard_room_speech_part_2:

    captain """
    They managed to surround the europeans and japanese in the \"International legations\" quarter, in China's capital Beijing.

    There, the besieged did their best to resists the chinese assaults, but it was obvious to everyone that they wouldn't last very long.
    """

    $ play_music('boxer', fadein_val=10.0)

    scene boxer_fight with fade

    captain """
    In order to break the siege and rescue their compatriots, the largest foreign nations formed expeditions to help lift the siege of Beijing.

    I was part of the most important one, and the only successful : The \"Gaselee Expedition\". Named after Alfred Gaselee, the british expedition leader.

    It was a mish-mash of troops from eight different countries : Japan, The British Empire, The United States, France, Russia, German Empire, Italy and Austria-Hungary.

    As an Indian officer, I was obviously part of the British army.

    We landed first in the old chinese capital of Tianjin. 

    Then we marched from there to reach Beijing, and rescue the civilians sieged there, as well as people from previous expeditions.

    The journey was a total nightmare.

    A march of almost a hundred miles were we were under constant attacks from the Chinese troops.

    If it was bad enough, some poorly lead and confused soldiers, notably from the French army, often ended up shooting at their allies. 

    But the worst part was the scolding heat.

    Even my fellow Indian soldiers were not immuned from it, and many died of sunstrokes.

    When we reached Beijing, our expedition of 20 000 soldiers was reduced to 10 000.

    By that time, the soldiers were angry tired and restless.

    They had started to commit such acts that I can't even repeat here.

    I was expected the exactions of the Japanese and the Russians, who were known for their ruthlessness.

    But in the end, our proud \"civilized\" europeans nations fared no better. 

    The final assault of the besieged was also an example of lack of discipline on the soldiers and their commanders.

    Each country was supposed to each attack a different gate of the city.

    But the russians were not happy with their assigned choice of gate.

    So they woke up early and assaulted the closest gate to the delegations quarters, were the americans were supposed to be.
    
    They wanted to be the first army to reach the defenders, and so claim the glory to have liberated the city by themselves.

    Bloody fouls.

    Luckily in the end, we managed to conquer Beijing without too much trouble.

    Even entering the Imperial City and routed out the Empress.

    It was an undeniable victory, but the price paid had be high.
    """

    scene boxer with fade

    captain """
    Afterwards, we stayed and occupied the city.

    To compensate themselves, soldiers went on a looting frenzy.

    Sadly, people in the British army also took their part in it.

    But not in the same outrageous manner as other nations.

    At least, looting on the part of British troops was carried out in the most orderly manner.
    
    We held loot auctions everyday except Sunday in front of the main-gate to the British Legation.

    It was the best way to compensate the loss of our compatriots who had suffered the siege for three months.

    There was no way around it I am afraid.

    Well in any case, that was my first campaign as a captain.

    And I do not regret it.

    I still stayed a few more months in China to insure the peaceful transition.

    At the end, my commanders were really pleased with me. 
    
    So I got to go to london to lead a training regiment near London.

    That was very rare for someone of Indian descent.

    In any case, that's why I live in England today.
    """

    scene billiard_room with fade

    $ play_music('previous')

    $ captain_details.unlock_knowledge('talker') 

    return