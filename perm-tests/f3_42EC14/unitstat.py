import json
d = json.load(open('build/GPOE8P/report.json'))
for u in d['units']:
    if '8042EAD4' in u['name'] or '8042E9FC' in u['name'] or '8042E8C4' in u['name']:
        m = u['measures']; md = u['metadata']
        print('%-28s fuzzy=%.4f code %s/%s fns %s/%s complete=%s' % (
            u['name'], m['fuzzy_match_percent'], m['matched_code'], m['total_code'],
            m['matched_functions'], m['total_functions'], md.get('complete')))
try:
    b = json.load(open('config/GPOE8P/psov3/linked_units_blocked.json'))
    keys = [str(k) for k in (b.keys() if isinstance(b, dict) else b)]
    print('blocked entries mentioning 8042E:', [k for k in keys if '8042E' in k])
except Exception as e:
    print('blocked file:', e)
lu = open('config/GPOE8P/psov3/linked_units.txt').read()
print('text_8042EAD4 in linked_units.txt:', 'text_8042EAD4' in lu)
