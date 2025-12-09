import streamlit as st
import json
from datetime import datetime

# Set page config - MUST BE FIRST and ONLY ONCE
st.set_page_config(page_title="Proverbs at Work Assessment", layout="wide")

# Hide any leftover sidebar space (mobile-proof)
hide_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {display: none !important;}
        div[data-testid="collapsedControl"] {display: none !important;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# HARD-CODED CORRECT ANSWERS FOR STREAMLIT CLOUD
CORRECT_ANSWERS = {
    1: "Usually", 2: "Usually", 3: "Usually", 4: "Not Usually", 5: "Usually",
    6: "Usually", 7: "Usually", 8: "Usually", 9: "Not Usually", 10: "Usually",
    11: "Usually", 12: "Not Usually", 13: "Not Usually", 14: "Not Usually", 15: "Usually",
    16: "Not Usually", 17: "Not Usually", 18: "Not Usually", 19: "Not Usually", 20: "Not Usually",
    21: "Not Usually", 22: "Usually", 23: "Not Usually", 24: "Usually", 25: "Usually",
    26: "Not Usually", 27: "Not Usually", 28: "Not Usually", 29: "Not Usually", 30: "Not Usually",
    31: "Usually", 32: "Usually", 33: "Not Usually", 34: "Usually", 35: "Usually",
    36: "Usually", 37: "Usually", 38: "Usually", 39: "Usually", 40: "Not Usually",
    41: "Usually", 42: "Usually", 43: "Usually", 44: "Not Usually", 45: "Not Usually",
    46: "Not Usually", 47: "Not Usually", 48: "Usually", 49: "Usually", 50: "Usually",
    51: "Usually", 52: "Usually"
}

# ============================================================================
# PASTE YOUR 52 ASSESSMENT QUESTIONS HERE
# ============================================================================
# Instructions:
# 1. Delete the example questions below (lines 29-62)
# 2. Paste all your 52 questions in the exact same format
# 3. Make sure each question has proper indentation (8 spaces or 2 tabs)
# 4. Each question (except the last) needs a comma after the closing }
# 5. The last question (52) should NOT have a comma
# ============================================================================

ASSESSMENT_DATA = [
    {
 "id": 1,
        "title": "Accept Instruction from Others",
        "question": "I willingly accept instruction from others?",
        "verses": [
            {"ref": "Proverbs 1:7-9", "text": "The fear of the LORD is the beginning of knowledge, But fools despise wisdom and instruction. My son, hear the instruction of your father, And do not forsake the law of your mother; For they will be a graceful ornament on your head, And chains about your neck."},
            {"ref": "Proverbs 3:1-4", "text": "My son, do not forget my law, But let your heart keep my commands; For length of days and long life And peace they will add to you. Let not mercy and truth forsake you; Bind them around your neck, Write them on the tablet of your heart, And so find favor and high esteem In the sight of God and man."},
            {"ref": "Proverbs 4:1-4", "text": "Hear, my children, the instruction of a father, And give attention to know understanding; For I give you good doctrine: Do not forsake my law. When I was my father's son, Tender and the only one in the sight of my mother, He also taught me, and said to me: Let your heart retain my words; Keep my commands, and live."},
            {"ref": "Proverbs 10:8", "text": "The wise in heart will receive commands, But a prating fool will fall."},
            {"ref": "Proverbs 13:1", "text": "A wise son heeds his father's instruction, But a scoffer does not listen to rebuke."}
        ],
        "dig_deeper": [
            "Looking at your life, how have you fallen short in the area of accepting instruction from others: your parents, teachers, Godly advisors? How about others that give commands or counsel i.e., your boss, your spouse? Give some examples of how this has hurt you.",
            "Taking things one-step further, how have you sought out (or applied your heart to) instruction and made an effort to listen (open your ears) for instruction?",
            "What do you think stops you from accepting or seeking out instruction willingly?",
            "Specifically, has your lack of accepting instruction affected you in your work? How?",
            "Is there something you could learn (be instructed in) right now that would make you a better employee in your current job or for future career aspirations?",
            "If so, how will you improve in this area?",
            "How can you minister to others that have an issue in this area?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 2,
        "title": "Accept Correction",
        "question": "I gracefully accept correction when it is given?",
        "verses": [
            {"ref": "Proverbs 3:11-12", "text": "My son, do not despise the chastening of the LORD, Nor detest His correction; For whom the LORD loves He corrects, Just as a father the son in whom he delights."},
            {"ref": "Proverbs 10:17", "text": "He who keeps instruction is in the way of life, But he who refuses correction goes astray."},
            {"ref": "Proverbs 12:1", "text": "Whoever loves instruction loves knowledge, But he who hates correction is stupid."},
            {"ref": "Proverbs 15:5", "text": "A fool despises his father's instruction, But he who receives correction is prudent."},
            {"ref": "Proverbs 15:31-32", "text": "The ear that hears the rebukes of life Will abide among the wise. He who disdains instruction despises his own soul, But he who heeds rebuke gets understanding."}
        ],
        "dig_deeper": [
            "After you have received criticism, explain your normal reaction initially and eventually?",
            "How quickly can you recover after hearing criticism? What about self-criticism? Are you hard on yourself?",
            "Can you think of someone that you have witnessed take criticism well? Describe what appealed to you.",
            "Describe some of the negative consequences you've experienced from not accepting correction:",
            "Which verses above will help you when you are tempted to harbor resentment against someone who offers criticism?",
            "How does a person's demeanor/style when offering criticism impact how well you accept the message?",
            "Explain how you would best like to hear criticism?",
            "Do you offer criticism as a friend, in love, with well-chosen words? If not, how can you improve?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 3,
        "title": "Administer Discipline to Others",
        "question": "I readily discipline those that need correction?",
        "verses": [
            {"ref": "Proverbs 13:24", "text": "He who spares his rod hates his son, But he who loves him disciplines him"},
            {"ref": "Proverbs 25:11-12", "text": "A word fitly spoken is like apples of gold In settings of silver. Like an earring of gold and an ornament of fine gold Is a wise rebuker to an obedient ear."},
            {"ref": "Proverbs 27:5-6", "text": "Open rebuke is better Than love carefully concealed. Faithful are the wounds of a friend, But the kisses of an enemy are deceitful."},
            {"ref": "Proverbs 29:15", "text": "The rod and rebuke give wisdom, But a child left to himself brings shame to his mother."}
        ],
        "dig_deeper": [
            "Are you consistent in your administration of discipline or constructive feedback?",
            "Is it hard for you to discipline or correct someone? Why do you think this is?",
            "Are you too harsh in your discipline?",
            "Are your words 'fitful'? Do you feel you can appropriately communicate a correction?",
            "Have you ever given someone a break because you felt sorry for them? How did it turn out?",
            "Can you accept discipline better because you now understand its value and motivation?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 4,
        "title": "Avoid Sinners Enticing You",
        "question": "I am easily misled into wrong behavior(s) by peer pressure?",
        "verses": [
            {"ref": "Proverbs 1:10-19", "text": "My son, if sinners entice you, Do not consent. If they say, 'Come with us, Let us lie in wait to shed blood; Let us lurk secretly for the innocent without cause; Let us swallow them alive like Sheol, We shall find all kinds of precious possessions, We shall fill our houses with spoil; Cast in your lot among us, Let us all have one purse'— My son, do not walk in the way with them, Keep your foot from their path; For their feet run to evil, And they make haste to shed blood."},
            {"ref": "Proverbs 4:14-19", "text": "Do not enter the path of the wicked, And do not walk in the way of evil. Avoid it, do not travel on it; Turn away from it and pass on. For they do not sleep unless they have done evil; And their sleep is taken away unless they make someone fall. For they eat the bread of wickedness, And drink the wine of violence. But the path of the just is like the shining sun, That shines ever brighter unto the perfect day. The way of the wicked is like darkness; They do not know what makes them stumble."},
            {"ref": "Proverbs 12:26", "text": "The righteous should choose his friends carefully, For the way of the wicked leads them astray."},
            {"ref": "Proverbs 13:20", "text": "He who walks with wise men will be wise, But the companion of fools will be destroyed."}
        ],
        "dig_deeper": [
            "Have you ever associated with people that cause you to behave poorly? Give some examples:",
            "Do you continue to associate with people who are enticing you into evil?",
            "Those greedy for gain, fools, violent, talebearers/gossips, flatterers, thieves - do you need to make some changes in your relationships?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 5,
        "title": "Seek Wisdom/Discretion",
        "question": "I really work hard at seeking wisdom/discretion; trying to figure out the right thing to do in difficult situations?",
        "verses": [
            {"ref": "Proverbs 2:1-9", "text": "My son, if you receive my words, And treasure my commands within you, So that you incline your ear to wisdom, And apply your heart to understanding; Yes, if you cry out for discernment, And lift up your voice for understanding, If you seek her as silver, And search for her as for hidden treasures; Then you will understand the fear of the LORD, And find the knowledge of God. For the LORD gives wisdom; From His mouth come knowledge and understanding; He stores up sound wisdom for the upright; He is a shield to those who walk uprightly; He guards the paths of justice, And preserves the way of His saints. Then you will understand righteousness and justice, Equity and every good path."},
            {"ref": "Proverbs 3:13-24", "text": "Happy is the man who finds wisdom, And the man who gains understanding; For her proceeds are better than the profits of silver, And her gain than fine gold. She is more precious than rubies, And all the things you may desire cannot compare with her. Length of days is in her right hand, In her left hand riches and honor. Her ways are ways of pleasantness, And all her paths are peace."},
            {"ref": "Proverbs 4:5-13", "text": "Get wisdom! Get understanding! Do not forget, nor turn away from the words of my mouth. Do not forsake her, and she will preserve you; Love her, and she will keep you. Wisdom is the principal thing; Therefore get wisdom. And in all your getting, get understanding."},
            {"ref": "Proverbs 16:16", "text": "How much better to get wisdom than gold! And to get understanding is to be chosen rather than silver."}
        ],
        "dig_deeper": [
            "Where do you go to as your source of information? Your boss, HR, training classes, peers, spouse, your own understanding?",
            "Have you looked specifically in the Word for the root of the problem and wisdom about the solution?",
            "Think of a difficult situation you've faced at work recently. Would you have reacted differently if you had sought wisdom?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 6,
        "title": "Seek Counsel",
        "question": "I ask others (especially Christians) for counsel and value their insight/opinions?",
        "verses": [
            {"ref": "Proverbs 11:14", "text": "Where there is no counsel, the people fall; But in the multitude of counselors there is safety."},
            {"ref": "Proverbs 15:22", "text": "Without counsel, plans go awry, But in the multitude of counselors they are established."},
            {"ref": "Proverbs 20:5", "text": "Counsel in the heart of man is like deep water, But a man of understanding will draw it out."},
            {"ref": "Proverbs 20:18", "text": "Plans are established by counsel; By wise counsel wage war."},
            {"ref": "Proverbs 24:6", "text": "For by wise counsel you will wage your own war, And in a multitude of counselors there is safety."}
        ],
        "dig_deeper": [
            "Do you value and seek out the opinions of many counselors?",
            "How does being shy, proud or insecure affect your willingness to seek advice?",
            "Can you remember a situation where you acted alone and you wish you had sought counsel?",
            "How will you balance seeking input from many versus too much input from the wrong individuals?",
            "Do you sincerely seek wise counsel, or just go through the motions?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 7,
        "title": "Keep the Lord's Commands",
        "question": "I try to follow the 10 Commandments?",
        "verses": [
            {"ref": "Proverbs 13:13-15", "text": "He who despises the word will be destroyed, But he who fears the commandment will be rewarded. The law of the wise is a fountain of life, To turn one away from the snares of death. Good understanding gains favor, But the way of the unfaithful is hard."},
            {"ref": "Proverbs 14:26-27", "text": "In the fear of the LORD there is strong confidence, And His children will have a place of refuge. The fear of the LORD is a fountain of life, To turn one away from the snares of death."},
            {"ref": "Proverbs 19:16", "text": "He who keeps the commandment keeps his soul, But he who is careless of his ways will die."},
            {"ref": "Proverbs 28:4", "text": "Those who forsake the law praise the wicked, But such as keep the law contend with them."},
            {"ref": "Proverbs 29:18", "text": "Where there is no revelation, the people cast off restraint; But happy is he who keeps the law."}
        ],
        "dig_deeper": [
            "Review the 10 Commandments (Exodus 20). Do you truly believe in them, trust them, and revere the Lord enough to try to keep them?",
            "How can you remind yourself of the commandments and hold yourself accountable?",
            "If you cannot live up to the commandments, do you believe that all things are possible through Christ?",
            "Does this release you from the responsibility to live lawfully? (See Romans 6:15.)",
            "Which list of characteristics best describes your life - the faithful or unfaithful? Why?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 8,
        "title": "Trust in the Lord",
        "question": "I demonstrate that I trust in the Lord?",
        "verses": [
            {"ref": "Proverbs 3:5-6", "text": "Trust in the LORD with all your heart, And lean not on your own understanding; In all your ways acknowledge Him, And He shall direct your paths."},
            {"ref": "Proverbs 3:25-26", "text": "Do not be afraid of sudden terror, Nor of trouble from the wicked when it comes; For the LORD will be your confidence, And will keep your foot from being caught."},
            {"ref": "Proverbs 16:9", "text": "A man's heart plans his way, But the LORD directs his steps."},
            {"ref": "Proverbs 19:21", "text": "There are many plans in a man's heart, Nevertheless the LORD's counsel—that will stand."},
            {"ref": "Proverbs 29:25", "text": "The fear of man brings a snare, But whoever trusts in the LORD shall be safe."}
        ],
        "dig_deeper": [
            "Do you exhibit confidence that the Lord is in control of your work and your life situations?",
            "What specifically can you do to demonstrate that trust and exhibit that confidence more? (perhaps give up some control, delegate, release yourself from your insatiable drive for success?)",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 9,
        "title": "Don't Be Wise in Your Own Eyes",
        "question": "I give others the impression that I know-it-all (am wise in my own eyes)?",
        "verses": [
            {"ref": "Proverbs 3:7-8", "text": "Do not be wise in your own eyes; Fear the LORD and depart from evil. It will be health to your flesh, And strength to your bones."},
            {"ref": "Proverbs 12:15", "text": "The way of a fool is right in his own eyes, But he who heeds counsel is wise."},
            {"ref": "Proverbs 16:2", "text": "All the ways of a man are pure in his own eyes, But the LORD weighs the spirits."},
            {"ref": "Proverbs 26:12", "text": "Do you see a man wise in his own eyes? There is more hope for a fool than for him."},
            {"ref": "Proverbs 28:26", "text": "He who trusts in his own heart is a fool, But whoever walks wisely will be delivered."}
        ],
        "dig_deeper": [
            "What, in your opinion, is the difference between being respected for your knowledge and being perceived as a 'know-it-all'?",
            "How could someone who is perceived as a 'know-it-all' or 'wise or pure in their own eyes' change other's impression of him/her?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 10,
        "title": "Don't Withhold Good When Due",
        "question": "I give credit to people, when credit is due?",
        "verses": [
            {"ref": "Proverbs 3:27-28", "text": "Do not withhold good from those to whom it is due, When it is in the power of your hand to do so. Do not say to your neighbor, 'Go, and come back, And tomorrow I will give it,' When you have it with you."}
        ],
        "dig_deeper": [
            "Are you fair in your payment of wages, return of debts owed, returning things borrowed, keeping of promises, providing necessary information and giving credit when credit is due? If not, where do you fall short?",
            "Do you feel you have a debt of praise to an employee or boss that has done a job well?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 11,
        "title": "Don't Be in Debt",
        "question": "I manage my finances well; avoid debt or pledging for others irresponsibly?",
        "verses": [
            {"ref": "Proverbs 22:7", "text": "The rich rules over the poor, And the borrower is servant to the lender."},
            {"ref": "Proverbs 22:26-27", "text": "Do not be one of those who shakes hands in a pledge, One of those who is surety for debts; If you have nothing with which to pay, Why should he take away your bed from under you?"}
        ],
        "dig_deeper": [
            "How can managing your finances well make you a better witness to others at work?",
            "How can managing your finances well make you a better employee/employer?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 12,
        "title": "Don't Devise Evil or Take Advantage",
        "question": "I plot against others (think about/plan to do something harmful to him or her)?",
        "verses": [
            {"ref": "Proverbs 3:29", "text": "Do not devise evil against your neighbor, For he dwells by you for safety's sake."},
            {"ref": "Proverbs 14:22", "text": "Do they not go astray who devise evil? But mercy and truth belong to those who devise good."},
            {"ref": "Proverbs 24:15-16", "text": "Do not lie in wait, O wicked man, against the dwelling of the righteous; Do not plunder his resting place; For a righteous man may fall seven times And rise again, But the wicked shall fall by calamity."}
        ],
        "dig_deeper": [
            "Have you ever acted to plot against someone? What motivated you: anger, revenge or pride?",
            "Did this approach work out well for you?",
            "Does it give you confidence not to worry about those that plot against you, knowing the righteous will rise again?",
            "If either acting to plot evil or worrying about those that plot against you is an issue, summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 13,
        "title": "Don't Strive",
        "question": "I start quarrels or easily get involved in quarrels?",
        "verses": [
            {"ref": "Proverbs 3:30", "text": "Do not strive with a man without cause, If he has done you no harm."},
            {"ref": "Proverbs 17:9", "text": "He who covers a transgression seeks love, But he who repeats a matter separates friends."},
            {"ref": "Proverbs 20:3", "text": "It is honorable for a man to stop striving, Since any fool can start a quarrel."},
            {"ref": "Proverbs 26:20-21", "text": "Where there is no wood, the fire goes out; And where there is no talebearer, strife ceases. As charcoal is to burning coals, and wood to fire, So is a contentious man to kindle strife."}
        ],
        "dig_deeper": [
            "Does conflict make you uncomfortable or would you say, 'bring it on'? Why do you think that is?",
            "What makes you get involved in arguments (your own or other's)?",
            "Why do you feel the need to stand your ground in an argument?",
            "If you backed down from an argument, how would you be perceived?",
            "Have you ever used 'casting lots' to end a quarrel? Would you trust the Lord to direct the outcome?",
            "What specific things can you do to avoid strife?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 14,
        "title": "Don't Have a Perverse Heart",
        "question": "I often feel like my heart just isn't in the right place (filled with perverse thoughts; prideful or stubborn feelings, wicked intent, etc.)?",
        "verses": [
            {"ref": "Proverbs 11:20", "text": "Those who are of a perverse heart are an abomination to the LORD, But the blameless in their ways are His delight."},
            {"ref": "Proverbs 12:8", "text": "A man will be commended according to his wisdom, But he who is of a perverse heart will be despised."},
            {"ref": "Proverbs 17:3", "text": "The refining pot is for silver and the furnace for gold, But the LORD tests the hearts."},
            {"ref": "Proverbs 21:4", "text": "A haughty look, a proud heart, And the plowing of the wicked are sin."},
            {"ref": "Proverbs 28:14", "text": "Happy is the man who is always reverent, But he who hardens his heart will fall into calamity."}
        ],
        "dig_deeper": [
            "Where does this attitude come from? Can you identify the root of the issue?",
            "What is the opposite of a perverse heart (see verses above)?",
            "What can you do to overcome this attitude?",
            "If you think your boss/coworker has this issue, what makes you think so? What behaviors lead you to believe this?",
            "How does this impact your job?",
            "What has been your response?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 15,
        "title": "Be an Excellent Wife",
        "question": "I'd say I'm an excellent wife/spouse?",
        "verses": [
            {"ref": "Proverbs 12:4", "text": "An excellent wife is the crown of her husband, But she who causes shame is like rottenness in his bones."},
            {"ref": "Proverbs 18:22", "text": "He who finds a wife finds a good thing, And obtains favor from the LORD."},
            {"ref": "Proverbs 19:14", "text": "Houses and riches are an inheritance from fathers, But a prudent wife is from the LORD."},
            {"ref": "Proverbs 31:10-31", "text": "Who can find a virtuous wife? For her worth is far above rubies. The heart of her husband safely trusts her; So he will have no lack of gain. She does him good and not evil All the days of her life. She seeks wool and flax, And willingly works with her hands... Strength and honor are her clothing; She shall rejoice in time to come. She opens her mouth with wisdom, And on her tongue is the law of kindness."}
        ],
        "dig_deeper": [
            "Have you ever considered the value you have as an excellent vs. a shameful wife/spouse? Describe how you have added value to your spouse.",
            "How can your excellence as a wife/spouse help those beyond your spouse: your household, your work, and your community?",
            "How can (has) being a contentious wife be(en) a detriment to your spouse?",
            "Where does that ability to be excellent come from (you or the Lord)?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 16,
        "title": "Avoid Anger",
        "question": "I let anger build up inside or boil over into outbursts?",
        "verses": [
            {"ref": "Proverbs 12:16", "text": "A fool's wrath is known at once, But a prudent man covers shame."},
            {"ref": "Proverbs 14:29", "text": "He who is slow to wrath has great understanding, But he who is impulsive exalts folly."},
            {"ref": "Proverbs 15:18", "text": "A wrathful man stirs up strife, But he who is slow to anger allays contention."},
            {"ref": "Proverbs 16:32", "text": "He who is slow to anger is better than the mighty, And he who rules his spirit than he who takes a city."},
            {"ref": "Proverbs 19:11", "text": "The discretion of a man makes him slow to anger, And his glory is to overlook a transgression."},
            {"ref": "Proverbs 29:22", "text": "An angry man stirs up strife, And a furious man abounds in transgression."}
        ],
        "dig_deeper": [
            "Has your anger ever made you look foolish?",
            "Has your anger ever hurt someone, irritated or made someone mad at you?",
            "Have you ever let a friend's anger make you angry?",
            "Why is your heart bitter/contentious?",
            "What do the verses above teach you that you can do to control your anger?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 17,
        "title": "Avoid Anxiety",
        "question": "I would describe myself as overly anxious/easily depressed?",
        "verses": [
            {"ref": "Proverbs 12:25", "text": "Anxiety in the heart of man causes depression, But a good word makes it glad."}
        ],
        "dig_deeper": [
            "Who do you need 'a good word' from? Will you tell them that?",
            "Do you give 'good words'? Whom can you give 'a good word' to?",
            "Can you find other verses about worry and anxiety throughout the Bible? (Try: Matthew 6:25, 27, 28, 31, 34; Matthew 10:19; Luke 12:11, 22, 25.)",
            "How do you deal with your anxiety? What helps put things in perspective for you?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 18,
        "title": "Don't Abuse Alcohol",
        "question": "I allow substance abuse to affect my life or the life of others?",
        "verses": [
            {"ref": "Proverbs 20:1", "text": "Wine is a mocker, Strong drink is a brawler, And whoever is led astray by it is not wise."},
            {"ref": "Proverbs 21:17", "text": "He who loves pleasure will be a poor man; He who loves wine and oil will not be rich."},
            {"ref": "Proverbs 23:29-35", "text": "Who has woe? Who has sorrow? Who has contentions? Who has complaints? Who has wounds without cause? Who has redness of eyes? Those who linger long at the wine, Those who go in search of mixed wine. Do not look on the wine when it is red, When it sparkles in the cup, When it swirls around smoothly; At the last it bites like a serpent, And stings like a viper."},
            {"ref": "Proverbs 31:4-7", "text": "It is not for kings to drink wine, Nor for princes intoxicating drink; Lest they drink and forget the law, And pervert the justice of all the afflicted."}
        ],
        "dig_deeper": [
            "How has substance abuse affected your work or personal life?",
            "What steps can you take to avoid or address substance abuse issues?",
            "How can you help others who struggle in this area?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 19,
        "title": "Don't Envy the Oppressors",
        "question": "I envy (or imitate) those who get ahead, even if by dishonest means?",
        "verses": [
            {"ref": "Proverbs 3:31-33", "text": "Do not envy the oppressor, And choose none of his ways; For the perverse person is an abomination to the LORD, But His secret counsel is with the upright. The curse of the LORD is on the house of the wicked, But He blesses the home of the just."},
            {"ref": "Proverbs 24:1-2", "text": "Do not be envious of evil men, Nor desire to be with them; For their heart devises violence, And their lips talk of troublemaking."},
            {"ref": "Proverbs 24:19-20", "text": "Do not fret because of evildoers, Nor be envious of the wicked; For there will be no prospect for the evil man; The lamp of the wicked will be put out."}
        ],
        "dig_deeper": [
            "Do these verses convince you of your need to put those thoughts of envy behind you? Why or why not?",
            "Have you ever witnessed the 'fall' of someone who got ahead by dishonest means or by oppressing others?",
            "What do you need to do to get beyond this thought-pattern of envy/coveting?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 20,
        "title": "Don't Envy/Be Jealous",
        "question": "I am jealous of someone or something they have?",
        "verses": [
            {"ref": "Proverbs 14:30", "text": "A sound heart is life to the body, But envy is rottenness to the bones."},
            {"ref": "Proverbs 27:4", "text": "Wrath is cruel and anger a torrent, But who is able to stand before jealousy?"}
        ],
        "dig_deeper": [
            "Have you ever thought that being jealous of someone is worse than being angry with him or her?",
            "Have you ever been the object of someone else's jealousy? How did that make you feel or impact your life?",
            "If you are the object of someone's jealousy, how will you deal with this?",
            "Are you jealous of someone and need to release them? If so, who and how will you do this?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 21,
        "title": "Don't Reward Evil",
        "question": "I've cheered on someone who did something bad or made fun of someone who was doing something good?",
        "verses": [
            {"ref": "Proverbs 17:13", "text": "Whoever rewards evil for good, Evil will not depart from his house."},
            {"ref": "Proverbs 17:15", "text": "He who justifies the wicked, and he who condemns the just, Both of them alike are an abomination to the LORD."},
            {"ref": "Proverbs 17:26", "text": "Also, to punish the righteous is not good, Nor to strike princes for their uprightness."},
            {"ref": "Proverbs 18:5", "text": "It is not good to show partiality to the wicked, Or to overthrow the righteous in judgment."}
        ],
        "dig_deeper": [
            "What does the Lord think of those that reward evil, justify the wicked, show them partiality or punish the righteous?",
            "How can participating in this behavior affect us if we are supervisors? What message does it send?",
            "If your boss struggles in this area, do you think they realize that they are giving this impression?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 22,
        "title": "Be Humble",
        "question": "I am humble?",
        "verses": [
            {"ref": "Proverbs 11:2", "text": "When pride comes, then comes shame; But with the humble is wisdom."},
            {"ref": "Proverbs 13:10", "text": "By pride comes nothing but strife, But with the well-advised is wisdom."},
            {"ref": "Proverbs 15:33", "text": "The fear of the LORD is the instruction of wisdom, And before honor is humility."},
            {"ref": "Proverbs 16:18-19", "text": "Pride goes before destruction, And a haughty spirit before a fall. Better to be of a humble spirit with the lowly, Than to divide the spoil with the proud."},
            {"ref": "Proverbs 18:12", "text": "Before destruction the heart of a man is haughty, And before honor is humility."},
            {"ref": "Proverbs 22:4", "text": "By humility and the fear of the LORD Are riches and honor and life."},
            {"ref": "Proverbs 29:23", "text": "A man's pride will bring him low, But the humble in spirit will retain honor."}
        ],
        "dig_deeper": [
            "How do the verses above contradict the worldly wisdom that to have success in your career you have to be aggressively promoting yourself?",
            "Can you be humble yet still get noticed, get ahead? Do you think this advice is misguided or will it work?",
            "How much humility will it take to admit to co-workers, employees, your boss, that you have been wrong?",
            "Can you prepare a statement that communicates your admission of failure(s) and what you are working on improving?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 23,
        "title": "Put Away A Deceitful Mouth",
        "question": "I lie or act deceitfully, tell tales, am slanderous, or falsely flatter others?",
        "verses": [
            {"ref": "Proverbs 4:24", "text": "Put away from you a deceitful mouth, And put perverse lips far from you."},
            {"ref": "Proverbs 10:18-19", "text": "Whoever hides hatred has lying lips, And whoever spreads slander is a fool. In the multitude of words sin is not lacking, But he who restrains his lips is wise."},
            {"ref": "Proverbs 12:17-19", "text": "He who speaks truth declares righteousness, But a false witness, deceit. There is one who speaks like the piercings of a sword, But the tongue of the wise promotes health. The truthful lip shall be established forever, But a lying tongue is but for a moment."},
            {"ref": "Proverbs 12:22", "text": "Lying lips are an abomination to the LORD, But those who deal truthfully are His delight."},
            {"ref": "Proverbs 26:28", "text": "A lying tongue hates those who are crushed by it, And a flattering mouth works ruin."}
        ],
        "dig_deeper": [
            "Do you have more of a problem with speaking truthfully (versus deceitfully; telling lies or flattering falsely), speaking hypocritically, speaking positively (versus negatively) or perhaps holding your tongue when you shouldn't speak?",
            "Go back and underline the verses/passages above that relate to the issue you struggle with the most.",
            "How has this contributed to your 'work-life' issues?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 24,
        "title": "Let Your Ways Be Established",
        "question": "I am known for being unwavering in my principles (having integrity)?",
        "verses": [
            {"ref": "Proverbs 4:25-27", "text": "Let your eyes look straight ahead, And your eyelids look right before you. Ponder the path of your feet, And let all your ways be established. Do not turn to the right or the left; Remove your foot from evil."},
            {"ref": "Proverbs 10:9", "text": "He who walks with integrity walks securely, But he who perverts his ways will become known."},
            {"ref": "Proverbs 11:3", "text": "The integrity of the upright will guide them, But the perversity of the unfaithful will destroy them."},
            {"ref": "Proverbs 20:7", "text": "The righteous man walks in his integrity; His children are blessed after him."},
            {"ref": "Proverbs 22:1", "text": "A good name is to be chosen rather than great riches, Loving favor rather than silver and gold."},
            {"ref": "Proverbs 28:6", "text": "Better is the poor who walks in his integrity Than one perverse in his ways, though he be rich."}
        ],
        "dig_deeper": [
            "Do the adjectives from the verses above (unwavering, considered, upright, of good reputation, excellent, unfaltering, controlled, satisfied, having integrity, principled, rooted) make you want to be known as being established in your ways?",
            "How hard is it to hold steadfast to your values in your workplace?",
            "Are you ever chided for holding firm to your values?",
            "If you are constantly being challenged by the ethics of the company, is this the right place for you?",
            "Do you respect others when they hold their ground or are predictable in their response?",
            "Does your mood often affect your response, causing others to perceive you 'turn to the right or the left'?",
            "Do you have 'situational ethics', that is, have different values depending on the situation or who is involved?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 25,
        "title": "Avoid Immoral Women",
        "question": "I exercise self-control over my sexual temptations?",
        "verses": [
            {"ref": "Proverbs 2:16-19", "text": "To deliver you from the immoral woman, From the seductress who flatters with her words, Who forsakes the companion of her youth, And forgets the covenant of her God. For her house leads down to death, And her paths to the dead; None who go to her return, Nor do they regain the paths of life—"},
            {"ref": "Proverbs 5:3-11", "text": "For the lips of an immoral woman drip honey, And her mouth is smoother than oil; But in the end she is bitter as wormwood, Sharp as a two-edged sword. Her feet go down to death, Her steps lay hold of hell. Lest you ponder her path of life—Her ways are unstable; You do not know them."},
            {"ref": "Proverbs 6:24-32", "text": "To keep you from the evil woman, From the flattering tongue of a seductress. Do not lust after her beauty in your heart, Nor let her allure you with her eyelids. For by means of a harlot A man is reduced to a crust of bread; And an adulteress will prey upon his precious life. Whoever commits adultery with a woman lacks understanding; He who does so destroys his own soul."},
            {"ref": "Proverbs 7:6-27", "text": "For at the window of my house I looked through my lattice, And saw among the simple, I perceived among the youths, A young man devoid of understanding, Passing along the street near her corner... Her house is the way to hell, Descending to the chambers of death."}
        ],
        "dig_deeper": [
            "How do these verses drive home the point that our temptations are bound to destroy us?",
            "Is your work environment a source of sexual temptation?",
            "What helps you deal with temptations in this area?",
            "Do you need to remove yourself from temptations or perhaps address/confront a sexually charged environment at work?",
            "Do you know of an instance where sexual temptation at work has caused an issue? Was it handled well?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 26,
        "title": "Don't Misplace Your Confidence",
        "question": "I often misjudge the faithfulness/character of others?",
        "verses": [
            {"ref": "Proverbs 25:19", "text": "Confidence in an unfaithful man in time of trouble Is like a bad tooth and a foot out of joint."},
            {"ref": "Proverbs 26:6-11", "text": "He who sends a message by the hand of a fool Cuts off his own feet and drinks violence. Like the legs of the lame that hang limp Is a proverb in the mouth of fools. Like one who binds a stone in a sling Is he who gives honor to a fool. As a dog returns to his own vomit, So a fool repeats his folly."}
        ],
        "dig_deeper": [
            "Have you been hurt by misjudging another's character/reliability?",
            "Have you put your confidence in a person that has proved unfaithful, or wasted your words of wisdom on a fool? Give an example. What did you learn?",
            "Are you surprised to see that the Bible actually portrays this as a character fault in you, the one placing the confidence in the other person?",
            "Can you think of examples in Christ's life where he was hurt by an unfaithful or foolish man?",
            "How will you choose to respond to the unfaithful or fools? Are they still redeemable?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 27,
        "title": "Avoid Folly",
        "question": "I allow my decisions, behavior or attitude to make me appear foolish/unwise?",
        "verses": [
            {"ref": "Proverbs 12:23", "text": "A prudent man conceals knowledge, But the heart of fools proclaims foolishness."},
            {"ref": "Proverbs 14:8-9", "text": "The wisdom of the prudent is to understand his way, But the folly of fools is deceit. Fools mock at sin, But among the upright there is favor."},
            {"ref": "Proverbs 14:16-18", "text": "A wise man fears and departs from evil, But a fool rages and is self-confident. A quick-tempered man acts foolishly, And a man of wicked intentions is hated. The simple inherit folly, But the prudent are crowned with knowledge."},
            {"ref": "Proverbs 17:12", "text": "Let a man meet a bear robbed of her cubs, Rather than a fool in his folly."},
            {"ref": "Proverbs 18:2", "text": "A fool has no delight in understanding, But in expressing his own heart."},
            {"ref": "Proverbs 26:4-5", "text": "Do not answer a fool according to his folly, Lest you also be like him. Answer a fool according to his folly, Lest he be wise in his own eyes."}
        ],
        "dig_deeper": [
            "The verses above teach us that the foolish: sin, don't accept instruction, proclaim their foolishness, deceive, mock sin, are self-confident, despise their mother, lack discernment, have no delight in understanding, squander what they have, don't foresee evil, are punished. Circle those bullets that describe you.",
            "How can you avoid appearing foolish?",
            "What can we learn from Proverbs 26:4-5 about how to deal with a fool?",
            "If you have a reputation for acting foolishly, how will you change this reputation?",
            "How will you handle foolishness in others?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 28,
        "title": "Don't Pledge Surety",
        "question": "I find myself putting my neck on the line for those who don't do what they said they would after all? (Taken advantage of)",
        "verses": [
            {"ref": "Proverbs 6:1-5", "text": "My son, if you become surety for your friend, If you have shaken hands in pledge for a stranger, You are snared by the words of your mouth; You are taken by the words of your mouth. So do this, my son, and deliver yourself; For you have come into the hand of your friend: Go and humble yourself; Plead with your friend. Give no sleep to your eyes, Nor slumber to your eyelids. Deliver yourself like a gazelle from the hand of the hunter."},
            {"ref": "Proverbs 11:15", "text": "He who is surety for a stranger will suffer, But one who hates being surety is secure."},
            {"ref": "Proverbs 17:18", "text": "A man devoid of understanding shakes hands in a pledge, And becomes surety for his friend."}
        ],
        "dig_deeper": [
            "Describe an instance where you put your neck on the line for someone and been burned.",
            "As Christians, we are called to be generous and giving but are we called to be taken advantage of?",
            "If you have already put your neck on the line for someone and are regretting your decision, based on the biblical instruction above, what will you do?",
            "Should we take into account the character of those we partner with or vouch for? How can that affect us?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 29,
        "title": "Don't Be a Sluggard/Lazy",
        "question": "I'm lazy about getting my work done?",
        "verses": [
            {"ref": "Proverbs 6:6-11", "text": "Go to the ant, you sluggard! Consider her ways and be wise, Which, having no captain, Overseer or ruler, Provides her supplies in the summer, And gathers her food in the harvest. How long will you slumber, O sluggard? When will you rise from your sleep? A little sleep, a little slumber, A little folding of the hands to sleep—So shall your poverty come on you like a prowler."},
            {"ref": "Proverbs 10:4-5", "text": "He who has a slack hand becomes poor, But the hand of the diligent makes rich. He who gathers in summer is a wise son; He who sleeps in harvest is a son who causes shame."},
            {"ref": "Proverbs 12:24", "text": "The hand of the diligent will rule, But the lazy man will be put to forced labor."},
            {"ref": "Proverbs 13:4", "text": "The soul of a lazy man desires, and has nothing; But the soul of the diligent shall be made rich."},
            {"ref": "Proverbs 20:4", "text": "The lazy man will not plow because of winter; He will beg during harvest and have nothing."},
            {"ref": "Proverbs 26:13-16", "text": "The lazy man says, 'There is a lion in the road! A fierce lion is in the streets!' As a door turns on its hinges, So does the lazy man on his bed."}
        ],
        "dig_deeper": [
            "Who considers you lazy?",
            "What gives them that impression?",
            "How has laziness affected your 'work-life'?",
            "Do you have a plan for your household? Are you laying up supplies, working when you should, knowing the state of and attending to your business?",
            "Are you being diligent or frivolous?",
            "Where is the line between being lazy and working too hard (being a workaholic)?",
            "What is the best balance for you? What do you need to do differently to achieve this?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 30,
        "title": "Don't Let a Perverse Mouth Sow Discord",
        "question": "I say things that stir up a controversy (i.e., spread rumors, speak falsely, wickedly)?",
        "verses": [
            {"ref": "Proverbs 6:12-19", "text": "A worthless person, a wicked man, Walks with a perverse mouth; He winks with his eyes, He shuffles his feet, He points with his fingers; Perversity is in his heart, He devises evil continually, He sows discord. Therefore his calamity shall come suddenly; Suddenly he shall be broken without remedy. These six things the LORD hates, Yes, seven are an abomination to Him: A proud look, A lying tongue, Hands that shed innocent blood, A heart that devises wicked plans, Feet that are swift in running to evil, A false witness who speaks lies, And one who sows discord among brethren."},
            {"ref": "Proverbs 16:27-28", "text": "An ungodly man digs up evil, And it is on his lips like a burning fire. A perverse man sows strife, And a whisperer separates the best of friends."},
            {"ref": "Proverbs 17:4", "text": "An evildoer gives heed to false lips; A liar listens eagerly to a spiteful tongue."}
        ],
        "dig_deeper": [
            "Is your speech filled with violence, perversion, evil, not acceptable, spreading rumors and bearing false witness? If so, how has it affected you or those around you?",
            "Why do you think you behave in this manner?",
            "If your speech stirs up controversy or is perverse, what does it say about the state of your heart?",
            "What can you do to change your speech, cleanse your heart?",
            "Who can you trust to hold you accountable as you attempt to change?",
            "Can you let someone know how their speech is affecting you and offer to help hold them accountable?",
            "Are you a good listener?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 31,
        "title": "Avoid Wickedness/Seek Righteousness",
        "question": "I want to be known for my righteousness?",
        "verses": [
            {"ref": "Proverbs 10:2-3", "text": "Treasures of wickedness profit nothing, But righteousness delivers from death. The LORD will not allow the righteous soul to famish, But He casts away the desire of the wicked."},
            {"ref": "Proverbs 10:16", "text": "The labor of the righteous leads to life, The wages of the wicked to sin."},
            {"ref": "Proverbs 11:5-6", "text": "The righteousness of the blameless will direct his way aright, But the wicked will fall by his own wickedness. The righteousness of the upright will deliver them, But the unfaithful will be caught by their lust."},
            {"ref": "Proverbs 14:34", "text": "Righteousness exalts a nation, But sin is a reproach to any people."},
            {"ref": "Proverbs 21:3", "text": "To do righteousness and justice Is more acceptable to the LORD than sacrifice."},
            {"ref": "Proverbs 28:1", "text": "The wicked flee when no one pursues, But the righteous are bold as a lion."}
        ],
        "dig_deeper": [
            "Did you think the term 'righteousness' had a bad connotation? Did it conjure up the idea of a person who is 'self-righteous' or 'holier than thou'? Why do you think this is?",
            "Where should your righteousness come from? (Hint: Matthew 6)",
            "Underline the positive consequences of righteousness in the passages above.",
            "What causes you/others to behave wickedly (do what you know is not right)?",
            "Even though it is not possible to be righteous without God, is it something to aspire to or is it futile?",
            "By reading these verses, could you be encouraged, even if you are dealing with a wicked co-worker, supervisor or employee? How?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 32,
        "title": "Store Knowledge",
        "question": "I've been trying to learn more, getting training, looking things up, and gaining/storing knowledge?",
        "verses": [
            {"ref": "Proverbs 10:14", "text": "Wise people store up knowledge, But the mouth of the foolish is near destruction."},
            {"ref": "Proverbs 15:14", "text": "The heart of him who has understanding seeks knowledge, But the mouth of fools feeds on foolishness."},
            {"ref": "Proverbs 18:15", "text": "The heart of the prudent acquires knowledge, And the ear of the wise seeks knowledge."},
            {"ref": "Proverbs 28:2", "text": "Because of the transgression of a land, many are its princes; But by a man of understanding and knowledge Right will be prolonged."}
        ],
        "dig_deeper": [
            "Could storing up more knowledge help you become wiser, advance your career?",
            "What type of knowledge do you need to seek?",
            "By gaining understanding and knowledge you could not only gain wisdom but also be able to help 'prolong what is right.' What does this mean to you?",
            "What is stopping you from growing in knowledge: fear, impatience, stubbornness, pride, anger, embarrassment, or incompetence? What can you do to overcome this?",
            "What will you do to expand your knowledge?",
            "In your pursuit of knowledge remember: What good is knowledge without love? How will you remind yourself of this?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 33,
        "title": "Don't Use Dishonest Means",
        "question": "I use dishonest means to accomplish my goals?",
        "verses": [
            {"ref": "Proverbs 11:1", "text": "Dishonest scales are an abomination to the LORD, But a just weight is His delight."},
            {"ref": "Proverbs 11:18", "text": "The wicked man does deceptive work, But he who sows righteousness will have a sure reward."},
            {"ref": "Proverbs 13:11", "text": "Wealth gained by dishonesty will be diminished, But he who gathers by labor will increase."},
            {"ref": "Proverbs 16:8", "text": "Better is a little with righteousness, Than vast revenues without justice."},
            {"ref": "Proverbs 20:17", "text": "Bread gained by deceit is sweet to a man, But afterward his mouth will be filled with gravel."},
            {"ref": "Proverbs 20:23", "text": "Diverse weights are an abomination to the LORD, And dishonest scales are not good."}
        ],
        "dig_deeper": [
            "If you've been deceptive, used dishonest scales or have been bribed or otherwise gained without justice, how can you make it right?",
            "If you believe others in the workplace are getting ahead by dishonest means, what can you do for them?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 34,
        "title": "Fairly Apply Justice",
        "question": "I've been able to be fair and impartial when judging others?",
        "verses": [
            {"ref": "Proverbs 16:10-11", "text": "Divination is on the lips of the king; His mouth must not transgress in judgment."},
            {"ref": "Proverbs 18:13", "text": "He who answers a matter before he hears it, It is folly and shame to him."},
            {"ref": "Proverbs 18:17", "text": "The first one to plead his cause seems right, Until his neighbor comes and examines him."},
            {"ref": "Proverbs 21:15", "text": "It is a joy for the just to do justice, But destruction will come to the workers of iniquity."},
            {"ref": "Proverbs 24:23-26", "text": "These things also belong to the wise: It is not good to show partiality in judgment. He who says to the wicked, 'You are righteous,' Him the people will curse; Nations will abhor him. But those who rebuke the wicked will have delight, And a good blessing will come upon them."},
            {"ref": "Proverbs 29:14", "text": "The king who judges the poor with truth, His throne will be established forever."}
        ],
        "dig_deeper": [
            "Have you shown partiality in judgment, not listened well enough to make good judgments, been easily misled with lies or not stood up for those that needed their cases plead? How can you make it right?",
            "Are you prepared to admit your failure and start new making sure you heed the advice in the verses above? How?",
            "If you feel someone has been unfair in their judgment, what is the cause?",
            "How will you let them know how this is affecting you?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 35,
        "title": "Hold Your Tongue",
        "question": "I'm able to hold my tongue; not saying something I regret or speak without thinking?",
        "verses": [
            {"ref": "Proverbs 11:13", "text": "A talebearer reveals secrets, But he who is of a faithful spirit conceals a matter."},
            {"ref": "Proverbs 13:3", "text": "He who guards his mouth preserves his life, But he who opens wide his lips shall have destruction."},
            {"ref": "Proverbs 15:1-2", "text": "A soft answer turns away wrath, But a harsh word stirs up anger. The tongue of the wise uses knowledge rightly, But the mouth of fools pours forth foolishness."},
            {"ref": "Proverbs 17:27-28", "text": "He who has knowledge spares his words, And a man of understanding is of a calm spirit. Even a fool is counted wise when he holds his peace; When he shuts his lips, he is considered perceptive."},
            {"ref": "Proverbs 21:23", "text": "Whoever guards his mouth and tongue Keeps his soul from troubles."},
            {"ref": "Proverbs 29:11", "text": "A fool vents all his feelings, But a wise man holds them back."}
        ],
        "dig_deeper": [
            "Have you ever really considered what a powerful tool or weapon the tongue can be?",
            "Go back and underline the verses that most apply to the issue you have with your tongue; are you backbiting, a gossip, speak too quickly, talk too much, etc.",
            "Describe a time when you should have held your tongue and didn't. What happened?",
            "From the verses above, list the benefits and traits associated with those that 'hold their tongue' or speak wisely:",
            "From the verses above, list the problems and traits associated with those that don't 'hold their tongue' or speak wisely:",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 36,
        "title": "Show Graciousness/Kindness",
        "question": "I demonstrate grace and kindness?",
        "verses": [
            {"ref": "Proverbs 11:16", "text": "A gracious woman retains honor, But ruthless men retain riches."},
            {"ref": "Proverbs 19:22", "text": "What is desired in a man is kindness, And a poor man is better than a liar."},
            {"ref": "Proverbs 20:28", "text": "Mercy and truth preserve the king, And by lovingkindness he upholds his throne."},
            {"ref": "Proverbs 21:13", "text": "Whoever shuts his ears to the cry of the poor Will also cry himself and not be heard."},
            {"ref": "Proverbs 22:11", "text": "He who loves purity of heart And has grace on his lips, The king will be his friend."}
        ],
        "dig_deeper": [
            "Have you considered that loving-kindness, and grace will bring honor, uphold your position, create loyalty and bring you favor?",
            "What are the opposite consequences?",
            "Would you rather have honor or riches?",
            "Is pampering different than being kind and gracious? Will it cause a servant to be insolent?",
            "If you aren't sure others would describe you as kind, what can you do to change your image?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 37,
        "title": "Be Merciful",
        "question": "I'm willing to forgive or show mercy to others?",
        "verses": [
            {"ref": "Proverbs 11:17", "text": "The merciful man does good for his own soul, But he who is cruel troubles his own flesh."},
            {"ref": "Proverbs 14:21", "text": "He who despises his neighbor sins; But he who has mercy on the poor, happy is he."},
            {"ref": "Proverbs 14:31", "text": "He who oppresses the poor reproaches his Maker, But he who honors Him has mercy on the needy."},
            {"ref": "Proverbs 19:17", "text": "He who has pity on the poor lends to the LORD, And He will pay back what he has given."},
            {"ref": "Proverbs 21:21", "text": "He who follows righteousness and mercy Finds life, righteousness, and honor."},
            {"ref": "Proverbs 28:13", "text": "He who covers his sins will not prosper, But whoever confesses and forsakes them will have mercy."}
        ],
        "dig_deeper": [
            "The verses above reflect that the opposite of being merciful is being cruel or oppressive. Had you considered that?",
            "Does this change your mind about how willing you are to be merciful (even when it is hard)?",
            "What stops you from showing mercy sometimes?",
            "Have you considered that your willingness to confess and forsake sin will be the way to achieve mercy from others? Have you done your part to receive mercy?",
            "How will the Lord reward you for showing mercy?",
            "Who do you need to show mercy to today?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 38,
        "title": "Be Patient",
        "question": "I am patient, not hasty, in my plans and with my goals?",
        "verses": [
            {"ref": "Proverbs 13:12", "text": "Hope deferred makes the heart sick, But when the desire comes, it is a tree of life."},
            {"ref": "Proverbs 13:19", "text": "A desire accomplished is sweet to the soul, But it is an abomination to fools to depart from evil."},
            {"ref": "Proverbs 20:21", "text": "An inheritance gained hastily at the beginning Will not be blessed at the end."},
            {"ref": "Proverbs 21:5", "text": "The plans of the diligent lead surely to plenty, But those of everyone who is hasty, surely to poverty."},
            {"ref": "Proverbs 25:15", "text": "By long forbearance a ruler is persuaded, And a gentle tongue breaks a bone."}
        ],
        "dig_deeper": [
            "How has being impatient, ever caused problems for you?",
            "Did you learn a lesson or are you still making mistakes by being hasty, not preparing, being heartsick while you wait?",
            "What strategies can you employ to help you be more patient?",
            "What strategy is shared in Luke 14:28 about counting the cost?",
            "How can you address others that rush in and experience problems as a result?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 39,
        "title": "Respect Authority/Faithful Messenger",
        "question": "I have handled the authority figures in my life well (Have or had a good relationship with i.e., my boss, parents, teachers)?",
        "verses": [
            {"ref": "Proverbs 13:17", "text": "A wicked messenger falls into trouble, But a faithful ambassador brings health."},
            {"ref": "Proverbs 14:35", "text": "The king's favor is toward a wise servant, But his wrath is against him who causes shame."},
            {"ref": "Proverbs 24:21-22", "text": "My son, fear the LORD and the king; Do not associate with those given to change; For their calamity will rise suddenly, And who knows the ruin those two can bring?"},
            {"ref": "Proverbs 25:13", "text": "Like the cold of snow in time of harvest Is a faithful messenger to those who send him, For he refreshes the soul of his masters."},
            {"ref": "Proverbs 27:18", "text": "Whoever keeps the fig tree will eat its fruit; So he who waits on his master will be honored."}
        ],
        "dig_deeper": [
            "Being faithful, having reverence (fear), humility and offering willing service to authority will be refreshing to authority. Are you offering the authority figures in your life, their due respect?",
            "If not, consider why. What you can do to change your attitude toward authority?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 40,
        "title": "Don't Be Scornful/Proud/Mockers",
        "question": "I'm known for acting scornful/proud/conceited or mocking (putting others down, making fun of them, glad at their calamity)?",
        "verses": [
            {"ref": "Proverbs 3:34", "text": "Surely He scorns the scornful, But gives grace to the humble."},
            {"ref": "Proverbs 14:6", "text": "A scoffer seeks wisdom and does not find it, But knowledge is easy to him who understands."},
            {"ref": "Proverbs 17:5", "text": "He who mocks the poor reproaches his Maker; He who is glad at calamity will not go unpunished."},
            {"ref": "Proverbs 21:24", "text": "A proud and haughty man—'Scoffer' is his name; He acts with arrogant pride."},
            {"ref": "Proverbs 22:10", "text": "Cast out the scoffer, and contention will leave; Yes, strife and reproach will cease."},
            {"ref": "Proverbs 29:8", "text": "Scoffers set a city aflame, But wise men turn away wrath."}
        ],
        "dig_deeper": [
            "Someone who is scornful, proud, a mocker seems to value themselves more than others. Could there, however, be other reasons for their behavior?",
            "How should you value others according to Philippians 2:3-4?",
            "It seems, even biblically, difficult to correct a scoffer? How can you change your own or others behavior, if this is a character flaw?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 41,
        "title": "Honor the Lord; With Your Possessions/Generosity",
        "question": "I'm known for my generosity?",
        "verses": [
            {"ref": "Proverbs 3:9-10", "text": "Honor the LORD with your possessions, And with the first fruits of all your increase; So your barns will be filled with plenty, And your vats will overflow with new wine."},
            {"ref": "Proverbs 11:25-26", "text": "The generous soul will be made rich, And he who waters will also be watered himself. The people will curse him who withholds grain, But blessing will be on the head of him who sells it."},
            {"ref": "Proverbs 22:9", "text": "He who has a generous eye will be blessed, For he gives of his bread to the poor."},
            {"ref": "Proverbs 28:27", "text": "He who gives to the poor will not lack, But he who hides his eyes will have many curses."}
        ],
        "dig_deeper": [
            "What stops you from being generous? Fear of not having enough, fear of being taken advantage of, lack of control about what someone else will do with your resources?",
            "What specifically, from the verses above, counter your argument?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 42,
        "title": "Have a Merry Heart",
        "question": "I'm described as positive, upbeat or cheerful?",
        "verses": [
            {"ref": "Proverbs 15:13", "text": "A merry heart makes a cheerful countenance, But by sorrow of the heart the spirit is broken."},
            {"ref": "Proverbs 15:15", "text": "All the days of the afflicted are evil, But he who is of a merry heart has a continual feast."},
            {"ref": "Proverbs 17:22", "text": "A merry heart does good, like medicine, But a broken spirit dries the bones."},
            {"ref": "Proverbs 18:14", "text": "The spirit of a man will sustain him in sickness, But who can bear a broken spirit?"},
            {"ref": "Proverbs 25:25", "text": "As cold water to a weary soul, So is good news from a far country."}
        ],
        "dig_deeper": [
            "Does sorrow or a broken spirit keep you from having a merry heart or a cheerful countenance? How does this impact the way you are perceived by others?",
            "What do these verses above teach you about what can you do to help make another's heart merry? Hint: what is 'the light of the eyes'? A smile?",
            "Would you know what not to do? Have you ever been accused of being insensitive by being too cheerful when another's heart is heavy?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 43,
        "title": "Be Content, Not Greedy",
        "question": "I display an attitude that I am content with what I have, not greedy?",
        "verses": [
            {"ref": "Proverbs 15:27", "text": "He who is greedy for gain troubles his own house, But he who hates bribes will live."},
            {"ref": "Proverbs 21:26", "text": "He covets greedily all day long, But the righteous gives and does not spare."},
            {"ref": "Proverbs 23:4-5", "text": "Do not overwork to be rich; Because of your own understanding, cease! Will you set your eyes on that which is not? For riches certainly make themselves wings; They fly away like an eagle toward heaven."},
            {"ref": "Proverbs 28:20", "text": "A faithful man will abound with blessings, But he who hastens to be rich will not go unpunished."},
            {"ref": "Proverbs 30:8-9", "text": "Remove falsehood and lies far from me; Give me neither poverty nor riches—Feed me with the food allotted to me; Lest I be full and deny You, And say, 'Who is the LORD?' Or lest I be poor and steal, And profane the name of my God."}
        ],
        "dig_deeper": [
            "If you have not come to the place that you are content with what you have what will change your attitude in this area?",
            "Does being content mean that you are lazy, don't aspire for career advancement, don't give 100%?",
            "Have you brought trouble to your own house by being greedy for gain? Give an example.",
            "Are other's attitudes and greed affecting the way you live? Do you need to address them so that you can achieve the right balance?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 44,
        "title": "Don't Cause Shame",
        "question": "I cause my parents, friends or loved one's shame?",
        "verses": [
            {"ref": "Proverbs 17:2", "text": "A wise servant will rule over a son who causes shame, And will share an inheritance among the brothers."},
            {"ref": "Proverbs 19:13", "text": "A foolish son is the ruin of his father, And the contentions of a wife are a continual dripping."},
            {"ref": "Proverbs 28:7", "text": "Whoever keeps the law is a discerning son, But a companion of gluttons shames his father."}
        ],
        "dig_deeper": [
            "Have you ever caused someone shame? If so, have you made amends? Will you? How/when?",
            "If your inheritance is eternal salvation, will your shameful behavior rob you of this? How can you make your salvation sure?",
            "If someone has caused you shame, will you be willing to forgive them? What will it take from them, from you?",
            "Are you a contentious spouse? Have you considered the impact you are having with your 'continual dripping'? What can you do to change?",
            "Does the company you keep bring shame to those you love? Do they have good and biblical reason to be ashamed?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 45,
        "title": "Don't Be a Rebel",
        "question": "I am rebellious/a rebel?",
        "verses": [
            {"ref": "Proverbs 17:11", "text": "An evil man seeks only rebellion; Therefore a cruel messenger will be sent against him."},
            {"ref": "Proverbs 18:1", "text": "A man who isolates himself seeks his own desire; He rages against all wise judgment."}
        ],
        "dig_deeper": [
            "A rebel, a lone ranger, seeking only one's own desire and unrest. If you or someone you know, exhibits this behavior, how will you warn them of the consequences?",
            "What can you offer such a person?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 46,
        "title": "Don't Take Revenge",
        "question": "I take the opportunity to 'get-even' or get revenge for something someone does to me?",
        "verses": [
            {"ref": "Proverbs 20:22", "text": "Do not say, 'I will recompense evil'; Wait for the LORD, and He will save you."},
            {"ref": "Proverbs 24:29", "text": "Do not say, 'I will do to him just as he has done to me; I will render to the man according to his work.'"},
            {"ref": "Proverbs 25:21-22", "text": "If your enemy is hungry, give him bread to eat; And if he is thirsty, give him water to drink; For so you will heap coals of fire on his head, And the LORD will reward you."}
        ],
        "dig_deeper": [
            "What does it feel like when you are bent on getting revenge? Explain the emotions involved, the ways you rationalize your response, the physical manifestations, etc.",
            "What, specifically will you do when you are tempted to say 'I will recompense (repay) evil' or 'I will do to him just as he has done to me'?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 47,
        "title": "Don't Gloat",
        "question": "I'm known for bragging about my accomplishments and/or rejoicing when an enemy fails?",
        "verses": [
            {"ref": "Proverbs 24:17-18", "text": "Do not rejoice when your enemy falls, And do not let your heart be glad when he stumbles; Lest the LORD see it, and it displease Him, And He turn away His wrath from him."},
            {"ref": "Proverbs 25:27", "text": "It is not good to eat much honey; So to seek one's own glory is not glory."},
            {"ref": "Proverbs 27:2", "text": "Let another man praise you, and not your own mouth; A stranger, and not your own lips."}
        ],
        "dig_deeper": [
            "The definition of gloating: to contemplate or dwell on one's own success or another's misfortune with smugness or malignant pleasure. If you are known for having this type of character, are you ready to change?",
            "What might cause one to develop these traits?",
            "What can influence someone to change?",
            "Can you think of other Bible verses to support these proverbs above?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 48,
        "title": "Avoid Conflict",
        "question": "I avoid getting into conflicts or am able to handle conflict well and resolve peacefully?",
        "verses": [
            {"ref": "Proverbs 25:8-10", "text": "Do not go hastily to court; For what will you do in the end, When your neighbor has put you to shame? Debate your case with your neighbor, And do not disclose the secret to another; Lest he who hears it expose your shame, And your reputation be ruined."},
            {"ref": "Proverbs 29:9", "text": "If a wise man contends with a foolish man, Whether the fool rages or laughs, there is no peace."}
        ],
        "dig_deeper": [
            "The best way to handle conflict, in some cases, seems to be to avoid it or at least handle it privately. Do you agree?",
            "If this isn't the best way to handle your issue, state why? Next, prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area; avoiding and/or handling conflict well:",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 49,
        "title": "Value Friends and Family",
        "question": "I have a good relationship with my family/friends?",
        "verses": [
            {"ref": "Proverbs 17:17", "text": "A friend loves at all times, And a brother is born for adversity."},
            {"ref": "Proverbs 18:24", "text": "A man who has friends must himself be friendly, But there is a friend who sticks closer than a brother."},
            {"ref": "Proverbs 27:9-10", "text": "Ointment and perfume delight the heart, And the sweetness of a man's friend gives delight by hearty counsel. Do not forsake your own friend or your father's friend, Nor go to your brother's house in the day of your calamity; Better is a neighbor nearby than a brother far away."},
            {"ref": "Proverbs 27:17", "text": "As iron sharpens iron, So a man sharpens the countenance of his friend."}
        ],
        "dig_deeper": [
            "Relationships with friends and family are to be valued, cultivated, genuine, joyous, deemed sweet and giving delight, respected and revered. Do you find your relationships with your friends and family lacking in these areas? If so, what can you do differently to repair/restore these relationships?",
            "Do you have 'fake friends' those that aren't genuine or ones that will stick closer than a brother?",
            "If others around you are having problems within their relationships, what will you do to encourage them to value their friends and family?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 50,
        "title": "Understands Human Nature",
        "question": "I have a good understanding of human nature. I can usually read how people will react?",
        "verses": [
            {"ref": "Proverbs 18:16", "text": "A man's gift makes room for him, And brings him before great men."},
            {"ref": "Proverbs 20:14", "text": "'It is good for nothing,' cries the buyer; But when he has gone his way, then he boasts."},
            {"ref": "Proverbs 21:14", "text": "A gift in secret pacifies anger, And a bribe behind the back, strong wrath."},
            {"ref": "Proverbs 25:17", "text": "Seldom set foot in your neighbor's house, Lest he become weary of you and hate you."},
            {"ref": "Proverbs 25:20", "text": "Like one who takes away a garment in cold weather, And like vinegar on soda, Is one who sings songs to a heavy heart."}
        ],
        "dig_deeper": [
            "Gifts, given from the heart, not in a flashy way, but sincere, in secret, can open doors and pacify anger, do you agree? Is this condoning bribes?",
            "Have you ever heard a person bargaining for a good deal? What does this tell us about human nature and negotiations?",
            "The Bible teaches us that we are born with a sin nature. We need to be aware of this in ourselves as we endeavor to change. We also need to be aware of this in others, but not hold it against them. What can we do for them, instead?",
            "Do you learn by observing others what makes them unique; their strengths? Do you agree? How will this change your interactions with others?",
            "Are you sensitive (self-aware) not only of when you respond in your sin nature, but when someone has had enough of you, when you are being too cheerful or when you've worn out your welcome?",
            "How can improving your skills of understanding human nature help you work with and/or lead others?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
        },
    {
         "id": 51,
        "title": "Respect Elders",
        "question": "I'd consider myself respectful of my elders? Or, if you are the elder, have you been respectful of yourself; imparting your knowledge to the younger generation?",
        "verses": [
            {"ref": "Proverbs 20:29", "text": "The glory of young men is their strength, And the splendor of old men is their gray head."}
        ],
        "dig_deeper": [
            "Have you realized that the gray hair of your elders may hold wisdom?",
            "Have you realized that if are the one with gray hair that you have a duty to those under your care/entrusted to you?",
            "As you read 1 Peter 5:5, what quality does 'respecting your elders' show in your character?",
            "As an elder, are you valuing yourself, passing on your wisdom and being an asset to those who are younger and have more strength and energy?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
        },
    {
        "id": 52,
        "title": "Great Commission",
        "question": "I have told others about my faith in God/Christ?",
        "verses": [
            {"ref": "Proverbs 24:11-12", "text": "Deliver those who are drawn toward death, And hold back those stumbling to the slaughter. If you say, 'Surely we did not know this,' Does not He who weighs the hearts consider it? He who keeps your soul, does He not know it? And will He not render to each man according to his deeds?"}
        ],
        "dig_deeper": [
            "Have you tried your best to share Christ with those around you that are drawn to death, stumbling to the slaughter?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
      ]
 }
]

# ============================================================================
# DO NOT EDIT BELOW THIS LINE
# ============================================================================

# Initialize session state
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "assessment_complete" not in st.session_state:
    st.session_state.assessment_complete = False
if "dig_deeper_responses" not in st.session_state:
    st.session_state.dig_deeper_responses = {}

# ————————————————————————————————————————
def render_assessment():
    st.title("Proverbs at Work Assessment")
    st.markdown("### Self-Evaluation")

    with st.form("assessment_form"):
        for item in ASSESSMENT_DATA:
            st.markdown(f"**{item['id']}. {item['title']}**")
            st.markdown(f"*{item['question']}*")

            prev = st.session_state.answers.get(item["id"], "Usually")
            index = 0 if prev == "Usually" else 1

            choice = st.radio(
                "",
                ["Usually", "Not Usually"],
                index=index,
                key=f"q_{item['id']}",
                label_visibility="collapsed",
                horizontal=True
            )
            st.session_state.answers[item["id"]] = choice
            st.markdown("---")

        if st.form_submit_button("See My Results", type="primary", use_container_width=True):
            st.session_state.assessment_complete = True
            st.rerun()

# ————————————————————————————————————————
def render_results():
    st.title("Assessment Results")

    # Make sure answers are always available (even after refresh)
    for item in ASSESSMENT_DATA:
        widget_key = f"q_{item['id']}"
        if widget_key in st.session_state:
            st.session_state.answers[item["id"]] = st.session_state[widget_key]

    # Calculate weaknesses
    weaknesses = [
        item for item in ASSESSMENT_DATA
        if st.session_state.answers.get(item["id"]) != CORRECT_ANSWERS.get(item["id"])
    ]

    st.markdown(f"### Areas of Weakness: {len(weaknesses)} out of 3")

    if len(weaknesses) == 0:
        st.balloons()
        st.success("Congratulations! You scored perfectly — no areas of weakness identified.")
    else:
        st.markdown("#### Click each topic below to view details and reflect")
        for item in weaknesses:
            with st.expander(f"{item['id']}. {item['title']}", expanded=False):
                st.markdown(f"**Question:** {item['question']}")
                st.markdown(f"**Your Answer:** {st.session_state.answers.get(item['id'], '—')}")
                st.markdown(f"**Desired Answer:** {CORRECT_ANSWERS[item['id']]}")

                st.markdown("---")
                st.subheader("Biblical References")
                for verse in item["verses"]:
                    st.markdown(f"**{verse['ref']}**")
                    st.markdown(f"_{verse['text']}_")
                    st.markdown("")  # spacing

                st.markdown("---")
                st.subheader("Dig Deeper Questions")
                for idx, question in enumerate(item["dig_deeper"]):
                    key = f"{item['id']}_dd_{idx}"
                    st.text_area(
                        label=question,
                        value=st.session_state.dig_deeper_responses.get(key, ""),
                        key=key,
                        height=130,
                        label_visibility="visible"
                    )

        # Report buttons
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Generate Printable Report", type="primary", use_container_width=True):
                generate_report(weaknesses)
        with col2:
            if st.button("Export as JSON", use_container_width=True):
                export_json(weaknesses)

    # Restart button
    st.markdown("---")
    if st.button("Take Assessment Again", type="secondary", use_container_width=True):
        st.session_state.answers = {}
        st.session_state.assessment_complete = False
        st.session_state.dig_deeper_responses = {}
        st.rerun()

# ————————————————————————————————————————
def generate_report(weaknesses):
    report = f"""
PROVERBS AT WORK ASSESSMENT - RESULTS
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
AREAS OF WEAKNESS: {len(weaknesses)}
{'='*80}
"""
    for item in weaknesses:
        report += f"\n{item['id']}. {item['title'].upper()}\n"
        report += f"Question: {item['question']}\n"
        report += f"Your Answer: {st.session_state.answers.get(item['id'], '—')}\n"
        report += f"Correct Answer: {CORRECT_ANSWERS[item['id']]}\n\nBiblical References:\n"
        for v in item["verses"]:
            report += f"{v['ref']}\n{v['text']}\n\n"
        report += "Dig Deeper Responses:\n"
        for i, q in enumerate(item["dig_deeper"]):
            key = f"{item['id']}_dd_{i}"
            report += f"{i+1}. {q}\n   → {st.session_state.dig_deeper_responses.get(key, 'No response')}\n"
        report += "\n" + "="*80 + "\n"

    st.download_button(
        "Download Report (TXT)",
        data=report,
        file_name=f"proverbs_assessment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )

# ————————————————————————————————————————
def export_json(weaknesses):
    data = {
        "timestamp": datetime.now().isoformat(),
        "weaknesses_count": len(weaknesses),
        "weaknesses": []
    }
    for item in weaknesses:
        entry = {
            "id": item["id"],
            "title": item["title"],
            "question": item["question"],
            "your_answer": st.session_state.answers.get(item["id"]),
            "correct_answer": CORRECT_ANSWERS[item["id"]],
            "verses": item["verses"],
            "dig_deeper": item["dig_deeper"],
            "responses": [
                st.session_state.dig_deeper_responses.get(f"{item['id']}_dd_{i}", "")
                for i in range(len(item["dig_deeper"]))
            ]
        }
        data["weaknesses"].append(entry)

    st.download_button(
        "Download JSON",
        data=json.dumps(data, indent=2),
        file_name=f"proverbs_assessment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json"
    )

# ————————————————————————————————————————
def main():
    if st.session_state.assessment_complete:
        render_results()
    else:
        render_assessment()

if __name__ == "__main__":
    main()

