# Test z fyziky - Ohmov zákon
# Autor: ChatGPT

def main():
    otazky = [
        ("Ktorý vzťah vyjadruje Ohmov zákon?",
         {"a": "U = R / I", "b": "U = I * R", "c": "R = U * I"}, "b"),

        ("Aký je odpor vodiča, ak ním prechádza prúd 2 A a napätie na ňom je 10 V?",
         {"a": "5 Ω", "b": "20 Ω", "c": "0,2 Ω"}, "a"),

        ("Ak sa napätie zvýši a odpor zostane rovnaký, prúd v obvode:",
         {"a": "Zníži sa", "b": "Zostane rovnaký", "c": "Zvýši sa"}, "c"),

        ("Jednotkou elektrického odporu je:",
         {"a": "Ampér (A)", "b": "Volt (V)", "c": "Ohm (Ω)"}, "c"),

        ("Vodič má odpor 50 Ω. Ak ním prechádza prúd 0,2 A, aké napätie je na vodiči?",
         {"a": "10 V", "b": "250 V", "c": "0,04 V"}, "a"),

        ("Čo vyjadruje odpor vodiča?",
         {"a": "Schopnosť vodiča viesť elektrický prúd",
          "b": "Schopnosť vodiča brániť prechodu elektrického prúdu",
          "c": "Množstvo náboja, ktoré vodič pojme"}, "b"),

        ("Prúd 3 A preteká odporom 4 Ω. Vypočítaj napätie.",
         {"a": "1,33 V", "b": "7 V", "c": "12 V"}, "c"),

        ("Ak sa odpor vodiča zdvojnásobí a napätie zostane rovnaké, prúd sa:",
         {"a": "Zdvojnásobí", "b": "Zníži na polovicu", "c": "Zostane rovnaký"}, "b"),

        ("Ktorá z nasledujúcich veličín nie je priamo zahrnutá v Ohmovom zákone?",
         {"a": "Napätie", "b": "Výkon", "c": "Prúd"}, "b"),

        ("Vypočítaj výkon spotrebiča, ak prúdom 2 A prechádza napätie 12 V.",
         {"a": "6 W", "b": "24 W", "c": "144 W"}, "b")
    ]

    body = 0

    print("="*60)
    print(" 🧮  TEST Z FYZIKY – OHMOV ZÁKON ")
    print("="*60)

    for i, (otazka, moznosti, spravna) in enumerate(otazky, 1):
        print(f"\n{i}. {otazka}")
        for kluc, text in moznosti.items():
            print(f"   {kluc}) {text}")
        odpoved = input("Tvoja odpoveď (a/b/c): ").lower().strip()
        if odpoved == spravna:
            print("✅ Správne!")
            body += 1
        else:
            print(f"❌ Nesprávne. Správna odpoveď je: {spravna}) {moznosti[spravna]}")

    # Vyhodnotenie
    percenta = round((body / len(otazky)) * 100)
    if percenta >= 90:
        znamka = 1
    elif percenta >= 75:
        znamka = 2
    elif percenta >= 60:
        znamka = 3
    elif percenta >= 45:
        znamka = 4
    else:
        znamka = 5

    print("\n" + "="*60)
    print(f"Získal(a) si {body} z {len(otazky)} bodov.")
    print(f"Úspešnosť: {percenta}%")
    print(f"Výsledná známka: {znamka}")
    print("="*60)


if __name__ == "__main__":
    main()
