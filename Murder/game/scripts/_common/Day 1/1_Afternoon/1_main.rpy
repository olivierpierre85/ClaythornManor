# ------------------------------------
#   DOCTOR / NURSE (shared arrival scene)
#   Friday Afternoon - Train Station -> Car -> Manor
# ------------------------------------
label common_day1_afternoon_station_doctor_nurse:

    nurse """
    Hi, I'm Rosalind Marsh. Are you going to Claythorn Manor?
    """

    footman """
    Yes, ma'am. This gentleman will come with us.
    """

    doctor """
    Nice to meet you, Miss Marsh. I'm Doctor Daniel Baldwin.
    """

    nurse """
    Nice to meet you, doctor. Was your trip pleasant?
    """

    doctor """
    It was pleasant, thank you.

    How about you?
    """

    nurse """
    It was fine, thank you. And what...
    """

    if current_character.text_id == "doctor":

        """
        She stops suddenly, surprised, a bit scared.

        Her gaze fixes on something behind me.

        I turn quickly.
        """

    else:

        """
        I stop.

        Something — someone — catches my eye over the doctor's shoulder.

        A man has appeared farther along the platform.

        He is tall and composed, and most of his face is concealed behind a tin mask.

        I have seen worse, working on the wards. Much worse.

        But I was not expecting it, and the surprise must have shown on my face.
        """

    broken """
    Hi, I'm Thomas Moody.

    Lady Claythorn invited me. Maybe you can help?
    """

    if current_character.text_id == "doctor":

        """
        It takes a moment before anyone can respond.

        We are all shocked by the mask covering most of his face.

        A "broken face" from the war.

        It's not the first one I've seen, but I'm still not used to it.

        Apparently, neither are the people next to me.
        """

    else:

        """
        Nobody speaks for a moment.

        Doctor Baldwin collects himself first.
        """

    doctor """
    Hello, Mr Moody. You're with the right people.

    This young man was about to drive us to Claythorn Manor.

    I'm Daniel Baldwin, and this is Rosalind Marsh.

    Nice to meet you.
    """

    """
    We exchange a few pleasantries, then go to the car and begin our journey to Claythorn Manor.
    """

    return
