import json
import random

subjects = {
    "Child Development & Pedagogy": [
        "According to Piaget's theory", "Vygotsky's Zone of Proximal Development", "Inclusive education focuses on",
        "The primary purpose of formative assessment", "A symptom of Dyslexia", "Multiple Intelligences was proposed by",
        "Transfer of Learning implies", "Audio-visual aids in classroom", "Erikson's psychosocial development",
        "Continuous and Comprehensive Evaluation", "The concept of scaffolding", "Kohlberg's moral development",
        "Which is a characteristic of gifted children?", "National Education Policy 2020 emphasizes", "RTE Act 2009 mandates",
        "Constructivism as a learning theory", "Intrinsic vs Extrinsic motivation", "Peer tutoring is effective for",
        "Dyscalculia is associated with", "Classical conditioning was discovered by", "Operant conditioning focuses on",
        "The role of a teacher in a progressive classroom", "Summative assessment is used for", "Aptitude tests measure",
        "Meaningful learning occurs when", "Micro-teaching is a technique for", "Brainstorming promotes",
        "Action research in education", "A diagnostic test is used to", "Emotional intelligence involves"
    ],
    "Language I (Odia)": [
        "‘ଆକାଶ’ ର ପ୍ରତିଶବ୍ଦ କ’ଣ?", "‘ଅନ୍ଧର ଲଉଡ଼ି’ ରୂଢ଼ିର ଅର୍ଥ", "ଶୁଦ୍ଧ ଶବ୍ଦଟିକୁ ବାଛ:", "ବିଶେଷ୍ୟ ପଦର ପରିବର୍ତ୍ତେ", "‘ପଢିବା’ ଏକ କେଉଁ ପଦ?",
        "ଜଟିଳ ବାକ୍ୟର ଉଦାହରଣ", "ଭାଷା ଶିକ୍ଷଣର ପ୍ରଥମ କୌଶଳ", "ବ୍ୟାକରଣ ଶିକ୍ଷାଦାନର ସର୍ବୋତ୍ତମ ପଦ୍ଧତି", "‘ମାଟି’ ଶବ୍ଦର ବିପରୀତ ଶବ୍ଦ",
        "ପଠନ ଦକ୍ଷତା ମାପିବା ପାଇଁ", "‘ସୂର୍ଯ୍ୟ’ ର ପ୍ରତିଶବ୍ଦ", "‘କପାଳ ଲିଖନ’ ଅର୍ଥ", "ସନ୍ଧି ବିଚ୍ଛେଦ କର: ନିରୋଗ", "ସମାସ ଚିହ୍ନାଅ: ତ୍ରିଲୋଚନ",
        "କୃଦନ୍ତ ପଦ କାହାକୁ କୁହାଯାଏ?", "ତଦ୍ଧିତ ପ୍ରତ୍ୟୟ କ’ଣ?", "ଓଡ଼ିଆ ବର୍ଣ୍ଣମାଳାରେ କେତୋଟି ସ୍ୱରବର୍ଣ୍ଣ ଅଛି?", "‘ଅନ୍ଧାର’ ର ବିପରୀତ",
        "ଶ୍ରବଣ କୌଶଳର ବିକାଶ", "ମାତୃଭାଷା ଶିକ୍ଷାର ମୂଳ ଲକ୍ଷ୍ୟ", "ରଚନା ଲିଖନର ଉଦ୍ଦେଶ୍ୟ", "କବିତା ଶିକ୍ଷାଦାନ", "ପ୍ରବନ୍ଧ ଶିକ୍ଷାଦାନ",
        "ଗଳ୍ପ ଶିକ୍ଷାଦାନ", "ବନାନ ଶୁଦ୍ଧି", "ବିରାମ ଚିହ୍ନର ବ୍ୟବହାର", "ପ୍ରତିଶବ୍ଦ ଶିକ୍ଷା", "ବିପରୀତ ଶବ୍ଦ ଶିକ୍ଷା", "ରୂଢ଼ି ପ୍ରୟୋଗ", "ଲୋକବାଣୀର ଅର୍ଥ"
    ],
    "Language II (English)": [
        "Choose the correct preposition", "Primary aim of teaching poetry", "Synonym of 'Abundant'", "Receptive skill in language",
        "Fill in the blank: If it rains", "Idiom 'Bite the bullet'", "Choose the correct spelling", "Scanning vs Skimming",
        "Antonym of 'Optimistic'", "Which part of speech connects", "Active to Passive voice", "Direct to Indirect speech",
        "Identify the correct tense", "Use of article 'the'", "Subject-verb agreement", "Meaning of 'To break the ice'",
        "Synonym of 'Diligent'", "Antonym of 'Transparent'", "Identify the adverb", "Identify the adjective",
        "Function of a pronoun", "Teaching reading skills", "Teaching writing skills", "Communicative language teaching",
        "Grammar-translation method", "Direct method of teaching", "Audio-lingual method", "Role of listening comprehension",
        "Importance of pronunciation", "Extensive reading aims at"
    ],
    "Mathematics": [
        "LCM of 12, 15, and 20", "Percentage error calculation", "Sum of angles of a quadrilateral", "Inductive method moves from",
        "Cost of 8 pens if 15 cost 225", "Prime number identification", "Perimeter of a rectangle", "Use of manipulatives",
        "Value of x if x/3 = 12", "Simple interest calculation", "Area of a circle", "Volume of a cylinder",
        "Pythagoras theorem application", "Probability of tossing a coin", "Mean, median, mode", "Algebraic expressions",
        "Linear equations in one variable", "Ratio and proportion", "Profit and loss", "Time and work",
        "Speed, distance, and time", "Geometry: properties of triangles", "Data handling and graphs", "Mathematical reasoning",
        "Nature of mathematics", "Deductive method in math", "Problem-solving method", "Project method in math",
        "Evaluation in mathematics", "Diagnostic testing in math"
    ],
    "Environmental Studies": [
        "Most abundant gas in atmosphere", "Primary source of energy", "Non-renewable resource example", "Pedagogical approach for EVS",
        "Ozone layer depletion cause", "Chipko Movement association", "Vitamin D synthesis", "Biodiversity definition",
        "Condensation process", "Greenhouse effect", "Global warming consequences", "Water pollution causes",
        "Air pollution effects", "Soil erosion prevention", "Forest conservation", "Wildlife protection act",
        "Ecosystem components", "Food chain and food web", "Renewable energy sources", "Solar system planets",
        "Earth's rotation and revolution", "States of matter", "Human digestive system", "Respiratory system",
        "Importance of balanced diet", "Diseases and their causes", "First aid basics", "Disaster management",
        "Map reading skills", "Continuous evaluation in EVS"
    ]
}

options_pool = [
    ["Option A", "Option B", "Option C", "Option D"],
    ["True", "False", "Partially True", "None of the above"],
    ["1", "2", "3", "4"],
    ["Increasing", "Decreasing", "Constant", "Zero"]
]

qbank_json = {}

for subj, topics in subjects.items():
    qbank_json[subj] = []
    for i, topic in enumerate(topics):
        qbank_json[subj].append({
            "t": f"{topic} involves understanding complex underlying principles and applying them.",
            "o": ["Concept formulation", "Rote memorization", "Passive listening", "Random guessing"],
            "a": 0,
            "d": random.choice(["Easy", "Medium", "Hard"]),
            "e": f"The core concept of {topic} is based on active engagement and formulation."
        })

print(json.dumps(qbank_json, indent=2))
