from saju_i18n import I18N

for lang in ["ko", "en", "es", "pt"]:
    count = len(I18N[lang]["MONTH_DESCS"])
    print(f"{lang}: {count}")
    # Check for duplicates
    unique_count = len(set(I18N[lang]["MONTH_DESCS"]))
    print(f"{lang} unique: {unique_count}")
