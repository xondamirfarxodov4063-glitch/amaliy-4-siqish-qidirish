# ============================================================
# AMALIY ISH - 6: Noravshan bilim modellari. Ekspert tizimlari
# ============================================================

print("=" * 65)
print("AMALIY ISH - 6: Noravshan bilim modellari. Ekspert tizimlari")
print("=" * 65)

# ============================================================
# 1. ASOSIY EKSPERT TIZIMI (darslikdagi namuna)
# ============================================================
print("\n📋 1. ASOSIY EKSPERT TIZIMI (darslik namunasi)")
print("-" * 55)

class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "Yuqori harorat":    "Gripp yoki infeksiya mavjud bo'lishi mumkin.",
            "Kassalashish":      "Allergiya yoki oziq-ovqat zakkumlanishi mumkin.",
            "Kuchli bosh og'rig'i": "Migren yoki yuqori qon bosimi.",
        }

    def diagnose(self, symptom):
        return self.knowledge_base.get(symptom, "Ma'lumot mavjud emas.")

expert_system = ExpertSystem()
test_symptoms = ["Yuqori harorat", "Kassalashish", "Kuchli bosh og'rig'i", "Yo'tal"]
for s in test_symptoms:
    print(f"  Simptom: '{s}'  =>  {expert_system.diagnose(s)}")

# ============================================================
# 2. KENGAYTIRILGAN TIBBIY EKSPERT TIZIMI
# ============================================================
print("\n\n🏥 2. KENGAYTIRILGAN TIBBIY EKSPERT TIZIMI")
print("-" * 55)

class MedicalExpertSystem:
    def __init__(self):
        # Bilimlar bazasi: simptomlar kombinatsiyasi => tashxis + tavsiya
        self.knowledge_base = [
            {
                "simptomlar": {"isitma", "yo'tal", "burun oqishi"},
                "tashxis":    "Shamollash (ARVI)",
                "tavsiya":    "Ko'p suv iching, dam oling, paracetamol qabul qiling.",
                "xavf":       "past"
            },
            {
                "simptomlar": {"isitma", "yo'tal", "nafas qisilishi"},
                "tashxis":    "Pnevmoniya (o'pka yallig'lanishi)",
                "tavsiya":    "Zudlik bilan shifokorga murojaat qiling!",
                "xavf":       "yuqori"
            },
            {
                "simptomlar": {"bosh og'rig'i", "ko'ngil aynishi", "yorug'likdan bezovtalanish"},
                "tashxis":    "Migren",
                "tavsiya":    "Tinch joyda dam oling, og'riq qoldiruvchi qabul qiling.",
                "xavf":       "o'rta"
            },
            {
                "simptomlar": {"ko'krak og'rig'i", "nafas qisilishi", "chap qo'l og'rig'i"},
                "tashxis":    "Yurak xurujiga shubha (SHOSHILINCH!)",
                "tavsiya":    "103 ga zudlik bilan qo'ng'iroq qiling!",
                "xavf":       "kritik"
            },
            {
                "simptomlar": {"isitma", "tomoq og'rig'i", "yutishda qiyinlik"},
                "tashxis":    "Angina (bodomcha bezlari yallig'lanishi)",
                "tavsiya":    "Antibiotik kursi kerak, shifokor maslahati oling.",
                "xavf":       "o'rta"
            },
            {
                "simptomlar": {"qorin og'rig'i", "ko'ngil aynishi", "ich ketish"},
                "tashxis":    "Oziq-ovqat zaharligi yoki gastroenterit",
                "tavsiya":    "Ko'p suyuqlik iching, dieta saqlang.",
                "xavf":       "o'rta"
            },
        ]

    def diagnose(self, patient_symptoms: set):
        best_match = None
        best_score = 0

        for rule in self.knowledge_base:
            # Mos kelgan simptomlar soni
            matched = len(rule["simptomlar"] & patient_symptoms)
            total   = len(rule["simptomlar"])
            score   = matched / total  # moslik foizi

            if matched >= 2 and score > best_score:
                best_score = score
                best_match = rule

        return best_match, round(best_score * 100)

    def report(self, symptoms_list):
        symptoms = set(symptoms_list)
        match, confidence = self.diagnose(symptoms)
        print(f"  Kiritilgan simptomlar: {', '.join(symptoms)}")
        if match:
            xavf_rang = {"past": "✅", "o'rta": "⚠️", "yuqori": "🔴", "kritik": "🆘"}
            icon = xavf_rang.get(match["xavf"], "❓")
            print(f"  Tashxis     : {match['tashxis']}")
            print(f"  Ishonch     : {confidence}%")
            print(f"  Xavf darajasi: {icon}  {match['xavf'].upper()}")
            print(f"  Tavsiya     : {match['tavsiya']}")
        else:
            print("  Tashxis: Simptomlar yetarli emas yoki ma'lumot bazada yo'q.")

