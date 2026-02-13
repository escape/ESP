#!/usr/bin/env python3
import argparse, json, sys, pathlib, hashlib
BASE = pathlib.Path(__file__).resolve().parents[1]

def hash_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(description='espctl — utilities for ESP datasets')
    sub = ap.add_subparsers(dest='cmd')
    v = sub.add_parser('validate', help='validate JSON against schema')
    v.add_argument('schema', type=str)
    v.add_argument('data', type=str)
    h = sub.add_parser('hash', help='sha256 of a file')
    h.add_argument('path', type=str)
    args = ap.parse_args()

    if args.cmd == 'hash':
        print(hash_file(pathlib.Path(args.path)))
        return

    if args.cmd == 'validate':
        try:
            import jsonschema
        except ImportError:
            print('Install jsonschema: pip install jsonschema', file=sys.stderr)
            sys.exit(1)
        schema = json.loads(pathlib.Path(args.schema).read_text())
        data = json.loads(pathlib.Path(args.data).read_text())
        jsonschema.validate(instance=data, schema=schema)
        print('OK')
        return

    ap.print_help()

if __name__ == '__main__':
    main()
