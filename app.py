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
       
    # ========================================
    # TOPIC 1: Accept Instruction from Others
    # ========================================
    {
        "id": 1,
        "title": "1. Accept Instruction from Others",
        "question": "Do I willingly accept instruction from others?",
        "verses": [
            {"ref": "Proverbs 1:7-9", "text": "7 The fear of the LORD is the beginning of knowledge, But fools despise wisdom and instruction. 8 My son, hear the instruction of your father, And do not forsake the law of your mother; 9 For they will be a graceful ornament on your head, And chains about your neck."},
            {"ref": "Proverbs 3:1-4", "text": "1 My son, do not forget my law, But let your heart keep my commands; 2 For length of days and long life And peace they will add to you. 3 Let not mercy and truth forsake you; Bind them around your neck, Write them on the tablet of your heart, 4 And so find favor and high esteem In the sight of God and man."},
            {"ref": "Proverbs 4:1-4", "text": "1 Hear, my children, the instruction of a father, And give attention to know understanding; 2 For I give you good doctrine: Do not forsake my law. 3 When I was my father's son, Tender and the only one in the sight of my mother, 4 He also taught me, and said to me: Let your heart retain my words; Keep my commands, and live."},
            {"ref": "Proverbs 4:20-23", "text": "20 My son, give attention to my words; Incline your ear to my sayings. 21 Do not let them depart from your eyes; Keep them in the midst of your heart; 22 For they are life to those who find them, And health to all their flesh. 23 Keep your heart with all diligence, For out of it spring the issues of life."},
            {"ref": "Proverbs 5:12-14", "text": "12 And say: How I have hated instruction, And my heart despised correction! 13 I have not obeyed the voice of my teachers, Nor inclined my ear to those who instructed me! 14 I was on the verge of total ruin, In the midst of the assembly and congregation."},
            {"ref": "Proverbs 6:20-23", "text": "20 My son, keep your father's command, And do not forsake the law of your mother. 21 Bind them continually upon your heart; Tie them around your neck. 22 When you roam, [they] will lead you; When you sleep, they will keep you; And when you awake, they will speak with you. 23 For the commandment is a lamp, And the law a light; Reproofs of instruction are the way of life."},
            {"ref": "Proverbs 10:8", "text": "8 The wise in heart will receive commands, But a prating fool will fall."},
            {"ref": "Proverbs 13:1", "text": "1 A wise son heeds his father's instruction, But a scoffer does not listen to rebuke."},
            {"ref": "Proverbs 19:27", "text": "27 Cease listening to instruction, my son, And you will stray from the words of knowledge."},
            {"ref": "Proverbs 23:12", "text": "12 Apply your heart to instruction, And your ears to words of knowledge."}
        ],
        "dig_deeper_questions": [
            " Looking at your life, how have you fallen short in the area of accepting instruction from others: your parents, teachers, Godly advisors? How about others that give commands or counsel i.e., your boss, your spouse? Give some examples of how this has hurt you.",
            " Taking things one-step further, how have you sought out (or applied your heart to) instruction and made an effort to listen (open your ears) for instruction? See Proverbs 23:12 above.",
            " What do you think stops you from accepting or seeking out instruction willingly?",
            " Specifically, has your lack of accepting instruction affected you in your work? How?",
            " Is there something you could learn (be instructed in) right now that would make you a better employee in your current job or for future career aspirations?",
            " If so, how will you improve in this area?",
            " How can you minister to others that have an issue in this area?",
            " Finally, review Chapter 2 – Self-Image Issues, regarding a \"Coachable Spirit\". How does this pertain to accepting instruction?",
            " Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 2: Accept Correction
    # ========================================
    {
        "id": 2,
        "title": "2. Accept Correction",
        "question": "Do I gracefully accept correction when it is given?",
        "verses": [
            {"ref": "Proverbs 1:20-33", "text": "20 Wisdom calls aloud outside; She raises her voice in the open squares. 21 She cries out in the chief concourses, At the openings of the gates in the city She speaks her words: 22 \"How long, you simple ones, will you love simplicity? For scorners delight in their scorning, And fools hate knowledge. 23 Turn at my rebuke; Surely I will pour out my spirit on you; I will make my words known to you. 24 Because I have called and you refused, I have stretched out my hand and no one regarded, 25 Because you disdained all my counsel, And would have none of my rebuke, 26 I also will laugh at your calamity; I will mock when your terror comes, 27 When your terror comes like a storm, And your destruction comes like a whirlwind, When distress and anguish come upon you. 28 \"Then they will call on me, but I will not answer; They will seek me diligently, but they will not find me. 29 Because they hated knowledge And did not choose the fear of the LORD, 30 They would have none of my counsel And despised my every rebuke. 31 Therefore they shall eat the fruit of their own way, And be filled to the full with their own fancies. 32 For the turning away of the simple will slay them, And the complacency of fools will destroy them; 33 But whoever listens to me will dwell safely, And will be secure, without fear of evil.\""},
            {"ref": "Proverbs 3:11-12", "text": "11 My son, do not despise the chastening of the LORD, Nor detest His correction; 12 For whom the LORD loves He corrects, Just as a father the son in whom he delights."},
            {"ref": "Proverbs 10:17", "text": "17 He who keeps instruction is in the way of life, But he who refuses correction goes astray."},
            {"ref": "Proverbs 12:1", "text": "1 Whoever loves instruction loves knowledge, But he who hates correction is stupid."},
            {"ref": "Proverbs 13:18", "text": "18 Poverty and shame will come to him who disdains correction, But he who regards a rebuke will be honored."},
            {"ref": "Proverbs 15:5", "text": "5 A fool despises his father's instruction, But he who receives correction is prudent."},
            {"ref": "Proverbs 15:10-12", "text": "10 Harsh discipline is for him who forsakes the way, And he who hates correction will die. 11 Hell and Destruction are before the LORD; So how much more the hearts of the sons of men. 12 A scoffer does not love one who corrects him, Nor will he go to the wise."},
            {"ref": "Proverbs 15:30-32", "text": "30 The light of the eyes rejoices the heart, And a good report makes the bones healthy. 31 The ear that hears the rebukes of life Will abide among the wise. 32 He who disdains instruction despises his own soul, But he who heeds rebuke gets understanding."},
            {"ref": "Proverbs 16:22", "text": "22 Understanding is a wellspring of life to him who has it. But the correction of fools is folly."},
            {"ref": "Proverbs 17:10", "text": "10 Rebuke is more effective for a wise man Than a hundred blows on a fool."},
            {"ref": "Proverbs 29:1", "text": "1 He who is often rebuked, and hardens his neck, Will suddenly be destroyed, and that without remedy."}
        ],
        "dig_deeper_questions": [
            " After you have received criticism, explain your normal reaction initially and eventually?",
            " How quickly can you recover after hearing criticism? What about self-criticism? Are you hard on yourself, beating yourself up and letting this affect your performance, long after others have moved on?",
            " Can you think of someone that you have witnessed take criticism well? Describe what about that person's reaction appealed to you.",
            " Delightful, \"in\" the way of life, knowledgeable, honored, prudent, wise, of good report, healthy, possesses understanding and cleansed away from evil, these are ways that Proverbs describes the person who accepts correction. Contrast that to the terms describing those who do not accept correction: going astray, stupid, poor, shameful, dead, despiser of one's own soul, fool, destroyed without remedy. Describe some of the negative consequences you've experienced from not accepting correction:",
            " Which verses above will help you when you are tempted to harbor resentment against someone who offers criticism?",
            " How does a person's demeanor/style when offering criticism impact how well you accept the message?",
            " Explain how you would best like to hear criticism?",
            " Do you offer criticism as a friend, in love, with well-chosen words, \"fitly spoken\"? If not, how can you improve?",
            " The next time you receive criticism in a way, other than your preference outlined above, could you communicate to the person offering the message, how you would rather it be delivered? How could this conversation be helpful?",
            " According to the verses above, should you offer criticism to fools? To wise men?",
            " Does your boss consider you wise enough to be worthy of criticism? This may depend on your reaction (do you harden your neck or do you have a \"coachable spirit\"). Think about it. Is there anything you need to change?",
            " Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 3: Administer Discipline to Others
    # ========================================
    {
        "id": 3,
        "title": "3. Administer Discipline to Others",
        "question": "Do I readily discipline those that need correction?",
        "verses": [
            {"ref": "Proverbs 13:24", "text": "24 He who spares his rod hates his son, But he who loves him disciplines him"},
            {"ref": "Proverbs 19:18", "text": "18 Chasten your son while there is hope, And do not set your heart on his destruction."},
            {"ref": "Proverbs 20:30", "text": "30 Blows that hurt cleanse away evil, As do stripes the inner depths of the heart."},
            {"ref": "Proverbs 21:11", "text": "11 When the scoffer is punished, the simple is made wise; But when the wise is instructed, he receives knowledge."},
            {"ref": "Proverbs 22:15", "text": "15 Foolishness is bound up in the heart of a child; The rod of correction will drive it far from him."},
            {"ref": "Proverbs 23:13-14", "text": "13 Do not withhold correction from a child, For if you beat him with a rod, he will not die. 14 You shall beat him with a rod, And deliver his soul from hell."},
            {"ref": "Proverbs 24:11-12", "text": "11 Deliver those who are drawn toward death, And hold back those stumbling to the slaughter. 12 If you say, \"Surely we did not know this,\" Does not He who weighs the hearts consider it? He who keeps your soul, does He not know it? And will He not render to each man according to his deeds?"},
            {"ref": "Proverbs 25:11-12", "text": "11 A word fitly spoken is like apples of gold In settings of silver. 12 Like an earring of gold and an ornament of fine gold Is a wise rebuker to an obedient ear."},
            {"ref": "Proverbs 26:3-5", "text": "3 A whip for the horse, A bridle for the donkey, And a rod for the fool's back. 4 Do not answer a fool according to his folly, Lest you also be like him. 5 Answer a fool according to his folly, Lest he be wise in his own eyes."},
            {"ref": "Proverbs 27:5", "text": "5 Open rebuke is better Than love carefully concealed."},
            {"ref": "Proverbs 27:6", "text": "6 Faithful are the wounds of a friend, But the kisses of an enemy are deceitful."},
            {"ref": "Proverbs 27:17", "text": "17 As iron sharpens iron, So a man sharpens the countenance of his friend."},
            {"ref": "Proverbs 29:15", "text": "15 The rod and rebuke give wisdom, But a child left to himself brings shame to his mother."}
        ],
        "dig_deeper_questions": [
            " Are you consistent in your administration of discipline or constructive feedback?",
            " Is it hard for you to discipline or correct someone? Why do you think this is?",
            " Are you too harsh (set your heart on his destruction) in your discipline?",
            " Are your words \"fitful\"? Do you feel you can appropriately communicate a correction or could use improvement in this area? (For help, see Chapter 6 – Communicating Issues.)",
            " Have you ever given someone a break (spared the rod) because you felt sorry for them? How did it turn out? Looking back, was that the \"loving\" thing to do?",
            " Can you accept discipline better because you now understand it's value and motivation (love/concern)?",
            " Summarize/prioritize things you can do, (do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 4: Avoid Sinners Enticing You
    # ========================================
    {
        "id": 4,
        "title": "4. Avoid Sinners Enticing You",
        "question": "Am I easily misled into wrong behavior by peer pressure?",
        "verses": [
            {"ref": "Proverbs 1:10-19", "text": "10 My son, if sinners entice you, Do not consent. 11 If they say, \"Come with us, Let us lie in wait to shed blood; Let us lurk secretly for the innocent without cause; 12 Let us swallow them alive like Sheol, 13 We shall find all kinds of precious possessions, We shall fill our houses with spoil; 14 Cast in your lot among us, Let us all have one purse\"— 15 My son, do not walk in the way with them, Keep your foot from their path; 16 For their feet run to evil, And they make haste to shed blood. 17 Surely, in vain the net is spread In the sight of any bird; 18 But they lie in wait for their own blood, They lurk secretly for their own lives. 19 So are the ways of everyone who is greedy for gain; It takes away the life of its owners."},
            {"ref": "Proverbs 4:14-19", "text": "14 Do not enter the path of the wicked, And do not walk in the way of evil. 15 Avoid it, do not travel on it; Turn away from it and pass on. 16 For they do not sleep unless they have done evil; And their sleep is taken away unless they make someone fall. 17 For they eat the bread of wickedness, And drink the wine of violence. 18 But the path of the just is like the shining sun, That shines ever brighter unto the perfect day. 19 The way of the wicked is like darkness; They do not know what makes them stumble."},
            {"ref": "Proverbs 12:26", "text": "26 The righteous should choose his friends carefully, For the way of the wicked leads them astray."},
            {"ref": "Proverbs 13:20-21", "text": "20 He who walks with wise men will be wise, But the companion of fools will be destroyed. 21 Evil pursues sinners, But to the righteous, good shall be repaid."},
            {"ref": "Proverbs 16:29", "text": "29 A violent man entices his neighbor, And leads him in a way that is not good."},
            {"ref": "Proverbs 20:19", "text": "19 He who goes about as a talebearer reveals secrets; Therefore do not associate with one who flatters with his lips."},
            {"ref": "Proverbs 28:10", "text": "10 Whoever causes the upright to go astray in an evil way, He himself will fall into his own pit; But the blameless will inherit good."},
            {"ref": "Proverbs 28:17", "text": "17 A man burdened with bloodshed will flee into a pit; Let no one help him."},
            {"ref": "Proverbs 29:24", "text": "24 Whoever is a partner with a thief hates his own life; He swears to tell the truth, but reveals nothing."}
        ],
        "dig_deeper_questions": [
            "1. Have you ever associated with people that cause you to behave poorly? Give some examples:",
            "2. Do you continue to associate with people who are enticing you into evil?",
            "3. Those greedy for gain, fools, violent, talebearers/gossips, flatterers, thieves, are just some of the types of sinners enumerated in the verses above. Look around your close circle of friends. Do you need to make some changes in your relationships?",
            "4. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 5: Seek Wisdom/Discretion
    # ========================================
    {
        "id": 5,
        "title": "5. Seek Wisdom/Discretion",
        "question": "Do I work hard at seeking wisdom and discretion to figure out the right thing to do in difficult situations?",
        "verses": [
            {"ref": "Proverbs 2:1-9", "text": "1 My son, if you receive my words, And treasure my commands within you, 2 So that you incline your ear to wisdom, And apply your heart to understanding; 3 Yes, if you cry out for discernment, And lift up your voice for understanding, 4 If you seek her as silver, And search for her as for hidden treasures; 5 Then you will understand the fear of the LORD, And find the knowledge of God. 6 For the LORD gives wisdom; From His mouth come knowledge and understanding; 7 He stores up sound wisdom for the upright; He is a shield to those who walk uprightly; 8 He guards the paths of justice, And preserves the way of His saints. 9 Then you will understand righteousness and justice, Equity and every good path."},
            {"ref": "Proverbs 3:13-24", "text": "13 Happy is the man who finds wisdom, And the man who gains understanding; 14 For her proceeds are better than the profits of silver, And her gain than fine gold. 15 She is more precious than rubies, And all the things you may desire cannot compare with her. 16 Length of days is in her right hand, In her left hand riches and honor. 17 Her ways are ways of pleasantness, And all her paths are peace. 18 She is a tree of life to those who take hold of her, And happy are all who retain her. 19 The LORD by wisdom founded the earth; By understanding He established the heavens; 20 By His knowledge the depths were broken up, And clouds drop down the dew. 21 My son, let them not depart from your eyes— Keep sound wisdom and discretion; 22 So they will be life to your soul And grace to your neck. 23 Then you will walk safely in your way, And your foot will not stumble. 24 When you lie down, you will not be afraid; Yes, you will lie down and your sleep will be sweet."},
            {"ref": "Proverbs 3:35", "text": "35 The wise shall inherit glory, But shame shall be the legacy of fools."},
            {"ref": "Proverbs 4:5-13", "text": "5 Get wisdom! Get understanding! Do not forget, nor turn away from the words of my mouth. 6 Do not forsake her, and she will preserve you; Love her, and she will keep you. 7 Wisdom is the principal thing; Therefore get wisdom. And in all your getting, get understanding. 8 Exalt her, and she will promote you; She will bring you honor, when you embrace her. 9 She will place on your head an ornament of grace; A crown of glory she will deliver to you.\" 10 Hear, my son, and receive my sayings, And the years of your life will be many. 11 I have taught you in the way of wisdom; I have led you in right paths. 12 When you walk, your steps will not be hindered, And when you run, you will not stumble. 13 Take firm hold of instruction, do not let go; Keep her, for she is your life."},
            {"ref": "Proverbs 8:1-9", "text": "1 Does not wisdom cry out, And understanding lift up her voice? 2 She takes her stand on the top of the high hill, Beside the way, where the paths meet. 3 She cries out by the gates, at the entry of the city, At the entrance of the doors: 4 \"To you, O men, I call, And my voice is to the sons of men. 5 O you simple ones, understand prudence, And you fools, be of an understanding heart. 6 Listen, for I will speak of excellent things, And from the opening of my lips will come right things; 7 For my mouth will speak truth; Wickedness is an abomination to my lips. 8 All the words of my mouth are with righteousness; Nothing crooked or perverse is in them. 9 They are all plain to him who understands, And right to those who find knowledge."},
            {"ref": "Proverbs 10:1", "text": "1 The proverbs of Solomon: A wise son makes a glad father, But a foolish son is the grief of his mother."},
            {"ref": "Proverbs 10:13", "text": "13 Wisdom is found on the lips of him who has understanding, But a rod is for the back of him who is devoid of understanding."},
            {"ref": "Proverbs 11:22", "text": "22 As a ring of gold in a swine's snout, So is a lovely woman who lacks discretion."},
            {"ref": "Proverbs 15:24", "text": "24 The way of life winds upward for the wise, That he may turn away from hell"},
            {"ref": "Proverbs 16:16", "text": "16 How much better to get wisdom than gold! And to get understanding is to be chosen rather than silver."},
            {"ref": "Proverbs 16:21", "text": "21 The wise in heart will be called prudent, And sweetness of the lips increases learning."},
            {"ref": "Proverbs 18:15", "text": "15 The heart of the prudent acquires knowledge, And the ear of the wise seeks knowledge."},
            {"ref": "Proverbs 19:8", "text": "8 He who gets wisdom loves his own soul; He who keeps understanding will find good."},
            {"ref": "Proverbs 21:16", "text": "16 A man who wanders from the way of understanding Will rest in the assembly of the dead."},
            {"ref": "Proverbs 21:22", "text": "22 A wise man scales the city of the mighty, And brings down the trusted stronghold."},
            {"ref": "Proverbs 24:3-5", "text": "3 Through wisdom a house is built, And by understanding it is established; 4 By knowledge the rooms are filled With all precious and pleasant riches. 5 A wise man is strong, Yes, a man of knowledge increases strength;"},
            {"ref": "Proverbs 24:7", "text": "7 Wisdom is too lofty for a fool; He does not open his mouth in the gate."},
            {"ref": "Proverbs 24:13-14", "text": "13 My son, eat honey because it is good, And the honeycomb which is sweet to your taste; 14 So shall the knowledge of wisdom be to your soul; If you have found it, there is a prospect, And your hope will not be cut off."},
            {"ref": "Proverbs 27:11", "text": "11 My son, be wise, and make my heart glad, That I may answer him who reproaches me."}
        ],
        "dig_deeper_questions": [
            "1. Where do you go to as your source of information? Your boss, the Human Resources Department, management training classes, a career or life coach, your peers, other respected colleagues, your spouse, your own understanding?",
            "2. Have you looked specifically in the Word instead for the root of the problem and wisdom about the solution?",
            "3. When you do seek wisdom, it is important that you: a. Obtain knowledge (accumulate the available information or facts on the subject); b. Be wise (discern the true nature of things; that the knowledge you receive is knowledge that stands up to the test/will of the Word of God (1 Corinthians 2:15, 1 Thessalonians 5:21, 1 John 4:1, Hebrews 5:14, Romans 12:2) and; c. Gain understanding (learn how to apply this wisdom practically). If your issue is leadership, for example, and you gather knowledge about Servant Leadership and you see in God's Word that Jesus calls us to practice this leadership, what can you do, practically, to model this (assuming that literally washing your employee's feet may not be culturally acceptable)?",
            "4. When reading the sections on Authority, Self-Image and Your Job, did you have any \"aha\" moments? Did the perspective provided help you gain wisdom about your \"work-life\" issue? Explain.",
            "5. Think of a difficult situation you've faced at work recently and determine to explore what the Lord's wisdom has to say about that situation. Would you, or could you, have reacted differently if you had this wisdom at the time you were dealing with the problem? Explain below, then share this information with someone.",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 6: Seek Counsel
    # ========================================
    {
        "id": 6,
        "title": "6. Seek Counsel",
        "question": "Do I ask others (especially Christians) for counsel and value their insights and opinions?",
        "verses": [
            {"ref": "Proverbs 11:14", "text": "14 Where there is no counsel, the people fall; But in the multitude of counselors there is safety."},
            {"ref": "Proverbs 15:22", "text": "22 Without counsel, plans go awry, But in the multitude of counselors they are established."},
            {"ref": "Proverbs 20:5", "text": "5 Counsel in the heart of man is like deep water, But a man of understanding will draw it out."},
            {"ref": "Proverbs 20:18", "text": "18 Plans are established by counsel; By wise counsel wage war."},
            {"ref": "Proverbs 24:6", "text": "6 For by wise counsel you will wage your own war, And in a multitude of counselors there is safety."}
        ],
        "dig_deeper_questions": [
            "1. Do you value and seek out the opinions of many counselors?",
            "2. How does being shy, proud or insecure affect your willingness to seek advice? Are any of these an issue for you? Are those acceptable excuses to not follow this piece of wisdom?",
            "3. Can you remember a situation where you acted alone and you wish you had sought counsel? Share some examples:",
            "4. Modern management theory suggests collaboration and seeking input from many individuals, departments, etc. is appropriate. This, in essence, is a democracy. Are there problems with seeking too much input or input from the wrong individuals? How will you balance this?",
            "5. Do you (or others you deal with) sincerely seek wise counsel, the right amount of counsel, or just go through the motions of being democratic? Remember the Lord knows our hearts.",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 7: Keep the Lord's Commands
    # ========================================
    {
        "id": 7,
        "title": "7. Keep the Lord's Commands",
        "question": "Do I try to follow the 10 Commandments?",
        "verses": [
            {"ref": "Proverbs 13:13-15", "text": "13 He who despises the word will be destroyed, But he who fears the commandment will be rewarded. 14 The law of the wise is a fountain of life, To turn one away from the snares of death. 15 Good understanding gains favor, But the way of the unfaithful is hard."},
            {"ref": "Proverbs 14:26-27", "text": "26 In the fear of the LORD there is strong confidence, And His children will have a place of refuge. 27 The fear of the LORD is a fountain of life, To turn one away from the snares of death."},
            {"ref": "Proverbs 16:20", "text": "20 He who heeds the word wisely will find good, And whoever trusts in the LORD, happy is he."},
            {"ref": "Proverbs 19:16", "text": "16 He who keeps the commandment keeps his soul, But he who is careless of his ways will die."},
            {"ref": "Proverbs 19:23", "text": "23 The fear of the LORD leads to life, And he who has it will abide in satisfaction; He will not be visited with evil."},
            {"ref": "Proverbs 28:4", "text": "4 Those who forsake the law praise the wicked, But such as keep the law contend with them."},
            {"ref": "Proverbs 28:9", "text": "9 One who turns away his ear from hearing the law, even his prayer is an abomination."},
            {"ref": "Proverbs 29:18", "text": "18 Where there is no revelation, the people cast off restraint; But happy is he who keeps the law."}
        ],
        "dig_deeper_questions": [
            "1. Review the 10 Commandments (Exodus 20). Do you feel you truly believe in them, trust them, and revere the Lord enough to try to keep them?",
            "2. How can you remind yourself of the commandments and hold yourself accountable to them in every circumstance?",
            "3. If you cannot live up to the commandments, \"the law\", do you believe that all things are possible through Christ and that he has paid the price for your failures?",
            "4. Does this release you from the responsibility to live lawfully? (See Romans 6:15.)",
            "5. The verses above show that those that DON'T revere or fear the Lord and keep His commandments will suffer. They tell us… a) The way of the unfaithful, the careless, the one who turns his ear from the law is hard and leads to death. This causes one: • to be dissatisfied, • visited with evil, • to praise wickedness, • to cast off restraint, and • results in unhappiness and • prayers that are an abomination. b) Being a faithful Christian, however, should help you: • be rewarded, • turn away from the snares of death, • gain favor, • have strong confidence, • have a safe refuge, • find good, • be happy, • keep your soul, • abide in satisfaction, • not be visited with evil, and • allow you to contend with the wicked. Which list of characteristics, paragraph (a or b) above, best describes your life? Is your life reflecting the rewards of a faithful Christian, why or why not?",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 8: Trust in the Lord
    # ========================================
    {
        "id": 8,
        "title": "8. Trust in the Lord",
        "question": "Do I demonstrate that I trust in the Lord?",
        "verses": [
            {"ref": "Proverbs 3:5-6", "text": "5 Trust in the LORD with all your heart, And lean not on your own understanding; 6 In all your ways acknowledge Him, And He shall direct your paths."},
            {"ref": "Proverbs 3:25-26", "text": "25 Do not be afraid of sudden terror, Nor of trouble from the wicked when it comes; 26 For the LORD will be your confidence, And will keep your foot from being caught."},
            {"ref": "Proverbs 16:4", "text": "4 The LORD has made all for Himself, Yes, even the wicked for the day of doom."},
            {"ref": "Proverbs 16:9", "text": "9 A man's heart plans his way, But the LORD directs his steps."},
            {"ref": "Proverbs 16:33", "text": "33 The lot is cast into the lap, But its every decision is from the LORD."},
            {"ref": "Proverbs 18:10-11", "text": "10 The name of the LORD is a strong tower; The righteous run to it and are safe. 11 The rich man's wealth is his strong city, And like a high wall in his own esteem."},
            {"ref": "Proverbs 19:21", "text": "21 There are many plans in a man's heart, Nevertheless the LORD's counsel—that will stand."},
            {"ref": "Proverbs 21:1", "text": "1 The king's heart is in the hand of the LORD, Like the rivers of water; He turns it wherever He wishes."},
            {"ref": "Proverbs 21:30-31", "text": "30 There is no wisdom or understanding Or counsel against the LORD. 31 The horse is prepared for the day of battle, But deliverance is of the LORD."},
            {"ref": "Proverbs 22:17-21", "text": "17 Incline your ear and hear the words of the wise, And apply your heart to my knowledge; 18 For it is a pleasant thing if you keep them within you; Let them all be fixed upon your lips, 19 So that your trust may be in the LORD; I have instructed you today, even you. 20 Have I not written to you excellent things Of counsels and knowledge, 21 That I may make you know the certainty of the words of truth, That you may answer words of truth To those who send to you?"},
            {"ref": "Proverbs 29:25", "text": "25 The fear of man brings a snare, But whoever trusts in the LORD shall be safe."},
            {"ref": "Proverbs 30:1-6", "text": "1 The words of Agur the son of Jakeh, his utterance. This man declared to Ithiel—to Ithiel and Ucal: 2 Surely I am more stupid than any man, And do not have the understanding of a man. 3 I neither learned wisdom Nor have knowledge of the Holy One. 4 Who has ascended into heaven, or descended? Who has gathered the wind in His fists? Who has bound the waters in a garment? Who has established all the ends of the earth? What is His name, and what is His Son's name, If you know? 5 Every word of God is pure; He is a shield to those who put their trust in Him. 6 Do not add to His words, Lest He rebuke you, and you be found a liar."}
        ],
        "dig_deeper_questions": [
            "1. Do you exhibit confidence that the Lord is in control of your work and your life situations?",
            "2. What specifically can you do to demonstrate that trust and exhibit that confidence more? (perhaps give up some control, delegate, release yourself from your insatiable drive for success?)",
            "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 9: Don't Be Wise in Your Own Eyes
    # ========================================
    {
        "id": 9,
        "title": "9. Don't Be Wise in Your Own Eyes",
        "question": "Do I give others the impression that I know-it-all (am wise in my own eyes)?",
        "verses": [
            {"ref": "Proverbs 3:7-8", "text": "7 Do not be wise in your own eyes; Fear the LORD and depart from evil. 8 It will be health to your flesh, And strength to your bones."},
            {"ref": "Proverbs 12:15", "text": "15 The way of a fool is right in his own eyes, But he who heeds counsel is wise."},
            {"ref": "Proverbs 14:12", "text": "12 There is a way that seems right to a man, But its end is the way of death."},
            {"ref": "Proverbs 14:14", "text": "14 The backslider in heart will be filled with his own ways, But a good man will be satisfied from above."},
            {"ref": "Proverbs 16:2", "text": "2 All the ways of a man are pure in his own eyes, But the LORD weighs the spirits."},
            {"ref": "Proverbs 16:25", "text": "25 There is a way that seems right to a man, But its end is the way of death."},
            {"ref": "Proverbs 20:24", "text": "24 A man's steps are of the LORD; How then can a man understand his own way?"},
            {"ref": "Proverbs 21:2", "text": "2 Every way of a man is right in his own eyes, But the LORD weighs the hearts."},
            {"ref": "Proverbs 26:12", "text": "12 Do you see a man wise in his own eyes? There is more hope for a fool than for him."},
            {"ref": "Proverbs 27:1-2", "text": "1 Do not boast about tomorrow, For you do not know what a day may bring forth. 2 Let another man praise you, and not your own mouth; A stranger, and not your own lips."},
            {"ref": "Proverbs 28:11", "text": "11 The rich man is wise in his own eyes, But the poor who has understanding searches him out."},
            {"ref": "Proverbs 28:26", "text": "26 He who trusts in his own heart is a fool, But whoever walks wisely will be delivered."},
            {"ref": "Proverbs 30:12", "text": "12 There is a generation that is pure in its own eyes, Yet is not washed from its filthiness."},
            {"ref": "Proverbs 30:32-33", "text": "32 If you have been foolish in exalting yourself, Or if you have devised evil, put your hand on your mouth. 33 For as the churning of milk produces butter, And wringing the nose produces blood, So the forcing of wrath produces strife."}
        ],
        "dig_deeper_questions": [
            "1. What, in your opinion, is the difference between being respected for your knowledge and being perceived as a \"know-it-all\"?",
            "2. How could someone who is perceived as a \"know-it-all\" or \"wise or pure in their own eyes\" change other's impression of him/her?",
            "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 10: Don't Withhold Good When Due
    # ========================================
    {
        "id": 10,
        "title": "10. Don't Withhold Good When Due",
        "question": "Do I give credit to people when credit is due?",
        "verses": [
            {"ref": "Proverbs 3:27-28", "text": "27 Do not withhold good from those to whom it is due, When it is in the power of your hand to do so. 28 Do not say to your neighbor, Go, and come back, And tomorrow I will give it,\" When you have it with you."}
        ],
        "dig_deeper_questions": [
            "1. Are you fair in your payment of wages, return of debts owed, returning things borrowed, keeping of promises, providing the information necessary for people to do their jobs well and giving credit when credit is due? If not, where do you fall short?",
            "2. The verse above pertains to payment of debts; do you feel you have a debt of praise to an employee or boss that has done a job well?",
            "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 11: Don't be in Debt
    # ========================================
    {
        "id": 11,
        "title": "11. Don't be in Debt",
        "question": "Do I manage my finances well and avoid debt or pledging for others irresponsibly?",
        "verses": [
            {"ref": "Proverbs 22:7", "text": "7 The rich rules over the poor, And the borrower is servant to the lender."},
            {"ref": "Proverbs 22:26-27", "text": "26 Do not be one of those who shakes hands in a pledge, One of those who is surety for debts; 27 If you have nothing with which to pay, Why should he take away your bed from under you?"}
        ],
        "dig_deeper_questions": [
            "1. How can managing your finances well make you a better witness to others at work?",
            "2. How can managing your finances well make you a better employee/employer?",
            "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 12: Don't Devise Evil or Take Advantage
    # ========================================
    {
        "id": 12,
        "title": "12. Don't Devise Evil or Take Advantage",
        "question": "Do I plot against others (think about or plan to do something harmful to them)?",
        "verses": [
            {"ref": "Proverbs 3:29", "text": "29 Do not devise evil against your neighbor, For he dwells by you for safety's sake."},
            {"ref": "Proverbs 14:22", "text": "22 Do they not go astray who devise evil? But mercy and truth belong to those who devise good."},
            {"ref": "Proverbs 23:10-11", "text": "10 Do not remove the ancient landmark, Nor enter the fields of the fatherless; 11 For their Redeemer is mighty; He will plead their cause against you."},
            {"ref": "Proverbs 24:15-16", "text": "15 Do not lie in wait, O wicked man, against the dwelling of the righteous; Do not plunder his resting place; 16 For a righteous man may fall seven times And rise again, But the wicked shall fall by calamity."}
        ],
        "dig_deeper_questions": [
            "1. Have you ever acted to plot against someone? What motivated you to take this approach: anger, revenge or pride?",
            "2. Did this approach work out well for you?",
            "3. Proverbs 24:15-16 (the last verse in this section) notes how wicked men, will be thwarted if they try to devise evil against the righteous. Does this give you confidence not to worry about those that plot against you?",
            "4. If either acting to plot evil or worrying about those that plot against you is an issue, summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 13: Don't Strive
    # ========================================
    {
        "id": 13,
        "title": "13. Don't Strive",
        "question": "Do I start quarrels or easily get involved in quarrels?",
        "verses": [
            {"ref": "Proverbs 3:30", "text": "30 Do not strive with a man without cause, If he has done you no harm."},
            {"ref": "Proverbs 11:12", "text": "12 He who is devoid of wisdom despises his neighbor, But a man of understanding holds his peace."},
            {"ref": "Proverbs 11:29", "text": "29 He who troubles his own house will inherit the wind, And the fool will be servant to the wise of heart."},
            {"ref": "Proverbs 16:7", "text": "7 When a man's ways please the LORD, He makes even his enemies to be at peace with him."},
            {"ref": "Proverbs 16:14-15", "text": "14 As messengers of death is the king's wrath, But a wise man will appease it. 15 In the light of the king's face is life, And his favor is like a cloud of the latter rain."},
            {"ref": "Proverbs 17:1", "text": "1 Better is a dry morsel with quietness, Than a house full of feasting with strife."},
            {"ref": "Proverbs 17:9", "text": "9 He who covers a transgression seeks love, But he who repeats a matter separates friends."},
            {"ref": "Proverbs 18:18-19", "text": "18 Casting lots causes contentions to cease, And keeps the mighty apart. 19 A brother offended is harder to win than a strong city, And contentions are like the bars of a castle."},
            {"ref": "Proverbs 19:12", "text": "12 The king's wrath is like the roaring of a lion, But his favor is like dew on the grass."},
            {"ref": "Proverbs 20:2-3", "text": "2 The wrath of a king is like the roaring of a lion; Whoever provokes him to anger sins against his own life. 3 It is honorable for a man to stop striving, Since any fool can start a quarrel."},
            {"ref": "Proverbs 21:9", "text": "9 Better to dwell in a corner of a housetop, Than in a house shared with a contentious woman."},
            {"ref": "Proverbs 26:2", "text": "2 Like a flitting sparrow, like a flying swallow, So a curse without cause shall not alight."},
            {"ref": "Proverbs 26:20-21", "text": "20 Where there is no wood, the fire goes out; And where there is no talebearer, strife ceases. 21 As charcoal is to burning coals, and wood to fire, So is a contentious man to kindle strife."},
            {"ref": "Proverbs 28:25", "text": "25 He who is of a proud heart stirs up strife, But he who trusts in the LORD will be prospered."}
        ],
        "dig_deeper_questions": [
            "1. Does conflict make you uncomfortable or would you say, \"bring it on\"? Why do you think that is?",
            "2. What makes you get involved in arguments (your own or other's)?",
            "3. Why do you feel the need to stand your ground in an argument?",
            "4. If you backed down from an argument, how would you be perceived?",
            "5. Have you ever used \"casting lots\" to end a quarrel? Would you trust the Lord to direct the outcome and live peaceably with the result?",
            "6. What specific things can you do to avoid strife? List the things that stand out as most important to you, personally, from the verses above.",
            "7. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 14: Don't Have a Perverse Heart
    # ========================================
    {
        "id": 14,
        "title": "14. Don't Have a Perverse Heart",
        "question": "Do I often feel like my heart just isn't in the right place (filled with perverse thoughts, prideful or stubborn feelings, wicked intent, etc.)?",
        "verses": [
            {"ref": "Proverbs 11:20", "text": "20 Those who are of a perverse heart are an abomination to the LORD, But the blameless in their ways are His delight."},
            {"ref": "Proverbs 12:8", "text": "8 A man will be commended according to his wisdom, But he who is of a perverse heart will be despised."},
            {"ref": "Proverbs 14:2", "text": "2 He who walks in his uprightness fears the LORD, But he who is perverse in his ways despises Him."},
            {"ref": "Proverbs 17:3", "text": "3 The refining pot is for silver and the furnace for gold, But the LORD tests the hearts."},
            {"ref": "Proverbs 20:27", "text": "27 The spirit of a man is the lamp of the LORD, Searching all the inner depths of his heart."},
            {"ref": "Proverbs 21:4", "text": "4 A haughty look, a proud heart, And the plowing of the wicked are sin."},
            {"ref": "Proverbs 21:27", "text": "27 The sacrifice of the wicked is an abomination; How much more when he brings it with wicked intent!"},
            {"ref": "Proverbs 22:5", "text": "5 Thorns and snares are in the way of the perverse; He who guards his soul will be far from them."},
            {"ref": "Proverbs 27:19", "text": "19 As in water face reflects face, So a man's heart reveals the man."},
            {"ref": "Proverbs 28:14", "text": "14 Happy is the man who is always reverent, But he who hardens his heart will fall into calamity."},
            {"ref": "Proverbs 28:18", "text": "18 Whoever walks blamelessly will be saved, But he who is perverse in his ways will suddenly fall."}
        ],
        "dig_deeper_questions": [
            "1. Where does this attitude come from? Can you identify the root of the issue?",
            "2. What is the opposite of a perverse heart (see verses above)?",
            "3. What can you do to overcome this attitude?",
            "4. If you think your boss/coworker has this issue, what makes you think so? What behaviors lead you to believe this?",
            "5. How does this impact your job?",
            "6. What has been your response?",
            "7. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 15: Be an Excellent Wife
    # ========================================
    {
        "id": 15,
        "title": "15. Be an Excellent Wife",
        "question": "Would I say I'm an excellent wife/spouse? (If applicable, or substitute 'spouse/partner')",
        "verses": [
            {"ref": "Proverbs 12:4", "text": "4 An excellent wife is the crown of her husband, But she who causes shame is like rottenness in his bones."},
            {"ref": "Proverbs 18:22", "text": "22 He who finds a wife finds a good thing, And obtains favor from the LORD."},
            {"ref": "Proverbs 19:14", "text": "14 Houses and riches are an inheritance from fathers, But a prudent wife is from the LORD."},
            {"ref": "Proverbs 31:10-31", "text": "10 Who can find a virtuous wife? For her worth is far above rubies. 11 The heart of her husband safely trusts her; So he will have no lack of gain. 12 She does him good and not evil All the days of her life. 13 She seeks wool and flax, And willingly works with her hands. 14 She is like the merchant ships, She brings her food from afar. 15 She also rises while it is yet night, And provides food for her household, And a portion for her maidservants. 16 She considers a field and buys it; From her profits she plants a vineyard. 17 She girds herself with strength, And strengthens her arms. 18 She perceives that her merchandise is good, And her lamp does not go out by night. 19 She stretches out her hands to the distaff, And her hand holds the spindle. 20 She extends her hand to the poor, Yes, she reaches out her hands to the needy. 21 She is not afraid of snow for her household, For all her household is clothed with scarlet. 22 She makes tapestry for herself; Her clothing is fine linen and purple. 23 Her husband is known in the gates, When he sits among the elders of the land. 24 She makes linen garments and sells them, And supplies sashes for the merchants. 25 Strength and honor are her clothing; She shall rejoice in time to come. 26 She opens her mouth with wisdom, And on her tongue is the law of kindness. 27 She watches over the ways of her household, And does not eat the bread of idleness. 28 Her children rise up and call her blessed; Her husband also, and he praises her: 29 \"Many daughters have done well, But you excel them all.\" 30 Charm is deceitful and beauty is passing, But a woman who fears the LORD, she shall be praised. 31 Give her of the fruit of her hands, And let her own works praise her in the gates."},
            {"ref": "Proverbs 25:24", "text": "24 It is better to dwell in a corner of a housetop, Than in a house shared with a contentious woman."}
        ],
        "dig_deeper_questions": [
            "1. Have you ever considered the value you have as an excellent vs. a shameful wife/spouse? Describe how you have added value to your spouse.",
            "2. How can your excellence as a wife/spouse help those beyond your spouse: your household, your work, and your community?",
            "3. How can (has) being a contentious wife be(en) a detriment to your spouse?",
            "4. Where does that ability to be excellent come from (you or the Lord)?",
            "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 16: Avoid Anger
    # ========================================
    {
        "id": 16,
        "title": "16. Avoid Anger",
        "question": "Do I let anger build up inside or boil over into outbursts?",
        "verses": [
            {"ref": "Proverbs 12:16", "text": "16 A fool's wrath is known at once, But a prudent man covers shame."},
            {"ref": "Proverbs 14:10", "text": "10 The heart knows its own bitterness, And a stranger does not share its joy."},
            {"ref": "Proverbs 14:16-17", "text": "16 A wise man fears and departs from evil, But a fool rages and is self-confident. 17 A quick-tempered man acts foolishly, And a man of wicked intentions is hated."},
            {"ref": "Proverbs 14:29", "text": "29 He who is slow to wrath has great understanding, But he who is impulsive exalts folly."},
            {"ref": "Proverbs 15:18", "text": "18 A wrathful man stirs up strife, But he who is slow to anger allays contention"},
            {"ref": "Proverbs 16:32", "text": "32 He who is slow to anger is better than the mighty, And he who rules his spirit than he who takes a city."},
            {"ref": "Proverbs 19:11", "text": "11 The discretion of a man makes him slow to anger, And his glory is to overlook a transgression."},
            {"ref": "Proverbs 19:19", "text": "19 A man of great wrath will suffer punishment; For if you rescue him, you will have to do it again."},
            {"ref": "Proverbs 21:29", "text": "29 A wicked man hardens his face, But as for the upright, he establishes his way."},
            {"ref": "Proverbs 22:24-25", "text": "24 Make no friendship with an angry man, And with a furious man do not go, 25 Lest you learn his ways And set a snare for your soul."},
            {"ref": "Proverbs 27:15-16", "text": "15 A continual dripping on a very rainy day And a contentious woman are alike; 16 Whoever restrains her restrains the wind, And grasps oil with his right hand."},
            {"ref": "Proverbs 29:22", "text": "22 An angry man stirs up strife, And a furious man abounds in transgression."}
        ],
        "dig_deeper_questions": [
            "1. Has your anger ever made you look foolish?",
            "2. Has your anger ever hurt someone, irritated (continual dripping) or made someone mad at you?",
            "3. Have you ever let a friend's anger make you angry?",
            "4. Why is your heart bitter/contentious?",
            "5. What do the verses below teach you that can you do to control your anger?",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 17: Avoid Anxiety
    # ========================================
    {
        "id": 17,
        "title": "17. Avoid Anxiety",
        "question": "Would I describe myself as overly anxious or easily depressed?",
        "verses": [
            {"ref": "Proverbs 12:25", "text": "25 Anxiety in the heart of man causes depression, But a good word makes it glad."}
        ],
        "dig_deeper_questions": [
            "1. Who do you need \"a good word\" from? Will you tell them that?",
            "2. Do you give \"good words\"? Whom can you give \"a good word\" to?",
            "3. Can you find other verses about worry and anxiety throughout the Bible? (Try: Matthew 6:25, 27, 28, 31, 34; Matthew 10:19; Mark 3:11; Luke 12:11, 22, 25.)",
            "4. How do you deal with your anxiety? What helps put things in perspective for you?",
            "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 18: Don't Abuse Alcohol
    # ========================================
    {
        "id": 18,
        "title": "18. Don't Abuse Alcohol",
        "question": "Do I allow substance abuse to affect my life or the life of others?",
        "verses": [
            {"ref": "Proverbs 20:1", "text": "1 Wine is a mocker, Strong drink is a brawler, And whoever is led astray by it is not wise."},
            {"ref": "Proverbs 21:17", "text": "17 He who loves pleasure will be a poor man; He who loves wine and oil will not be rich."},
            {"ref": "Proverbs 23:29-35", "text": "29 Who has woe? Who has sorrow? Who has contentions? Who has complaints? Who has wounds without cause? Who has redness of eyes? 30 Those who linger long at the wine, Those who go in search of mixed wine. 31 Do not look on the wine when it is red, When it sparkles in the cup, When it swirls around smoothly; 32 At the last it bites like a serpent, And stings like a viper. 33 Your eyes will see strange things, And your heart will utter perverse things. 34 Yes, you will be like one who lies down in the midst of the sea, Or like one who lies at the top of the mast, saying: 35 \"They have struck me, but I was not hurt; They have beaten me, but I did not feel it. When shall I awake, that I may seek another drink?\""},
            {"ref": "Proverbs 31:4-7", "text": "4 It is not for kings, O Lemuel, It is not for kings to drink wine, Nor for princes intoxicating drink; 5 Lest they drink and forget the law, And pervert the justice of all the afflicted. 6 Give strong drink to him who is perishing, And wine to those who are bitter of heart. 7 Let him drink and forget his poverty, And remember his misery no more."}
        ],
        "dig_deeper_questions": []
    },
    
    # ========================================
    # TOPIC 19: Don't Envy the Oppressors
    # ========================================
    {
        "id": 19,
        "title": "19. Don't Envy the Oppressors",
        "question": "Do I envy (or imitate) those who get ahead, even if by dishonest means?",
        "verses": [
            {"ref": "Proverbs 3:31-33", "text": "31 Do not envy the oppressor, And choose none of his ways; 32 For the perverse person is an abomination to the LORD, But His secret counsel is with the upright. 33 The curse of the LORD is on the house of the wicked, But He blesses the home of the just."},
            {"ref": "Proverbs 12:12", "text": "12 The wicked covet the catch of evil men, But the root of the righteous yields fruit."},
            {"ref": "Proverbs 24:1-2", "text": "1 Do not be envious of evil men, Nor desire to be with them; 2 For their heart devises violence, And their lips talk of troublemaking."},
            {"ref": "Proverbs 24:19-20", "text": "19 Do not fret because of evildoers, Nor be envious of the wicked; 20 For there will be no prospect for the evil man; The lamp of the wicked will be put out."},
            {"ref": "Proverbs 28:3", "text": "3 A poor man who oppresses the poor Is like a driving rain which leaves no food."}
        ],
        "dig_deeper_questions": [
            "1. Do these verses convince you of your need to put those thoughts of envy behind you? Why or why not?",
            "2. Have you ever witnessed the \"fall\" of someone who got ahead by dishonest means or by oppressing others? Some are never \"caught\" in this life, but can you list some consequences for those that are caught; for themselves, for their families?",
            "3. What do you need to do to get beyond this thought-pattern of envy/coveting? The Bible has plenty more to say about this. You might need to research some more versus and quote them here.",
            "4. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 20: Don't Envy/Be Jealous
    # ========================================
    {
        "id": 20,
        "title": "20. Don't Envy/Be Jealous",
        "question": "Am I jealous of someone or something they have?",
        "verses": [
            {"ref": "Proverbs 14:30", "text": "30 A sound heart is life to the body, But envy is rottenness to the bones."},
            {"ref": "Proverbs 27:3-4", "text": "3 A stone is heavy and sand is weighty, But a fool's wrath is heavier than both of them. 4 Wrath is cruel and anger a torrent, But who is able to stand before jealousy?"}
        ],
        "dig_deeper_questions": [
            "1. Have you ever thought that being jealous of someone is worse than being angry with him or her?",
            "2. Have you ever been the object of someone else's jealousy? How did that make you feel or impact your life?",
            "3. If you are the object of someone's jealousy, how will you deal with this?",
            "4. Are you jealous of someone and need to release them (just as you would need to forgive them if you were angry)? If so, who and how will you do this?",
            "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
        # ========================================
    # TOPIC 21: Don't Reward Evil
    # ========================================
    {
        "id": 21,
        "title": "21. Don't Reward Evil",
        "question": "Have I cheered on someone who did something bad or made fun of someone who was doing something good?",
        "verses": [
            {"ref": "Proverbs 17:13", "text": "13 Whoever rewards evil for good, Evil will not depart from his house."},
            {"ref": "Proverbs 17:15", "text": "15 He who justifies the wicked, and he who condemns the just, Both of them alike are an abomination to the LORD."},
            {"ref": "Proverbs 17:26", "text": "26 Also, to punish the righteous is not good, Nor to strike princes for their uprightness."},
            {"ref": "Proverbs 18:5", "text": "5 It is not good to show partiality to the wicked, Or to overthrow the righteous in judgment."}
        ],
        "dig_deeper_questions": [
            "1. What does the Lord think of those that reward evil, justify the wicked, show them partiality or punish the righteous?",
            "2. How can participating in this behavior affect us if we are supervisors? What message does it send?",
            "3. If your boss struggles in this area, do you think they realize that they are giving this impression?",
            "4. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 22: Be Humble
    # ========================================
    {
        "id": 22,
        "title": "22. Be Humble",
        "question": "Am I humble?",
        "verses": [
            {"ref": "Proverbs 11:2", "text": "2 When pride comes, then comes shame; But with the humble is wisdom."},
            {"ref": "Proverbs 12:9", "text": "9 Better is the one who is slighted but has a servant, Than he who honors himself but lacks bread."},
            {"ref": "Proverbs 13:10", "text": "10 By pride comes nothing but strife, But with the well-advised is wisdom."},
            {"ref": "Proverbs 14:3", "text": "3 In the mouth of a fool is a rod of pride, But the lips of the wise will preserve them."},
            {"ref": "Proverbs 15:25", "text": "25 The LORD will destroy the house of the proud, But He will establish the boundary of the widow."},
            {"ref": "Proverbs 15:33", "text": "33 The fear of the LORD is the instruction of wisdom, And before honor is humility."},
            {"ref": "Proverbs 16:5", "text": "5 Everyone proud in heart is an abomination to the LORD; Though they join forces, none will go unpunished."},
            {"ref": "Proverbs 16:18-19", "text": "18 Pride goes before destruction, And a haughty spirit before a fall. 19 Better to be of a humble spirit with the lowly, Than to divide the spoil with the proud."},
            {"ref": "Proverbs 18:12", "text": "12 Before destruction the heart of a man is haughty, And before honor is humility."},
            {"ref": "Proverbs 20:6", "text": "6 Most men will proclaim each his own goodness, But who can find a faithful man?"},
            {"ref": "Proverbs 20:9", "text": "9 Who can say, \"I have made my heart clean, I am pure from my sin\"?"},
            {"ref": "Proverbs 22:4", "text": "4 By humility and the fear of the LORD Are riches and honor and life."},
            {"ref": "Proverbs 25:6-7", "text": "6 Do not exalt yourself in the presence of the king, And do not stand in the place of the great; 7 For it is better that he say to you, Come up here,\" Than that you should be put lower in the presence of the prince, Whom your eyes have seen."},
            {"ref": "Proverbs 27:1-2", "text": "1 Do not boast about tomorrow, For you do not know what a day may bring forth. 2 Let another man praise you, and not your own mouth; A stranger, and not your own lips."},
            {"ref": "Proverbs 29:23", "text": "23 A man's pride will bring him low, But the humble in spirit will retain honor."}
        ],
        "dig_deeper_questions": [
            "1. How does the parable below and the verses above contradict the worldly wisdom that to have success in your career you have to be aggressively promoting yourself?\n\nLuke 14:7-11 NIV\n7 When he noticed how the guests picked the places of honor at the table, he told them this parable: 8 \"When someone invites you to a wedding feast, do not take the place of honor, for a person more distinguished than you may have been invited. 9 If so, the host who invited both of you will come and say to you, 'Give this person your seat.' Then, humiliated, you will have to take the least important place.10 But when you are invited, take the lowest place, so that when your host comes, he will say to you, 'Friend, move up to a better place.' Then you will be honored in the presence of all the other guests. 11 For all those who exalt themselves will be humbled, and those who humble themselves will be exalted.\"",
            "2. It is hard to advise people to be humble in a competitive organization. Can you be humble yet still get noticed, get ahead? Do you think this advice is misguided or will it work?",
            "3. How much humility will it take to admit to co-workers, employees, your boss, that you have been wrong in one or more of your behaviors/management techniques?",
            "4. Can you prepare a statement that communicates your admission of failure(s)? Let others know you are humble enough to \"start over\", admit you know you have failed and what you are working on improving (so that they can help hold you accountable). See Chapter 6 - Communicating Issues to help with this exercise.",
            "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 23: Put Away A Deceitful Mouth
    # ========================================
    {
        "id": 23,
        "title": "23. Put Away A Deceitful Mouth",
        "question": "Do I lie or act deceitfully, tell tales, am slanderous, or falsely flatter others?",
        "verses": [
            {"ref": "Proverbs 4:24", "text": "24 Put away from you a deceitful mouth, And put perverse lips far from you."},
            {"ref": "Proverbs 10:11-12", "text": "11 The mouth of the righteous is a well of life, But violence covers the mouth of the wicked. 12 Hatred stirs up strife, But love covers all sins."},
            {"ref": "Proverbs 10:18-21", "text": "18 Whoever hides hatred has lying lips, And whoever spreads slander is a fool. 19 In the multitude of words sin is not lacking, But he who restrains his lips is wise. 20 The tongue of the righteous is choice silver; The heart of the wicked is worth little. 21 The lips of the righteous feed many, But fools die for lack of wisdom."},
            {"ref": "Proverbs 11:9-11", "text": "9 The hypocrite with his mouth destroys his neighbor, But through knowledge the righteous will be delivered. 10 When it goes well with the righteous, the city rejoices; And when the wicked perish, there is jubilation. 11 By the blessing of the upright the city is exalted, But it is overthrown by the mouth of the wicked."},
            {"ref": "Proverbs 12:13-14", "text": "13 The wicked is ensnared by the transgression of his lips, But the righteous will come through trouble. 14 A man will be satisfied with good by the fruit of his mouth, And the recompense of a man's hands will be rendered to him."},
            {"ref": "Proverbs 12:17-20", "text": "17 He who speaks truth declares righteousness, But a false witness, deceit. 18 There is one who speaks like the piercings of a sword, But the tongue of the wise promotes health. 19 The truthful lip shall be established forever, But a lying tongue is but for a moment. 20 Deceit is in the heart of those who devise evil, But counselors of peace have joy."},
            {"ref": "Proverbs 12:22", "text": "22 Lying lips are an abomination to the LORD, But those who deal truthfully are His delight."},
            {"ref": "Proverbs 13:5", "text": "5 A righteous man hates lying, But a wicked man is loathsome and comes to shame."},
            {"ref": "Proverbs 14:5", "text": "5 A faithful witness does not lie, But a false witness will utter lies."},
            {"ref": "Proverbs 14:25", "text": "25 A true witness delivers souls, But a deceitful witness speaks lies."},
            {"ref": "Proverbs 15:4", "text": "4 A wholesome tongue is a tree of life, But perverseness in it breaks the spirit."},
            {"ref": "Proverbs 16:13", "text": "13 Righteous lips are the delight of kings, And they love him who speaks what is right."},
            {"ref": "Proverbs 17:7", "text": "7 Excellent speech is not becoming to a fool, Much less lying lips to a prince."},
            {"ref": "Proverbs 17:20", "text": "20 He who has a deceitful heart finds no good, And he who has a perverse tongue falls into evil."},
            {"ref": "Proverbs 18:20-21", "text": "20 A man's stomach shall be satisfied from the fruit of his mouth; From the produce of his lips he shall be filled. 21 Death and life are in the power of the tongue, And those who love it will eat its fruit."},
            {"ref": "Proverbs 19:5", "text": "5 A false witness will not go unpunished, And he who speaks lies will not escape."},
            {"ref": "Proverbs 19:9", "text": "9 A false witness will not go unpunished, And he who speaks lies shall perish."},
            {"ref": "Proverbs 19:28", "text": "28 A disreputable witness scorns justice, And the mouth of the wicked"},
            {"ref": "Proverbs 21:6", "text": "6 Getting treasures by a lying tongue Is the fleeting fantasy of those who seek death."},
            {"ref": "Proverbs 24:28", "text": "28 Do not be a witness against your neighbor without cause, For would you deceive with your lips?"},
            {"ref": "Proverbs 25:18", "text": "18 A man who bears false witness against his neighbor Is like a club, a sword, and a sharp arrow."},
            {"ref": "Proverbs 26:18-19", "text": "18 Like a madman who throws firebrands, arrows, and death, 19 Is the man who deceives his neighbor, And says, \"I was only joking!\""},
            {"ref": "Proverbs 26:22-28", "text": "22 The words of a talebearer are like tasty trifles, And they go down into the inmost body. 23 Fervent lips with a wicked heart Are like earthenware covered with silver dross. 24 He who hates, disguises it with his lips, And lays up deceit within himself; 25 When he speaks kindly, do not believe him, For there are seven abominations in his heart; 26 Though his hatred is covered by deceit, His wickedness will be revealed before the assembly. 27 Whoever digs a pit will fall into it, And he who rolls a stone will have it roll back on him. 28 A lying tongue hates those who are crushed by it, And a flattering mouth works ruin."},
            {"ref": "Proverbs 28:23", "text": "23 He who rebukes a man will find more favor afterward Than he who flatters with the tongue."},
            {"ref": "Proverbs 29:5", "text": "5 A man who flatters his neighbor Spreads a net for his feet."},
            {"ref": "Proverbs 30:8", "text": "8 Remove falsehood and lies far from me; Give me neither poverty nor riches— Feed me with the food allotted to me;"},
            {"ref": "Proverbs 30:10", "text": "10 Do not malign a servant to his master, Lest he curse you, and you be found guilty."}
        ],
        "dig_deeper_questions": [
            "1. Your speech or what you say (or don't say) can reveal a lot about you. Do you have more of a problem with speaking truthfully (versus deceitfully; telling lies or flattering falsely), speaking hypocritically, speaking positively (versus negatively) or perhaps holding your tongue when you shouldn't speak?",
            "2. Go back and underline the verses/passages above that relate to the issue you struggle with the most.",
            "3. How has this contributed to your \"work-life\" issues? (Maybe i.e., you can't trust your co-worker that is a false flatterer).",
            "4. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 24: Let Your Ways Be Established
    # ========================================
    {
        "id": 24,
        "title": "24. Let Your Ways Be Established",
        "question": "Am I known for being unwavering in my principles (having integrity)?",
        "verses": [
            {"ref": "Proverbs 4:25-27", "text": "25 Let your eyes look straight ahead, And your eyelids look right before you. 26 Ponder the path of your feet, And let all your ways be established. 27 Do not turn to the right or the left; Remove your foot from evil."},
            {"ref": "Proverbs 10:9-10", "text": "9 He who walks with integrity walks securely, But he who perverts his ways will become known. 10 He who winks with the eye causes trouble, But a prating fool will fall."},
            {"ref": "Proverbs 11:3", "text": "3 The integrity of the upright will guide them, But the perversity of the unfaithful will destroy them."},
            {"ref": "Proverbs 14:15", "text": "15 The simple believes every word, But the prudent considers well his steps."},
            {"ref": "Proverbs 16:3", "text": "3 Commit your works to the LORD, And your thoughts will be established."},
            {"ref": "Proverbs 16:17", "text": "17 The highway of the upright is to depart from evil; He who keeps his way preserves his soul."},
            {"ref": "Proverbs 20:7", "text": "7 The righteous man walks in his integrity; His children are blessed after him."},
            {"ref": "Proverbs 20:11", "text": "11 Even a child is known by his deeds, Whether what he does is pure and right."},
            {"ref": "Proverbs 21:29", "text": "29 A wicked man hardens his face, But as for the upright, he establishes his way."},
            {"ref": "Proverbs 22:1", "text": "1 A good name is to be chosen rather than great riches, Loving favor rather than silver and gold."},
            {"ref": "Proverbs 22:29", "text": "29 Do you see a man who excels in his work? He will stand before kings; He will not stand before unknown men."},
            {"ref": "Proverbs 25:26", "text": "26 A righteous man who falters before the wicked Is like a murky spring and a polluted well."},
            {"ref": "Proverbs 25:28", "text": "28 Whoever has no rule over his own spirit Is like a city broken down, without walls."},
            {"ref": "Proverbs 27:7-8", "text": "7 A satisfied soul loathes the honeycomb, But to a hungry soul every bitter thing is sweet. 8 Like a bird that wanders from its nest Is a man who wanders from his place."},
            {"ref": "Proverbs 27:21", "text": "21 The refining pot is for silver and the furnace for gold, And a man is valued by what others say of him."},
            {"ref": "Proverbs 28:6", "text": "6 Better is the poor who walks in his integrity Than one perverse in his ways, though he be rich."}
        ],
        "dig_deeper_questions": [
            "1. Unwavering, considered, upright, of good reputation, excellent, unfaltering, controlled, satisfied, having integrity, principled, rooted, do these adjectives from the verses above make you want to be known as being established in your ways?",
            "2. How hard is it to hold steadfast to your values in your workplace?",
            "3. Are you ever chided for holding firm to your values?",
            "4. If you are constantly being challenged by the ethics of the company, the owner, the management, your boss, co-workers etc., is this the right place for you? Can you be a good example by staying or should you remove yourself from the temptation to conform?",
            "5. Do you respect others when they hold their ground or are predictable in their response? Give an example/name a person that comes to mind that has a reputation like this:",
            "6. Does your mood often affect your response, causing others to others to perceive you \"turn to the right or the left\"; so that they do not know where you will be coming from?",
            "7. Do you have \"situational ethics\", that is, have different values depending on the situation or who is involved? i.e., You insist on having a good work life balance for yourself but don't seem to notice when your employees are staying late to accomplish their tasks or vice versa.",
            "8. Do you feel too predictable sometimes? Do you think your steadfast, righteous manner makes you appear boring? How can these verses help you get past this self-criticism?",
            "9. If you, or someone you know or work with has a character flaw in this area, summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 25: Avoid Immoral Women
    # ========================================
    {
        "id": 25,
        "title": "25. Avoid Immoral Women",
        "question": "Do I exercise self-control over my sexual temptations?",
        "verses": [
            {"ref": "Proverbs 2:16-19", "text": "16 To deliver you from the immoral woman, From the seductress who flatters with her words, 17 Who forsakes the companion of her youth, And forgets the covenant of her God. 18 For her house leads down to death, And her paths to the dead; 19 None who go to her return, Nor do they regain the paths of life—"},
            {"ref": "Proverbs 5:1-11", "text": "1 My son, pay attention to my wisdom; Lend your ear to my understanding, 2 That you may preserve discretion, And your lips may keep knowledge. 3 For the lips of an immoral woman drip honey, And her mouth is smoother than oil; 4 But in the end she is bitter as wormwood, Sharp as a two-edged sword. 5 Her feet go down to death, Her steps lay hold of hell. 6 Lest you ponder her path of life— Her ways are unstable; You do not know them. 7 Therefore hear me now, my children, And do not depart from the words of my mouth. 8 Remove your way far from her, And do not go near the door of her house, 9 Lest you give your honor to others, And your years to the cruel one; 10 Lest aliens be filled with your wealth, And your labors go to the house of a foreigner; 11 And you mourn at last, When your flesh and your body are consumed,"},
            {"ref": "Proverbs 5:15-20", "text": "15 Drink water from your own cistern, And running water from your own well. 16 Should your fountains be dispersed abroad, Streams of water in the streets? 17 Let them be only your own, And not for strangers with you. 18 Let your fountain be blessed, And rejoice with the wife of your youth. 19 As a loving deer and a graceful doe, Let her breasts satisfy you at all times; And always be enraptured with her love. 20 For why should you, my son, be enraptured by an immoral woman, And be embraced in the arms of a seductress?"},
            {"ref": "Proverbs 6:24-35", "text": "24 To keep you from the evil woman, From the flattering tongue of a seductress. 25 Do not lust after her beauty in your heart, Nor let her allure you with her eyelids. 26 For by means of a harlot A man is reduced to a crust of bread; And an adulteress will prey upon his precious life. 27 Can a man take fire to his bosom, And his clothes not be burned? 28 Can one walk on hot coals, And his feet not be seared? 29 So is he who goes in to his neighbor's wife; Whoever touches her shall not be innocent. 30 People do not despise a thief If he steals to satisfy himself when he is starving. 31 Yet when he is found, he must restore sevenfold; He may have to give up all the substance of his house. 32 Whoever commits adultery with a woman lacks understanding; He who does so destroys his own soul. 33 Wounds and dishonor he will get, And his reproach will not be wiped away. 34 For jealousy is a husband's fury; Therefore he will not spare in the day of vengeance. 35 He will accept no recompense, Nor will he be appeased though you give many gifts."},
            {"ref": "Proverbs 7:1-27", "text": "1 My son, keep my words, And treasure my commands within you. 2 Keep my commands and live, And my law as the apple of your eye. 3 Bind them on your fingers; Write them on the tablet of your heart. 4 Say to wisdom, \"You are my sister,\" And call understanding your nearest kin, 5 That they may keep you from the immoral woman, From the seductress who flatters with her words. 6 For at the window of my house I looked through my lattice, 7 And saw among the simple, I perceived among the youths, A young man devoid of understanding, 8 Passing along the street near her corner; And he took the path to her house 9 In the twilight, in the evening, In the black and dark night. 10 And there a woman met him, With the attire of a harlot, and a crafty heart. 11 She was loud and rebellious, Her feet would not stay at home. 12 At times she was outside, at times in the open square, Lurking at every corner. 13 So she caught him and kissed him; With an impudent face she said to him: 14 \"I have peace offerings with me; Today I have paid my vows. 15 So I came out to meet you, Diligently to seek your face, And I have found you. 16 I have spread my bed with tapestry, Colored coverings of Egyptian linen. 17 I have perfumed my bed With myrrh, aloes, and cinnamon. 18 Come, let us take our fill of love until morning; Let us delight ourselves with love. 19 For my husband is not at home; He has gone on a long journey; 20 He has taken a bag of money with him, And will come home on the appointed day.\" 21 With her enticing speech she caused him to yield, With her flattering lips she seduced him. 22 Immediately he went after her, as an ox goes to the slaughter, Or as a fool to the correction of the stocks, 23 Till an arrow struck his liver. As a bird hastens to the snare, He did not know it would cost his life. 24 Now therefore, listen to me, my children; Pay attention to the words of my mouth: 25 Do not let your heart turn aside to her ways, Do not stray into her paths; 26 For she has cast down many wounded, And all who were slain by her were strong men. 27 Her house is the way to hell, Descending to the chambers of death."},
            {"ref": "Proverbs 9:13-18", "text": "13 A foolish woman is clamorous; She is simple, and knows nothing. 14 For she sits at the door of her house, On a seat by the highest places of the city, 15 To call to those who pass by, Who go straight on their way: 16 \"Whoever is simple, let him turn in here\"; And as for him who lacks understanding, she says to him, 17 \"Stolen water is sweet, And bread eaten in secret is pleasant.\" 18 But he does not know that the dead are there, That her guests are in the depths of hell."},
            {"ref": "Proverbs 22:14", "text": "14 The mouth of an immoral woman is a deep pit; He who is abhorred by the LORD will fall there."},
            {"ref": "Proverbs 23:27-28", "text": "27 For a harlot is a deep pit, And a seductress is a narrow well. 28 She also lies in wait as for a victim, And increases the unfaithful among men."},
            {"ref": "Proverbs 29:3", "text": "3 Whoever loves wisdom makes his father rejoice, But a companion of harlots wastes his wealth."},
            {"ref": "Proverbs 30:20", "text": "20 This is the way of an adulterous woman: She eats and wipes her mouth, And says, \"I have done no wickedness.\""}
        ],
        "dig_deeper_questions": [
            "1. Talking about sex is uncomfortable, but the Bible gives plenty of advice against the seductress. As a woman, I think if Solomon were speaking to his daughter, he'd equally warn her of the seducer (male). Regardless, if you are struggling with sexual temptation at work or in your personal life, how do these verses drive home the point that our temptations are bound to destroy us?",
            "2. Is your work environment a source of sexual temptation?",
            "3. What helps you deal with temptations in this area?",
            "4. Do you need to remove yourself from temptations or perhaps address/confront a sexually charged environment at work? When?",
            "5. Do you know of an instance where sexual temptation at work has caused an issue for you or someone else? Was it handled well?",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 26: Don't Misplace your Confidence
    # ========================================
    {
        "id": 26,
        "title": "26. Don't Misplace your Confidence",
        "question": "Do I often misjudge the faithfulness/character of others?",
        "verses": [
            {"ref": "Proverbs 25:19", "text": "19 Confidence in an unfaithful man in time of trouble Is like a bad tooth and a foot out of joint."},
            {"ref": "Proverbs 23:9", "text": "9 Do not speak in the hearing of a fool, For he will despise the wisdom of your words."},
            {"ref": "Proverbs 26:6-11", "text": "6 He who sends a message by the hand of a fool Cuts off his own feet and drinks violence. 7 Like the legs of the lame that hang limp Is a proverb in the mouth of fools. 8 Like one who binds a stone in a sling Is he who gives honor to a fool. 9 Like a thorn that goes into the hand of a drunkard Is a proverb in the mouth of fools. 10 The great God who formed everything Gives the fool his hire and the transgressor his wages. 11 As a dog returns to his own vomit, So a fool repeats his folly."}
        ],
        "dig_deeper_questions": [
            "1. Have you been hurt by misjudging another's character/reliability?",
            "2. Like the verses above, have you put your confidence in a person that has proved unfaithful, or wasted your words of wisdom on a fool? Give an example. Include: What did you do? What did you learn from this experience?",
            "3. Are you surprised to see that the Bible actually portrays this as a character fault in you, the one placing the confidence in the other person?",
            "4. Can you think of examples in Christ's life where he was hurt by an unfaithful or foolish man?\n\nProverbs caution us against placing our trust in a fool but remember that often those that are Christ's followers are labelled fools in this world. Be careful when you judge someone a fool. Think about how foolish Christ himself seemed to the \"righteous\" when he ate with sinners, spoke to a Samaritan woman, etc.\n\nHere's a tough question:",
            "5. How will you choose to respond to the unfaithful or fools? Are they still redeemable? (Perhaps the next section will help as it describes even more the fool that these proverbs warn us about).",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 27: Avoid Folly
    # ========================================
    {
        "id": 27,
        "title": "27. Avoid Folly",
        "question": "Do I allow my decisions, behavior or attitude to make me appear foolish/unwise?",
        "verses": [
            {"ref": "Proverbs 5:21-23", "text": "21 For the ways of man are before the eyes of the LORD, And He ponders all his paths. 22 His own iniquities entrap the wicked man, And he is caught in the cords of his sin. 23 He shall die for lack of instruction, And in the greatness of his folly he shall go astray."},
            {"ref": "Proverbs 12:23", "text": "23 A prudent man conceals knowledge, But the heart of fools proclaims foolishness."},
            {"ref": "Proverbs 13:16", "text": "16 Every prudent man acts with knowledge, But a fool lays open his folly."},
            {"ref": "Proverbs 14:1", "text": "1 The wise woman builds her house, But the foolish pulls it down with her hands."},
            {"ref": "Proverbs 14:7-9", "text": "7 Go from the presence of a foolish man, When you do not perceive in him the lips of knowledge. 8 The wisdom of the prudent is to understand his way, But the folly of fools is deceit. 9 Fools mock at sin, But among the upright there is favor."},
            {"ref": "Proverbs 14:7-24", "text": "7 Go from the presence of a foolish man, When you do not perceive in him the lips of knowledge. 8 The wisdom of the prudent is to understand his way, But the folly of fools is deceit. 9 Fools mock at sin, But among the upright there is favor."},
            {"ref": "Proverbs 14:15-18", "text": "15 The simple believes every word, But the prudent considers well his steps. 16 A wise man fears and departs from evil, But a fool rages and is self-confident. 17 A quick-tempered man acts foolishly, And a man of wicked intentions is hated. 18 The simple inherit folly, But the prudent are crowned with knowledge."},
            {"ref": "Proverbs 14:24", "text": "24 The crown of the wise is their riches, But the foolishness of fools is folly."},
            {"ref": "Proverbs 14:33", "text": "33 Wisdom rests in the heart of him who has understanding, But what is in the heart of fools is made known."},
            {"ref": "Proverbs 15:20-21", "text": "20 A wise son makes a father glad, But a foolish man despises his mother. 21 Folly is joy to him who is destitute of discernment, But a man of understanding walks uprightly."},
            {"ref": "Proverbs 17:12", "text": "12 Let a man meet a bear robbed of her cubs, Rather than a fool in his folly."},
            {"ref": "Proverbs 17:16", "text": "16 Why is there in the hand of a fool the purchase price of wisdom, Since he has no heart for it?"},
            {"ref": "Proverbs 17:24-25", "text": "24 Wisdom is in the sight of him who has understanding, But the eyes of a fool are on the ends of the earth. 25 A foolish son is a grief to his father, And bitterness to her who bore him."},
            {"ref": "Proverbs 18:2-3", "text": "2 A fool has no delight in understanding, But in expressing his own heart. 3 When the wicked comes, contempt comes also; And with dishonor comes reproach."},
            {"ref": "Proverbs 19:10", "text": "10 Luxury is not fitting for a fool, Much less for a servant to rule over princes."},
            {"ref": "Proverbs 21:20", "text": "20 There is desirable treasure, And oil in the dwelling of the wise, But a foolish man squanders it."},
            {"ref": "Proverbs 22:3", "text": "3 A prudent man foresees evil and hides himself, But the simple pass on and are punished."},
            {"ref": "Proverbs 27:12", "text": "12 A prudent man foresees evil and hides himself; The simple pass on and are punished."},
            {"ref": "Proverbs 27:22", "text": "22 Though you grind a fool in a mortar with a pestle along with crushed grain, Yet his foolishness will not depart from him."}
        ],
        "dig_deeper_questions": [
            "1. The verses above teach us that the foolish:\n• Sin\n• Don't accept instruction\n• Proclaim their foolishness\n• Deceive\n• Mock sin\n• Always seems right in their own eyes\n• Believe everything they hear\n• Rage\n• Are self-confident\n• Despise their mother\n• Consider folly their joy\n• Lack discernment\n• Have no delight in understanding but express their own heart bringing grief, contempt, and dishonor\n• Squander what they have\n• Don't foresee evil\n• Are punished\n• Are pains and never seem to learn\n\nI bet you could almost immediately think of a name of a person to place besides each bullet…couldn't you? Resist, however, and circle those bullets that describe you instead.",
            "2. How can you avoid appearing foolish?",
            "3. In Proverbs 26:4-5 we see two verses about how to deal with a fool. What can we learn from them?",
            "4. Perhaps we should not stoop to a fool's level, getting drawn into an argument or stubborn battle, but instead answer them in the way their foolishness requires, not let them get away with their foolishness. Is this what you read?",
            "5. If you have a reputation for acting foolishly, how will you change this reputation?",
            "6. How will you handle foolishness in others?",
            "7. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 28: Don't Pledge Surety
    # ========================================
    {
        "id": 28,
        "title": "28. Don't Pledge Surety",
        "question": "Do I find myself putting my neck on the line for those who don't do what they said they would after all? (Taken advantage of)",
        "verses": [
            {"ref": "Proverbs 6:1-5", "text": "1 My son, if you become surety for your friend, If you have shaken hands in pledge for a stranger, 2 You are snared by the words of your mouth; You are taken by the words of your mouth. 3 So do this, my son, and deliver yourself; For you have come into the hand of your friend: Go and humble yourself; Plead with your friend. 4 Give no sleep to your eyes, Nor slumber to your eyelids. 5 Deliver yourself like a gazelle from the hand of the hunter, And like a bird from the hand of the fowler."},
            {"ref": "Proverbs 11:15", "text": "15 He who is surety for a stranger will suffer, But one who hates being surety is secure."},
            {"ref": "Proverbs 17:18", "text": "18 A man devoid of understanding shakes hands in a pledge, And becomes surety for his friend."},
            {"ref": "Proverbs 20:16", "text": "16 Take the garment of one who is surety for a stranger, And hold it as a pledge when it is for a seductress."},
            {"ref": "Proverbs 27:13", "text": "13 Take the garment of him who is surety for a stranger, And hold it in pledge when he is surety for a seductress."}
        ],
        "dig_deeper_questions": [
            "1. Describe an instance where you put your neck on the line for someone and been burned.",
            "2. As Christians, we are called to be generous and giving but are we called to be taken advantage of?",
            "3. If you have already put your neck on the line for someone (like guaranteeing a debt) and are regretting your decision, based on the biblical instruction above, what will you do?",
            "4. Should we take into account the character of those we partner with or vouch for? Are they risk takers? Do they lend to strangers or loose women? How can that affect us?",
            "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 29: Don't Be a Sluggard/Lazy
    # ========================================
    {
        "id": 29,
        "title": "29. Don't Be a Sluggard/Lazy",
        "question": "Am I lazy about getting my work done?",
        "verses": [
            {"ref": "Proverbs 6:6-11", "text": "6 Go to the ant, you sluggard! Consider her ways and be wise, 7 Which, having no captain, Overseer or ruler, 8 Provides her supplies in the summer, And gathers her food in the harvest. 9 How long will you slumber, O sluggard? When will you rise from your sleep? 10 A little sleep, a little slumber, A little folding of the hands to sleep— 11 So shall your poverty come on you like a prowler, And your need like an armed man."},
            {"ref": "Proverbs 10:4-5", "text": "4 He who has a slack hand becomes poor, But the hand of the diligent makes rich. 5 He who gathers in summer is a wise son; He who sleeps in harvest is a son who causes shame."},
            {"ref": "Proverbs 10:26", "text": "26 As vinegar to the teeth and smoke to the eyes, So is the lazy man to those who send him."},
            {"ref": "Proverbs 12:11", "text": "11 He who tills his land will be satisfied with bread, But he who follows frivolity is devoid of understanding."},
            {"ref": "Proverbs 12:24", "text": "24 The hand of the diligent will rule, But the lazy man will be put to forced labor."},
            {"ref": "Proverbs 12:27", "text": "27 The lazy man does not roast what he took in hunting, But diligence is man's precious possession."},
            {"ref": "Proverbs 13:4", "text": "4 The soul of a lazy man desires, and has nothing; But the soul of the diligent shall be made rich."},
            {"ref": "Proverbs 15:19", "text": "19 The way of the lazy man is like a hedge of thorns, But the way of the upright is a highway."},
            {"ref": "Proverbs 18:9", "text": "9 He who is slothful in his work Is a brother to him who is a great destroyer."},
            {"ref": "Proverbs 19:15", "text": "15 Laziness casts one into a deep sleep, And an idle person will suffer hunger."},
            {"ref": "Proverbs 19:24", "text": "24 A lazy man buries his hand in the bowl, And will not so much as bring it to his mouth again."},
            {"ref": "Proverbs 20:4", "text": "4 The lazy man will not plow because of winter; He will beg during harvest and have nothing."},
            {"ref": "Proverbs 20:13", "text": "13 Do not love sleep, lest you come to poverty; Open your eyes, and you will be satisfied with bread."},
            {"ref": "Proverbs 21:25", "text": "25 The desire of the lazy man kills him, For his hands refuse to labor."},
            {"ref": "Proverbs 22:13", "text": "13 The lazy man says, \"There is a lion outside! I shall be slain in the streets!\""},
            {"ref": "Proverbs 24:30-34", "text": "30 I went by the field of the lazy man, And by the vineyard of the man devoid of understanding; 31 And there it was, all overgrown with thorns; Its surface was covered with nettles; Its stone wall was broken down. 32 When I saw it, I considered it well; I looked on it and received instruction: 33 A little sleep, a little slumber, A little folding of the hands to rest; 34 So shall your poverty come like a prowler, And your need like an armed man."},
            {"ref": "Proverbs 26:13-16", "text": "13 The lazy man says, \"There is a lion in the road! A fierce lion is in the streets!\" 14 As a door turns on its hinges, So does the lazy man on his bed. 15 The lazy man buries his hand in the bowl; It wearies him to bring it back to his mouth. 16 The lazy man is wiser in his own eyes Than seven men who can answer sensibly."},
            {"ref": "Proverbs 27:23-27", "text": "23 Be diligent to know the state of your flocks, And attend to your herds; 24 For riches are not forever, Nor does a crown endure to all generations. 25 When the hay is removed, and the tender grass shows itself, And the herbs of the mountains are gathered in, 26 The lambs will provide your clothing, And the goats the price of a field; 27 You shall have enough goats' milk for your food, For the food of your household, And the nourishment of your maidservants."},
            {"ref": "Proverbs 28:19", "text": "19 He who tills his land will have plenty of bread, But he who follows frivolity will have poverty enough!"}
        ],
        "dig_deeper_questions": [
            "1. Who considers you lazy?",
            "2. What gives them that impression?",
            "3. How has laziness affected your \"work-life\"?",
            "4. Do you have a plan for your household? Are you laying up supplies, working when you should, knowing the state of and attending to your business?",
            "5. Are you being diligent or frivolous?",
            "6. Where is the line between being lazy and working too hard (being a workaholic)? Consider Psalm 127:2 and Proverbs 23:4:\n\nPsalm 127:2 NIV\n2 In vain you rise early\n\t\t\t\tand stay up late, toiling for food to eat—\n\t\t\t\tfor he grants sleep to those he loves.\nFootnotes: [a] Or eat— / for while they sleep he provides for\n\nProverbs 23:4\n4 Do not overwork to be rich;\nBecause of your own understanding, cease!",
            "7. What is the best balance for you? What do you need to do differently to achieve this?",
            "8. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 30: Don't Let a Perverse Mouth Sow Discord
    # ========================================
    {
        "id": 30,
        "title": "30. Don't Let a Perverse Mouth Sow Discord",
        "question": "Do I say things that stir up a controversy (i.e., spread rumors, speak falsely, wickedly)?",
        "verses": [
            {"ref": "Proverbs 6:12-19", "text": "12 A worthless person, a wicked man, Walks with a perverse mouth; 13 He winks with his eyes, He shuffles his feet, He points with his fingers; 14 Perversity is in his heart, He devises evil continually, He sows discord. 15 Therefore his calamity shall come suddenly; Suddenly he shall be broken without remedy. 16 These six things the LORD hates, Yes, seven are an abomination to Him: 17 A proud look, A lying tongue, Hands that shed innocent blood, 18 A heart that devises wicked plans, Feet that are swift in running to evil, 19 A false witness who speaks lies, And one who sows discord among brethren."},
            {"ref": "Proverbs 10:6", "text": "6 Blessings are on the head of the righteous, But violence covers the mouth of the wicked."},
            {"ref": "Proverbs 10:31-32", "text": "31 The mouth of the righteous brings forth wisdom, But the perverse tongue will be cut out. 32 The lips of the righteous know what is acceptable, But the mouth of the wicked what is perverse."},
            {"ref": "Proverbs 15:7", "text": "7 The lips of the wise disperse knowledge, But the heart of the fool does not do so."},
            {"ref": "Proverbs 16:27-28", "text": "27 An ungodly man digs up evil, And it is on his lips like a burning fire. 28 A perverse man sows strife, And a whisperer separates the best of friends."},
            {"ref": "Proverbs 17:4", "text": "4 An evildoer gives heed to false lips; A liar listens eagerly to a spiteful tongue."},
            {"ref": "Proverbs 19:1", "text": "1 Better is the poor who walks in his integrity Than one who is perverse in his lips, and is a fool."},
            {"ref": "Proverbs 20:15", "text": "15 There is gold and a multitude of rubies, But the lips of knowledge are a precious jewel."},
            {"ref": "Proverbs 21:28", "text": "28 A false witness shall perish, But the man who hears him will speak endlessly."}
        ],
        "dig_deeper_questions": [
            "1. Is your speech filled with violence, perversion, evil, not acceptable, spreading rumors and bearing false witness? If so, how has it affected you or those around you?",
            "2. Why do you think you behave in this manner?",
            "3. If your speech stirs up controversy or is perverse, what does it say about the state of your heart?",
            "4. What can you do to change your speech, cleanse your heart?",
            "5. Who can you trust to hold you accountable as you attempt to change?",
            "6. Can you let someone know how their speech is affecting you and offer to help hold them accountable? If so, who? How? (Hint: use the Communication Worksheet provided in Chapter 6 – Communicating Issues).",
            "7. Note: the second line of verse Proverbs 21:28 above, it juxtaposes a liar (who will perish) with one who listens well (and, therefore, will be regarded/respected when they speak). Are you a good listener?",
            "8. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 31: Avoid Wickedness/Seek Righteousness
    # ========================================
    {
        "id": 31,
        "title": "31. Avoid Wickedness/Seek Righteousness",
        "question": "Do I want to be known for my righteousness?",
        "verses": [
            {"ref": "Proverbs 10:2-3", "text": "2 Treasures of wickedness profit nothing, But righteousness delivers from death. 3 The LORD will not allow the righteous soul to famish, But He casts away the desire of the wicked."},
            {"ref": "Proverbs 10:7", "text": "7 The memory of the righteous is blessed, But the name of the wicked will rot."},
            {"ref": "Proverbs 10:16", "text": "16 The labor of the righteous leads to life, The wages of the wicked to sin."},
            {"ref": "Proverbs 10:23-25", "text": "23 To do evil is like sport to a fool, But a man of understanding has wisdom. 24 The fear of the wicked will come upon him, And the desire of the righteous will be granted. 25 When the whirlwind passes by, the wicked is no more, But the righteous has an everlasting foundation."},
            {"ref": "Proverbs 10:27-30", "text": "27 The fear of the LORD prolongs days, But the years of the wicked will be shortened. 28 The hope of the righteous will be gladness, But the expectation of the wicked will perish. 29 The way of the LORD is strength for the upright, But destruction will come to the workers of iniquity. 30 The righteous will never be removed, But the wicked will not inhabit the earth."},
            {"ref": "Proverbs 11:5-8", "text": "5 The righteousness of the blameless will direct his way aright, But the wicked will fall by his own wickedness. 6 The righteousness of the upright will deliver them, But the unfaithful will be caught by their lust. 7 When a wicked man dies, his expectation will perish, And the hope of the unjust perishes. 8 The righteous is delivered from trouble, And it comes to the wicked instead."},
            {"ref": "Proverbs 11:19", "text": "19 As righteousness leads to life, So he who pursues evil pursues it to his own death."},
            {"ref": "Proverbs 11:21", "text": "21 Though they join forces, the wicked will not go unpunished; But the posterity of the righteous will be delivered."},
            {"ref": "Proverbs 11:23", "text": "23 The desire of the righteous is only good, But the expectation of the wicked is wrath."},
            {"ref": "Proverbs 11:27", "text": "27 He who earnestly seeks good finds favor, But trouble will come to him who seeks evil."},
            {"ref": "Proverbs 11:30-31", "text": "30 The fruit of the righteous is a tree of life, And he who wins souls is wise. 31 If the righteous will be recompensed on the earth, How much more the ungodly and the sinner."},
            {"ref": "Proverbs 13:6", "text": "6 Righteousness guards him whose way is blameless, But wickedness overthrows the sinner."},
            {"ref": "Proverbs 13:9", "text": "9 The light of the righteous rejoices, But the lamp of the wicked will be put out."},
            {"ref": "Proverbs 13:25", "text": "25 The righteous eats to the satisfying of his soul, But the stomach of the wicked shall be in want."},
            {"ref": "Proverbs 14:11", "text": "11 The house of the wicked will be overthrown, But the tent of the upright will flourish."},
            {"ref": "Proverbs 14:19", "text": "19 The evil will bow before the good, And the wicked at the gates of the righteous."},
            {"ref": "Proverbs 14:32", "text": "32 The wicked is banished in his wickedness, But the righteous has a refuge in his death."},
            {"ref": "Proverbs 14:34", "text": "34 Righteousness exalts a nation, But sin is a reproach to any people."},
            {"ref": "Proverbs 15:3", "text": "3 The eyes of the LORD are in every place, Keeping watch on the evil and the good."},
            {"ref": "Proverbs 15:6", "text": "6 In the house of the righteous there is much treasure, But in the revenue of the wicked is trouble."},
            {"ref": "Proverbs 15:8-9", "text": "8 The sacrifice of the wicked is an abomination to the LORD, But the prayer of the upright is His delight. 9 The way of the wicked is an abomination to the LORD, But He loves him who follows righteousness."},
            {"ref": "Proverbs 15:29", "text": "29 The LORD is far from the wicked, But He hears the prayer of the righteous."},
            {"ref": "Proverbs 16:12", "text": "12 It is an abomination for kings to commit wickedness, For a throne is established by righteousness."},
            {"ref": "Proverbs 16:31", "text": "31 The silver-haired head is a crown of glory, If it is found in the way of righteousness."},
            {"ref": "Proverbs 18:3", "text": "3 When the wicked comes, contempt comes also; And with dishonor comes reproach."},
            {"ref": "Proverbs 20:26", "text": "26 A wise king sifts out the wicked, And brings the threshing wheel over them."},
            {"ref": "Proverbs 21:3", "text": "3 To do righteousness and justice Is more acceptable to the LORD than sacrifice."},
            {"ref": "Proverbs 21:7-8", "text": "7 The violence of the wicked will destroy them, Because they refuse to do justice. 8 The way of a guilty man is perverse; But as for the pure, his work is right."},
            {"ref": "Proverbs 21:10", "text": "10 The soul of the wicked desires evil; His neighbor finds no favor in his eyes."},
            {"ref": "Proverbs 21:12", "text": "12 The righteous God wisely considers the house of the wicked, Overthrowing the wicked for their wickedness."},
            {"ref": "Proverbs 21:18", "text": "18 The wicked shall be a ransom for the righteous, And the unfaithful for the upright."},
            {"ref": "Proverbs 22:8", "text": "8 He who sows iniquity will reap sorrow, And the rod of his anger will fail."},
            {"ref": "Proverbs 22:12", "text": "12 The eyes of the LORD preserve knowledge, But He overthrows the words of the faithless."},
            {"ref": "Proverbs 28:1", "text": "1 The wicked flee when no one pursues, But the righteous are bold as a lion."},
            {"ref": "Proverbs 28:12", "text": "12 When the righteous rejoice, there is great glory; But when the wicked arise, men hide themselves."},
            {"ref": "Proverbs 28:28", "text": "28 When the wicked arise, men hide themselves; But when they perish, the righteous increase."},
            {"ref": "Proverbs 29:6-7", "text": "6 By transgression an evil man is snared, But the righteous sings and rejoices. 7 The righteous considers the cause of the poor, But the wicked does not understand such knowledge."},
            {"ref": "Proverbs 29:10", "text": "10 The bloodthirsty hate the blameless, But the upright seek his well-being."},
            {"ref": "Proverbs 29:16", "text": "16 When the wicked are multiplied, transgression increases; But the righteous will see their fall."}
        ],
        "dig_deeper_questions": [
            "1. Did you think the term \"righteousness\" had a bad connotation? Did it conjure up the idea of a person who is \"self-righteous\" or considers themselves, \"holier than thou\"? A hypocritical or judgmental Christian perhaps? Why do you think this is?",
            "2. Where should your righteousness come from? (Hint: Mathew 6).",
            "3. Underline the positive consequences of righteousness in the passages above.",
            "4. What causes you/others to behave wickedly (do what you know is not right)?",
            "5. Even though it is not possible to be righteous without God, is it something to aspire to or is it futile?",
            "6. By reading these verses, could you be encouraged, even if you are dealing with a wicked co-worker, supervisor or employee? How?",
            "7. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 32: Store Knowledge
    # ========================================
    {
        "id": 32,
        "title": "32. Store Knowledge",
        "question": "Have I been trying to learn more, getting training, looking things up, and gaining/storing knowledge?",
        "verses": [
            {"ref": "Proverbs 10:14", "text": "14 Wise people store up knowledge, But the mouth of the foolish is near destruction."},
            {"ref": "Proverbs 15:14", "text": "14 The heart of him who has understanding seeks knowledge, But the mouth of fools feeds on foolishness."},
            {"ref": "Proverbs 28:2", "text": "2 Because of the transgression of a land, many are its princes; But by a man of understanding and knowledge Right will be prolonged."}
        ],
        "dig_deeper_questions": [
            "1. Could storing up more knowledge help you become wiser, advance your career?",
            "2. What type of knowledge do you need to seek?",
            "3. By gaining understanding and knowledge you could not only gain wisdom (and possibly career advantage) but also be able to help \"prolong what is right\" – Proverbs 28:2. What does this mean to you?",
            "4. What is stopping you from growing in knowledge: fear, impatience, stubbornness, pride, anger, embarrassment, or incompetence? What can you do to overcome this?",
            "5. What will you do to expand your knowledge?",
            "6. In your pursuit of knowledge remember an important balance that the Bible teaches. What good is knowledge without love? How will you remind yourself of this?\n\n1 Corinthians 13:8 NIV\n8 Love never fails. But where there are prophecies, they will cease; where there are tongues, they will be stilled;\nwhere there is knowledge, it will pass away.",
            "7. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 33: Don't Use Dishonest Means
    # ========================================
    {
        "id": 33,
        "title": "33. Don't Use Dishonest Means",
        "question": "Do I use dishonest means to accomplish my goals?",
        "verses": [
            {"ref": "Proverbs 11:1", "text": "1 Dishonest scales are an abomination to the LORD, But a just weight is His delight."},
            {"ref": "Proverbs 11:18", "text": "18 The wicked man does deceptive work, But he who sows righteousness will have a sure reward."},
            {"ref": "Proverbs 11:24", "text": "24 There is one who scatters, yet increases more; And there is one who withholds more than is right, But it leads to poverty."},
            {"ref": "Proverbs 13:11", "text": "11 Wealth gained by dishonesty will be diminished, But he who gathers by labor will increase."},
            {"ref": "Proverbs 16:8", "text": "8 Better is a little with righteousness, Than vast revenues without justice. 11 Honest weights and scales are the LORD's; All the weights in the bag are His work."},
            {"ref": "Proverbs 17:23", "text": "23 A wicked man accepts a bribe behind the back To pervert the ways of justice."},
            {"ref": "Proverbs 20:10", "text": "10 Diverse weights and diverse measures, They are both alike, an abomination to the LORD."},
            {"ref": "Proverbs 20:17", "text": "17 Bread gained by deceit is sweet to a man, But afterward his mouth will be filled with gravel."},
            {"ref": "Proverbs 20:23", "text": "23 Diverse weights are an abomination to the LORD, And dishonest scales are not good."},
            {"ref": "Proverbs 29:27", "text": "27 An unjust man is an abomination to the righteous, And he who is upright in the way is an abomination to the wicked."}
        ],
        "dig_deeper_questions": [
            "1. If you've been deceptive, used dishonest scales or have been bribed or otherwise gained without justice, how can you make it right?",
            "2. If you believe others in the workplace are getting ahead by dishonest means, what can you do for them?",
            "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 34: Fairly Apply Justice
    # ========================================
    {
        "id": 34,
        "title": "34. Fairly Apply Justice",
        "question": "Have I been able to be fair and impartial when judging others?",
        "verses": [
            {"ref": "Proverbs 16:10-11", "text": "10 Divination is on the lips of the king; His mouth must not transgress in judgment."},
            {"ref": "Proverbs 18:13", "text": "13 He who answers a matter before he hears it, It is folly and shame to him."},
            {"ref": "Proverbs 18:17", "text": "17 The first one to plead his cause seems right, Until his neighbor comes and examines him."},
            {"ref": "Proverbs 20:8", "text": "8 A king who sits on the throne of judgment Scatters all evil with his eyes."},
            {"ref": "Proverbs 21:15", "text": "15 It is a joy for the just to do justice, But destruction will come to the workers of iniquity."},
            {"ref": "Proverbs 22:22-23", "text": "22 Do not rob the poor because he is poor, Nor oppress the afflicted at the gate; 23 For the LORD will plead their cause, And plunder the soul of those who plunder them."},
            {"ref": "Proverbs 23:10-11", "text": "10 Do not remove the ancient landmark, Nor enter the fields of the fatherless; 11 For their Redeemer is mighty; He will plead their cause against you."},
            {"ref": "Proverbs 24:23-26", "text": "23 These things also belong to the wise: It is not good to show partiality in judgment. 24 He who says to the wicked, \"You are righteous,\" Him the people will curse; Nations will abhor him. 25 But those who rebuke the wicked will have delight, And a good blessing will come upon them. 26 He who gives a right answer kisses the lips."},
            {"ref": "Proverbs 28:5", "text": "5 Evil men do not understand justice, But those who seek the LORD understand all."},
            {"ref": "Proverbs 28:8", "text": "8 One who increases his possessions by usury and extortion Gathers it for him who will pity the poor."},
            {"ref": "Proverbs 28:21", "text": "21 To show partiality is not good, Because for a piece of bread a man will transgress."},
            {"ref": "Proverbs 29:2", "text": "2 When the righteous are in authority, the people rejoice; But when a wicked man rules, the people groan."},
            {"ref": "Proverbs 29:4", "text": "4 The king establishes the land by justice, But he who receives bribes overthrows it."},
            {"ref": "Proverbs 29:12-14", "text": "12 If a ruler pays attention to lies, All his servants become wicked. 13 The poor man and the oppressor have this in common: The LORD gives light to the eyes of both. 14 The king who judges the poor with truth, His throne will be established forever."},
            {"ref": "Proverbs 31:8-9", "text": "8 Open your mouth for the speechless, In the cause of all who are appointed to die. 9 Open your mouth, judge righteously, And plead the cause of the poor and needy."}
        ],
        "dig_deeper_questions": [
            "1. Have you shown partiality in judgment, not listened well enough to make good judgments, been easily misled with lies or not stood up for those that needed their cases plead? (Underline as many as apply). How can you make it right?",
            "2. Are you prepared to admit your failure and start new making sure you heed the advice in the verses above? How?",
            "3. If you feel someone, probably your boss, has been unfair in their judgment is it because they have been partial, not listened well, been misled by lies have accepted bribes, or simply not stood up for those that can't stand up for themselves? (Underline as many as apply).",
            "4. How will you let them know how this is affecting you (See Chapter 6 – Communicating Issues for some help with this)?",
            "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 35: Hold Your Tongue
    # ========================================
    {
        "id": 35,
        "title": "35. Hold Your Tongue",
        "question": "Am I able to hold my tongue; not saying something I regret or speak without thinking?",
        "verses": [
            {"ref": "Proverbs 11:13", "text": "13 A talebearer reveals secrets, But he who is of a faithful spirit conceals a matter."},
            {"ref": "Proverbs 13:2-3", "text": "2 A man shall eat well by the fruit of his mouth, But the soul of the unfaithful feeds on violence. 3 He who guards his mouth preserves his life, But he who opens wide his lips shall have destruction."},
            {"ref": "Proverbs 14:23", "text": "23 In all labor there is profit, But idle chatter leads only to poverty."},
            {"ref": "Proverbs 15:1-2", "text": "1 A soft answer turns away wrath, But a harsh word stirs up anger. 2 The tongue of the wise uses knowledge rightly, But the mouth of fools pours forth foolishness."},
            {"ref": "Proverbs 15:23", "text": "23 A man has joy by the answer of his mouth, And a word spoken in due season, how good it is!"},
            {"ref": "Proverbs 15:26", "text": "26 The thoughts of the wicked are an abomination to the LORD, But the words of the pure are pleasant."},
            {"ref": "Proverbs 15:28", "text": "28 The heart of the righteous studies how to answer, But the mouth of the wicked pours forth evil."},
            {"ref": "Proverbs 16:1", "text": "1 The preparations of the heart belong to man, But the answer of the tongue is from the LORD."},
            {"ref": "Proverbs 16:23-24", "text": "23 The heart of the wise teaches his mouth, And adds learning to his lips. 24 Pleasant words are like a honeycomb, Sweetness to the soul and health to the bones."},
            {"ref": "Proverbs 17:27-28", "text": "27 He who has knowledge spares his words, And a man of understanding is of a calm spirit. 28 Even a fool is counted wise when he holds his peace; When he shuts his lips, he is considered perceptive."},
            {"ref": "Proverbs 18:2", "text": "2 A fool has no delight in understanding, But in expressing his own heart."},
            {"ref": "Proverbs 18:4", "text": "4 The words of a man's mouth are deep waters; The wellspring of wisdom is a flowing brook."},
            {"ref": "Proverbs 18:6-8", "text": "6 A fool's lips enter into contention, And his mouth calls for blows. 7 A fool's mouth is his destruction, And his lips are the snare of his soul. 8 The words of a talebearer are like tasty trifles, And they go down into the inmost body."},
            {"ref": "Proverbs 18:23", "text": "23 The poor man uses entreaties, But the rich answers roughly."},
            {"ref": "Proverbs 20:12", "text": "12 The hearing ear and the seeing eye, The LORD has made them both."},
            {"ref": "Proverbs 20:25", "text": "25 It is a snare for a man to devote rashly something as holy, And afterward to reconsider his vows."},
            {"ref": "Proverbs 21:23", "text": "23 Whoever guards his mouth and tongue Keeps his soul from troubles."},
            {"ref": "Proverbs 23:9", "text": "9 Do not speak in the hearing of a fool, For he will despise the wisdom of your words."},
            {"ref": "Proverbs 25:23", "text": "23 The north wind brings forth rain, And a backbiting tongue an angry countenance."},
            {"ref": "Proverbs 29:11", "text": "11 A fool vents all his feelings, But a wise man holds them back."}
        ],
        "dig_deeper_questions": [
            "1. Have you ever really considered what a powerful tool or weapon the tongue can be?",
            "2. Go back and underline the versus that most apply to the issue you have with your tongue; are you backbiting, a gossip, speak too quickly, talk too much, etc.",
            "3. Describe a time when you should have held your tongue and didn't. Maybe you said something you regret (gossiped, said something hurtful, said too much, spoke too soon)?",
            "4. From the verses above, list the benefits and traits associated with those that \"hold their tongue\" or speak wisely:",
            "5. From the verses above, list the problems and traits associated with those that don't \"hold their tongue\" or speak wisely:",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 36: Show Graciousness/Kindness
    # ========================================
    {
        "id": 36,
        "title": "36. Show Graciousness/Kindness",
        "question": "Do I demonstrate grace and kindness?",
        "verses": [
            {"ref": "Proverbs 11:16", "text": "16 A gracious woman retains honor, But ruthless men retain riches."},
            {"ref": "Proverbs 19:22", "text": "22 What is desired in a man is kindness, And a poor man is better than a liar."},
            {"ref": "Proverbs 20:28", "text": "28 Mercy and truth preserve the king, And by lovingkindness he upholds his throne."},
            {"ref": "Proverbs 21:13", "text": "13 Whoever shuts his ears to the cry of the poor Will also cry himself and not be heard."},
            {"ref": "Proverbs 22:11", "text": "11 He who loves purity of heart And has grace on his lips, The king will be his friend"},
            {"ref": "Proverbs 29:19-21", "text": "19 A servant will not be corrected by mere words; For though he understands, he will not respond. 20 Do you see a man hasty in his words? There is more hope for a fool than for him. 21 He who pampers his servant from childhood Will have him as a son in the end."}
        ],
        "dig_deeper_questions": [
            "1. Have you considered that loving-kindness, and grace will bring honor, uphold your position, create loyalty and bring you favor?",
            "2. What are the opposite consequences?",
            "3. Would you rather have honor or riches?",
            "4. In Proverbs 29:19-21 Is pampering different than being kind and gracious? Will it cause a servant to be insolent; expecting to be treated as a son? Is this an admonishment against being too lax with your employees or is this showing the difference in the level of respect one receives from kinder treatment: the willing obedience of a son versus the grudging obedience of a servant.",
            "5. If you aren't sure others would describe you as kind, what can you do to change your image?",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 37: Be Merciful
    # ========================================
    {
        "id": 37,
        "title": "37. Be Merciful",
        "question": "Am I willing to forgive or show mercy to others?",
        "verses": [
            {"ref": "Proverbs 11:17", "text": "17 The merciful man does good for his own soul, But he who is cruel troubles his own flesh."},
            {"ref": "Proverbs 12:10", "text": "10 A righteous man regards the life of his animal, But the tender mercies of the wicked are cruel."},
            {"ref": "Proverbs 14:21", "text": "21 He who despises his neighbor sins; But he who has mercy on the poor, happy is he."},
            {"ref": "Proverbs 14:31", "text": "31 He who oppresses the poor reproaches his Maker, But he who honors Him has mercy on the needy."},
            {"ref": "Proverbs 16:6", "text": "6 In mercy and truth Atonement is provided for iniquity; And by the fear of the LORD one departs from evil."},
            {"ref": "Proverbs 19:17", "text": "17 He who has pity on the poor lends to the LORD, And He will pay back what he has given."},
            {"ref": "Proverbs 21:21", "text": "21 He who follows righteousness and mercy Finds life, righteousness, and honor."},
            {"ref": "Proverbs 28:13", "text": "13 He who covers his sins will not prosper, But whoever confesses and forsakes them will have mercy."}
        ],
        "dig_deeper_questions": [
            "1. The verses above reflect, that the opposite of being merciful is being cruel or oppressive. Had you considered that?",
            "2. Does this change your mind about how willing you are to be merciful (even when it is hard)?",
            "3. What stops you from showing mercy sometimes?",
            "4. Have you considered that your willingness to confess and forsake sin will be the way to achieve mercy from others? Have you done your part to receive mercy?",
            "5. How will the Lord reward you for showing mercy?",
            "6. Who do you need to show mercy to today?",
            "7. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 38: Be Patient
    # ========================================
    {
        "id": 38,
        "title": "38. Be Patient",
        "question": "Am I patient, not hasty, in my plans and with my goals?",
        "verses": [
            {"ref": "Proverbs 13:12", "text": "12 Hope deferred makes the heart sick, But when the desire comes, it is a tree of life."},
            {"ref": "Proverbs 13:19", "text": "19 A desire accomplished is sweet to the soul, But it is an abomination to fools to depart from evil."},
            {"ref": "Proverbs 20:21", "text": "21 An inheritance gained hastily at the beginning Will not be blessed at the end."},
            {"ref": "Proverbs 21:5", "text": "5 The plans of the diligent lead surely to plenty, But those of everyone who is hasty, surely to poverty."},
            {"ref": "Proverbs 24:27", "text": "27 Prepare your outside work, Make it fit for yourself in the field; And afterward build your house."},
            {"ref": "Proverbs 25:15", "text": "15 By long forbearance a ruler is persuaded, And a gentle tongue breaks a bone."}
        ],
        "dig_deeper_questions": [
            "1. How has being impatient, ever caused problems for you?",
            "2. Did you learn a lesson or are you still making mistakes by being hasty, not preparing, being heartsick while you wait? Underline as many as apply.",
            "3. What strategies can you employ to help you be more patient?",
            "4. What strategy is shared below:\n\nLuke 14:28 NIV\n28 \"Suppose one of you wants to build a tower. Won't you first sit down and estimate the cost to see if you have enough money to complete it?",
            "5. How can you address others that rush in and experience problems as a result? Maybe you can think of a fairy tale that could illustrate this point? (Hint: I'll huff and I'll puff and I'll blow your house down).",
            "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 39: Respect Authority/Faithful Messenger
    # ========================================
    {
        "id": 39,
        "title": "39. Respect Authority/Faithful Messenger",
        "question": "Have I handled the authority figures in my life well (Have or had a good relationship with i.e., my boss, parents, teachers)?",
        "verses": [
            {"ref": "Proverbs 13:17", "text": "17 A wicked messenger falls into trouble, But a faithful ambassador brings health."},
            {"ref": "Proverbs 14:35", "text": "35 The king's favor is toward a wise servant, But his wrath is against him who causes shame."},
            {"ref": "Proverbs 24:21-22", "text": "21 My son, fear the LORD and the king; Do not associate with those given to change; 22 For their calamity will rise suddenly, And who knows the ruin those two can bring?"},
            {"ref": "Proverbs 25:1-7", "text": "These also are proverbs of Solomon which the men of Hezekiah king of Judah copied: 2 It is the glory of God to conceal a matter, But the glory of kings is to search out a matter. 3 As the heavens for height and the earth for depth, So the heart of kings is unsearchable. 4 Take away the dross from silver, And it will go to the silversmith for jewelry. 5 Take away the wicked from before the king, And his throne will be established in righteousness. 6 Do not exalt yourself in the presence of the king, And do not stand in the place of the great; 7 For it is better that he say to you, Come up here,\" Than that you should be put lower in the presence of the prince, Whom your eyes have seen."},
            {"ref": "Proverbs 25:13", "text": "13 Like the cold of snow in time of harvest Is a faithful messenger to those who send him, For he refreshes the soul of his masters."},
            {"ref": "Proverbs 27:18", "text": "18 Whoever keeps the fig tree will eat its fruit; So he who waits on his master will be honored."},
            {"ref": "Proverbs 29:26", "text": "26 Many seek the ruler's favor, But justice for man comes from the LORD."}
        ],
        "dig_deeper_questions": [
            "1. Being faithful, having reverence (fear), humility and offering willing service to authority will be refreshing to authority. Even if it is not rewarded, justice for man comes from the Lord. Are you offering the authority figures in your life, their due respect?",
            "2. If not, consider why. What you can do to change your attitude toward authority? I suggest you re-read Chapter 1 - Authority Issues for more information.",
            "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    
    # ========================================
    # TOPIC 40: Don't Be Scornful/Proud/Mockers (Scoffers)
    # ========================================
    {
        "id": 40,
        "title": "40. Don't Be Scornful/Proud/Mockers (Scoffers)",
        "question": "Am I known for acting scornful/proud/conceited or mocking (putting others down, making fun of them, glad at their calamity)?",
        "verses": [
            {"ref": "Proverbs 3:34", "text": "34 Surely He scorns the scornful, But gives grace to the humble."},
            {"ref": "Proverbs 14:6", "text": "6 A scoffer seeks wisdom and does not find it, But knowledge is easy to him who understands."},
            {"ref": "Proverbs 17:5", "text": "5 He who mocks the poor reproaches his Maker; He who is glad at calamity will not go unpunished."},
            {"ref": "Proverbs 17:21", "text": "21 He who begets a scoffer does so to his sorrow, And the father of a fool has no joy."},
            {"ref": "Proverbs 19:25", "text": "25 Strike a scoffer, and the simple will become wary; Rebuke one who has understanding, and he will discern knowledge."},
            {"ref": "Proverbs 19:29", "text": "29 Judgments are prepared for scoffers, And beatings for the backs of fools"},
            {"ref": "Proverbs 21:24", "text": "24 A proud and haughty man—\"Scoffer\" is his name; He acts with arrogant pride."},
            {"ref": "Proverbs 22:2", "text": "2 The rich and the poor have this in common, The LORD is the maker of them all."},
            {"ref": "Proverbs 22:10", "text": "10 Cast out the scoffer, and contention will leave; Yes, strife and reproach will cease."},
            {"ref": "Proverbs 29:8", "text": "8 Scoffers set a city aflame, But wise men turn away wrath."},
            {"ref": "Proverbs 30:13-14", "text": "13 There is a generation—oh, how lofty are their eyes! And their eyelids are lifted up. 14 There is a generation whose teeth are like swords, And whose fangs are like knives, To devour the poor from off the earth, And the needy from among men."},
            {"ref": "Proverbs 30:17", "text": "17 The eye that mocks his father, And scorns obedience to his mother, The ravens of the valley will pick it out, And the young eagles will eat it."}
        ],
        "dig_deeper_questions": [
            "1. Someone who is scornful, proud, a mocker seems to value themselves more than others. Could there, however, be other reasons for their behavior?",
            "2. Consider this verse:\n\nPhilippians 2:3-4 (NKJV)\n3 Let nothing be done through selfish ambition or conceit, but in lowliness of mind let each esteem others better than himself. 4 Let each of you look out not only for his own interests, but also for the interests of others.\n\nHow should you value others?",
            "3. It seems, even biblically, difficult to correct a scoffer? How can you change your own or others behavior, if this is a character flaw?",
            "4. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
},
    # ========================================
    # TOPIC 41: Honor the Lord; With Your Possessions/Generosity
    # ========================================
        {
        "id": 41,
        "title": "41. Honor the Lord; With Your Possessions/Generosity",
        "question": "I'm known for my generosity?",
        "verses": [
            {"ref": "Proverbs 3:9-10", "text": "Honor the LORD with your possessions, And with the first fruits of all your increase; So your barns will be filled with plenty, And your vats will overflow with new wine."},
            {"ref": "Proverbs 10:15", "text": "The rich man's wealth is his strong city; The destruction of the poor is their poverty"},
            {"ref": "Proverbs 10:22", "text": "The blessing of the LORD makes one rich, And He adds no sorrow with it."},
            {"ref": "Proverbs 11:4", "text": "Riches do not profit in the day of wrath, But righteousness delivers from death."},
            {"ref": "Proverbs 11:25-26", "text": "The generous soul will be made rich, And he who waters will also be watered himself. The people will curse him who withholds grain, But blessing will be on the head of him who sells it."},
            {"ref": "Proverbs 11:28", "text": "He who trusts in his riches will fall, But the righteous will flourish like foliage."},
            {"ref": "Proverbs 13:7-8", "text": "There is one who makes himself rich, yet has nothing; And one who makes himself poor, yet has great riches. The ransom of a man's life is his riches, But the poor does not hear rebuke."},
            {"ref": "Proverbs 13:22", "text": "A good man leaves an inheritance to his children's children, But the wealth of the sinner is stored up for the righteous."},
            {"ref": "Proverbs 14:20", "text": "The poor man is hated even by his own neighbor, But the rich has many friends."},
            {"ref": "Proverbs 17:8", "text": "A present is a precious stone in the eyes of its possessor; Wherever he turns, he prospers."},
            {"ref": "Proverbs 25:14", "text": "Whoever falsely boasts of giving Is like clouds and wind without rain."}
        ],
        "dig_deeper_questions": [
            "What stops you from being generous? Fear of not having enough, fear of being taken advantage of, lack of control about what someone else will do with your resources?",
            "What specifically, from the verses above, counter your argument?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 42: Have a Merry Heart
    # ========================================
    {
        "id": 42,
        "title": "42. Have a Merry Heart",
        "question": "I'm described as positive, upbeat or cheerful?",
        "verses": [
            {"ref": "Proverbs 15:13", "text": "A merry heart makes a cheerful countenance, But by sorrow of the heart the spirit is broken."},
            {"ref": "Proverbs 15:15", "text": "All the days of the afflicted are evil, But he who is of a merry heart has a continual feast."},
            {"ref": "Proverbs 15:30", "text": "The light of the eyes rejoices the heart, And a good report makes the bones healthy."},
            {"ref": "Proverbs 17:22", "text": "A merry heart does good, like medicine, But a broken spirit dries the bones."},
            {"ref": "Proverbs 18:14", "text": "The spirit of a man will sustain him in sickness, But who can bear a broken spirit?"},
            {"ref": "Proverbs 25:25", "text": "As cold water to a weary soul, So is good news from a far country."}
        ],
        "dig_deeper_questions": [
            "Does sorrow or a broken spirit keep you from having a merry heart or a cheerful countenance? How does this impact the way you are perceived by others?",
            "What do these verses above teach you about what can you do to help make another's heart merry? Hint: what is 'the light of the eyes'? A smile?",
            "Would you know what not to do? (some that are not good at understanding human nature might, unintentionally try to be too bright and cheery when another's heart is heavy). Have you ever been accused of this, being insensitive? Proverbs 25:20 ((NKJV)) 20 Like one who takes away a garment in cold weather, And like vinegar on soda, Is one who sings songs to a heavy heart.",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 43: Be Content, Not Greedy
    # ========================================
    {
        "id": 43,
        "title": "43. Be Content, Not Greedy",
        "question": "I display an attitude that I am content with what I have, not greedy?",
        "verses": [
            {"ref": "Proverbs 15:27", "text": "He who is greedy for gain troubles his own house, But he who hates bribes will live."},
            {"ref": "Proverbs 21:26", "text": "He covets greedily all day long, But the righteous gives and does not spare."},
            {"ref": "Proverbs 22:9", "text": "He who has a generous eye will be blessed, For he gives of his bread to the poor."},
            {"ref": "Proverbs 22:16", "text": "He who oppresses the poor to increase his riches, And he who gives to the rich, will surely come to poverty."},
            {"ref": "Proverbs 23:1-5", "text": "When you sit down to eat with a ruler, Consider carefully what is before you; And put a knife to your throat If you are a man given to appetite. Do not desire his delicacies, For they are deceptive food. Do not overwork to be rich; Because of your own understanding, cease! Will you set your eyes on that which is not? For riches certainly make themselves wings; They fly away like an eagle toward heaven."},
            {"ref": "Proverbs 23:6-10", "text": "Do not eat the bread of a miser, Nor desire his delicacies; For as he thinks in his heart, so is he. 'Eat and drink!' he says to you, But his heart is not with you. The morsel you have eaten, you will vomit up, And waste your pleasant words. Do not speak in the hearing of a fool, For he will despise the wisdom of your words."},
            {"ref": "Proverbs 25:16", "text": "Have you found honey? Eat only as much as you need, Lest you be filled with it and vomit."},
            {"ref": "Proverbs 27:20", "text": "Hell and Destruction are never full; So the eyes of man are never satisfied."},
            {"ref": "Proverbs 28:20", "text": "A faithful man will abound with blessings, But he who hastens to be rich will not go unpunished."},
            {"ref": "Proverbs 28:22", "text": "A man with an evil eye hastens after riches, And does not consider that poverty will come upon him."},
            {"ref": "Proverbs 28:15-16", "text": "Like a roaring lion and a charging bear Is a wicked ruler over poor people. A ruler who lacks understanding is a great oppressor, But he who hates covetousness will prolong his days."},
            {"ref": "Proverbs 28:27", "text": "He who gives to the poor will not lack, But he who hides his eyes will have many curses."},
            {"ref": "Proverbs 30:8-9", "text": "Remove falsehood and lies far from me; Give me neither poverty nor riches— Feed me with the food allotted to me; Lest I be full and deny You, And say, 'Who is the LORD?' Or lest I be poor and steal, And profane the name of my God."},
            {"ref": "Proverbs 30:15-16", "text": "The leech has two daughters— Give and Give! There are three things that are never satisfied, Four never say, 'Enough!': The grave, The barren womb, The earth that is not satisfied with water— And the fire never says, 'Enough!'"}
        ],
        "dig_deeper_questions": [
            "If you have not come to the place that you are content with what you have what will change your attitude in this area?",
            "Does being content mean that you are lazy, don't aspire for career advancement, don't give 100%?",
            "Have you brought trouble to your own house by being greedy for gain? Give an example.",
            "Are other's attitudes and greed affecting the way you live? Do you eat with 'misers' or do your daughters, spouse or boss say 'Give and Give' and need to be addressed so that you can achieve the right balance in your life and teach them contentment in theirs?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 44: Don't Cause Shame
    # ========================================
    {
        "id": 44,
        "title": "44. Don't Cause Shame",
        "question": "I cause my parents, friends or loved one's shame?",
        "verses": [
            {"ref": "Proverbs 17:2", "text": "A wise servant will rule over a son who causes shame, And will share an inheritance among the brothers."},
            {"ref": "Proverbs 19:13", "text": "A foolish son is the ruin of his father, And the contentions of a wife are a continual dripping."},
            {"ref": "Proverbs 28:7", "text": "Whoever keeps the law is a discerning son, But a companion of gluttons shames his father."}
        ],
        "dig_deeper_questions": [
            "Have you ever caused someone shame? If so, have you made amends? Will you? How/when?",
            "If your inheritance is eternal salvation, will your shameful behavior rob you of this? How can you make your salvation sure? 1 John 1:9 NIV 9 If we confess our sins, he is faithful and just and will forgive us our sins and purify us from all unrighteousness.",
            "If someone has caused you shame, will you be willing to forgive them? What will it take from them, from you?",
            "Are you a contentious spouse? Maybe you are not causing shame or ruin, but have you considered the impact you are having with your 'continual dripping'? What can you do to change?",
            "Does the company you keep bring shame to those you love? Is it because your loved one is being too judgmental (remember, Jesus was scorned by the Pharisees for keeping company with sinners and tax collectors, Mark 2:16) or do they have good and biblical reason to be ashamed?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 45: Don't Be a Rebel
    # ========================================
    {
        "id": 45,
        "title": "45. Don't Be a Rebel",
        "question": "I am rebellious/a rebel?",
        "verses": [
            {"ref": "Proverbs 17:11", "text": "An evil man seeks only rebellion; Therefore a cruel messenger will be sent against him."},
            {"ref": "Proverbs 18:1", "text": "A man who isolates himself seeks his own desire; He rages against all wise judgment."}
        ],
        "dig_deeper_questions": [
            "A rebel, a lone ranger, seeking only one's own desire and unrest. If you or someone you know, exhibits this behavior, how will you warn them of the consequences?",
            "What can you offer such a person?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 46: Don't Take Revenge
    # ========================================
    {
        "id": 46,
        "title": "46. Don't Take Revenge",
        "question": "I take the opportunity to 'get-even' or get revenge for something someone does to me?",
        "verses": [
            {"ref": "Proverbs 20:22", "text": "Do not say, 'I will recompense evil'; Wait for the LORD, and He will save you."},
            {"ref": "Proverbs 24:29", "text": "Do not say, 'I will do to him just as he has done to me; I will render to the man according to his work.'"},
            {"ref": "Proverbs 25:21-22", "text": "If your enemy is hungry, give him bread to eat; And if he is thirsty, give him water to drink; For so you will heap coals of fire on his head, And the LORD will reward you."}
        ],
        "dig_deeper_questions": [
            "What does it feel like when you are bent on getting revenge? Explain the emotions involved, the ways you rationalize your response, the physical manifestations, etc.",
            "What, specifically will you do when you are tempted to say 'I will recompense (repay) evil' or 'I will do to him just as he has done to me'?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 47: Don't Gloat
    # ========================================
    {
        "id": 47,
        "title": "47. Don't Gloat",
        "question": "I'm known for bragging about my accomplishments and/or rejoicing when an enemy fails?",
        "verses": [
            {"ref": "Proverbs 24:17-18", "text": "Do not rejoice when your enemy falls, And do not let your heart be glad when he stumbles; Lest the LORD see it, and it displease Him, And He turn away His wrath from him."},
            {"ref": "Proverbs 25:27", "text": "It is not good to eat much honey; So to seek one's own glory is not glory"}
        ],
        "dig_deeper_questions": [
            "The definition of gloating: to contemplate or dwell on one's own success or another's misfortune with smugness or malignant pleasure. If you are known for having this type of character, are you ready to change?",
            "What might cause one to develop these traits?",
            "What can influence someone to change?",
            "Can you think of other Bible verses to support these proverbs above? (Hint: Proverbs 27:2).",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 48: Avoid Conflict
    # ========================================
    {
        "id": 48,
        "title": "48. Avoid Conflict",
        "question": "I avoid getting into conflicts or am able to handle conflict well and resolve peacefully?",
        "verses": [
            {"ref": "Proverbs 25:8-10", "text": "Do not go hastily to court; For what will you do in the end, When your neighbor has put you to shame? Debate your case with your neighbor, And do not disclose the secret to another; Lest he who hears it expose your shame, And your reputation be ruined."},
            {"ref": "Proverbs 29:9", "text": "If a wise man contends with a foolish man, Whether the fool rages or laughs, there is no peace."}
        ],
        "dig_deeper_questions": [
            "The best way to handle conflict, in some cases, seems to be to avoid it or at least handle it privately. Do you agree?",
            "If this isn't the best way to handle your issue, state why? Next, prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area; avoiding and/or handling conflict well: Note: The rest of the Bible has plenty to say about Avoiding Conflict and Handling Grievances. This is such an important part of learning how to address 'work-life' issues that I've devoted two subsections in Chapter 6 – Communicating Issues of this book to examine what the Bible has to say in this area. I then provide a communication tool designed for use as a wise strategy for handling handle conflict."
        ]
    },
    # ========================================
    # TOPIC 49: Value Friends and Family
    # ========================================
    {
        "id": 49,
        "title": "49. Value Friends and Family",
        "question": "I have a good relationship with my family/friends?",
        "verses": [
            {"ref": "Proverbs 17:17", "text": "A friend loves at all times, And a brother is born for adversity."},
            {"ref": "Proverbs 18:24", "text": "A man who has friends must himself be friendly, But there is a friend who sticks closer than a brother."},
            {"ref": "Proverbs 19:4", "text": "Wealth makes many friends, But the poor is separated from his friend."},
            {"ref": "Proverbs 19:6-7", "text": "Many entreat the favor of the nobility, And every man is a friend to one who gives gifts. All the brothers of the poor hate him; How much more do his friends go far from him! He may pursue them with words, yet they abandon him."},
            {"ref": "Proverbs 19:26", "text": "He who mistreats his father and chases away his mother Is a son who causes shame and brings reproach"},
            {"ref": "Proverbs 20:20", "text": "Whoever curses his father or his mother, His lamp will be put out in deep darkness."},
            {"ref": "Proverbs 23:15-26", "text": "My son, if your heart is wise, My heart will rejoice—indeed, I myself; Yes, my inmost being will rejoice When your lips speak right things. Do not let your heart envy sinners, But be zealous for the fear of the LORD all the day; For surely there is a hereafter, And your hope will not be cut off. Hear, my son, and be wise; And guide your heart in the way. Do not mix with winebibbers, Or with gluttonous eaters of meat; For the drunkard and the glutton will come to poverty, And drowsiness will clothe a man with rags. Listen to your father who begot you, And do not despise your mother when she is old. Buy the truth, and do not sell it, Also wisdom and instruction and understanding. The father of the righteous will greatly rejoice, And he who begets a wise child will delight in him. Let your father and your mother be glad, And let her who bore you rejoice. My son, give me your heart, And let your eyes observe my ways."},
            {"ref": "Proverbs 27:9-10", "text": "Ointment and perfume delight the heart, And the sweetness of a man's friend gives delight by hearty counsel. Do not forsake your own friend or your father's friend, Nor go to your brother's house in the day of your calamity; Better is a neighbor nearby than a brother far away."},
            {"ref": "Proverbs 27:14", "text": "He who blesses his friend with a loud voice, rising early in the morning, It will be counted a curse to him."},
            {"ref": "Proverbs 28:24", "text": "Whoever robs his father or his mother, And says, 'It is no transgression,' The same is companion to a destroyer."},
            {"ref": "Proverbs 29:17", "text": "Correct your son, and he will give you rest; Yes, he will give delight to your soul."},
            {"ref": "Proverbs 30:11", "text": "There is a generation that curses its father, And does not bless its mother."}
        ],
        "dig_deeper_questions": [
            "Relationships with friends and family are to be valued, cultivated, genuine, joyous, deemed sweet and giving delight, respected and revered. Do you find your relationships with your friends and family lacking in these areas? If so, what can you do differently to repair/restore these relationships?",
            "Do you have 'fake friends' those that aren't genuine and may require you to be fake back or even may bring you ruin (Proverbs 18:24) or ones that will stick closer than a brother?",
            "If others around you are having problems within their relationships, what will you do to encourage them to value their friends and family?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 50: Understands Human Nature
    # ========================================
    {
        "id": 50,
        "title": "50. Understands Human Nature",
        "question": "I have a good understanding of human nature. I can usually read how people will react?",
        "verses": [
            {"ref": "Proverbs 18:16", "text": "A man's gift makes room for him, And brings him before great men."},
            {"ref": "Proverbs 21:14", "text": "A gift in secret pacifies anger, And a bribe behind the back, strong wrath."},
            {"ref": "Proverbs 20:14", "text": "'It is good for nothing,' cries the buyer; But when he has gone his way, then he boasts."},
            {"ref": "Proverbs 25:17", "text": "Seldom set foot in your neighbor's house, Lest he become weary of you and hate you."},
            {"ref": "Proverbs 25:20", "text": "Like one who takes away a garment in cold weather, And like vinegar on soda, Is one who sings songs to a heavy heart."},
            {"ref": "Proverbs 30:24-31", "text": "There are four things which are little on the earth, But they are exceedingly wise: The ants are a people not strong, Yet they prepare their food in the summer; The rock badgers are a feeble folk, Yet they make their homes in the crags; The locusts have no king, Yet they all advance in ranks; The spider skillfully grasps with its hands, And it is in kings' palaces. There are three things which are majestic in pace, Yes, four which are stately in walk: A lion, which is mighty among beasts And does not turn away from any; A greyhound, A male goat also, And a king whose troops are with him."}
        ],
        "dig_deeper_questions": [
            "Gifts, given from the bosom (the heart), not in a flashy way, broadcast so that you will get a reward, but sincere, in secret, can open doors and pacify anger, do you agree? Is this condoning bribes?",
            "Have you ever heard a person bargaining for a good deal? Will they say one thing to get that deal ('it's good for nothing') and then brag of their accomplishment ('I got a great deal!')? What does this tell us about human nature and negotiations? Should you assume the best or worst in others?",
            "Secular psychology links our negative behavior like greed, or reactions like anger or anxiety, etc. to experiences we have had from our childhoods. The Bible teaches us, however, that we are born with a sin nature. Our behavior and responses will often be wicked. We need to be aware of this in ourselves as we endeavor to change. We also need to be aware of this in others, but not hold it against them. What can we do for them, instead?",
            "Do you learn by observing others (animals or man) what it is about them that makes them unique; their strengths? (Even a scary spider has them.) If you only focus on a man's sinful nature you may miss that they are still a child of God (or a potential believer) and/or can be used by Him. Do you agree? How will this change your interactions with others?",
            "Are you sensitive (self-aware) not only of when you respond in your sin nature, but maybe when someone has had enough of you, when you are being too cheerful or when you've worn out your welcome? Do you know when to back off or change your tactics or do you need to work on this?",
            "Further, in Proverbs 30:25-28, what wisdom can you learn from the least/little animals about getting along: Preparedness, suitable environment, cooperation and diligence?",
            "In Proverbs 30:29-31, what can you learn about leadership, having a stately walk, from the stately animals listed: Strength and courage, quickness, agility and surefootedness?",
            "How can improving your skills of understanding human nature help you work with and/or lead others?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    # ========================================
    # TOPIC 51: Respect Elders
    # ========================================
    {
        "id": 51,
        "title": "51. Respect Elders",
        "question": "I'd consider myself respectful of my elders? Or, if you are the elder, have you been respectful of yourself; imparting your knowledge to the younger generation?",
        "verses": [
            {"ref": "Proverbs 20:29", "text": "The glory of young men is their strength, And the splendor of old men is their gray head."}
        ],
        "dig_deeper_questions": [
            "Have you realized that the gray hair of your elders may hold wisdom?",
            "Have you realized that if are the one with gray hair that you have a duty to those under your care/entrusted to you? 1 Peter 5 : 1-4 NIV To the Elders and the Flock 5 To the elders among you, I appeal as a fellow elder and a witness of Christ's sufferings who also will share in the glory to be revealed: 2 Be shepherds of God's flock that is under your care, watching over them—not because you must, but because you are willing, as God wants you to be; not pursuing dishonest gain, but eager to serve; 3 not lording it over those entrusted to you, but being examples to the flock.4 And when the Chief Shepherd appears, you will receive the crown of glory that will never fade away.",
            "As you read this verse below, what quality does 'respecting your elders' show in your character? 1 Peter 5:5 NIV 5 In the same way, you who are younger, submit yourselves to your elders. All of you, clothe yourselves with humility toward one another, because, 'God opposes the proud but shows favor to the humble.'",
            "As an elder, are you valuing yourself, passing on your wisdom and being an asset to those who are younger and have more strength and energy?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
        # ========================================
    # TOPIC 52: Great Commission
    # ========================================
    {
        "id": 52,
        "title": "52. Great Commission",
        "question": "I have told others about my faith in God/Christ?",
        "verses": [
            {"ref": "Proverbs 24:11-12", "text": "Deliver those who are drawn toward death, And hold back those stumbling to the slaughter. If you say, 'Surely we did not know this,' Does not He who weighs the hearts consider it? He who keeps your soul, does He not know it? And will He not render to each man according to his deeds?"}
        ],
        "dig_deeper_questions": [
            "Have you tried your best to share Christ with those around you that are drawn to death, stumbling to the slaughter?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    }
]


# ============================================================================
# DO DO NOT EDIT BELOW THIS LINE
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

    st.markdown(f"### Areas of Weakness: {len(weaknesses)} out of 52")

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
                for idx, question in enumerate(item["dig_deeper_questions"]):
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
        for i, q in enumerate(item["dig_deeper_questions"]):
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
            "dig_deeper": item["dig_deeper_questions"],
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
    
