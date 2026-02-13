import sys, json, pathlib

def load_jsonl(path):
    for line in pathlib.Path(path).read_text().splitlines():
        if line.strip():
            yield json.loads(line)

def main():
    if len(sys.argv) < 2:
        print('usage: load_samples.py <jsonl>')
        sys.exit(1)
    count = 0
    for rec in load_jsonl(sys.argv[1]):
        # In a real system, validate and POST to registry API.
        count += 1
    print(f'Loaded {count} records (dry run).')

if __name__ == '__main__':
    main()
