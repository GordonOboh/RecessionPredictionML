import re

def extract_sty_packages(log_path, output_path=None):
    pattern = re.compile(r'(/.*?\.sty)')

    with open(log_path, 'r') as f:
        log_text = f.read()

    matches = pattern.findall(log_text)
    unique_sty_paths = sorted(set(matches))

    if output_path:
        with open(output_path, 'w') as out_file:
            for path in unique_sty_paths:
                out_file.write(path + '\n')
        print(f"Extracted {len(unique_sty_paths)} .sty file paths to {output_path}")
    else:
        print(f"Found {len(unique_sty_paths)} .sty files:")
        for path in unique_sty_paths:
            print(path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python extract_sty_paths.py <log_file> [output_file]")
    else:
        log_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        extract_sty_packages(log_file, output_file)
