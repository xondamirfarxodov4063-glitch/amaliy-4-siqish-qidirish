# ============================================================
# AMALIY ISH - 5: Bilimlar Bazasi va Bilimlarni Taqdim Etish
# ============================================================

print("=" * 65)
print("AMALIY ISH - 5: Bilimlar Bazasi va Taqdim Etish Modellari")
print("=" * 65)

# ============================================================
# 1. FREYM MODEL (Frame Model)
# ============================================================
print("\n📦 1. FREYM MODEL (Frame Model)")
print("-" * 50)

class FrameModel:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def display(self):
        print(f"  Freym: {self.name}")
        for key, value in self.properties.items():
            print(f"    {key}: {value}")

# Tibbiyot sohasiga oid freymlar
doctor_frame = FrameModel("Shifokor", {
    "Mutaxassislik": "Kardiologiya",
    "Tajriba": "10 yil",
    "Ish joyi": "Farg'ona shahri kasalxonasi",
    "Muolaja turi": "Yurak-qon tomir kasalliklari"
})

patient_frame = FrameModel("Bemor", {
    "Ism": "Aliyev Vohid",
    "Yosh": "45",
    "Tashxis": "Gipertoniya",
    "Holat": "Betob",
    "Dori": "Amlodipine 5mg"
})

doctor_frame.display()
print()
patient_frame.display()

# ============================================================
# 2. PRODUKSION MODEL (Production Model) — if-then qoidalari
# ============================================================
print("\n\n📋 2. PRODUKSION MODEL (if-then qoidalari)")
print("-" * 50)

class ProductionModel:
    def __init__(self):
        self.rules = [
            {"shart": "betob",        "natija": "Darhol davolanish kerak!"},
            {"shart": "gipertoniya",  "natija": "Qon bosimini nazorat qiling va dori qabul qiling."},
            {"shart": "sog'lom",      "natija": "Profilaktik tekshiruvdan o'ting."},
            {"shart": "yuqori harorat","natija": "Isitma tushiruvchi dori qabul qiling, shifokorga murojaat qiling."},
        ]

    def apply_rules(self, condition):
        for rule in self.rules:
            if rule["shart"] in condition.lower():
                return f"  Shart: '{condition}' => {rule['natija']}"
        return f"  Shart: '{condition}' => Qoida topilmadi."

pm = ProductionModel()
cases = ["betob", "gipertoniya", "sog'lom", "yuqori harorat", "gripp"]
for case in cases:
    print(pm.apply_rules(case))

# ============================================================
# 3. MANTIQIY MODEL (Logical Model)
# ============================================================
print("\n\n🔣 3. MANTIQIY MODEL (Logical Model)")
print("-" * 50)

def logical_rule(patient_condition, age, temperature):
    """
    Mantiqiy qoidalar (predikat mantiq):
    P(x) = betob(x) AND yosh(x) > 60 => shoshilinch yordam
    Q(x) = harorat(x) > 38.5 => isitma
    """
    result = []

    # Qoida 1: P(x) = betob AND yosh > 60
    if patient_condition == "betob" and age > 60:
        result.append("P(x): Keksa betob bemor — shoshilinch tibbiy yordam kerak!")

    # Qoida 2: Q(x) = harorat > 38.5
    if temperature > 38.5:
        result.append(f"Q(x): Harorat {temperature}°C > 38.5°C — isitma mavjud, davo kerak.")

    # Qoida 3: NOT betob AND yosh <= 40
    if patient_condition != "betob" and age <= 40:
        result.append("R(x): Yosh va sog'lom — profilaktik nazorat yetarli.")

    if not result:
        result.append("Hech qanday kritik holat aniqlanmadi.")

    return result

# Test holatlari
test_cases = [
    ("betob", 65, 39.2),
    ("sog'lom", 30, 36.6),
    ("betob", 45, 37.0),
]

for condition, age, temp in test_cases:
    print(f"\n  Holat: '{condition}', Yosh: {age}, Harorat: {temp}°C")
    for r in logical_rule(condition, age, temp):
        print(f"    => {r}")

