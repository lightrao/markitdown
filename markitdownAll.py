import os
from markitdown import MarkItDown

def convert_all_files():
    # Define directories
    source_dir = "rawFiles"
    dest_dir = "mdFiles"

    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created directory: {dest_dir}")

    # Initialize MarkItDown
    md = MarkItDown()

    # Get list of files
    files = os.listdir(source_dir)
    
    if not files:
        print(f"No files found in {source_dir}")
        return

    print(f"Found {len(files)} files in {source_dir}...")

    for filename in files:
        input_path = os.path.join(source_dir, filename)
        
        # Skip if it's a directory
        if not os.path.isfile(input_path):
            continue

        # Construct output path
        # Use os.path.splitext to handle filenames with multiple dots correctly (gets the last extension)
        file_base_name = os.path.splitext(filename)[0]
        output_filename = f"{file_base_name}.md"
        output_path = os.path.join(dest_dir, output_filename)

        print(f"Converting: {filename} -> {output_filename}")

        try:
            # Perform conversion
            result = md.convert(input_path)
            
            # Write result to file with UTF-8 encoding
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result.text_content)
            
            print("[OK] Success")
            
        except Exception as e:
            print(f"[ERROR] Error converting {filename}: {e}")

if __name__ == "__main__":
    convert_all_files()
