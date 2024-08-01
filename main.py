import os

def txt2stendhal(input_file, output_file_base):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    title = os.path.splitext(os.path.basename(input_file))[0] + " part"
    author = "LaurinSorgend"
    
    max_chars_per_page = 252
    max_pages_per_file = 100
    words = content.split()
    pages = []
    current_page = ""
    
    for word in words:
        if len(current_page) + len(word) + 1 <= max_chars_per_page:
            if current_page:
                current_page += " " + word
            else:
                current_page = word
        else:
            pages.append(current_page)
            current_page = word
    
    if current_page:
        pages.append(current_page)
    
    total_files = (len(pages) + max_pages_per_file - 1) // max_pages_per_file
    
    for file_index in range(total_files):
        start_page = file_index * max_pages_per_file
        end_page = min((file_index + 1) * max_pages_per_file, len(pages))
        output_file = f"{output_file_base}_part{file_index + 1}.stendhal"
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"title: {title} {file_index + 1}\n")
            file.write(f"author: {author}\n")
            file.write("pages:\n")
            for page in pages[start_page:end_page]:
                file.write(f"#- {page}\n")
        
        print(f"Processed {end_page - start_page} pages into {output_file}.")

if __name__ == "__main__":
    input_file = "D:\Dokumente\programming\epub2txt\The Outsider_Albert Camus.txt"
    output_file_base = 'output'
    txt2stendhal(input_file, output_file_base)