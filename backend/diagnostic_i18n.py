import sys
import os

# Try to import get_localized_data
sys.path.append(os.getcwd())
try:
    from saju_i18n import get_localized_data
    
    for lang in ['ko', 'en', 'es', 'pt']:
        data = get_localized_data(lang)
        kw = data.get("MONTH_KEYWORDS", [])
        ds = data.get("MONTH_DESCS", [])
        print(f"[{lang}] Keywords count: {len(kw)}")
        print(f"[{lang}] Descs count: {len(ds)}")
        if kw:
            print(f"[{lang}] First keyword: {kw[0]}")
        if ds:
            print(f"[{lang}] First desc: {ds[0][:50]}...")
        print("-" * 20)
except Exception as e:
    print(f"Error: {e}")
