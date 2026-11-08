import os, glob, statistics

files = sorted(glob.glob('/tmp/opencode/*.dat'))
# exclude vtebench? none
rows_out = []
for f in files:
    name = os.path.basename(f).replace('.dat','')
    with open(f) as fh:
        lines = [l.strip() for l in fh if l.strip()]
    if not lines:
        continue
    headers = lines[0].split()
    # data rows
    cols = {h: [] for h in headers}
    for line in lines[1:]:
        parts = line.split()
        for idx,h in enumerate(headers):
            val = parts[idx] if idx < len(parts) else '_'
            if val != '_':
                cols[h].append(float(val))
    # mean per benchmark
    means = {h: (statistics.mean(cols[h]) if cols[h] else None) for h in headers}
    # overall mean across benchmarks (of per-benchmark means)
    vals = [m for m in means.values() if m is not None]
    overall = statistics.mean(vals) if vals else None
    total_samples = sum(len(cols[h]) for h in headers)
    rows_out.append((name, means, overall, total_samples, {h:len(cols[h]) for h in headers}))

# print table
print(f"{'terminal':28} {'overall_ms':>12} {'samples':>8}")
for name, means, overall, ts, sc in sorted(rows_out, key=lambda x: (x[2] if x[2] is not None else 1e9)):
    print(f"{name:28} {overall:12.1f} {ts:8d}")
print()
# per-benchmark means table
benchs = headers
print("Per-benchmark mean ms (lower better):")
header = f"{'terminal':28}" + "".join(f"{b[:12]:>14}" for b in benchs)
print(header)
for name, means, overall, ts, sc in sorted(rows_out, key=lambda x: (x[2] if x[2] is not None else 1e9)):
    row = f"{name:28}" + "".join((f"{means[b]:14.1f}" if means[b] is not None else f"{'_':>14}") for b in benchs)
    print(row)
