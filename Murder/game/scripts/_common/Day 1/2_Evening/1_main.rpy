# ------------------------------------
#               HOST
# ------------------------------------
label common_day1_evening_host_welcome_speech:
    
    host """ 
    Welcome, everyone. My apologies for keeping you waiting. 
    
    Now that we're all gathered, I'd like to express my gratitude once more.

    As you already know, you are here because of the heroic acts you've committed in the past.

    I've taken notice of these actions and felt it was my responsibility to extend a formal 'thank you.'

    I realize the invitation letter you received was somewhat vague, so let me clarify its contents now.

    My first gift to you is a stay at my manor. 
    
    You'll be fully catered to, enjoying the most refined food, expertly prepared by my personal chef.

    During the three days we'll spend together, we'll also partake in various activities, which I'm sure you'll find enjoyable.

    My second gift is a sum of eight thousand pounds, to be shared among you. 
    
    This is my way of thanking those as selfless as yourselves, who help others without thought of reward.
    """
    
    """
    Following her speech, our host settled back down in her chair.
    """

    return

# ------------------------------------
#               CAPTAIN
# ------------------------------------
label common_day1_evening_captain_billiard_room_speech_part_1:
    
    captain """
    It was in June of 1900, so some of you might remember.

    In China, a group of rebels, called the "Boxers," had taken up arms against foreign presence in their country.

    They were a group of mostly peasants, poorly armed.

    We called them "Boxers" because of their use of martial arts in their fights.
    """

    return

label common_day1_evening_captain_billiard_room_speech_part_2:

    captain """
    They managed to surround the Europeans and Japanese in the "International Legations" quarter, in China's capital, Beijing.

    There, the besieged did their best to resist the Chinese assaults, but it was obvious to everyone that they wouldn't last very long.
    """

    $ play_music('boxer', fadein_val=10.0)

    scene boxer_fight with fade

    captain """
    In order to break the siege and rescue their compatriots, the largest foreign nations formed expeditions to help lift the siege of Beijing.

    I was part of the most important one, and the only successful one: The \"Gaselee Expedition,\" named after Alfred Gaselee, the British expedition leader.

    It was a mish-mash of troops from eight different countries: Japan, The British Empire, The United States, France, Russia, German Empire, Italy, and Austria-Hungary.

    As an Indian officer, I was obviously part of the British army.

    We first landed in the old Chinese capital of Tianjin.

    Then we marched from there to reach Beijing, and rescue the civilians besieged there, as well as people from previous expeditions.

    The journey was a total nightmare.

    We endured a march of almost a hundred miles, where we were under constant attacks from Chinese troops.

    If that wasn't bad enough, some poorly led and confused soldiers, notably from the French army, often ended up shooting at their allies.

    But the worst part was the scorching heat.

    Even my fellow Indian soldiers were not immune to it, and many died of sunstroke.

    By the time we reached Beijing, our expedition of 20,000 soldiers was reduced to 10,000.

    By that time, the soldiers were angry, tired, and restless.

    They had started to commit such acts that I can't even repeat here.

    I was expecting the exactions of the Japanese and the Russians, who were known for their ruthlessness.

    But in the end, our proud "civilized" European nations fared no better.

    The final assault of the besieged was also an example of a lack of discipline among the soldiers and their commanders.

    Each country was supposed to attack a different gate of the city.

    But the Russians were not happy with their assigned choice of gate.

    So they woke up early and assaulted the closest gate to the legation quarters, where the Americans were supposed to be.

    They wanted to be the first army to reach the defenders, and so claim the glory of having liberated the city by themselves.

    Bloody fools.

    Luckily, in the end, we managed to conquer Beijing without too much trouble.

    We even entered the Imperial City and routed out the Empress.

    It was an undeniable victory, but the price paid was high.
    """

    scene boxer with fade

    captain """
    Afterwards, we stayed and occupied the city.

    To compensate themselves, soldiers went on a looting frenzy.

    Sadly, people in the British army also took part in it.

    But not in the same outrageous manner as other nations.

    At least, looting on the part of British troops was carried out in the most orderly fashion.

    We held loot auctions every day except Sunday in front of the main gate to the British Legation.

    It was the best way to compensate for the loss of our compatriots who had suffered the siege for three months.

    There was no way around it, I'm afraid.

    Well, in any case, that was my first campaign as a captain.

    And I do not regret it.

    I stayed a few more months in China to ensure the peaceful transition.

    In the end, my commanders were really pleased with me.

    So, I got to go to London to lead a training regiment near London.

    That was very rare for someone of Indian descent.

    In any case, that's why I live in England today.
    """

    scene billiard_room with fade

    $ play_music('PREVIOUS')

    $ captain_details.description_hidden.unlock('talker') 

    return

# ------------------------------------
#               LAD - PSYCHIC
# ------------------------------------
label common_day1_drinks_lad_psychic_encounter:

    lad """
    Nice to meet you, Miss Baxter. I am Ted Harring.
    """

    psychic """
    Nice to meet you, Mr. Harring.
    """

    return