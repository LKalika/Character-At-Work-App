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
        "question": "Do I willingly accept instruction from parents, teachers, bosses, spouse, and God?",
        "verses": [
            {"ref": "Proverbs 1:7", "text": "The fear of the LORD is the beginning of knowledge, But fools despise wisdom and instruction."},
            {"ref": "Proverbs 1:8-9", "text": "My son, hear the instruction of your father, And do not forsake the law of your mother; For they will be a graceful ornament on your head, And chains about your neck."},
            {"ref": "Proverbs 3:1-4", "text": "My son, do not forget my law, But let your heart keep my commands; For length of days and long life And peace they will add to you. Let not mercy and truth forsake you; Bind them around your neck, Write them on the tablet of your heart, And so find favor and high esteem In the sight of God and man."},
            {"ref": "Proverbs 4:1-4", "text": "Hear, my children, the instruction of a father, And give attention to know understanding; For I give you good doctrine: Do not forsake my law. When I was my father’s son, Tender and the only one in the sight of my mother, He also taught me, and said to me: Let your heart retain my words; Keep my commands, and live."},
            {"ref": "Proverbs 4:20-23", "text": "My son, give attention to my words; Incline your ear to my sayings. Do not let them depart from your eyes; Keep them in the midst of your heart; For they are life to those who find them, And health to all their flesh. Keep your heart with all diligence, For out of it spring the issues of life."},
            {"ref": "Proverbs 5:12-14", "text": "And say: How I have hated instruction, And my heart despised correction! I have not obeyed the voice of my teachers, Nor inclined my ear to those who instructed me! I was on the verge of total ruin, In the midst of the assembly and congregation.”"},
            {"ref": "Proverbs 6:20-23", "text": "My son, keep your father’s command, And do not forsake the law of your mother. Bind them continually upon your heart; Tie them around your neck. When you roam, they will lead you; When you sleep, they will keep you; And when you awake, they will speak with you. For the commandment is a lamp, And the law a light; Reproofs of instruction are the way of life,"},
            {"ref": "Proverbs 10:8", "text": "The wise in heart will receive commands, But a prating fool will fall."},
            {"ref": "Proverbs 13:1", "text": "A wise son heeds his father’s instruction, But a scoffer does not listen to rebuke."},
            {"ref": "Proverbs 19:27", "text": "Cease listening to instruction, my son, And you will stray from the words of knowledge."},
            {"ref": "Proverbs 23:12", "text": "Apply your heart to instruction, And your ears to words of knowledge."}
        ],
        "dig_deeper": [
            "Looking at your life, how have you fallen short in the area of accepting instruction from others: your parents, teachers, Godly advisors? How about others that give commands or counsel i.e., your boss, your spouse? Give some examples of how this has hurt you.",
            "Taking things one-step further, how have you sought out (or applied your heart to) instruction and made an effort to listen (open your ears) for instruction? See Proverbs 23:12 above.",
            "What do you think stops you from accepting or seeking out instruction willingly?",
            "Specifically, has your lack of accepting instruction affected you in your work? How?",
            "Is there something you could learn (be instructed in) right now that would make you a better employee in your current job or for future career aspirations?",
            "If so, how will you improve in this area?",
            "How can you minister to others that have an issue in this area?",
            "Finally, review Chapter 2 – Self -Image Issues, regarding a “Coachable Spirit”. How does this pertain to accepting instruction?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 2,
        "title": "Accept Correction",
        "question": "Do I receive correction and rebuke well, or do I get defensive and resentful?",
        "verses": [
            {"ref": "Proverbs 1:20-33", "text": "Wisdom calls aloud outside; She raises her voice in the open squares. She cries out in the chief concourses, At the openings of the gates in the city She speaks her words: “ How long, you simple ones, will you love simplicity? For scorners delight in their scorning, And fools hate knowledge. Turn at my rebuke; Surely I will pour out my spirit on you; I will make my words known to you. Because I have called and you refused, I have stretched out my hand and no one regarded, Because you disdained all my counsel, And would have none of my rebuke, I also will laugh at your calamity; I will mock when your terror comes, When your terror comes like a storm, And your destruction comes like a whirlwind, When distress and anguish come upon you. “ Then they will call on me, but I will not answer; They will seek me diligently, but they will not find me. Because they hated knowledge And did not choose the fear of the LORD, They would have none of my counsel And despised my every rebuke. Therefore they shall eat the fruit of their own way, And be filled to the full with their own fancies. For the turning away of the simple will slay them, And the complacency of fools will destroy them; But whoever listens to me will dwell safely, And will be secure, without fear of evil.”"},
            {"ref": "Proverbs 3:11-12", "text": "My son, do not despise the chastening of the LORD, Nor detest His correction; For whom the LORD loves He corrects, Just as a father the son in whom he delights."},
            {"ref": "Proverbs 10:17", "text": "He who keeps instruction is in the way of life, But he who refuses correction goes astray."},
            {"ref": "Proverbs 12:1", "text": "Whoever loves instruction loves knowledge, But he who hates correction is stupid."},
            {"ref": "Proverbs 13:18", "text": "Poverty and shame will come to him who disdains correction, But he who regards a rebuke will be honored."},
            {"ref": "Proverbs 15:5", "text": "A fool despises his father’s instruction, But he who receives correction is prudent."},
            {"ref": "Proverbs 15:10-12", "text": "Harsh discipline is for him who forsakes the way, And he who hates correction will die. Hell and Destruction are before the LORD; So how much more the hearts of the sons of men. A scoffer does not love one who corrects him, Nor will he go to the wise."},
            {"ref": "Proverbs 15:30-32", "text": "The light of the eyes rejoices the heart, And a good report makes the bones healthy. The ear that hears the rebukes of life Will abide among the wise. He who disdains instruction despises his own soul, But he who heeds rebuke gets understanding."},
            {"ref": "Proverbs 16:22", "text": "Understanding is a wellspring of life to him who has it. But the correction of fools is folly."},
            {"ref": "Proverbs 17:10", "text": "Rebuke is more effective for a wise man Than a hundred blows on a fool."},
            {"ref": "Proverbs 29:1", "text": "He who is often rebuked, and hardens his neck, Will suddenly be destroyed, and that without remedy."}
        ],
        "dig_deeper": [
            "After you have received criticism, explain your normal reaction initially and eventually?",
            "How quickly can you recover after hearing criticism?  What about self-criticism?  Are you hard on yourself, beating yourself up and letting this affect your performance, long after others have moved on?",
            "Can you think of someone that you have witnessed take criticism well? Describe what about that person’s reaction appealed to you.",
            "Delightful, “in” the way of life, knowledgeable, honored, prudent, wise, of good report, healthy, possesses understanding and cleansed away from evil, these are ways that Proverbs describes the person who accepts correction. Contrast that to the terms describing those who do not accept correction: going astray, stupid, poor, shameful, dead, despiser of one’s own soul, fool, destroyed without remedy. Describe some of the negative consequences you’ve experienced from not accepting correction:",
            "Which verses above will help you when you are tempted to harbor resentment against someone who offers criticism?",
            "How does a person’s demeanor/style when offering criticism impact how well you accept the message?",
            "Explain how you would best like to hear criticism?",
            "Do you offer criticism as a friend, in love, with well-chosen words, “fitly spoken”?  If not, how can you improve?",
            "The next time you receive criticism in a way, other than your preference outlined above, could you communicate to the person offering the message, how you would rather it be delivered?   How could this conversation be helpful?",
            "According to the verses above, should you offer criticism to fools? To wise men?",
            "Does your boss consider you wise enough to be worthy of criticism? This may depend on your reaction (do you harden your neck or do you have a  “coachable spirit”). Think about it.  Is there anything you need to change?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 3,
        "title": "Administer Discipline to Others",
        "question": "Am I consistent and loving in administering discipline or feedback to others?",
        "verses": [
            {"ref": "Proverbs 13:24", "text": "He who spares his rod hates his son, But he who loves him disciplines him promptly."},
            {"ref": "Proverbs 19:18", "text": "Chasten your son while there is hope, And do not set your heart on his destruction."},
            {"ref": "Proverbs 20:30", "text": "Blows that hurt cleanse away evil, As do stripes the inner depths of the heart."},
            {"ref": "Proverbs 21:11", "text": "When the scoffer is punished, the simple is made wise; But when the wise is instructed, he receives knowledge."},
            {"ref": "Proverbs 22:15", "text": "Foolishness is bound up in the heart of a child; The rod of correction will drive it far from him."},
            {"ref": "Proverbs 23:13-14", "text": "Do not withhold correction from a child, For if you beat him with a rod, he will not die. You shall beat him with a rod, And deliver his soul from hell."},
            {"ref": "Proverbs 24:11-12", "text": "Deliver those who are drawn toward death, And hold back those stumbling to the slaughter. If you say, “Surely we did not know this,” Does not He who weighs the hearts consider it? He who keeps your soul, does He not know it? And will He not render to each man according to his deeds?"},
            {"ref": "Proverbs 25:11-12", "text": "A word fitly spoken is like apples of gold In settings of silver. Like an earring of gold and an ornament of fine gold Is a wise rebuker to an obedient ear."},
            {"ref": "Proverbs 26:3-5", "text": "A whip for the horse, A bridle for the donkey, And a rod for the fool’s back. Do not answer a fool according to his folly, Lest you also be like him. Answer a fool according to his folly, Lest he be wise in his own eyes."},
            {"ref": "Proverbs 27:5", "text": "Open rebuke is better Than love carefully concealed."},
            {"ref": "Proverbs 27:6", "text": "Faithful are the wounds of a friend, But the kisses of an enemy are deceitful."},
            {"ref": "Proverbs 27:17", "text": "As iron sharpens iron, So a man sharpens the countenance of his friend."},
            {"ref": "Proverbs 29:15", "text": "The rod and rebuke give wisdom, But a child left to himself brings shame to his mother."}
        ],
        "dig_deeper": [
            "Are you consistent in your administration of discipline or constructive feedback?",
            "Is it hard for you to discipline or correct someone?  Why do you think this is?",
            "Are you too harsh (set your heart on his destruction) in your discipline?",
            "Are your words “fitly”? Do you feel you can appropriately communicate a correction or could use improvement in this area? (For help, see Chapter 6 – Communicating Issues.)",
            "Have you ever given someone a break (spared the rod) because you felt sorry for them? How did it turn out? Looking back, was that the “loving” thing to do?",
            "Can you accept discipline better because you now understand it’s value and motivation (love/concern)?",
            "Summarize/prioritize things you can do, (do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 4,
        "title": "Avoid Sinners Enticing You",
        "question": "Am I careful about the company I keep and who influences me?",
        "verses": [
            {"ref": "Proverbs 1:10-19", "text": "My son, if sinners entice you, Do not consent. If they say, “Come with us, Let us lie in wait to shed blood; Let us lurk secretly for the innocent without cause; Let us swallow them alive like Sheol, And whole, like those who go down to the Pit; We shall find all kinds of precious possessions, We shall fill our houses with spoil; Cast in your lot among us, Let us all have one purse”— My son, do not walk in the way with them, Keep your foot from their path; For their feet run to evil, And they make haste to shed blood. Surely, in vain the net is spread In the sight of any bird; But they lie in wait for their own blood, They lurk secretly for their own lives. So are the ways of everyone who is greedy for gain; It takes away the life of its owners."},
            {"ref": "Proverbs 4:14-19", "text": "Do not enter the path of the wicked, And do not walk in the way of evil. Avoid it, do not travel on it; Turn away from it and pass on. For they do not sleep unless they have done evil; And their sleep is taken away unless they make someone fall. For they eat the bread of wickedness, And drink the wine of violence. But the path of the just is like the shining sun, That shines ever brighter unto the perfect day. The way of the wicked is like darkness; They do not know what makes them stumble."},
            {"ref": "Proverbs 12:26", "text": "The righteous should choose his friends carefully, For the way of the wicked leads them astray."},
            {"ref": "Proverbs 13:20-21", "text": "He who walks with wise men will be wise, But the companion of fools will be destroyed. Evil pursues sinners, But to the righteous, good shall be repaid."},
            {"ref": "Proverbs 16:29", "text": "A violent man entices his neighbor, And leads him in a way that is not good."},
            {"ref": "Proverbs 20:19", "text": "He who goes about as a talebearer reveals secrets; Therefore do not associate with one who flatters with his lips."},
            {"ref": "Proverbs 28:10", "text": "Whoever causes the upright to go astray in an evil way, He himself will fall into his own pit; But the blameless will inherit good."},
            {"ref": "Proverbs 28:17", "text": "A man burdened with bloodshed will flee into a pit; Let no one help him."},
            {"ref": "Proverbs 29:24", "text": "Whoever is a partner with a thief hates his own life; He swears to tell the truth, but reveals nothing."}
        ],
        "dig_deeper": [
            "Have you ever associated with people that cause you to behave poorly?  Give some examples:",
            "Do you continue to associate with people who are enticing you into evil?",
            "Those greedy for gain, fools, violent, talebearers/gossips, flatterers, thieves, are just some of the types of sinners enumerated in the verses above.  Look around your close circle of friends.  Do you need to make some changes in your relationships?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 5,
        "title": "Seek Wisdom/Discretion",
        "question": "Do I actively seek godly wisdom and understanding?",
        "verses": [
            {"ref": "Proverbs 2:1-9", "text": "My son, if you receive my words, And treasure my commands within you, So that you incline your ear to wisdom, And apply your heart to understanding; Yes, if you cry out for discernment, And lift up your voice for understanding, If you seek her as silver, And search for her as for hidden treasures; Then you will understand the fear of the LORD, And find the knowledge of God. For the LORD gives wisdom; From His mouth come knowledge and understanding; He stores up sound wisdom for the upright; He is a shield to those who walk uprightly; He guards the paths of justice, And preserves the way of His saints. Then you will understand righteousness and justice, Equity and every good path."},
            {"ref": "Proverbs 3:13-24", "text": "Happy is the man who finds wisdom, And the man who gains understanding; For her proceeds are better than the profits of silver, And her gain than fine gold. She is more precious than rubies, And all the things you may desire cannot compare with her. Length of days is in her right hand, In her left hand riches and honor. Her ways are ways of pleasantness, And all her paths are peace. She is a tree of life to those who take hold of her, And happy are all who retain her. The LORD by wisdom founded the earth; By understanding He established the heavens; By His knowledge the depths were broken up, And clouds drop down the dew. My son, let them not depart from your eyes— Keep sound wisdom and discretion; So they will be life to your soul And grace to your neck. Then you will walk safely in your way, And your foot will not stumble. When you lie down, you will not be afraid; Yes, you will lie down and your sleep will be sweet."},
            {"ref": "Proverbs 3:35", "text": "The wise shall inherit glory, But shame shall be the legacy of fools."},
            {"ref": "Proverbs 4:5-13", "text": "Get wisdom! Get understanding! Do not forget, nor turn away from the words of my mouth. Do not forsake her, and she will preserve you; Love her, and she will keep you. Wisdom is the principal thing; Therefore get wisdom. And in all your getting, get understanding. Exalt her, and she will promote you; She will bring you honor, when you embrace her. She will place on your head an ornament of grace; A crown of glory she will deliver to you.” Hear, my son, and receive my sayings, And the years of your life will be many. I have taught you in the way of wisdom; I have led you in right paths. When you walk, your steps will not be hindered, And when you run, you will not stumble. Take firm hold of instruction, do not let go; Keep her, for she is your life."},
            {"ref": "Proverbs 8:1-9", "text": "Does not wisdom cry out, And understanding lift up her voice? She takes her stand on the top of the high hill, Beside the way, where the paths meet. She cries out by the gates, at the entry of the city, At the entrance of the doors: “ To you, O men, I call, And my voice is to the sons of men. O you simple ones, understand prudence, And you fools, be of an understanding heart. Listen, for I will speak of excellent things, And from the opening of my lips will come right things; For my mouth will speak truth; Wickedness is an abomination to my lips. All the words of my mouth are with righteousness; Nothing crooked or perverse is in them. They are all plain to him who understands, And right to those who find knowledge."},
            {"ref": "Proverbs 10:1", "text": "The proverbs of Solomon: A wise son makes a glad father, But a foolish son is the grief of his mother."},
            {"ref": "Proverbs 10:13", "text": "Wisdom is found on the lips of him who has understanding, But a rod is for the back of him who is devoid of understanding."},
            {"ref": "Proverbs 11:22", "text": "As a ring of gold in a swine’s snout, So is a lovely woman who lacks discretion."},
            {"ref": "Proverbs 15:24", "text": "The way of life winds upward for the wise, That he may turn away from hell."},
            {"ref": "Proverbs 16:16", "text": "How much better to get wisdom than gold! And to get understanding is to be chosen rather than silver."},
            {"ref": "Proverbs 16:21", "text": "The wise in heart will be called prudent, And sweetness of the lips increases learning."},
            {"ref": "Proverbs 18:15", "text": "The heart of the prudent acquires knowledge, And the ear of the wise seeks knowledge."},
            {"ref": "Proverbs 19:8", "text": "He who gets wisdom loves his own soul; He who keeps understanding will find good."},
            {"ref": "Proverbs 21:16", "text": "A man who wanders from the way of understanding Will rest in the assembly of the dead."},
            {"ref": "Proverbs 21:22", "text": "A wise man scales the city of the mighty, And brings down the trusted stronghold."},
            {"ref": "Proverbs 24:3-5", "text": "Through wisdom a house is built, And by understanding it is established; By knowledge the rooms are filled With all precious and pleasant riches. A wise man is strong, Yes, a man of knowledge increases strength;"},
            {"ref": "Proverbs 24:7", "text": "Wisdom is too lofty for a fool; He does not open his mouth in the gate."},
            {"ref": "Proverbs 24:13-14", "text": "My son, eat honey because it is good, And the honeycomb which is sweet to your taste; So shall the knowledge of wisdom be to your soul; If you have found it, there is a prospect, And your hope will not be cut off."},
            {"ref": "Proverbs 27:11", "text": "My son, be wise, and make my heart glad, That I may answer him who reproaches me."}
        ],
        "dig_deeper": [
            "Where do you go to as your source of information?  Your boss, the Human Resources Department, management training classes, a career or life coach, your peers, other respected colleagues, your spouse, your own understanding?",
            "Have you looked specifically in the Word instead for the root of the problem and wisdom about the solution?",
            "When you do seek wisdom, it is important that you: Obtain knowledge (accumulate the available information or facts on the subject); Be wise (discern the true nature of things; that the knowledge you receive is knowledge that stands up to the test/will of the Word of God (1 Corinthians 2:15, 1 Thessalonians 5:21, 1 John 4:1, Hebrews 5:14, Romans 12:2) and; Gain understanding (learn how to apply this wisdom practically).",
            "If your issue is leadership, for example, and you gather knowledge about Servant Leadership and you see in God’s Word that Jesus calls us to practice this leadership, what can you do, practically, to model this (assuming that literally washing your employee’s feet may not be culturally acceptable)?",
            "When reading the sections on Authority, Self-Image and Your Job, did you have any “aha” moments?  Did the perspective provided help you gain wisdom about your “work-life” issue? Explain.",
            "Think of a difficult situation you’ve faced at work recently and determine to explore what the Lord’s wisdom has to say about that situation.  Would you, or could you, have reacted differently if you had this wisdom at the time you were dealing with the problem?  Explain below, then share this information with someone.",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 6,
        "title": "Seek Counsel",
        "question": "Do I seek wise counsel from multiple sources before making decisions?",
        "verses": [
            {"ref": "Proverbs 11:14", "text": "Where there is no counsel, the people fall; But in the multitude of counselors there is safety."},
            {"ref": "Proverbs 15:22", "text": "Without counsel, plans go awry, But in the multitude of counselors they are established."},
            {"ref": "Proverbs 20:5", "text": "Counsel in the heart of man is like deep water, But a man of understanding will draw it out."},
            {"ref": "Proverbs 20:18", "text": "Plans are established by counsel; By wise counsel wage war."},
            {"ref": "Proverbs 24:6", "text": "For by wise counsel you will wage your own war, And in a multitude of counselors there is safety."}
        ],
        "dig_deeper": [
            "Do you value and seek out the opinions of many counselors?",
            "How does being shy, proud or insecure affect your willingness to seek advice? Are any of these an issue for you?  Are those acceptable excuses to not follow this piece of wisdom?",
            "Can you remember a situation where you acted alone and you wish you had sought counsel?  Share some examples:",
            "Modern management theory suggests collaboration and seeking input from many individuals, departments, etc. is appropriate.  This, in essence, is a democracy.  Are there problems with seeking too much input or input from the wrong individuals?  How will you balance this?",
            "Do you (or others you deal with) sincerely seek wise counsel, the right amount of counsel, or just go through the motions of being democratic?  Remember the Lord knows our hearts.",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 7,
        "title": "Keep the Lord’s Commands",
        "question": "Do I fear the Lord and keep His commandments in daily life?",
        "verses": [
            {"ref": "Proverbs 13:13-15", "text": "He who despises the word will be destroyed, But he who fears the commandment will be rewarded. The law of the wise is a fountain of life, To turn one away from the snares of death. Good understanding gains favor, But the way of the unfaithful is hard."},
            {"ref": "Proverbs 14:26-27", "text": "In the fear of the LORD there is strong confidence, And His children will have a place of refuge. The fear of the LORD is a fountain of life, To turn one away from the snares of death."},
            {"ref": "Proverbs 16:20", "text": "He who heeds the word wisely will find good, And whoever trusts in the LORD, happy is he."},
            {"ref": "Proverbs 19:16", "text": "He who keeps the commandment keeps his soul, But he who is careless of his ways will die."},
            {"ref": "Proverbs 19:23", "text": "The fear of the LORD leads to life, And he who has it will abide in satisfaction; He will not be visited with evil."},
            {"ref": "Proverbs 28:4", "text": "Those who forsake the law praise the wicked, But such as keep the law contend with them."},
            {"ref": "Proverbs 28:9", "text": "One who turns away his ear from hearing the law, even his prayer is an abomination."},
            {"ref": "Proverbs 29:18", "text": "Where there is no revelation, the people cast off restraint; But happy is he who keeps the law."}
        ],
        "dig_deeper": [
            "Review the 10 Commandments (Exodus 20).  Do you feel you truly believe in them, trust them, and revere the Lord enough to try to keep them?",
            "How can you remind yourself of the commandments and hold yourself accountable to them in every circumstance?",
            "If you cannot live up to the commandments, “the law”, do you believe that all things are possible through Christ and that he has paid the price for your failures?",
            "Does this release you from the responsibility to live lawfully?  (See Romans 6:15.)",
            "The verses above show that those that DON’T revere or fear the Lord and keep His commandments will suffer. They tell us… The way of the unfaithful, the careless, the one who turns his ear from the law is hard and leads to death.  This causes one: to be dissatisfied, visited with evil, to praise wickedness, to cast off restraint, and results in unhappiness and prayers that are an abomination. Being a faithful Christian, however, should help you: be rewarded, turn away from the snares of death, gain favor, have strong confidence, have a safe refuge, find good, be happy, keep your soul, abide in satisfaction, not be visited with evil, and allow you to contend with the wicked. Which list of characteristics, paragraph (a or b) above, best describes your life?  Is your life reflecting the rewards of a faithful Christian, why or why not?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 8,
        "title": "Trust in the Lord",
        "question": "Do I trust the Lord fully with my work and life paths?",
        "verses": [
            {"ref": "Proverbs 3:5-6", "text": "Trust in the LORD with all your heart, And lean not on your own understanding; In all your ways acknowledge Him, And He shall direct your paths."},
            {"ref": "Proverbs 3:25-26", "text": "Do not be afraid of sudden terror, Nor of trouble from the wicked when it comes; For the LORD will be your confidence, And will keep your foot from being caught."},
            {"ref": "Proverbs 16:4", "text": "The LORD has made all for Himself, Yes, even the wicked for the day of doom."},
            {"ref": "Proverbs 16:9", "text": "A man's heart plans his way, But the LORD directs his steps."},
            {"ref": "Proverbs 16:33", "text": "The lot is cast into the lap, But its every decision is from the LORD."},
            {"ref": "Proverbs 18:10-11", "text": "The name of the LORD is a strong tower; The righteous run to it and are safe. The rich man's wealth is his strong city, And like a high wall in his own esteem."},
            {"ref": "Proverbs 19:21", "text": "There are many plans in a man's heart, Nevertheless the LORD's counsel—that will stand."},
            {"ref": "Proverbs 21:1", "text": "The king's heart is in the hand of the LORD, Like the rivers of water; He turns it wherever He wishes."},
            {"ref": "Proverbs 21:30-31", "text": "There is no wisdom or understanding Or counsel against the LORD. The horse is prepared for the day of battle, But deliverance is of the LORD."},
            {"ref": "Proverbs 22:17-21", "text": "Incline your ear and hear the words of the wise, And apply your heart to my knowledge; For it is a pleasant thing if you keep them within you; Let them all be fixed upon your lips, So that your trust may be in the LORD; I have instructed you today, even you. Have I not written to you excellent things Of counsels and knowledge, That I may make you know the certainty of the words of truth, That you may answer words of truth To those who send to you?"},
            {"ref": "Proverbs 29:25", "text": "The fear of man brings a snare, But whoever trusts in the LORD shall be safe."},
            {"ref": "Proverbs 30:1-6", "text": "The words of Agur the son of Jakeh, his utterance. This man declared to Ithiel—to Ithiel and Ucal: Surely I am more stupid than any man, And do not have the understanding of a man. I neither learned wisdom Nor have knowledge of the Holy One. Who has ascended into heaven, or descended? Who has gathered the wind in His fists? Who has bound the waters in a garment? Who has established all the ends of the earth? What is His name, and what is His Son's name, If you know? Every word of God is pure; He is a shield to those who put their trust in Him. Do not add to His words, Lest He rebuke you, and you be found a liar."}
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
            {"ref": "Proverbs 14:12", "text": "There is a way that seems right to a man, But its end is the way of death."},
            {"ref": "Proverbs 14:14", "text": "The backslider in heart will be filled with his own ways, But a good man will be satisfied from above."},
            {"ref": "Proverbs 16:2", "text": "All the ways of a man are pure in his own eyes, But the LORD weighs the spirits."},
            {"ref": "Proverbs 16:25", "text": "There is a way that seems right to a man, But its end is the way of death."},
            {"ref": "Proverbs 20:24", "text": "A man's steps are of the LORD; How then can a man understand his own way?"},
            {"ref": "Proverbs 21:2", "text": "Every way of a man is right in his own eyes, But the LORD weighs the hearts."},
            {"ref": "Proverbs 26:12", "text": "Do you see a man wise in his own eyes? There is more hope for a fool than for him."},
            {"ref": "Proverbs 27:1-2", "text": "Do not boast about tomorrow, For you do not know what a day may bring forth. Let another man praise you, and not your own mouth; A stranger, and not your own lips."},
            {"ref": "Proverbs 28:11", "text": "The rich man is wise in his own eyes, But the poor who has understanding searches him out."},
            {"ref": "Proverbs 28:26", "text": "He who trusts in his own heart is a fool, But whoever walks wisely will be delivered."},
            {"ref": "Proverbs 30:12", "text": "There is a generation that is pure in its own eyes, Yet is not washed from its filthiness."},
            {"ref": "Proverbs 30:32-33", "text": "If you have been foolish in exalting yourself, Or if you have devised evil, put your hand on your mouth. For as the churning of milk produces butter, And wringing the nose produces blood, So the forcing of wrath produces strife."}
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
            {"ref": "Proverbs 3:27-28", "text": "Do not withhold good from those to whom it is due, When it is in the power of your hand to do so. Do not say to your neighbor, Go, and come back, And tomorrow I will give it, When you have it with you."}
        ],
        "dig_deeper": [
            "Are you fair in your payment of wages, return of debts owed, returning things borrowed, keeping of promises, providing the information necessary for people to do their jobs well and giving credit when credit is due?  If not, where do you fall short?",
            "The verse above pertains to payment of debts; do you feel you have a debt of praise to an employee or boss that has done a job well?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 11,
        "title": "Don't be in Debt",
        "question": "I avoid unnecessary debt and financial bondage?",
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
        "question": "I avoid plotting evil or taking advantage of others?",
        "verses": [
            {"ref": "Proverbs 3:29", "text": "Do not devise evil against your neighbor, For he dwells by you for safety's sake."},
            {"ref": "Proverbs 14:22", "text": "Do they not go astray who devise evil? But mercy and truth belong to those who devise good."},
            {"ref": "Proverbs 23:10-11", "text": "Do not remove the ancient landmark, Nor enter the fields of the fatherless; For their Redeemer is mighty; He will plead their cause against you."},
            {"ref": "Proverbs 24:15-16", "text": "Do not lie in wait, O wicked man, against the dwelling of the righteous; Do not plunder his resting place; For a righteous man may fall seven times And rise again, But the wicked shall be cast down by calamity."}
        ],
        "dig_deeper": [
            "Have you ever acted to plot against someone?   What motivated you to take this approach: anger, revenge or pride?",
            "Did this approach work out well for you?",
            "Proverbs 24:15-16 (the last verse in this section) notes how wicked men, will be thwarted if they try to devise evil against the righteous.  Does this give you confidence not to worry about those that plot against you?",
            "If either acting to plot evil or worrying about those that plot against you is an issue, summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 13,
        "title": "Don't Strive",
        "question": "I avoid unnecessary strife and arguments?",
        "verses": [
            {"ref": "Proverbs 3:30", "text": "Do not strive with a man without cause, If he has done you no harm."},
            {"ref": "Proverbs 11:12", "text": "He who is devoid of wisdom despises his neighbor, But a man of understanding holds his peace."},
            {"ref": "Proverbs 11:29", "text": "He who troubles his own house will inherit the wind, And the fool will be servant to the wise of heart."},
            {"ref": "Proverbs 16:7", "text": "When a man's ways please the LORD, He makes even his enemies to be at peace with him."},
            {"ref": "Proverbs 16:14-15", "text": "As messengers of death is the king's wrath, But a wise man will appease it. In the light of the king's face is life, And his favor is like a cloud of the latter rain."},
            {"ref": "Proverbs 17:1", "text": "Better is a dry morsel with quietness, Than a house full of feasting with strife."},
            {"ref": "Proverbs 17:9", "text": "He who covers a transgression seeks love, But he who repeats a matter separates friends."},
            {"ref": "Proverbs 18:18-19", "text": "Casting lots causes contentions to cease, And keeps the mighty apart. A brother offended is harder to win than a strong city, And contentions are like the bars of a castle."},
            {"ref": "Proverbs 19:12", "text": "The king's wrath is like the roaring of a lion, But his favor is like dew on the grass."},
            {"ref": "Proverbs 20:2-3", "text": "The wrath of a king is like the roaring of a lion; Whoever provokes him to anger sins against his own life. It is honorable for a man to stop striving, Since any fool can start a quarrel."},
            {"ref": "Proverbs 21:9", "text": "Better to dwell in a corner of a housetop, Than in a house shared with a contentious woman."},
            {"ref": "Proverbs 26:2", "text": "Like a flitting sparrow, like a flying swallow, So a curse without cause shall not alight."},
            {"ref": "Proverbs 26:20-21", "text": "Where there is no wood, the fire goes out; And where there is no talebearer, strife ceases. As charcoal is to burning coals, and wood to fire, So is a contentious man to kindle strife."},
            {"ref": "Proverbs 28:25", "text": "He who is of a proud heart stirs up strife, But he who trusts in the LORD will be prospered."}
        ],
        "dig_deeper": [
            "Does conflict make you uncomfortable or would you say, \"bring it on\"? Why do you think that is?",
            "What makes you get involved in arguments (your own or other's)?",
            "Why do you feel the need to stand your ground in an argument?",
            "If you backed down from an argument, how would you be perceived?",
            "Have you ever used \"casting lots\" to end a quarrel?   Would you trust the Lord to direct the outcome and live peaceably with the result?",
            "What specific things can you do to avoid strife?  List the things that stand out as most important to you, personally, from the verses above.",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 14,
        "title": "Don't Have a Perverse Heart",
        "question": "Is my heart upright toward God and others, or perverse?",
        "verses": [
            {"ref": "Proverbs 11:20", "text": "Those who are of a perverse heart are an abomination to the LORD, But the blameless in their ways are His delight."},
            {"ref": "Proverbs 12:8", "text": "A man will be commended according to his wisdom, But he who is of a perverse heart will be despised."},
            {"ref": "Proverbs 14:2", "text": "He who walks in his uprightness fears the LORD, But he who is perverse in his ways despises Him."},
            {"ref": "Proverbs 17:3", "text": "The refining pot is for silver and the furnace for gold, But the LORD tests the hearts."},
            {"ref": "Proverbs 20:27", "text": "The spirit of man is the lamp of the LORD, Searching all the inner depths of his heart."},
            {"ref": "Proverbs 21:4", "text": "A haughty look, a proud heart, And the plowing of the wicked are sin."},
            {"ref": "Proverbs 21:27", "text": "The sacrifice of the wicked is an abomination; How much more when he brings it with wicked intent!"},
            {"ref": "Proverbs 22:5", "text": "Thorns and snares are in the way of the perverse; He who guards his soul will be far from them."},
            {"ref": "Proverbs 27:19", "text": "As in water face reflects face, So a man's heart reveals the man."},
            {"ref": "Proverbs 28:14", "text": "Happy is the man who is always reverent, But he who hardens his heart will fall into calamity."},
            {"ref": "Proverbs 28:18", "text": "Whoever walks blamelessly will be saved, But he who is perverse in his ways will suddenly fall."}
        ],
        "dig_deeper": [
            "Where does this attitude come from?  Can you identify the root of the issue?",
            "What is the opposite of a perverse heart (see verses above)?",
            "What can you do to overcome this attitude?",
            "If you think your boss/coworker has this issue, what makes you think so?  What behaviors lead you to believe this?",
            "How does this impact your job?",
            "What has been your response?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 15,
        "title": "Be an Excellent Wife",
        "question": "Am I an excellent, virtuous spouse who adds value to my family and work?",
        "verses": [
            {"ref": "Proverbs 12:4", "text": "An excellent wife is the crown of her husband, But she who causes shame is like rottenness in his bones."},
            {"ref": "Proverbs 18:22", "text": "He who finds a wife finds a good thing, And obtains favor from the LORD."},
            {"ref": "Proverbs 19:14", "text": "Houses and riches are an inheritance from fathers, But a prudent wife is from the LORD."},
            {"ref": "Proverbs 31:10-31", "text": "Who can find a virtuous wife? For her worth is far above rubies. The heart of her husband safely trusts her; So he will have no lack of gain. She does him good and not evil All the days of her life. She seeks wool and flax, And willingly works with her hands. She is like the merchant ships, She brings her food from afar. She also rises while it is yet night, And provides food for her household, And a portion for her maidservants. She considers a field and buys it; From her profits she plants a vineyard. She girds herself with strength, And strengthens her arms. She perceives that her merchandise is good, And her lamp does not go out by night. She stretches out her hands to the distaff, And her hand holds the spindle. She extends her hand to the poor, Yes, she reaches out her hands to the needy. She is not afraid of snow for her household, For all her household is clothed with scarlet. She makes tapestry for herself; Her clothing is fine linen and purple. Her husband is known in the gates, When he sits among the elders of the land. She makes linen garments and sells them, And supplies sashes for the merchants. Strength and honor are her clothing; She shall rejoice in time to come. She opens her mouth with wisdom, And on her tongue is the law of kindness. She watches over the ways of her household, And does not eat the bread of idleness. Her children rise up and call her blessed; Her husband also, and he praises her: \"Many daughters have done well, But you excel them all.\" Charm is deceitful and beauty is passing, But a woman who fears the LORD, she shall be praised. Give her of the fruit of her hands, And let her own works praise her in the gates."},
            {"ref": "Proverbs 25:24", "text": "It is better to dwell in a corner of a housetop, Than in a house shared with a contentious woman."}
        ],
        "dig_deeper": [
            "Have you ever considered the value you have as an excellent vs. a shameful wife/spouse?  Describe how you have added value to your spouse.",
            "How can your excellence as a wife/spouse help those beyond your spouse: your household, your work, and your community?",
            "How can (has) being a contentious wife be(en) a detriment to your spouse?",
            "Where does that ability to be excellent come from (you or the Lord)?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 16,
        "title": "Avoid Anger",
        "question": "Am I slow to anger and in control of my temper?",
        "verses": [
            {"ref": "Proverbs 12:16", "text": "A fool's wrath is known at once, But a prudent man covers shame."},
            {"ref": "Proverbs 14:10", "text": "The heart knows its own bitterness, And a stranger does not share its joy."},
            {"ref": "Proverbs 14:16-17", "text": "A wise man fears and departs from evil, But a fool rages and is self-confident. A quick-tempered man acts foolishly, And a man of wicked intentions is hated."},
            {"ref": "Proverbs 14:29", "text": "He who is slow to wrath has great understanding, But he who is impulsive exalts folly."},
            {"ref": "Proverbs 15:18", "text": "A wrathful man stirs up strife, But he who is slow to anger allays contention."},
            {"ref": "Proverbs 16:32", "text": "He who is slow to anger is better than the mighty, And he who rules his spirit than he who takes a city."},
            {"ref": "Proverbs 19:11", "text": "The discretion of a man makes him slow to anger, And his glory is to overlook a transgression."},
            {"ref": "Proverbs 19:19", "text": "A man of great wrath will suffer punishment; For if you rescue him, you will have to do it again."},
            {"ref": "Proverbs 21:29", "text": "A wicked man hardens his face, But as for the upright, he establishes his way."},
            {"ref": "Proverbs 22:24-25", "text": "Make no friendship with an angry man, And with a furious man do not go, Lest you learn his ways And set a snare for your soul."},
            {"ref": "Proverbs 27:15-16", "text": "A continual dripping on a very rainy day And a contentious woman are alike; Whoever restrains her restrains the wind, And grasps oil with his right hand."},
            {"ref": "Proverbs 29:22", "text": "An angry man stirs up strife, And a furious man abounds in transgression."}
        ],
        "dig_deeper": [
            "Has your anger ever made you look foolish?",
            "Has your anger ever hurt someone, irritated (continual dripping) or made someone mad at you?",
            "Have you ever let a friend's anger make you angry?",
            "Why is your heart bitter/contentious?",
            "What do the verses below teach you that can you do to control your anger?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 17,
        "title": "Avoid Anxiety",
        "question": "Do I avoid anxiety by speaking good words and trusting God?",
        "verses": [
            {"ref": "Proverbs 12:25", "text": "Anxiety in the heart of man causes depression, But a good word makes it glad."}
        ],
        "dig_deeper": [
            "Who do you need “a good word” from?  Will you tell them that?",
            "Do you give “good words”? Whom can you give “a good word” to?",
            "Can you find other verses about worry and anxiety throughout the Bible?   (Try: Matthew 6:25, 27, 28, 31, 34; Matthew 10:19; Mark 3:11; Luke 12:11, 22, 25.)",
            "How do you deal with your anxiety?  What helps put things in perspective for you?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 18,
        "title": "Don’t Abuse Alcohol",
        "question": "Do I avoid excess in alcohol or anything that leads me astray?",
        "verses": [
            {"ref": "Proverbs 20:1", "text": "Wine is a mocker, Strong drink is a brawler, And whoever is led astray by it is not wise."},
            {"ref": "Proverbs 21:17", "text": "He who loves pleasure will be a poor man; He who loves wine and oil will not be rich."},
            {"ref": "Proverbs 23:29-35", "text": "Who has woe? Who has sorrow? Who has contentions? Who has complaints? Who has wounds without cause? Who has redness of eyes? Those who linger long at the wine, Those who go in search of mixed wine. Do not look on the wine when it is red, When it sparkles in the cup, When it swirls around smoothly; At the last it bites like a serpent, And stings like a viper. Your eyes will see strange things, And your heart will utter perverse things. Yes, you will be like one who lies down in the midst of the sea, Or like one who lies at the top of the mast, saying: “They have struck me, but I was not hurt; They have beaten me, but I did not feel it. When shall I awake, that I may seek another drink?”"},
            {"ref": "Proverbs 31:4-7", "text": "It is not for kings, O Lemuel, It is not for kings to drink wine, Nor for princes intoxicating drink; Lest they drink and forget the law, And pervert the justice of all the afflicted. Give strong drink to him who is perishing, And wine to those who are bitter of heart. Let him drink and forget his poverty, And remember his misery no more."}
        ],
        "dig_deeper": [
            "Do you personally struggle with alcohol or other substances that mock or control you?",
            "Have you seen alcohol or other addictions destroy someone’s career or family?",
            "What boundaries or habits could you put in place to protect yourself and set a godly example at work?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 19,
        "title": "Don’t Envy the Oppressors",
        "question": "Do I envy those who get ahead by dishonest or oppressive means?",
        "verses": [
            {"ref": "Proverbs 3:31-33", "text": "Do not envy the oppressor, And choose none of his ways; For the perverse person is an abomination to the LORD, But His secret counsel is with the upright. The curse of the LORD is on the house of the wicked, But He blesses the home of the just."},
            {"ref": "Proverbs 12:12", "text": "The wicked covet the catch of evil men, But the root of the righteous yields fruit."},
            {"ref": "Proverbs 24:1-2", "text": "Do not be envious of evil men, Nor desire to be with them; For their heart devises violence, And their lips talk of troublemaking."},
            {"ref": "Proverbs 24:19-20", "text": "Do not fret because of evildoers, Nor be envious of the wicked; For there will be no prospect for the evil man; The lamp of the wicked will be put out."},
            {"ref": "Proverbs 28:3", "text": "A poor man who oppresses the poor Is like a driving rain which leaves no food."}
        ],
        "dig_deeper": [
            "Do these verses convince you of your need to put those thoughts of envy behind you? Why or why not?",
            "Have you ever witnessed the “fall” of someone who got ahead by dishonest means or by oppressing others?   Some are never “caught” in this life, but can you list some consequences for those that are caught; for themselves, for their families?",
            "What do you need to do to get beyond this thought-pattern of envy/coveting?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
           "id": 20,
        "title": "Don't Envy/Be Jealous",
        "question": "Do I envy or become jealous of the success, possessions, or position of others?",
        "verses": [
            {"ref": "Proverbs 3:31-32", "text": "Do not envy the oppressor, And choose none of his ways; For the perverse person is an abomination to the LORD, But His secret counsel is with the upright."},
            {"ref": "Proverbs 14:30", "text": "A sound heart is life to the body, But envy is rottenness to the bones."},
            {"ref": "Proverbs 23:17-18", "text": "Do not let your heart envy sinners, But be zealous for the fear of the LORD all the day; For surely there is a hereafter, And your hope will not be cut off."},
            {"ref": "Proverbs 24:1-2", "text": "Do not be envious of evil men, Nor desire to be with them; For their heart devises violence, And their lips talk of troublemaking."},
            {"ref": "Proverbs 24:19-20", "text": "Do not fret because of evildoers, Nor be envious of the wicked; For there will be no prospect for the evil man; The lamp of the wicked will be put out."},
            {"ref": "Proverbs 27:4", "text": "Wrath is cruel and anger a torrent, But who is able to stand before envy?"}
        ],
        "dig_deeper": [
            "When have you felt envy or jealousy toward someone at work or in life? What triggered it?",
            "How did that envy affect your thoughts, words, or actions toward that person?",
            "According to Proverbs 14:30, what does envy do to your own body and soul?",
            "The verses above warn against envying sinners, oppressors, and evil men. Why do you think we are still tempted to envy them?",
            "What promises does God give in Proverbs 23:17-18 and 24:19-20 to help you overcome envy?",
            "What practical step can you take this week to replace envy with contentment and celebration of others’ success?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 21,
        "title": "Don't Reward Evil",
        "question": "Do I reward evil with evil, or do I overcome evil with good?",
        "verses": [
            {"ref": "Proverbs 17:13", "text": "Whoever rewards evil for good, Evil will not depart from his house."},
            {"ref": "Proverbs 20:22", "text": "Do not say, “I will recompense evil”; Wait for the LORD, and He will save you."},
            {"ref": "Proverbs 24:29", "text": "Do not say, “I will do to him just as he has done to me; I will render to the man according to his work.”"},
            {"ref": "Proverbs 25:21-22", "text": "If your enemy is hungry, give him bread to eat; And if he is thirsty, give him water to drink; For so you will heap coals of fire on his head, And the LORD will reward you."}
        ],
        "dig_deeper": [
            "Have you ever repaid evil for evil (gossip, revenge, withholding help, etc.)? What was the result?",
            "Why is it so tempting to “get even” when someone wrongs us?",
            "According to Proverbs 25:21-22 and Romans 12:20-21, how should we respond when someone treats us badly?",
            "What does it mean to “heap coals of fire on his head”? Is this punishment or a way to bring conviction and possible repentance?",
            "Think of someone who has wronged you recently. What is one practical way you can repay them with good this week?",
            "How does refusing to reward evil protect your own house and life (Proverbs 17:13)?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 22,
        "title": "Be Humble",
        "question": "Am I humble or proud in spirit?",
        "verses": [
            {"ref": "Proverbs 11:2", "text": "When pride comes, then comes shame; But with the humble is wisdom."},
            {"ref": "Proverbs 15:33", "text": "The fear of the LORD is the instruction of wisdom, And before honor is humility."},
            {"ref": "Proverbs 16:18-19", "text": "Pride goes before destruction, And a haughty spirit before a fall. Better to be of a humble spirit with the lowly, Than to divide the spoil with the proud."},
            {"ref": "Proverbs 18:12", "text": "Before destruction the heart of a man is haughty, And before honor is humility."},
            {"ref": "Proverbs 22:4", "text": "By humility and the fear of the LORD Are riches and honor and life."},
            {"ref": "Proverbs 29:23", "text": "A man’s pride will bring him low, But the humble in spirit will retain honor."}
        ],
        "dig_deeper": [
            "Where in your life or work do you struggle most with pride?",
            "How has pride ever led to shame or a fall for you?",
            "What practical habits help you stay humble before God and others?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 23,
        "title": "Put Away A Deceitful Mouth",
        "question": "Do I speak truthfully, or do I lie, flatter, or slander?",
        "verses": [
            {"ref": "Proverbs 4:24", "text": "Put away from you a deceitful mouth, And put perverse lips far from you."},
            {"ref": "Proverbs 6:12-14", "text": "A worthless person, a wicked man, Walks with a perverse mouth…"},
            {"ref": "Proverbs 10:18", "text": "Whoever hides hatred has lying lips, And whoever spreads slander is a fool."},
            {"ref": "Proverbs 12:22", "text": "Lying lips are an abomination to the LORD, But those who deal truthfully are His delight."},
            {"ref": "Proverbs 26:28", "text": "A lying tongue hates those who are crushed by it, And a flattering mouth works ruin."}
        ],
        "dig_deeper": [
            "List any areas where you are tempted to lie, exaggerate, flatter, or gossip.",
            "What damage have you seen lying or flattery cause in the workplace?",
            "How can you replace deceitful speech with truthful, edifying words this week?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 24,
        "title": "Let Your Ways Be Established",
        "question": "Are my ways steady and established, or do I waver and stumble?",
        "verses": [
            {"ref": "Proverbs 4:26-27", "text": "Ponder the path of your feet, And let all your ways be established. Do not turn to the right or the left; Remove your foot from evil."}
        ],
        "dig_deeper": [
            "In what area of life or work do your “ways” feel unsteady right now?",
            "What specific steps can you take to “ponder the path” and establish your ways this week?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 25,
        "title": "Avoid Immoral Women",
        "question": "Do I guard my eyes, heart, and steps from sexual immorality and seductive women (or men)?",
        "verses": [
            {"ref": "Proverbs 2:16-19", "text": "To deliver you from the immoral woman, From the seductress who flatters with her words…"},
            {"ref": "Proverbs 5:3-23", "text": "For the lips of an immoral woman drip honey… (full warning passage)"},
            {"ref": "Proverbs 6:24-35", "text": "To keep you from the evil woman…"},
            {"ref": "Proverbs 7:1-27", "text": "My son, keep my words… (the entire dramatic story of the young man and the adulteress)"},
            {"ref": "Proverbs 9:13-18", "text": "A foolish woman is clamorous… Stolen water is sweet…"},
            {"ref": "Proverbs 22:14", "text": "The mouth of an immoral woman is a deep pit…"},
            {"ref": "Proverbs 23:27-28", "text": "For a harlot is a deep pit…"},
            {"ref": "Proverbs 30:20", "text": "This is the way of an adulterous woman…"}
        ],
        "dig_deeper": [
            "Have you ever been enticed or drawn toward sexual immorality (pornography, flirting, emotional/physical affairs)? How close did you get?",
            "What safeguards do you currently have in place to protect your marriage, your witness, and your soul?",
            "How does the imagery (“her house is the way to hell”, “fire in the bosom”) affect your view of sexual sin?",
            "If you have fallen, have you repented and set boundaries? What steps will you take this week?",
            "How can you help someone else struggling without falling yourself?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 26,
        "title": "Don't Misplace Your Confidence",
        "question": "Do I put my confidence in the Lord rather than in man, riches, or myself?",
        "verses": [
            {"ref": "Proverbs 3:26", "text": "For the LORD will be your confidence, And will keep your foot from being caught."},
            {"ref": "Proverbs 11:28", "text": "He who trusts in his riches will fall, But the righteous will flourish like foliage."},
            {"ref": "Proverbs 14:26", "text": "In the fear of the LORD there is strong confidence…"},
            {"ref": "Proverbs 28:26", "text": "He who trusts in his own heart is a fool, But whoever walks wisely will be delivered."}
        ],
        "dig_deeper": [
            "Where have you been tempted to put confidence in money, position, talent, or people instead of God?",
            "What does it look like practically to make the Lord your confidence at work?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 27,
        "title": "Avoid Folly",
        "question": "Do I avoid foolish and sinful behavior?",
        "verses": [
            {"ref": "Proverbs 1:22", "text": "How long, you simple ones, will you love simplicity?..."},
            {"ref": "Proverbs 9:6", "text": "Forsake foolishness and live…"},
            {"ref": "Proverbs 14:7-9", "text": "Go from the presence of a foolish man… Fools mock at sin…"},
            {"ref": "Proverbs 26:11", "text": "As a dog returns to his own vomit, So a fool repeats his folly."}
        ],
        "dig_deeper": [
            "What recurring foolish or sinful habits do you need to forsake?",
            "How can you practically “go from the presence” of foolish influences?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 28,
        "title": "Don't Pledge Surety",
        "question": "Am I careful about co-signing or becoming surety for others’ debts?",
        "verses": [
            {"ref": "Proverbs 6:1-5", "text": "My son, if you become surety for your friend… Do this… deliver yourself…"},
            {"ref": "Proverbs 11:15", "text": "He who is surety for a stranger will suffer, But one who hates being surety is secure."},
            {"ref": "Proverbs 17:18", "text": "A man devoid of understanding shakes hands in a pledge, And becomes surety for his friend."},
            {"ref": "Proverbs 22:26-27", "text": "Do not be one of those who shakes hands in a pledge…"},
            {"ref": "Proverbs 27:13", "text": "Take the garment of him who is surety for a stranger…"}
        ],
        "dig_deeper": [
            "Have you ever co-signed or guaranteed someone else’s debt? How did it turn out?",
            "Why does God so strongly warn against surety?",
            "What boundaries will you set going forward regarding financial guarantees?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 29,
        "title": "Don't be a Sluggard/Lazy",
        "question": "Am I diligent and hardworking, or do I exhibit laziness?",
        "verses": [
            {"ref": "Proverbs 6:6-11", "text": "Go to the ant, you sluggard!..."},
            {"ref": "Proverbs 10:4-5", "text": "He who has a slack hand becomes poor…"},
            {"ref": "Proverbs 12:24", "text": "The hand of the diligent will rule, But the lazy man will be put to forced labor."},
            {"ref": "Proverbs 13:4", "text": "The soul of a lazy man desires, and has nothing; But the soul of the diligent shall be made rich."},
            {"ref": "Proverbs 15:19", "text": "The way of the lazy man is like a hedge of thorns…"},
            {"ref": "Proverbs 18:9", "text": "He who is slothful in his work Is a brother to him who is a great destroyer."},
            {"ref": "Proverbs 19:15", "text": "Laziness casts one into a deep sleep, And an idle person will suffer hunger."},
            {"ref": "Proverbs 20:4", "text": "The lazy man will not plow because of winter; He will beg during harvest and have nothing."},
            {"ref": "Proverbs 21:25", "text": "The desire of the lazy man kills him, For his hands refuse to labor."},
            {"ref": "Proverbs 24:30-34", "text": "I went by the field of the lazy man… (the vineyard overgrown with thorns)"},
            {"ref": "Proverbs 26:13-16", "text": "The lazy man says, “There is a lion in the road!”…"}
        ],
        "dig_deeper": [
            "In what areas of work or home life are you tempted to be lazy?",
            "How has laziness ever cost you opportunities or relationships?",
            "What specific steps will you take this week to become more diligent?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {      
            "id": 30,
        "title": "Don't let a Perverse Mouth Sow Discord",
        "question": "Do my words bring peace and unity, or do they sow discord and division?",
        "verses": [
            {"ref": "Proverbs 6:12-15", "text": "A worthless person, a wicked man, Walks with a perverse mouth; He winks with his eyes, He shuffles his feet, He points with his fingers; Perversity is in his heart, He devises evil continually, He sows discord. Therefore his calamity shall come suddenly; Suddenly he shall be broken without remedy."},
            {"ref": "Proverbs 6:16-19", "text": "These six things the LORD hates, Yes, seven are an abomination to Him: … A false witness who speaks lies, And one who sows discord among brethren."},
            {"ref": "Proverbs 10:12", "text": "Hatred stirs up strife, But love covers all sins."},
            {"ref": "Proverbs 15:18", "text": "A wrathful man stirs up strife, But he who is slow to anger allays contention."},
            {"ref": "Proverbs 16:28", "text": "A perverse man sows strife, And a whisperer separates the best of friends."},
            {"ref": "Proverbs 22:10", "text": "Cast out the scoffer, and contention will leave; Yes, strife and reproach will cease."},
            {"ref": "Proverbs 26:20-21", "text": "Where there is no wood, the fire goes out; And where there is no talebearer, strife ceases. As charcoal is to burning coals, and wood to fire, So is a contentious man to kindle strife."},
            {"ref": "Proverbs 28:25", "text": "He who is of a proud heart stirs up strife, But he who trusts in the LORD will be prospered."}
        ],
        "dig_deeper": [
            "Have your words (gossip, criticism, sarcasm, complaining) ever sown discord at work or home?",
            "What damage have you seen division cause in a team, church, or family?",
            "What practical steps can you take this week to become a peacemaker instead of a strife-starter?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 31,
        "title": "Avoid Wickedness/Seek Righteousness",
        "question": "Am I actively fleeing wickedness and pursuing righteousness in every area of life?",
        "verses": [
            {"ref": "Proverbs 3:7", "text": "Do not be wise in your own eyes; Fear the LORD and depart from evil."},
            {"ref": "Proverbs 4:14-15", "text": "Do not enter the path of the wicked, And do not walk in the way of evil. Avoid it, do not travel on it; Turn away from it and pass on."},
            {"ref": "Proverbs 8:13", "text": "The fear of the LORD is to hate evil; Pride and arrogance and the evil way And the perverse mouth I hate."},
            {"ref": "Proverbs 11:5", "text": "The righteousness of the blameless will direct his way aright, But the wicked will fall by his own wickedness."},
            {"ref": "Proverbs 11:19", "text": "As righteousness leads to life, So he who pursues evil pursues it to his own death."},
            {"ref": "Proverbs 12:28", "text": "In the way of righteousness is life, And in its pathway there is no death."},
            {"ref": "Proverbs 13:6", "text": "Righteousness guards him whose way is blameless, But wickedness overthrows the sinner."},
            {"ref": "Proverbs 14:34", "text": "Righteousness exalts a nation, But sin is a reproach to any people."},
            {"ref": "Proverbs 15:9", "text": "The way of the wicked is an abomination to the LORD, But He loves him who follows righteousness."},
            {"ref": "Proverbs 21:21", "text": "He who follows righteousness and mercy Finds life, righteousness, and honor."}
        ],
        "dig_deeper": [
            "In what specific area of your life or work do you need to more actively “depart from evil” right now?",
            "What does it look like practically to “pursue righteousness” in your daily decisions?",
            "How does choosing righteousness affect your witness and influence at work?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 32,
        "title": "Store Knowledge",
        "question": "Do I continually store up godly knowledge and understanding?",
        "verses": [
            {"ref": "Proverbs 10:14", "text": "Wise people store up knowledge, But the mouth of the foolish is near destruction."},
            {"ref": "Proverbs 15:14", "text": "The heart of him who has understanding seeks knowledge, But the mouth of fools feeds on foolishness."},
            {"ref": "Proverbs 18:15", "text": "The heart of the prudent acquires knowledge, And the ear of the wise seeks knowledge."},
            {"ref": "Proverbs 19:2", "text": "Also it is not good for a soul to be without knowledge, And he sins who hastens with his feet."},
            {"ref": "Proverbs 23:12", "text": "Apply your heart to instruction, And your ears to words of knowledge."},
            {"ref": "Proverbs 24:4", "text": "By knowledge the rooms are filled With all precious and pleasant riches."}
        ],
        "dig_deeper": [
            "How are you currently “storing up” godly knowledge (Bible reading, books, sermons, mentors, etc.)?",
            "In what work-related skill or spiritual area do you most need to grow in knowledge right now?",
            "What is one new habit you can start this week to seek and store more knowledge?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 33,
        "title": "Don't Use Dishonest Means",
        "question": "Do I reject dishonest gain and dishonest scales?",
        "verses": [
            {"ref": "Proverbs 11:1", "text": "Dishonest scales are an abomination to the LORD, But a just weight is His delight."},
            {"ref": "Proverbs 13:11", "text": "Wealth gained by dishonesty will be diminished, But he who gathers by labor will increase."},
            {"ref": "Proverbs 16:8", "text": "Better is a little with righteousness, Than vast revenues without justice."},
            {"ref": "Proverbs 20:10", "text": "Diverse weights and diverse measures, They are both alike, an abomination to the LORD."},
            {"ref": "Proverbs 20:17", "text": "Bread gained by deceit is sweet to a man, But afterward his mouth will be filled with gravel."},
            {"ref": "Proverbs 20:23", "text": "Diverse weights are an abomination to the LORD, And dishonest scales are not good."},
            {"ref": "Proverbs 21:6", "text": "Getting treasures by a lying tongue Is the fleeting fantasy of those who seek death."}
        ],
        "dig_deeper": [
            "Have you ever cut corners, exaggerated, or used dishonest means to gain advantage at work?",
            "What does “bread gained by deceit” tasting sweet at first but turning to gravel teach us?",
            "What practical steps can you take to ensure complete honesty in your business and finances?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 34,
        "title": "Fairly Apply Justice",
        "question": "Do I judge and treat people fairly and impartially?",
        "verses": [
            {"ref": "Proverbs 18:5", "text": "It is not good to show partiality to the wicked, Or to overthrow the righteous in judgment."},
            {"ref": "Proverbs 20:8", "text": "A king who sits on the throne of judgment Scatters all evil with his eyes."},
            {"ref": "Proverbs 24:23-25", "text": "These things also belong to the wise: It is not good to show partiality in judgment… But those who rebuke the wicked will have delight…"},
            {"ref": "Proverbs 28:21", "text": "To show partiality is not good, Because for a piece of bread a man will transgress."},
            {"ref": "Proverbs 29:14", "text": "The king who judges the poor with truth, His throne will be established forever."},
            {"ref": "Proverbs 31:8-9", "text": "Open your mouth for the speechless… judge righteously, And plead the cause of the poor and needy."}
        ],
        "dig_deeper": [
            "Where are you most tempted to show partiality (favoritism, fear of man, bribes, etc.)?",
            "How can you ensure you treat everyone fairly at work, especially those above and below you?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 35,
        "title": "Hold Your Tongue",
        "question": "Do I guard my mouth and speak wisely?",
        "verses": [
            {"ref": "Proverbs 10:19", "text": "In the multitude of words sin is not lacking, But he who restrains his lips is wise."},
            {"ref": "Proverbs 17:27-28", "text": "He who has knowledge spares his words… Even a fool is counted wise when he holds his peace."},
            {"ref": "Proverbs 21:23", "text": "Whoever guards his mouth and tongue Keeps his soul from troubles."}
        ],
        "dig_deeper": [
            "When have you regretted speaking too much or too quickly?",
            "What triggers you to talk too much or say things you shouldn’t?",
            "What practical habits can help you hold your tongue more effectively?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 36,
        "title": "title": "Show Graciousness/Kindness",
        "question": "Am I known for graciousness and kindness in the workplace?",
        "verses": [
            {"ref": "Proverbs 11:16", "text": "A gracious woman retains honor, But ruthless men retain riches."},
            {"ref": "Proverbs 19:22", "text": "What is desired in a man is kindness…"},
            {"ref": "Proverbs 22:11", "text": "He who loves purity of heart And has grace on his lips, The king will be his friend."}
        ],
        "dig_deeper": [
            "Have you considered that kindness and grace bring honor and favor?",
            "What are the opposite consequences of being ruthless or unkind?",
            "How can you show more kindness at work this week?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 37,
        "title": "Be Merciful",
        "question": "Am I quick to show mercy and forgive others?",
        "verses": [
            {"ref": "Proverbs 11:17", "text": "The merciful man does good for his own soul, But he who is cruel troubles his own flesh."},
            {"ref": "Proverbs 14:21", "text": "…he who has mercy on the poor, happy is he."},
            {"ref": "Proverbs 19:17", "text": "He who has pity on the poor lends to the LORD…"},
            {"ref": "Proverbs 21:21", "text": "He who follows righteousness and mercy Finds life, righteousness, and honor."}
        ],
        "dig_deeper": [
            "Who do you need to show mercy to right now?",
            "How does refusing to show mercy actually hurt you more than the other person?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 38,
        "title": "Be Patient",
        "question": "Am I patient and diligent instead of hasty and impulsive?",
        "verses": [
            {"ref": "Proverbs 14:29", "text": "He who is slow to wrath has great understanding, But he who is impulsive exalts folly."},
            {"ref": "Proverbs 19:2", "text": "Also it is not good for a soul to be without knowledge, And he sins who hastens with his feet."},
            {"ref": "Proverbs 21:5", "text": "The plans of the diligent lead surely to plenty, But those of everyone who is hasty, surely to poverty."}
        ],
        "dig_deeper": [
            "Where do you most struggle with impatience?",
            "How has haste ever cost you?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 39,
        "title": "Respect Authority/Faithful Messenger",
        "question": "Do I respect authority and serve faithfully as a messenger?",
        "verses": [
            {"ref": "Proverbs 13:17", "text": "A wicked messenger falls into trouble, But a faithful ambassador brings health."},
            {"ref": "Proverbs 25:13", "text": "Like the cold of snow in time of harvest Is a faithful messenger to those who send him…"}
        ],
        "dig_deeper": [
            "Do you serve those in authority over you with faithfulness and excellence?",
            "How can you be a “refreshing” messenger this week?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 40,
        "title": "Don't Be Scornful/Proud/Mockers (Scoffers)",
        "question": "Am I humble, or do I mock, scorn, and act proudly?",
        "verses": [
            {"ref": "Proverbs 3:34", "text": "Surely He scorns the scornful, But gives grace to the humble."},
            {"ref": "Proverbs 21:24", "text": "A proud and haughty man—“Scoffer” is his name; He acts with arrogant pride."},
            {"ref": "Proverbs 22:10", "text": "Cast out the scoffer, and contention will leave…"}
        ],
        "dig_deeper": [
            "Where do you see pride or scorn show up in your attitude or speech?",
            "How can you cultivate genuine humility this week?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 41,
        "title": "Honor the Lord With Your Possessions/Generosity",
        "question": "Do I honor God with my finances and practice generosity?",
        "verses": [
            {"ref": "Proverbs 3:9-10", "text": "Honor the LORD with your possessions, And with the firstfruits of all your increase; So your barns will be filled with plenty…"},
            {"ref": "Proverbs 11:24-25", "text": "There is one who scatters, yet increases more… The generous soul will be made rich…"}
        ],
        "dig_deeper": [
            "What stops you from being generous?",
            "How does honoring God with the “firstfruits” change your financial perspective?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 42,
        "title": "Have a Merry Heart",
        "question": "Do I maintain a merry heart and cheerful countenance?",
        "verses": [
            {"ref": "Proverbs 15:13", "text": "A merry heart makes a cheerful countenance, But by sorrow of the heart the spirit is broken."},
            {"ref": "Proverbs 15:15", "text": "…he who is of a merry heart has a continual feast."},
            {"ref": "Proverbs 17:22", "text": "A merry heart does good, like medicine, But a broken spirit dries the bones."}
        ],
        "dig_deeper": [
            "Does sorrow or a broken spirit keep you from having a merry heart?",
            "How can you cultivate joy and cheerfulness even in hard seasons?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 43,
        "title": "Be Content, Not Greedy",
        "question": "Am I content with what I have, or always grasping for more?",
        "verses": [
            {"ref": "Proverbs 15:27", "text": "He who is greedy for gain troubles his own house, But he who hates bribes will live."},
            {"ref": "Proverbs 21:26", "text": "He covets greedily all day long, But the righteous gives and does not spare."},
            {"ref": "Proverbs 22:9", "text": "He who has a generous eye will be blessed, For he gives of his bread to the poor."},
            {"ref": "Proverbs 22:16", "text": "He who oppresses the poor to increase his riches, And he who gives to the rich, will surely come to poverty."},
            {"ref": "Proverbs 23:4-5", "text": "Do not overwork to be rich; Because of your own understanding, cease! Will you set your eyes on that which is not? For riches certainly make themselves wings; They fly away like an eagle toward heaven."},
            {"ref": "Proverbs 27:20", "text": "Hell and Destruction are never full; So the eyes of man are never satisfied."},
            {"ref": "Proverbs 28:20", "text": "A faithful man will abound with blessings, But he who hastens to be rich will not go unpunished."},
            {"ref": "Proverbs 28:22", "text": "A man with an evil eye hastens after riches, And does not consider that poverty will come upon him."},
            {"ref": "Proverbs 30:8-9", "text": "Remove falsehood and lies far from me; Give me neither poverty nor riches— Feed me with the food allotted to me; Lest I be full and deny You, And say, “Who is the LORD?” Or lest I be poor and steal, And profane the name of my God."}
        ],
        "dig_deeper": [
            "If you have not come to the place that you are content with what you have, what will change your attitude in this area?",
            "Does being content mean that you are lazy, don’t aspire for career advancement, don’t give 100%?",
            "Have you brought trouble to your own house by being greedy for gain? Give an example.",
            "Are others’ attitudes and greed affecting the way you live?",
            "Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
        ]
    },
    {
        "id": 44,
        "title": "Don't Cause Shame",
        "question": "Do my actions or words bring shame to others or to myself?",
        "verses": [
            {"ref": "Proverbs 17:2", "text": "A wise servant will rule over a son who causes shame, And will share an inheritance among the brothers."},
            {"ref": "Proverbs 19:13", "text": "A foolish son is the ruin of his father, And the contentions of a wife are a continual dripping."},
            {"ref": "Proverbs 28:7", "text": "Whoever keeps the law is a discerning son, But a companion of gluttons shames his father."}
        ],
        "dig_deeper": [
            "Have you ever caused someone shame? If so, have you made amends? Will you? How/when?",
            "If your inheritance is eternal salvation, will your shameful behavior rob you of this?",
            "If someone has caused you shame, will you be willing to forgive them?",
            "Are you a contentious spouse? What can you do to change?",
            "Does the company you keep bring shame to those you love?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 45,
        "title": "Don't be a Rebel",
        "question": "Am I rebellious or do I isolate myself from wise judgment?",
        "verses": [
            {"ref": "Proverbs 17:11", "text": "An evil man seeks only rebellion; Therefore a cruel messenger will be sent against him."},
            {"ref": "Proverbs 18:1", "text": "A man who isolates himself seeks his own desire; He rages against all wise judgment."}
        ],
        "dig_deeper": [
            "A rebel, a lone ranger, seeking only one’s own desire and unrest. If you or someone you know exhibits this behavior, how will you warn them of the consequences?",
            "What can you offer such a person?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 46,
        "title": "Don't Take Revenge",
        "question": "Do I leave vengeance to God instead of taking revenge?",
        "verses": [
            {"ref": "Proverbs 20:22", "text": "Do not say, “I will recompense evil”; Wait for the LORD, and He will save you."},
            {"ref": "Proverbs 24:29", "text": "Do not say, “I will do to him just as he has done to me; I will render to the man according to his work.”"},
            {"ref": "Proverbs 25:21-22", "text": "If your enemy is hungry, give him bread to eat; And if he is thirsty, give him water to drink; For so you will heap coals of fire on his head, And the LORD will reward you."}
        ],
        "dig_deeper": [
            "What does it feel like when you are bent on getting revenge?",
            "What, specifically, will you do when tempted to repay evil?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 47,
        "title": "Don't Gloat",
        "question": "Do I rejoice when my enemy falls, or let my heart be glad when he stumbles?",
        "verses": [
            {"ref": "Proverbs 24:17-18", "text": "Do not rejoice when your enemy falls, And do not let your heart be glad when he stumbles; Lest the LORD see it, and it displease Him, And He turn away His wrath from him."}
        ],
        "dig_deeper": [
            "The definition of gloating: to contemplate or dwell on one's own success or another's misfortune with smugness. If you are known for this, are you ready to change?",
            "What might cause one to develop these traits?",
            "What can influence someone to change?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 48,
        "title": "Avoid Conflict",
        "question": "Do I handle conflict wisely or escalate it?",
        "verses": [
            {"ref": "Proverbs 25:8-10", "text": "Do not go hastily to court; For what will you do in the end, When your neighbor has put you to shame?..."},
            {"ref": "Proverbs 29:9", "text": "If a wise man contends with a foolish man, Whether the fool rages or laughs, there is no peace."}
        ],
        "dig_deeper": [
            "The best way to handle conflict sometimes is to avoid it or handle it privately. Do you agree?",
            "If this isn’t the best way, state why.",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 49,
        "title": "Value Friends and Family",
        "question": "Do I cherish and nurture my relationships with friends and family?",
        "verses": [
            {"ref": "Proverbs 17:17", "text": "A friend loves at all times, And a brother is born for adversity."},
            {"ref": "Proverbs 18:24", "text": "A man who has friends must himself be friendly, But there is a friend who sticks closer than a brother."},
            {"ref": "Proverbs 27:10", "text": "Do not forsake your own friend or your father’s friend…"}
        ],
        "dig_deeper": [
            "Do you find your relationships lacking in genuineness, joy, or reverence?",
            "Do you have “fake friends” or true friends who stick closer than a brother?",
            "How can you encourage others to value their friends and family?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 50,
        "title": "Understands Human Nature",
        "question": "Do I understand human nature and respond wisely to people?",
        "verses": [
            {"ref": "Proverbs 18:16", "text": "A man’s gift makes room for him, And brings him before great men."},
            {"ref": "Proverbs 20:14", "text": "“It is good for nothing,” cries the buyer; But when he has gone his way, then he boasts."},
            {"ref": "Proverbs 25:17", "text": "Seldom set foot in your neighbor’s house, Lest he become weary of you and hate you."},
            {"ref": "Proverbs 25:20", "text": "Like one who takes away a garment in cold weather… Is one who sings songs to a heavy heart."},
            {"ref": "Proverbs 30:24-31", "text": "There are four things which are little on the earth, But they are exceedingly wise… (ants, rock badgers, locusts, spider, lion, greyhound, goat, king)"}
        ],
        "dig_deeper": [
            "Gifts in secret can open doors — do you agree? Is this condoning bribes?",
            "What does bargaining behavior tell us about human nature?",
            "What can we learn from the “little but wise” creatures?",
            "How can understanding human nature help you lead and work with others?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 51,
        "title": "Respect Elders",
        "question": "Do I honor and learn from those with experience and gray hair?",
        "verses": [
            {"ref": "Proverbs 20:29", "text": "The glory of young men is their strength, And the splendor of old men is their gray head."}
        ],
        "dig_deeper": [
            "Have you realized that gray hair may hold wisdom?",
            "If you have gray hair, do you have a duty to those under you?",
            "As a younger person, does respecting elders show humility?",
            "Summarize/prioritize things you can do… to improve in this area:"
        ]
    },
    {
        "id": 52,
        "title": "Great Commission",
        "question": "Am I actively trying to deliver those who are drawn toward death (sharing the Gospel at work)?",
        "verses": [
            {"ref": "Proverbs 24:11-12", "text": "Deliver those who are drawn toward death, And hold back those stumbling to the slaughter. If you say, “Surely we did not know this,” Does not He who weighs the hearts consider it? He who keeps your soul, does He not know it? And will He not render to each man according to his deeds?"}
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
