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
            ProverbTopic(
                number=1,
                title="Accept Instruction from Others",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I willingly accept instruction from others?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to be willing to accept instruction from others?",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 1:7-9 (NKJV)",
                        text="7 The fear of the LORD is the beginning of knowledge, But fools despise wisdom and instruction. 8 My son, hear the instruction of your father, And do not forsake the law of your mother; 9 For they will be a graceful ornament on your head, And chains about your neck."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 3:1-4 (NKJV)",
                        text="1 My son, do not forget my law, But let your heart keep my commands; 2 For length of days and long life And peace they will add to you. 3 Let not mercy and truth forsake you; Bind them around your neck, Write them on the tablet of your heart, 4 And so find favor and high esteem In the sight of God and man."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 4:1-4 (NKJV)",
                        text="1 Hear, my children, the instruction of a father, And give attention to know understanding; 2 For I give you good doctrine: Do not forsake my law. 3 When I was my father's son, Tender and the only one in the sight of my mother, 4 He also taught me, and said to me: Let your heart retain my words; Keep my commands, and live."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 4:20-23 (NKJV)",
                        text="20 My son, give attention to my words; Incline your ear to my sayings. 21 Do not let them depart from your eyes; Keep them in the midst of your heart; 22 For they are life to those who find them, And health to all their flesh. 23 Keep your heart with all diligence, For out of it spring the issues of life."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 5:12-14 (NKJV)",
                        text="12 And say: How I have hated instruction, And my heart despised correction! 13 I have not obeyed the voice of my teachers, Nor inclined my ear to those who instructed me! 14 I was on the verge of total ruin, In the midst of the assembly and congregation."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 6:20-23 (NKJV)",
                        text="20 My son, keep your father's command, And do not forsake the law of your mother. 21 Bind them continually upon your heart; Tie them around your neck. 22 When you roam, [they] will lead you; When you sleep, they will keep you; And when you awake, they will speak with you. 23 For the commandment is a lamp, And the law a light; Reproofs of instruction are the way of life."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 10:8 (NKJV)",
                        text="8 The wise in heart will receive commands, But a prating fool will fall."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 13:1 (NKJV)",
                        text="1 A wise son heeds his father's instruction, But a scoffer does not listen to rebuke."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:27 (NKJV)",
                        text="27 Cease listening to instruction, my son, And you will stray from the words of knowledge."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 23:12 (NKJV)",
                        text="12 Apply your heart to instruction, And your ears to words of knowledge."
                    )
                ],
                dig_deeper_questions=[
                    "1. Looking at your life, how have you fallen short in the area of accepting instruction from others: your parents, teachers, Godly advisors? How about others that give commands or counsel i.e., your boss, your spouse? Give some examples of how this has hurt you.",
                    "2. Taking things one-step further, how have you sought out (or applied your heart to) instruction and made an effort to listen (open your ears) for instruction? See Proverbs 23:12 above.",
                    "3. What do you think stops you from accepting or seeking out instruction willingly?",
                    "4. Specifically, has your lack of accepting instruction affected you in your work? How?",
                    "5. Is there something you could learn (be instructed in) right now that would make you a better employee in your current job or for future career aspirations?",
                    "6. If so, how will you improve in this area?",
                    "7. How can you minister to others that have an issue in this area?",
                    "8. Finally, review Chapter 2 – Self-Image Issues, regarding a \"Coachable Spirit\". How does this pertain to accepting instruction?",
                    "9. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 2: Accept Correction
            # ========================================
            ProverbTopic(
                number=2,
                title="Accept Correction",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I gracefully accept correction when it is given?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to gracefully accept correction when it is given to them.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 1:20-33",
                        text="20 Wisdom calls aloud outside; She raises her voice in the open squares. 21 She cries out in the chief concourses, At the openings of the gates in the city She speaks her words: 22 \"How long, you simple ones, will you love simplicity? For scorners delight in their scorning, And fools hate knowledge. 23 Turn at my rebuke; Surely I will pour out my spirit on you; I will make my words known to you. 24 Because I have called and you refused, I have stretched out my hand and no one regarded, 25 Because you disdained all my counsel, And would have none of my rebuke, 26 I also will laugh at your calamity; I will mock when your terror comes, 27 When your terror comes like a storm, And your destruction comes like a whirlwind, When distress and anguish come upon you. 28 \"Then they will call on me, but I will not answer; They will seek me diligently, but they will not find me. 29 Because they hated knowledge And did not choose the fear of the LORD, 30 They would have none of my counsel And despised my every rebuke. 31 Therefore they shall eat the fruit of their own way, And be filled to the full with their own fancies. 32 For the turning away of the simple will slay them, And the complacency of fools will destroy them; 33 But whoever listens to me will dwell safely, And will be secure, without fear of evil.\""
                    ),
                    ScriptureVerse(
                        reference="Proverbs 3:11-12 (NKJV)",
                        text="11 My son, do not despise the chastening of the LORD, Nor detest His correction; 12 For whom the LORD loves He corrects, Just as a father the son in whom he delights."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 10:17 (NKJV)",
                        text="17 He who keeps instruction is in the way of life, But he who refuses correction goes astray."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 12:1 (NKJV)",
                        text="1 Whoever loves instruction loves knowledge, But he who hates correction is stupid."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 13:18 (NKJV)",
                        text="18 Poverty and shame will come to him who disdains correction, But he who regards a rebuke will be honored."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 15:5 (NKJV)",
                        text="5 A fool despises his father's instruction, But he who receives correction is prudent."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 15:10-12 (NKJV)",
                        text="10 Harsh discipline is for him who forsakes the way, And he who hates correction will die. 11 Hell and Destruction are before the LORD; So how much more the hearts of the sons of men. 12 A scoffer does not love one who corrects him, Nor will he go to the wise."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 15:30-32 (NKJV)",
                        text="30 The light of the eyes rejoices the heart, And a good report makes the bones healthy. 31 The ear that hears the rebukes of life Will abide among the wise. 32 He who disdains instruction despises his own soul, But he who heeds rebuke gets understanding."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:22 (NKJV)",
                        text="22 Understanding is a wellspring of life to him who has it. But the correction of fools is folly."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 17:10 (NKJV)",
                        text="10 Rebuke is more effective for a wise man Than a hundred blows on a fool."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 29:1 (NKJV)",
                        text="1 He who is often rebuked, and hardens his neck, Will suddenly be destroyed, and that without remedy."
                    )
                ],
                dig_deeper_questions=[
                    "1. After you have received criticism, explain your normal reaction initially and eventually?",
                    "2. How quickly can you recover after hearing criticism? What about self-criticism? Are you hard on yourself, beating yourself up and letting this affect your performance, long after others have moved on?",
                    "3. Can you think of someone that you have witnessed take criticism well? Describe what about that person's reaction appealed to you.",
                    "4. Delightful, \"in\" the way of life, knowledgeable, honored, prudent, wise, of good report, healthy, possesses understanding and cleansed away from evil, these are ways that Proverbs describes the person who accepts correction. Contrast that to the terms describing those who do not accept correction: going astray, stupid, poor, shameful, dead, despiser of one's own soul, fool, destroyed without remedy. Describe some of the negative consequences you've experienced from not accepting correction:",
                    "5. Which verses above will help you when you are tempted to harbor resentment against someone who offers criticism?",
                    "6. How does a person's demeanor/style when offering criticism impact how well you accept the message?",
                    "7. Explain how you would best like to hear criticism?",
                    "8. Do you offer criticism as a friend, in love, with well-chosen words, \"fitly spoken\"? If not, how can you improve?",
                    "9. The next time you receive criticism in a way, other than your preference outlined above, could you communicate to the person offering the message, how you would rather it be delivered? How could this conversation be helpful?",
                    "10. According to the verses above, should you offer criticism to fools? To wise men?",
                    "11. Does your boss consider you wise enough to be worthy of criticism? This may depend on your reaction (do you harden your neck or do you have a \"coachable spirit\"). Think about it. Is there anything you need to change?",
                    "10. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 3: Administer Discipline to Others
            # ========================================
            ProverbTopic(
                number=3,
                title="Administer Discipline to Others",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I readily discipline those that need correction?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to readily discipline those that need correction?",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 13:24 (NKJV)",
                        text="24 He who spares his rod hates his son, But he who loves him disciplines him"
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:18 (NKJV)",
                        text="18 Chasten your son while there is hope, And do not set your heart on his destruction."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 20:30 (NKJV)",
                        text="30 Blows that hurt cleanse away evil, As do stripes the inner depths of the heart."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:11 (NKJV)",
                        text="11 When the scoffer is punished, the simple is made wise; But when the wise is instructed, he receives knowledge."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 22:15 (NKJV)",
                        text="15 Foolishness is bound up in the heart of a child; The rod of correction will drive it far from him."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 23:13-14 (NKJV)",
                        text="13 Do not withhold correction from a child, For if you beat him with a rod, he will not die. 14 You shall beat him with a rod, And deliver his soul from hell."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 24:11-12 (NKJV)",
                        text="11 Deliver those who are drawn toward death, And hold back those stumbling to the slaughter. 12 If you say, \"Surely we did not know this,\" Does not He who weighs the hearts consider it? He who keeps your soul, does He not know it? And will He not render to each man according to his deeds?"
                    ),
                    ScriptureVerse(
                        reference="Proverbs 25:11-12 (NKJV)",
                        text="11 A word fitly spoken is like apples of gold In settings of silver. 12 Like an earring of gold and an ornament of fine gold Is a wise rebuker to an obedient ear."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 26:3-5 (NKJV)",
                        text="3 A whip for the horse, A bridle for the donkey, And a rod for the fool's back. 4 Do not answer a fool according to his folly, Lest you also be like him. 5 Answer a fool according to his folly, Lest he be wise in his own eyes."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 27:5 (NKJV)",
                        text="5 Open rebuke is better Than love carefully concealed."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 27:6 (NKJV)",
                        text="6 Faithful are the wounds of a friend, But the kisses of an enemy are deceitful."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 27:17 (NKJV)",
                        text="17 As iron sharpens iron, So a man sharpens the countenance of his friend."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 29:15 (NKJV)",
                        text="15 The rod and rebuke give wisdom, But a child left to himself brings shame to his mother."
                    )
                ],
                dig_deeper_questions=[
                    "1. Are you consistent in your administration of discipline or constructive feedback?",
                    "2. Is it hard for you to discipline or correct someone? Why do you think this is?",
                    "3. Are you too harsh (set your heart on his destruction) in your discipline?",
                    "4. Are your words \"fitful\"? Do you feel you can appropriately communicate a correction or could use improvement in this area? (For help, see Chapter 6 – Communicating Issues.)",
                    "5. Have you ever given someone a break (spared the rod) because you felt sorry for them? How did it turn out? Looking back, was that the \"loving\" thing to do?",
                    "6. Can you accept discipline better because you now understand it's value and motivation (love/concern)?",
                    "7. Summarize/prioritize things you can do, (do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 4: Avoid Sinners Enticing You
            # ========================================
            ProverbTopic(
                number=4,
                title="Avoid Sinners Enticing You",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I am easily misled into wrong behavior (s) by peer pressure?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to be easily misled into wrong behavior(s) by peer pressure?",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 1:10-19 (NKJV)",
                        text="10 My son, if sinners entice you, Do not consent. 11 If they say, \"Come with us, Let us lie in wait to shed blood; Let us lurk secretly for the innocent without cause; 12 Let us swallow them alive like Sheol, 13 We shall find all kinds of precious possessions, We shall fill our houses with spoil; 14 Cast in your lot among us, Let us all have one purse\"— 15 My son, do not walk in the way with them, Keep your foot from their path; 16 For their feet run to evil, And they make haste to shed blood. 17 Surely, in vain the net is spread In the sight of any bird; 18 But they lie in wait for their own blood, They lurk secretly for their own lives. 19 So are the ways of everyone who is greedy for gain; It takes away the life of its owners."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 4:14-19 (NKJV)",
                        text="14 Do not enter the path of the wicked, And do not walk in the way of evil. 15 Avoid it, do not travel on it; Turn away from it and pass on. 16 For they do not sleep unless they have done evil; And their sleep is taken away unless they make someone fall. 17 For they eat the bread of wickedness, And drink the wine of violence. 18 But the path of the just is like the shining sun, That shines ever brighter unto the perfect day. 19 The way of the wicked is like darkness; They do not know what makes them stumble."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 12:26 (NKJV)",
                        text="26 The righteous should choose his friends carefully, For the way of the wicked leads them astray."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 13:20-21 (NKJV)",
                        text="20 He who walks with wise men will be wise, But the companion of fools will be destroyed. 21 Evil pursues sinners, But to the righteous, good shall be repaid."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:29 (NKJV)",
                        text="29 A violent man entices his neighbor, And leads him in a way that is not good."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 20:19 (NKJV)",
                        text="19 He who goes about as a talebearer reveals secrets; Therefore do not associate with one who flatters with his lips."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:10 (NKJV)",
                        text="10 Whoever causes the upright to go astray in an evil way, He himself will fall into his own pit; But the blameless will inherit good."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:17 (NKJV)",
                        text="17 A man burdened with bloodshed will flee into a pit; Let no one help him."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 29:24 (NKJV)",
                        text="24 Whoever is a partner with a thief hates his own life; He swears to tell the truth, but reveals nothing."
                    )
                ],
                dig_deeper_questions=[
                    "1. Have you ever associated with people that cause you to behave poorly? Give some examples:",
                    "2. Do you continue to associate with people who are enticing you into evil?",
                    "3. Those greedy for gain, fools, violent, talebearers/gossips, flatterers, thieves, are just some of the types of sinners enumerated in the verses above. Look around your close circle of friends. Do you need to make some changes in your relationships?",
                    "4. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 5: Seek Wisdom/Discretion
            # ========================================
            ProverbTopic(
                number=5,
                title="Seek Wisdom/Discretion",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I really work hard at seeking wisdom/discretion; trying to figure out the right thing to do in difficult situations?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to really try to seek wisdom/discretion to figure out the right thing to do in difficult situations.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 2:1-9 (NKJV)",
                        text="1 My son, if you receive my words, And treasure my commands within you, 2 So that you incline your ear to wisdom, And apply your heart to understanding; 3 Yes, if you cry out for discernment, And lift up your voice for understanding, 4 If you seek her as silver, And search for her as for hidden treasures; 5 Then you will understand the fear of the LORD, And find the knowledge of God. 6 For the LORD gives wisdom; From His mouth come knowledge and understanding; 7 He stores up sound wisdom for the upright; He is a shield to those who walk uprightly; 8 He guards the paths of justice, And preserves the way of His saints. 9 Then you will understand righteousness and justice, Equity and every good path."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 3:13-24 (NKJV)",
                        text="13 Happy is the man who finds wisdom, And the man who gains understanding; 14 For her proceeds are better than the profits of silver, And her gain than fine gold. 15 She is more precious than rubies, And all the things you may desire cannot compare with her. 16 Length of days is in her right hand, In her left hand riches and honor. 17 Her ways are ways of pleasantness, And all her paths are peace. 18 She is a tree of life to those who take hold of her, And happy are all who retain her. 19 The LORD by wisdom founded the earth; By understanding He established the heavens; 20 By His knowledge the depths were broken up, And clouds drop down the dew. 21 My son, let them not depart from your eyes— Keep sound wisdom and discretion; 22 So they will be life to your soul And grace to your neck. 23 Then you will walk safely in your way, And your foot will not stumble. 24 When you lie down, you will not be afraid; Yes, you will lie down and your sleep will be sweet."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 3:35 (NKJV)",
                        text="35 The wise shall inherit glory, But shame shall be the legacy of fools."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 4:5-13 (NKJV)",
                        text="5 Get wisdom! Get understanding! Do not forget, nor turn away from the words of my mouth. 6 Do not forsake her, and she will preserve you; Love her, and she will keep you. 7 Wisdom is the principal thing; Therefore get wisdom. And in all your getting, get understanding. 8 Exalt her, and she will promote you; She will bring you honor, when you embrace her. 9 She will place on your head an ornament of grace; A crown of glory she will deliver to you.\" 10 Hear, my son, and receive my sayings, And the years of your life will be many. 11 I have taught you in the way of wisdom; I have led you in right paths. 12 When you walk, your steps will not be hindered, And when you run, you will not stumble. 13 Take firm hold of instruction, do not let go; Keep her, for she is your life."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 8:1-9 (NKJV)",
                        text="1 Does not wisdom cry out, And understanding lift up her voice? 2 She takes her stand on the top of the high hill, Beside the way, where the paths meet. 3 She cries out by the gates, at the entry of the city, At the entrance of the doors: 4 \"To you, O men, I call, And my voice is to the sons of men. 5 O you simple ones, understand prudence, And you fools, be of an understanding heart. 6 Listen, for I will speak of excellent things, And from the opening of my lips will come right things; 7 For my mouth will speak truth; Wickedness is an abomination to my lips. 8 All the words of my mouth are with righteousness; Nothing crooked or perverse is in them. 9 They are all plain to him who understands, And right to those who find knowledge."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 10:1 (NKJV)",
                        text="1 The proverbs of Solomon: A wise son makes a glad father, But a foolish son is the grief of his mother."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 10:13 (NKJV)",
                        text="13 Wisdom is found on the lips of him who has understanding, But a rod is for the back of him who is devoid of understanding."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 11:22 (NKJV)",
                        text="22 As a ring of gold in a swine's snout, So is a lovely woman who lacks discretion."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 15:24 (NKJV)",
                        text="24 The way of life winds upward for the wise, That he may turn away from hell"
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:16 (NKJV)",
                        text="16 How much better to get wisdom than gold! And to get understanding is to be chosen rather than silver."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:21 (NKJV)",
                        text="21 The wise in heart will be called prudent, And sweetness of the lips increases learning."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 18:15 (NKJV)",
                        text="15 The heart of the prudent acquires knowledge, And the ear of the wise seeks knowledge."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:8 (NKJV)",
                        text="8 He who gets wisdom loves his own soul; He who keeps understanding will find good."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:16 (NKJV)",
                        text="16 A man who wanders from the way of understanding Will rest in the assembly of the dead."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:22 (NKJV)",
                        text="22 A wise man scales the city of the mighty, And brings down the trusted stronghold."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 24:3-5 (NKJV)",
                        text="3 Through wisdom a house is built, And by understanding it is established; 4 By knowledge the rooms are filled With all precious and pleasant riches. 5 A wise man is strong, Yes, a man of knowledge increases strength;"
                    ),
                    ScriptureVerse(
                        reference="Proverbs 24:7 (NKJV)",
                        text="7 Wisdom is too lofty for a fool; He does not open his mouth in the gate."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 24:13-14 (NKJV)",
                        text="13 My son, eat honey because it is good, And the honeycomb which is sweet to your taste; 14 So shall the knowledge of wisdom be to your soul; If you have found it, there is a prospect, And your hope will not be cut off."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 27:11 (NKJV)",
                        text="11 My son, be wise, and make my heart glad, That I may answer him who reproaches me."
                    )
                ],
                dig_deeper_questions=[
                    "1. Where do you go to as your source of information? Your boss, the Human Resources Department, management training classes, a career or life coach, your peers, other respected colleagues, your spouse, your own understanding?",
                    "2. Have you looked specifically in the Word instead for the root of the problem and wisdom about the solution?",
                    "3. When you do seek wisdom, it is important that you: a. Obtain knowledge (accumulate the available information or facts on the subject); b. Be wise (discern the true nature of things; that the knowledge you receive is knowledge that stands up to the test/will of the Word of God (1 Corinthians 2:15, 1 Thessalonians 5:21, 1 John 4:1, Hebrews 5:14, Romans 12:2) and; c. Gain understanding (learn how to apply this wisdom practically). If your issue is leadership, for example, and you gather knowledge about Servant Leadership and you see in God's Word that Jesus calls us to practice this leadership, what can you do, practically, to model this (assuming that literally washing your employee's feet may not be culturally acceptable)?",
                    "4. When reading the sections on Authority, Self-Image and Your Job, did you have any \"aha\" moments? Did the perspective provided help you gain wisdom about your \"work-life\" issue? Explain.",
                    "5. Think of a difficult situation you've faced at work recently and determine to explore what the Lord's wisdom has to say about that situation. Would you, or could you, have reacted differently if you had this wisdom at the time you were dealing with the problem? Explain below, then share this information with someone.",
                    "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 6: Seek Counsel
            # ========================================
            ProverbTopic(
                number=6,
                title="Seek Counsel",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I ask others (especially Christians) for counsel and value their insight/opinions?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to seek counsel/value proper insights and opinions.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 11:14 (NKJV)",
                        text="14 Where there is no counsel, the people fall; But in the multitude of counselors there is safety."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 15:22 (NKJV)",
                        text="22 Without counsel, plans go awry, But in the multitude of counselors they are established."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 20:5 (NKJV)",
                        text="5 Counsel in the heart of man is like deep water, But a man of understanding will draw it out."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 20:18 (NKJV)",
                        text="18 Plans are established by counsel; By wise counsel wage war."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 24:6 (NKJV)",
                        text="6 For by wise counsel you will wage your own war, And in a multitude of counselors there is safety."
                    )
                ],
                dig_deeper_questions=[
                    "1. Do you value and seek out the opinions of many counselors?",
                    "2. How does being shy, proud or insecure affect your willingness to seek advice? Are any of these an issue for you? Are those acceptable excuses to not follow this piece of wisdom?",
                    "3. Can you remember a situation where you acted alone and you wish you had sought counsel? Share some examples:",
                    "4. Modern management theory suggests collaboration and seeking input from many individuals, departments, etc. is appropriate. This, in essence, is a democracy. Are there problems with seeking too much input or input from the wrong individuals? How will you balance this?",
                    "5. Do you (or others you deal with) sincerely seek wise counsel, the right amount of counsel, or just go through the motions of being democratic? Remember the Lord knows our hearts.",
                    "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 7: Keep the Lord's Commands
            # ========================================
            ProverbTopic(
                number=7,
                title="Keep the Lord's Commands",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I try to follow the 10 Commandments?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to follow the 10 Commandments.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 13:13-15 (NKJV)",
                        text="13 He who despises the word will be destroyed, But he who fears the commandment will be rewarded. 14 The law of the wise is a fountain of life, To turn one away from the snares of death. 15 Good understanding gains favor, But the way of the unfaithful is hard."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 14:26-27 (NKJV)",
                        text="26 In the fear of the LORD there is strong confidence, And His children will have a place of refuge. 27 The fear of the LORD is a fountain of life, To turn one away from the snares of death."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:20 (NKJV)",
                        text="20 He who heeds the word wisely will find good, And whoever trusts in the LORD, happy is he."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:16 (NKJV)",
                        text="16 He who keeps the commandment keeps his soul, But he who is careless of his ways will die."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:23 (NKJV)",
                        text="23 The fear of the LORD leads to life, And he who has it will abide in satisfaction; He will not be visited with evil."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:4 (NKJV)",
                        text="4 Those who forsake the law praise the wicked, But such as keep the law contend with them."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:9 (NKJV)",
                        text="9 One who turns away his ear from hearing the law, even his prayer is an abomination."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 29:18 (NKJV)",
                        text="18 Where there is no revelation, the people cast off restraint; But happy is he who keeps the law."
                    )
                ],
                dig_deeper_questions=[
                    "1. Review the 10 Commandments (Exodus 20). Do you feel you truly believe in them, trust them, and revere the Lord enough to try to keep them?",
                    "2. How can you remind yourself of the commandments and hold yourself accountable to them in every circumstance?",
                    "3. If you cannot live up to the commandments, \"the law\", do you believe that all things are possible through Christ and that he has paid the price for your failures?",
                    "4. Does this release you from the responsibility to live lawfully? (See Romans 6:15.)",
                    "5. The verses above show that those that DON'T revere or fear the Lord and keep His commandments will suffer. They tell us… a) The way of the unfaithful, the careless, the one who turns his ear from the law is hard and leads to death. This causes one: • to be dissatisfied, • visited with evil, • to praise wickedness, • to cast off restraint, and • results in unhappiness and • prayers that are an abomination. b) Being a faithful Christian, however, should help you: • be rewarded, • turn away from the snares of death, • gain favor, • have strong confidence, • have a safe refuge, • find good, • be happy, • keep your soul, • abide in satisfaction, • not be visited with evil, and • allow you to contend with the wicked. Which list of characteristics, paragraph (a or b) above, best describes your life? Is your life reflecting the rewards of a faithful Christian, why or why not?",
                    "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 8: Trust in the Lord
            # ========================================
            ProverbTopic(
                number=8,
                title="Trust in the Lord",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I demonstrate that I trust in the Lord?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to demonstrate that they trust in the Lord.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 3:5-6 (NKJV)",
                        text="5 Trust in the LORD with all your heart, And lean not on your own understanding; 6 In all your ways acknowledge Him, And He shall direct your paths."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 3:25-26 (NKJV)",
                        text="25 Do not be afraid of sudden terror, Nor of trouble from the wicked when it comes; 26 For the LORD will be your confidence, And will keep your foot from being caught."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:4 (NKJV)",
                        text="4 The LORD has made all for Himself, Yes, even the wicked for the day of doom."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:9 (NKJV)",
                        text="9 A man's heart plans his way, But the LORD directs his steps."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:33 (NKJV)",
                        text="33 The lot is cast into the lap, But its every decision is from the LORD."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 18:10-11 (NKJV)",
                        text="10 The name of the LORD is a strong tower; The righteous run to it and are safe. 11 The rich man's wealth is his strong city, And like a high wall in his own esteem."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:21 (NKJV)",
                        text="21 There are many plans in a man's heart, Nevertheless the LORD's counsel—that will stand."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:1 (NKJV)",
                        text="1 The king's heart is in the hand of the LORD, Like the rivers of water; He turns it wherever He wishes."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:30-31 (NKJV)",
                        text="30 There is no wisdom or understanding Or counsel against the LORD. 31 The horse is prepared for the day of battle, But deliverance is of the LORD."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 22:17-21 (NKJV)",
                        text="17 Incline your ear and hear the words of the wise, And apply your heart to my knowledge; 18 For it is a pleasant thing if you keep them within you; Let them all be fixed upon your lips, 19 So that your trust may be in the LORD; I have instructed you today, even you. 20 Have I not written to you excellent things Of counsels and knowledge, 21 That I may make you know the certainty of the words of truth, That you may answer words of truth To those who send to you?"
                    ),
                    ScriptureVerse(
                        reference="Proverbs 29:25 (NKJV)",
                        text="25 The fear of man brings a snare, But whoever trusts in the LORD shall be safe."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 30:1-6 (NKJV)",
                        text="1 The words of Agur the son of Jakeh, his utterance. This man declared to Ithiel—to Ithiel and Ucal: 2 Surely I am more stupid than any man, And do not have the understanding of a man. 3 I neither learned wisdom Nor have knowledge of the Holy One. 4 Who has ascended into heaven, or descended? Who has gathered the wind in His fists? Who has bound the waters in a garment? Who has established all the ends of the earth? What is His name, and what is His Son's name, If you know? 5 Every word of God is pure; He is a shield to those who put their trust in Him. 6 Do not add to His words, Lest He rebuke you, and you be found a liar."
                    )
                ],
                dig_deeper_questions=[
                    "1. Do you exhibit confidence that the Lord is in control of your work and your life situations?",
                    "2. What specifically can you do to demonstrate that trust and exhibit that confidence more? (perhaps give up some control, delegate, release yourself from your insatiable drive for success?)",
                    "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 9: Don't Be Wise in Your Own Eyes
            # ========================================
            ProverbTopic(
                number=9,
                title="Don't Be Wise in Your Own Eyes",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I give others the impression that I know-it-all (am wise in my own eyes)?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to think they know-it-all (or act are wise/pure in their own eyes).",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 3:7-8 (NKJV)",
                        text="7 Do not be wise in your own eyes; Fear the LORD and depart from evil. 8 It will be health to your flesh, And strength to your bones."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 12:15 (NKJV)",
                        text="15 The way of a fool is right in his own eyes, But he who heeds counsel is wise."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 14:12 (NKJV)",
                        text="12 There is a way that seems right to a man, But its end is the way of death."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 14:14 (NKJV)",
                        text="14 The backslider in heart will be filled with his own ways, But a good man will be satisfied from above."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:2 (NKJV)",
                        text="2 All the ways of a man are pure in his own eyes, But the LORD weighs the spirits."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:25 (NKJV)",
                        text="25 There is a way that seems right to a man, But its end is the way of death."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 20:24 (NKJV)",
                        text="24 A man's steps are of the LORD; How then can a man understand his own way?"
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:2 (NKJV)",
                        text="2 Every way of a man is right in his own eyes, But the LORD weighs the hearts."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 26:12 (NKJV)",
                        text="12 Do you see a man wise in his own eyes? There is more hope for a fool than for him."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 27:1-2 (NKJV)",
                        text="1 Do not boast about tomorrow, For you do not know what a day may bring forth. 2 Let another man praise you, and not your own mouth; A stranger, and not your own lips."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:11 (NKJV)",
                        text="11 The rich man is wise in his own eyes, But the poor who has understanding searches him out."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:26 (NKJV)",
                        text="26 He who trusts in his own heart is a fool, But whoever walks wisely will be delivered."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 30:12 (NKJV)",
                        text="12 There is a generation that is pure in its own eyes, Yet is not washed from its filthiness."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 30:32-33 (NKJV)",
                        text="32 If you have been foolish in exalting yourself, Or if you have devised evil, put your hand on your mouth. 33 For as the churning of milk produces butter, And wringing the nose produces blood, So the forcing of wrath produces strife."
                    )
                ],
                dig_deeper_questions=[
                    "1. What, in your opinion, is the difference between being respected for your knowledge and being perceived as a \"know-it-all\"?",
                    "2. How could someone who is perceived as a \"know-it-all\" or \"wise or pure in their own eyes\" change other's impression of him/her?",
                    "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 10: Don't Withhold Good When Due
            # ========================================
            ProverbTopic(
                number=10,
                title="Don't Withhold Good When Due",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I give credit to people, when credit is due?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to give credit to people when credit is due.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 3:27-28 (NKJV)",
                        text="27 Do not withhold good from those to whom it is due, When it is in the power of your hand to do so. 28 Do not say to your neighbor, Go, and come back, And tomorrow I will give it,\" When you have it with you."
                    )
                ],
                dig_deeper_questions=[
                    "1. Are you fair in your payment of wages, return of debts owed, returning things borrowed, keeping of promises, providing the information necessary for people to do their jobs well and giving credit when credit is due? If not, where do you fall short?",
                    "2. The verse above pertains to payment of debts; do you feel you have a debt of praise to an employee or boss that has done a job well?",
                    "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            # ========================================
            # TOPIC 11: Don't be in Debt
            # ========================================
            ProverbTopic(
                number=11,
                title="Don't be in Debt",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I manage my finances well; avoid debt or pledging for others irresponsibly?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to manage their finances well.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 22:7 (NKJV)",
                        text="7 The rich rules over the poor, And the borrower is servant to the lender."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 22:26-27 (NKJV)",
                        text="26 Do not be one of those who shakes hands in a pledge, One of those who is surety for debts; 27 If you have nothing with which to pay, Why should he take away your bed from under you?"
                    )
                ],
                dig_deeper_questions=[
                    "1. How can managing your finances well make you a better witness to others at work?",
                    "2. How can managing your finances well make you a better employee/employer?",
                    "3. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 12: Don't Devise Evil or Take Advantage
            # ========================================
            ProverbTopic(
                number=12,
                title="Don't Devise Evil or Take Advantage",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I plot against others (think about/plan to do something harmful to him or her)?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to plot against others to do harmful things to them.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 3:29 (NKJV)",
                        text="29 Do not devise evil against your neighbor, For he dwells by you for safety's sake."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 14:22 (NKJV)",
                        text="22 Do they not go astray who devise evil? But mercy and truth belong to those who devise good."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 23:10-11 (NKJV)",
                        text="10 Do not remove the ancient landmark, Nor enter the fields of the fatherless; 11 For their Redeemer is mighty; He will plead their cause against you."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 24:15-16 (NKJV)",
                        text="15 Do not lie in wait, O wicked man, against the dwelling of the righteous; Do not plunder his resting place; 16 For a righteous man may fall seven times And rise again, But the wicked shall fall by calamity."
                    )
                ],
                dig_deeper_questions=[
                    "1. Have you ever acted to plot against someone? What motivated you to take this approach: anger, revenge or pride?",
                    "2. Did this approach work out well for you?",
                    "3. Proverbs 24:15-16 (the last verse in this section) notes how wicked men, will be thwarted if they try to devise evil against the righteous. Does this give you confidence not to worry about those that plot against you?",
                    "4. If either acting to plot evil or worrying about those that plot against you is an issue, summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 13: Don't Strive
            # ========================================
            ProverbTopic(
                number=13,
                title="Don't Strive",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I start quarrels or easily get involved in quarrels?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to start quarrels or easily gets involved in quarrels.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 3:30 (NKJV)",
                        text="30 Do not strive with a man without cause, If he has done you no harm."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 11:12 (NKJV)",
                        text="12 He who is devoid of wisdom despises his neighbor, But a man of understanding holds his peace."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 11:29 (NKJV)",
                        text="29 He who troubles his own house will inherit the wind, And the fool will be servant to the wise of heart."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:7 (NKJV)",
                        text="7 When a man's ways please the LORD, He makes even his enemies to be at peace with him."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:14-15 (NKJV)",
                        text="14 As messengers of death is the king's wrath, But a wise man will appease it. 15 In the light of the king's face is life, And his favor is like a cloud of the latter rain."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 17:1 (NKJV)",
                        text="1 Better is a dry morsel with quietness, Than a house full of feasting with strife."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 17:9 (NKJV)",
                        text="9 He who covers a transgression seeks love, But he who repeats a matter separates friends."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 18:18-19 (NKJV)",
                        text="18 Casting lots causes contentions to cease, And keeps the mighty apart. 19 A brother offended is harder to win than a strong city, And contentions are like the bars of a castle."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:12 (NKJV)",
                        text="12 The king's wrath is like the roaring of a lion, But his favor is like dew on the grass."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 20:2-3 (NKJV)",
                        text="2 The wrath of a king is like the roaring of a lion; Whoever provokes him to anger sins against his own life. 3 It is honorable for a man to stop striving, Since any fool can start a quarrel."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:9 (NKJV)",
                        text="9 Better to dwell in a corner of a housetop, Than in a house shared with a contentious woman."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 26:2 (NKJV)",
                        text="2 Like a flitting sparrow, like a flying swallow, So a curse without cause shall not alight."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 26:20-21 (NKJV)",
                        text="20 Where there is no wood, the fire goes out; And where there is no talebearer, strife ceases. 21 As charcoal is to burning coals, and wood to fire, So is a contentious man to kindle strife."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:25 (NKJV)",
                        text="25 He who is of a proud heart stirs up strife, But he who trusts in the LORD will be prospered."
                    )
                ],
                dig_deeper_questions=[
                    "1. Does conflict make you uncomfortable or would you say, \"bring it on\"? Why do you think that is?",
                    "2. What makes you get involved in arguments (your own or other's)?",
                    "3. Why do you feel the need to stand your ground in an argument?",
                    "4. If you backed down from an argument, how would you be perceived?",
                    "5. Have you ever used \"casting lots\" to end a quarrel? Would you trust the Lord to direct the outcome and live peaceably with the result?",
                    "6. What specific things can you do to avoid strife? List the things that stand out as most important to you, personally, from the verses above.",
                    "7. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 14: Don't Have a Perverse Heart
            # ========================================
            ProverbTopic(
                number=14,
                title="Don't Have a Perverse Heart",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I often feel like my heart just isn't in the right place (filled with perverse thoughts; prideful or stubborn feelings, wicked intent, etc.)?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to have a perverse heart (filled with perverse thoughts; prideful or stubborn feelings, wicked intent, etc.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 11:20 (NKJV)",
                        text="20 Those who are of a perverse heart are an abomination to the LORD, But the blameless in their ways are His delight."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 12:8 (NKJV)",
                        text="8 A man will be commended according to his wisdom, But he who is of a perverse heart will be despised."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 14:2 (NKJV)",
                        text="2 He who walks in his uprightness fears the LORD, But he who is perverse in his ways despises Him."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 17:3 (NKJV)",
                        text="3 The refining pot is for silver and the furnace for gold, But the LORD tests the hearts."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 20:27 (NKJV)",
                        text="27 The spirit of a man is the lamp of the LORD, Searching all the inner depths of his heart."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:4 (NKJV)",
                        text="4 A haughty look, a proud heart, And the plowing of the wicked are sin."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:27 (NKJV)",
                        text="27 The sacrifice of the wicked is an abomination; How much more when he brings it with wicked intent!"
                    ),
                    ScriptureVerse(
                        reference="Proverbs 22:5 (NKJV)",
                        text="5 Thorns and snares are in the way of the perverse; He who guards his soul will be far from them."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 27:19 (NKJV)",
                        text="19 As in water face reflects face, So a man's heart reveals the man."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:14 (NKJV)",
                        text="14 Happy is the man who is always reverent, But he who hardens his heart will fall into calamity."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:18 (NKJV)",
                        text="18 Whoever walks blamelessly will be saved, But he who is perverse in his ways will suddenly fall."
                    )
                ],
                dig_deeper_questions=[
                    "1. Where does this attitude come from? Can you identify the root of the issue?",
                    "2. What is the opposite of a perverse heart (see verses above)?",
                    "3. What can you do to overcome this attitude?",
                    "4. If you think your boss/coworker has this issue, what makes you think so? What behaviors lead you to believe this?",
                    "5. How does this impact your job?",
                    "6. What has been your response?",
                    "7. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 15: Be an Excellent Wife
            # ========================================
            ProverbTopic(
                number=15,
                title="Be an Excellent Wife",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I'd say I'm an excellent wife? (If applicable, or substitute \"spouse/partner\")",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to be or have an excellent wife (If applicable or substitute \"spouse\")",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 12:4 (NKJV)",
                        text="4 An excellent wife is the crown of her husband, But she who causes shame is like rottenness in his bones."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 18:22 (NKJV)",
                        text="22 He who finds a wife finds a good thing, And obtains favor from the LORD."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:14 (NKJV)",
                        text="14 Houses and riches are an inheritance from fathers, But a prudent wife is from the LORD."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 31:10-31 (NKJV)",
                        text="10 Who can find a virtuous wife? For her worth is far above rubies. 11 The heart of her husband safely trusts her; So he will have no lack of gain. 12 She does him good and not evil All the days of her life. 13 She seeks wool and flax, And willingly works with her hands. 14 She is like the merchant ships, She brings her food from afar. 15 She also rises while it is yet night, And provides food for her household, And a portion for her maidservants. 16 She considers a field and buys it; From her profits she plants a vineyard. 17 She girds herself with strength, And strengthens her arms. 18 She perceives that her merchandise is good, And her lamp does not go out by night. 19 She stretches out her hands to the distaff, And her hand holds the spindle. 20 She extends her hand to the poor, Yes, she reaches out her hands to the needy. 21 She is not afraid of snow for her household, For all her household is clothed with scarlet. 22 She makes tapestry for herself; Her clothing is fine linen and purple. 23 Her husband is known in the gates, When he sits among the elders of the land. 24 She makes linen garments and sells them, And supplies sashes for the merchants. 25 Strength and honor are her clothing; She shall rejoice in time to come. 26 She opens her mouth with wisdom, And on her tongue is the law of kindness. 27 She watches over the ways of her household, And does not eat the bread of idleness. 28 Her children rise up and call her blessed; Her husband also, and he praises her: 29 \"Many daughters have done well, But you excel them all.\" 30 Charm is deceitful and beauty is passing, But a woman who fears the LORD, she shall be praised. 31 Give her of the fruit of her hands, And let her own works praise her in the gates."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 25:24 (NKJV)",
                        text="24 It is better to dwell in a corner of a housetop, Than in a house shared with a contentious woman."
                    )
                ],
                dig_deeper_questions=[
                    "1. Have you ever considered the value you have as an excellent vs. a shameful wife/spouse? Describe how you have added value to your spouse.",
                    "2. How can your excellence as a wife/spouse help those beyond your spouse: your household, your work, and your community?",
                    "3. How can (has) being a contentious wife be(en) a detriment to your spouse?",
                    "4. Where does that ability to be excellent come from (you or the Lord)?",
                    "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 16: Avoid Anger
            # ========================================
            ProverbTopic(
                number=16,
                title="Avoid Anger",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I let anger build up inside or boil over into outbursts?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to allow anger to build up inside or to boil over into outbursts.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 12:16 (NKJV)",
                        text="16 A fool's wrath is known at once, But a prudent man covers shame."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 14:10 (NKJV)",
                        text="10 The heart knows its own bitterness, And a stranger does not share its joy."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 14:16-17 (NKJV)",
                        text="16 A wise man fears and departs from evil, But a fool rages and is self-confident. 17 A quick-tempered man acts foolishly, And a man of wicked intentions is hated."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 14:29 (NKJV)",
                        text="29 He who is slow to wrath has great understanding, But he who is impulsive exalts folly."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 15:18 (NKJV)",
                        text="18 A wrathful man stirs up strife, But he who is slow to anger allays contention"
                    ),
                    ScriptureVerse(
                        reference="Proverbs 16:32 (NKJV)",
                        text="32 He who is slow to anger is better than the mighty, And he who rules his spirit than he who takes a city."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:11 (NKJV)",
                        text="11 The discretion of a man makes him slow to anger, And his glory is to overlook a transgression."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 19:19 (NKJV)",
                        text="19 A man of great wrath will suffer punishment; For if you rescue him, you will have to do it again."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:29 (NKJV)",
                        text="29 A wicked man hardens his face, But as for the upright, he establishes his way."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 22:24-25 (NKJV)",
                        text="24 Make no friendship with an angry man, And with a furious man do not go, 25 Lest you learn his ways And set a snare for your soul."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 27:15-16 (NKJV)",
                        text="15 A continual dripping on a very rainy day And a contentious woman are alike; 16 Whoever restrains her restrains the wind, And grasps oil with his right hand."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 29:22 (NKJV)",
                        text="22 An angry man stirs up strife, And a furious man abounds in transgression."
                    )
                ],
                dig_deeper_questions=[
                    "1. Has your anger ever made you look foolish?",
                    "2. Has your anger ever hurt someone, irritated (continual dripping) or made someone mad at you?",
                    "3. Have you ever let a friend's anger make you angry?",
                    "4. Why is your heart bitter/contentious?",
                    "5. What do the verses below teach you that can you do to control your anger?",
                    "6. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 17: Avoid Anxiety
            # ========================================
            ProverbTopic(
                number=17,
                title="Avoid Anxiety",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I would describe myself as overly anxious/easily depressed?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to have a problem with anxiety/depression.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 12:25 (NKJV)",
                        text="25 Anxiety in the heart of man causes depression, But a good word makes it glad."
                    )
                ],
                dig_deeper_questions=[
                    "1. Who do you need \"a good word\" from? Will you tell them that?",
                    "2. Do you give \"good words\"? Whom can you give \"a good word\" to?",
                    "3. Can you find other verses about worry and anxiety throughout the Bible? (Try: Matthew 6:25, 27, 28, 31, 34; Matthew 10:19; Mark 3:11; Luke 12:11, 22, 25.)",
                    "4. How do you deal with your anxiety? What helps put things in perspective for you?",
                    "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 18: Don't Abuse Alcohol
            # ========================================
            ProverbTopic(
                number=18,
                title="Don't Abuse Alcohol",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I allow substance abuse to affect my life or the life of others?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to allow substance abuse to affect their life.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 20:1 (NKJV)",
                        text="1 Wine is a mocker, Strong drink is a brawler, And whoever is led astray by it is not wise."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 21:17 (NKJV)",
                        text="17 He who loves pleasure will be a poor man; He who loves wine and oil will not be rich."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 23:29-35 (NKJV)",
                        text="29 Who has woe? Who has sorrow? Who has contentions? Who has complaints? Who has wounds without cause? Who has redness of eyes? 30 Those who linger long at the wine, Those who go in search of mixed wine. 31 Do not look on the wine when it is red, When it sparkles in the cup, When it swirls around smoothly; 32 At the last it bites like a serpent, And stings like a viper. 33 Your eyes will see strange things, And your heart will utter perverse things. 34 Yes, you will be like one who lies down in the midst of the sea, Or like one who lies at the top of the mast, saying: 35 \"They have struck me, but I was not hurt; They have beaten me, but I did not feel it. When shall I awake, that I may seek another drink?\""
                    ),
                    ScriptureVerse(
                        reference="Proverbs 31:4-7 (NKJV)",
                        text="4 It is not for kings, O Lemuel, It is not for kings to drink wine, Nor for princes intoxicating drink; 5 Lest they drink and forget the law, And pervert the justice of all the afflicted. 6 Give strong drink to him who is perishing, And wine to those who are bitter of heart. 7 Let him drink and forget his poverty, And remember his misery no more."
                    )
                ],
                dig_deeper_questions=[
                    # Note: The PDF appears to have no "Dig Deeper" questions for this topic
                ]
            ),
            
            # ========================================
            # TOPIC 19: Don't Envy the Oppressors
            # ========================================
            ProverbTopic(
                number=19,
                title="Don't Envy the Oppressors",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I envy (or imitate) those who get ahead, even if by dishonest means?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to envy or imitate those who get ahead, even if by dishonest means.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 3:31-33 (NKJV)",
                        text="31 Do not envy the oppressor, And choose none of his ways; 32 For the perverse person is an abomination to the LORD, But His secret counsel is with the upright. 33 The curse of the LORD is on the house of the wicked, But He blesses the home of the just."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 12:12 (NKJV)",
                        text="12 The wicked covet the catch of evil men, But the root of the righteous yields fruit."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 24:1-2 (NKJV)",
                        text="1 Do not be envious of evil men, Nor desire to be with them; 2 For their heart devises violence, And their lips talk of troublemaking."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 24:19-20 (NKJV)",
                        text="19 Do not fret because of evildoers, Nor be envious of the wicked; 20 For there will be no prospect for the evil man; The lamp of the wicked will be put out."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 28:3 (NKJV)",
                        text="3 A poor man who oppresses the poor Is like a driving rain which leaves no food."
                    )
                ],
                dig_deeper_questions=[
                    "1. Do these verses convince you of your need to put those thoughts of envy behind you? Why or why not?",
                    "2. Have you ever witnessed the \"fall\" of someone who got ahead by dishonest means or by oppressing others? Some are never \"caught\" in this life, but can you list some consequences for those that are caught; for themselves, for their families?",
                    "3. What do you need to do to get beyond this thought-pattern of envy/coveting? The Bible has plenty more to say about this. You might need to research some more versus and quote them here.",
                    "4. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            ),
            
            # ========================================
            # TOPIC 20: Don't Envy/Be Jealous
            # ========================================
            ProverbTopic(
                number=20,
                title="Don't Envy/Be Jealous",
                assessment_questions=[
                    AssessmentQuestion(
                        text="I am jealous of someone or something they have?",
                        question_type="self"
                    ),
                    AssessmentQuestion(
                        text="My boss/co-worker/employee seems to be the jealous type.",
                        question_type="other"
                    )
                ],
                scripture_verses=[
                    ScriptureVerse(
                        reference="Proverbs 14:30 (NKJV)",
                        text="30 A sound heart is life to the body, But envy is rottenness to the bones."
                    ),
                    ScriptureVerse(
                        reference="Proverbs 27:3-4 (NKJV)",
                        text="3 A stone is heavy and sand is weighty, But a fool's wrath is heavier than both of them. 4 Wrath is cruel and anger a torrent, But who is able to stand before jealousy?"
                    )
                ],
                dig_deeper_questions=[
                    "1. Have you ever thought that being jealous of someone is worse than being angry with him or her?",
                    "2. Have you ever been the object of someone else's jealousy? How did that make you feel or impact your life?",
                    "3. If you are the object of someone's jealousy, how will you deal with this?",
                    "4. Are you jealous of someone and need to release them (just as you would need to forgive them if you were angry)? If so, who and how will you do this?",
                    "5. Summarize/prioritize things you can do, (or do for) your boss, co-worker, and/or employee, to improve in this area:"
                ]
            )
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