# ============================================================
# 4. SEMANTIK MODEL (Semantic Model)
# ============================================================
print("\n\n🌐 4. SEMANTIK MODEL (Semantic Network)")
print("-" * 50)

class SemanticNetwork:
    def __init__(self):
        self.nodes = {}   # Tushunchalar
        self.edges = []   # Munosabatlar

    def add_node(self, name, attributes):
        self.nodes[name] = attributes

    def add_relation(self, node1, relation, node2):
        self.edges.append((node1, relation, node2))

    def display(self):
        print("  Tugunlar (Tushunchalar):")
        for name, attrs in self.nodes.items():
            print(f"    [{name}]: {attrs}")
        print("\n  Munosabatlar (Bog'lanishlar):")
        for n1, rel, n2 in self.edges:
            print(f"    {n1}  --[{rel}]-->  {n2}")

    def query(self, node):
        print(f"\n  '{node}' tuguniga bog'liq munosabatlar:")
        for n1, rel, n2 in self.edges:
            if n1 == node or n2 == node:
                print(f"    {n1} --[{rel}]--> {n2}")

sn = SemanticNetwork()

# Tibbiyot ontologiyasi
sn.add_node("Kasallik",    {"turi": "abstrak tushuncha"})
sn.add_node("Gipertoniya", {"tur": "surunkali", "belgi": "yuqori qon bosimi"})
sn.add_node("Gripp",       {"tur": "yuqumli", "belgi": "isitma, yo'tal"})
sn.add_node("Dori",        {"turi": "davolash vositasi"})
sn.add_node("Amlodipine",  {"doza": "5mg", "maqsad": "qon bosimini tushirish"})
sn.add_node("Bemor",       {"holat": "davolanishda"})

sn.add_relation("Gipertoniya", "bu-tur",    "Kasallik")
sn.add_relation("Gripp",       "bu-tur",    "Kasallik")
sn.add_relation("Amlodipine",  "bu-tur",    "Dori")
sn.add_relation("Bemor",       "kasallangan", "Gipertoniya")
sn.add_relation("Gipertoniya", "davolanadi", "Amlodipine")
sn.add_relation("Shifokor",    "davolaydi", "Bemor")

sn.display()
sn.query("Gipertoniya")

# ============================================================
# 5. BILIMLAR BAZASI — barcha modellarni birlashtirish
# ============================================================
print("\n\n🧠 5. TO'LIQ BILIMLAR BAZASI (Knowledge Base)")
print("-" * 50)

class KnowledgeBase:
    def __init__(self):
        self.knowledge = [
            "davolanish zarur",
            "bemor betob",
            "yuqori qon bosimi aniqlandi",
            "profilaktika tavsiya etiladi"
        ]

class KnowledgeExtractor:
    @staticmethod
    def extract_facts(knowledge_list):
        production_rules = ["Agar '{fact}', u holda tegishli chora ko'rish kerak."]
        extracted_facts = []
        for fact in knowledge_list:
            if "davolanish" in fact or "betob" in fact or "qon bosimi" in fact:
                extracted_facts.append(production_rules[0].format(fact=fact))
        return extracted_facts

kb = KnowledgeBase()
extracted = KnowledgeExtractor.extract_facts(kb.knowledge)
print("  Bilimlar bazasidan ajratib olingan faktlar:")
for e in extracted:
    print(f"    => {e}")

# ============================================================
# XULOSA
# ============================================================
print("\n" + "=" * 65)
print("XULOSA")
print("=" * 65)
print("  1. Freym modeli   : Tuzilgan ma'lumotlar (Shifokor, Bemor freymi)")
print("  2. Produksion model: If-then qoidalari bilan 5 ta holat tahlil qilindi")
print("  3. Mantiqiy model  : Predikat mantiq qoidalari (P, Q, R) ishlatildi")
print("  4. Semantik model  : 6 tugun, 6 munosabatli ontologiya qurildi")
print("  5. Bilimlar bazasi : 4 ta faktdan 3 tasi ajratib olindi")
print("=" * 65)
