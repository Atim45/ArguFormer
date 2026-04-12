from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    # --- Ad Hominem ---
    "You are stupid so your argument is wrong",
    "Only an idiot would believe that",
    "You are completely dumb",
    "You are the dumbest person ever",
    "You're just a loser, so your opinion doesn't matter",
    "Don't listen to him, he's uneducated",
    "You're too young to understand anything",
    "You're a failure, so your argument is invalid",

    # --- Appeal to Emotion ---
    "Everyone believes this so it must be true",
    "Think about the poor children suffering",
    "If you don't agree, people will get hurt",
    "Imagine how sad this would make your family",
    "This will destroy our future if we don't act",
    "Do it for the people who are suffering",
    "You should feel ashamed if you disagree",
    "This is heartbreaking, so it must be wrong",

    # --- Strawman ---
    "You twisted my argument completely",
    "You attacked a point I never made",
    "So you're saying we should ban everything?",
    "You think we should just give up completely?",
    "You are claiming we should ignore all laws",
    "So you want chaos in society?",
    "You are exaggerating my position unfairly",
    "That's not what I said at all",

    # --- False Dilemma ---
    "You're either with us or against us",
    "We either do this or everything fails",
    "There are only two options here",
    "Either we act now or it's too late",
    "You must choose one side only",
    "It's all or nothing",
    "No middle ground exists",
    "Either accept it or leave",

    # --- Slippery Slope ---
    "If we allow this, everything will collapse",
    "This small step will lead to disaster",
    "Soon everything will spiral out of control",
    "One change will ruin everything",
    "This is the first step toward chaos",
    "Next thing you know, society will fall apart",
    "This will inevitably lead to worse things",
    "It starts small but ends terribly",

    # --- Circular Reasoning ---
    "It's true because it's correct",
    "I know I'm right because I am correct",
    "This is valid because it's true",
    "The law is just because it is the law",
    "We know this works because it works",
    "This is right since it's not wrong",
    "It must be true because it is",
    "That's correct because it's accurate",

    # --- Hasty Generalization ---
    "All politicians are corrupt",
    "Everyone from that place is rude",
    "All students are lazy",
    "Every rich person is greedy",
    "Nobody cares about honesty anymore",
    "People like that are always wrong",
    "That group never tells the truth",
    "Everyone does this",

    # --- Red Herring ---
    "Why talk about that when there are bigger problems",
    "This issue doesn't matter compared to others",
    "Let's focus on something else instead",
    "That’s not important right now",
    "There are more serious issues to discuss",
    "Why bring that up now?",
    "This is distracting from the real issue",
    "Let's change the topic"
]

labels = (
    ["Ad Hominem"] * 8 +
    ["Appeal to Emotion"] * 8 +
    ["Strawman"] * 8 +
    ["False Dilemma"] * 8 +
    ["Slippery Slope"] * 8 +
    ["Circular Reasoning"] * 8 +
    ["Hasty Generalization"] * 8 +
    ["Red Herring"] * 8
)

# Vectorizer with better settings
vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words='english')
X = vectorizer.fit_transform(texts)

# Better model config
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

def traditional_fallacy(sentence):
    vec = vectorizer.transform([sentence])
    return model.predict(vec)[0]