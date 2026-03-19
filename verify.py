files = ['frontend/index.html', 'frontend/test.html']
checks = {
    'startTestWithDuration': 'should NOT be found',
    'testDuration': 'should NOT be found',
    'Godu Godu': 'should BE found',
    'c1272d': 'should BE found',
}
for f in files:
    content = open(f, encoding='utf-8-sig').read()
    print(f'--- {f} ---')
    for k, v in checks.items():
        found = k in content
        print(f'  {k}: {"FOUND" if found else "NOT FOUND"}  ({v})')