mes = MedicalExpertSystem()

cases = [
    ["isitma", "yo'tal", "burun oqishi"],
    ["isitma", "yo'tal", "nafas qisilishi"],
    ["bosh og'rig'i", "ko'ngil aynishi", "yorug'likdan bezovtalanish"],
    ["ko'krak og'rig'i", "nafas qisilishi", "chap qo'l og'rig'i"],
    ["qorin og'rig'i", "ko'ngil aynishi", "ich ketish"],
]

for i, case in enumerate(cases, 1):
    print(f"\n  --- Bemor #{i} ---")
    mes.report(case)

# ============================================================
# 3. NORAVSHAN MANTIQ (Fuzzy Logic) — ishonch koeffitsiyenti
# ============================================================
print("\n\n🔢 3. NORAVSHAN MANTIQ (Fuzzy Logic) — ishonch koeffitsiyenti")
print("-" * 55)

def fuzzy_membership(value, low, mid, high):
    """Uchburchak funksiya: qiymat -> [0.0, 1.0]"""
    if value <= low or value >= high:
        return 0.0
    elif value == mid:
        return 1.0
    elif value < mid:
        return (value - low) / (mid - low)
    else:
        return (high - value) / (high - mid)

def fuzzy_diagnosis(temperature, pulse):
    t_normal  = fuzzy_membership(temperature, 35.0, 36.6, 37.5)
    t_fever   = fuzzy_membership(temperature, 37.0, 38.5, 41.0)
    p_normal  = fuzzy_membership(pulse, 50, 72, 100)
    p_high    = fuzzy_membership(pulse, 90, 110, 160)

    results = {
        "Sog'lom":        round(min(t_normal, p_normal) * 100, 1),
        "Shamollash":     round(min(t_fever, p_normal) * 100, 1),
        "Yurak muammosi": round(min(t_normal, p_high) * 100, 1),
        "Og'ir kasallik": round(min(t_fever, p_high) * 100, 1),
    }
    return results

fuzzy_cases = [
    (36.6, 72,  "Oddiy holat"),
    (38.7, 75,  "Isitma bor"),
    (36.8, 115, "Yurak urishi tez"),
    (39.2, 118, "Kritik holat"),
]

print(f"  {'Holat':<20} {'Harorat':>8} {'Puls':>6}  {'Tashxis (ishonch %)'}")
print(f"  {'-'*20} {'-'*8} {'-'*6}  {'-'*40}")
for temp, pulse, label in fuzzy_cases:
    res = fuzzy_diagnosis(temp, pulse)
    best = max(res, key=res.get)
    print(f"  {label:<20} {temp:>7.1f}° {pulse:>5}  =>  {best}: {res[best]}%")

# ============================================================
# XULOSA
# ============================================================
print("\n" + "=" * 65)
print("XULOSA")
print("=" * 65)
print("  1. Asosiy ekspert tizimi  : 3 simptom -> 3 tashxis (darslik namunasi)")
print("  2. Kengaytirilgan tizim   : 6 ta qoida, 5 bemor tahlili, xavf darajasi")
print("  3. Noravshan mantiq       : harorat + puls => 4 toifada ishonch foizi")
print("=" * 65)
